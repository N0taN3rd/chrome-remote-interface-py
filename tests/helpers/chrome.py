import asyncio
import os
import platform
from asyncio import AbstractEventLoop
from asyncio.subprocess import Process
from itertools import chain
from tempfile import TemporaryDirectory
from typing import Dict, Tuple, Optional

import uvloop

from cripy.cdp import CDP

__all__ = ["launch_chrome", "LaunchError"]

chromez = ["unstable", "beta", "stable", "chromium"]

dt_command = (
    "ls {0} /usr/share/applications/*.desktop | grep -E '(google-chrome*|chromium*|chrome*)' |"
    " xargs grep -E '^Exec=.*(google|chrome|chromium).*' | "
    "awk 'match($0, /[^:]+[^/]+([^ ]+)/, arr) {{ print arr[1] }}' | uniq | sort -r"
)

# https://peter.sh/experiments/chromium-command-line-switches/
# https://cs.chromium.org/chromium/src/chrome/common/chrome_switches.cc
DEFAULT_ARGS = [
    "--remote-debugging-port=9222",
    "--disable-background-networking",
    "--disable-background-timer-throttling",
    "--disable-client-side-phishing-detection",
    "--disable-default-apps",
    "--disable-extensions",
    "--disable-backgrounding-occluded-windows",
    "--disable-ipc-flooding-protection",
    "--disable-popup-blocking",
    "--disable-hang-monitor",
    "--disable-prompt-on-repost",
    "--disable-sync",
    "--disable-translate",
    "--disable-domain-reliability",
    "--disable-renderer-backgrounding",
    "--disable-infobars",
    "--disable-translate",
    "--disable-features=site-per-process",
    "--disable-breakpad",
    "--metrics-recording-only",
    "--no-first-run",
    "--safebrowsing-disable-auto-update",
    "--password-store=basic",
    "--use-mock-keychain",
    "--mute-audio",
    "--autoplay-policy=no-user-gesture-required",
    "--enable-automation",
]


class LaunchError(Exception):
    pass


chrome_execs = [
    "google-chrome-unstable",
    "google-chrome-beta",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]


async def run_command(cmd: str, loop: AbstractEventLoop, env: Dict) -> Tuple[str, str]:
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.DEVNULL,
        loop=loop,
        env=env,
    )
    stdout, stderr = await proc.communicate()
    await proc.wait()
    return stdout.decode("utf-8").strip(), stderr.decode("utf-8").strip()


async def which_chrome(loop: AbstractEventLoop, env: Dict) -> Optional[str]:
    for chrome in chrome_execs:
        exe, _ = await run_command(f"which {chrome}", loop, env)
        if exe:
            return exe
    return None


async def check_chrome_desktops(loop: AbstractEventLoop, env: Dict) -> Optional[str]:
    results = await asyncio.gather(
        run_command(dt_command.format("/usr/share/applications/*.desktop"), loop, env),
        run_command(
            dt_command.format("~/.local/share/applications/*.desktop"), loop, env
        ),
        loop=loop,
    )

    found: Dict[str, str] = dict(
        it
        for it in map(
            lambda cexe: (cexe[cexe.rindex("/") + 1 :], cexe),
            chain.from_iterable(map(lambda t: t[0].splitlines(), results)),
        )
    )

    for desired in chrome_execs:
        if desired in found:
            return found[desired]

    return None


async def find_chrome(loop: AbstractEventLoop, env: Dict) -> Optional[str]:
    plat = platform.system()
    if plat == "Linux":
        chrome_exe = await which_chrome(loop, env)
        if chrome_exe is None:
            chrome_exe = await check_chrome_desktops(loop, env)
        return chrome_exe


async def launch_chrome(
    headless: bool = True
) -> Tuple[Process, TemporaryDirectory, str]:
    loop = asyncio.get_event_loop()
    env = os.environ.copy()
    chrome_exe = await find_chrome(loop, env)
    if chrome_exe is None:
        raise LaunchError("Could not find chrome")
    tmpdir = TemporaryDirectory()
    args = [chrome_exe, f"--user-data-dir={tmpdir.name}"] + DEFAULT_ARGS
    if headless:
        args.extend(["--headless", "--hide-scrollbars", "about:blank"])
    else:
        args.append("about:blank")
    chrome_proc = await asyncio.create_subprocess_exec(
        *args,
        stderr=asyncio.subprocess.DEVNULL,
        stdin=asyncio.subprocess.DEVNULL,
        loop=loop,
        env=env,
    )
    for _ in range(100):
        try:
            targets = await CDP.List()
            for tab in targets:
                print(tab)
                if tab["type"] == "page":
                    return chrome_proc, tmpdir, tab["webSocketDebuggerUrl"]
        except Exception:
            await asyncio.sleep(1, loop=loop)
    chrome_proc.kill()
    await chrome_proc.wait()
    tmpdir.cleanup()
    raise LaunchError("Could not find tab for connecting to")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.get_event_loop().run_until_complete(launch_chrome())
    # cp, tmpdir, wsurl = ChromeLauncher.launch(headless=False)
    # tmpdir.cleanup()
    # cp.kill()
    # cp.wait()
