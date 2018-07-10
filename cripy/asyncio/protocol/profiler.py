from typing import Any, List, Optional, Union


__all__ = ["Profiler"]


class Profiler(object):
    dependencies = ['Runtime', 'Debugger']


    def __init__(self, chrome):
        """
        Construct a new Profiler object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.enable')
        return res

    async def getBestEffortCoverage(self) -> Optional[dict]:
        """
        Collect coverage data for the current isolate. The coverage data may be incomplete due to
garbage collection.
        """
        res = await self.chrome.send('Profiler.getBestEffortCoverage')
        return res

    async def setSamplingInterval(self, interval: int) -> Optional[dict]:
        """
        Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.

        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        msg_dict = dict()
        if interval is not None:
            msg_dict['interval'] = interval
        res = await self.chrome.send('Profiler.setSamplingInterval', msg_dict)
        return res

    async def start(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.start')
        return res

    async def startPreciseCoverage(self, callCount: Optional[bool] = None, detailed: Optional[bool] = None) -> Optional[dict]:
        """
        Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
coverage may be incomplete. Enabling prevents running optimized code and resets execution
counters.

        :param callCount: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :type callCount: Optional[bool]
        :param detailed: Collect block-based coverage.
        :type detailed: Optional[bool]
        """
        msg_dict = dict()
        if callCount is not None:
            msg_dict['callCount'] = callCount
        if detailed is not None:
            msg_dict['detailed'] = detailed
        res = await self.chrome.send('Profiler.startPreciseCoverage', msg_dict)
        return res

    async def startTypeProfile(self) -> Optional[dict]:
        """
        Enable type profile.
        """
        res = await self.chrome.send('Profiler.startTypeProfile')
        return res

    async def stop(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.stop')
        return res

    async def stopPreciseCoverage(self) -> Optional[dict]:
        """
        Disable precise code coverage. Disabling releases unnecessary execution count records and allows
executing optimized code.
        """
        res = await self.chrome.send('Profiler.stopPreciseCoverage')
        return res

    async def stopTypeProfile(self) -> Optional[dict]:
        """
        Disable type profile. Disabling releases type profile data collected so far.
        """
        res = await self.chrome.send('Profiler.stopTypeProfile')
        return res

    async def takePreciseCoverage(self) -> Optional[dict]:
        """
        Collect coverage data for the current isolate, and resets execution counters. Precise code
coverage needs to have started.
        """
        res = await self.chrome.send('Profiler.takePreciseCoverage')
        return res

    async def takeTypeProfile(self) -> Optional[dict]:
        """
        Collect type profile.
        """
        res = await self.chrome.send('Profiler.takeTypeProfile')
        return res

    def consoleProfileFinished(self, fn, once=False) -> None:
        if once:
            self.chrome.once("Profiler.consoleProfileFinished", fn)
        else:
            self.chrome.on("Profiler.consoleProfileFinished", fn)

    def consoleProfileStarted(self, fn, once=False) -> None:
        """
        Sent when new profile recording is started using console.profile() call.
        """
        if once:
            self.chrome.once("Profiler.consoleProfileStarted", fn)
        else:
            self.chrome.on("Profiler.consoleProfileStarted", fn)



