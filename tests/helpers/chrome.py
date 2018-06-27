import subprocess
import platform
import time
import os
from tempfile import TemporaryDirectory
import psutil
from requests import Session
from typing import Dict, Tuple, Optional

__all__ = ["ChromeFinder", "ChromeLauncher", "LaunchError"]

chromez = ["beta", "unstable", "stable", "chromium"]

dt_command = (
    "ls {0} /usr/share/applications/*.desktop | grep -E '(google-chrome*|chromium*|chrome*)' |"
    " xargs grep -E '^Exec=.*(google|chrome|chromium).*' | "
    "awk 'match($0, /[^:]+[^/]+([^ ]+)/, arr) {{ print arr[1] }}' | uniq"
)

# https://peter.sh/experiments/chromium-command-line-switches/
# https://cs.chromium.org/chromium/src/chrome/common/chrome_switches.cc
DEFAULT_ARGS = [
    "--disable-background-networking",
    "--disable-background-timer-throttling",
    "--disable-client-side-phishing-detection",
    "--disable-default-apps",
    "--disable-extensions",
    "--disable-hang-monitor",
    "--disable-prompt-on-repost",
    "--disable-sync",
    "--disable-translate",
    "--metrics-recording-only",
    "--no-first-run",
    "--safebrowsing-disable-auto-update",
    "--password-store=basic",
    "--disable-features=site-per-process",
    "--use-mock-keychain",
    "--mute-audio",
    "--disable-domain-reliability",  # no Domain Reliability Monitoring
    "--disable-renderer-backgrounding",
    "--disable-infobars",
    "--disable-translate"
]


class ChromeFinder(object):
    """Locates a usable chrome executable if it exists"""

    @classmethod
    def find_chrome(cls) -> Optional[str]:
        """
        Retrieve the full path to a chrome executable on this system if it exists.

        :return: The full path to a usable chrome executable. If one does not exist returns None
        """
        plat = platform.system()
        if plat == "Linux":
            return cls.linux()

    @classmethod
    def select_chrome(cls, chromes: Dict[str, str]) -> str:
        for crm in chromez:
            if crm in chromes:
                return chromes[crm]

    @classmethod
    def linux(cls) -> Optional[str]:
        maybe_chromes = cls.which_chrome()
        if maybe_chromes:
            return maybe_chromes
        return cls.chrome_desktops()

    @classmethod
    def chrome_desktops(cls) -> Optional[str]:
        desktops = [
            "/usr/share/applications/*.desktop",
            "~/.local/share/applications/*.desktop",
        ]
        for dt in desktops:
            ignore, results = cls.run_command(dt_command.format(dt), None)
            found = {}
            if results is not None:
                for exe in results.split("\n"):
                    if "google-" in exe:
                        split = exe.split("-")
                        if len(split) == 2:
                            which = "stable"
                        else:
                            which = split[-1]
                    elif "chromium" in exe:
                        which = "chromium"
                    else:
                        which = None
                    if which and which not in found:
                        found[which] = exe
            if len(found) > 0:
                return cls.select_chrome(found)
        raise None

    @classmethod
    def run_command(
        cls, cmd: str, which: Optional[str] = None
    ) -> Tuple[str, Optional[str]]:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            result = stdout.decode().strip()
        else:
            result = None
        return which, result

    @classmethod
    def which_chrome(cls) -> Optional[str]:
        execs = [
            "google-chrome-beta",
            "google-chrome-unstable",
            "google-chrome-stable",
            "chromium-browser",
            "chromium",
        ]
        results = []
        for exe in execs:
            results.append(cls.run_command(f"which {exe}", exe))
        if all(map(lambda x: x[1] is None, results)):
            return None
        crms = dict()
        for which, exe in results:
            if "google-" in which:
                crms[which.split("-")[-1]] = exe
            else:
                crms["chromium"] = exe
        return cls.select_chrome(crms)


class LaunchError(Exception):
    pass


class ChromeLauncher(ChromeFinder):
    @classmethod
    def launch(cls, headless=True) -> Tuple[psutil.Popen, TemporaryDirectory, str]:
        exe = cls.find_chrome()
        if exe is None:
            raise LaunchError(
                "Could not find a usable chrome executable on this system"
            )
        tmpdir = TemporaryDirectory()
        args = [exe, f"--user-data-dir={tmpdir.name}"] + DEFAULT_ARGS
        if headless:
            args += ["--headless", "--disable-gpu", "--hide-scrollbars"]
        args.append("--remote-debugging-port=9222")
        cp = psutil.Popen(
            args,
            stderr=subprocess.DEVNULL,
            env=os.environ.copy(),
        )
        with Session() as session:
            for i in range(100):
                time.sleep(0.1)
                try:
                    data = session.get("http://localhost:9222/json").json()
                    for d in data:
                        if d["type"] == "page":
                            return cp, tmpdir, d["webSocketDebuggerUrl"]
                    break
                except Exception as e:
                    print(e)
                    print(type(e))
                    continue
            else:
                tmpdir.cleanup()
                cp.kill()
                cp.wait()
                raise TimeoutError("Could not start server")


if __name__ == "__main__":
    cp, tmpdir, wsurl = ChromeLauncher.launch(headless=False)
    tmpdir.cleanup()
    cp.kill()
    cp.wait()
