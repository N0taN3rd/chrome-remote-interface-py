from pyee import EventEmitter
from cripy.chrome.execution_context import ExecutionContext, JSHandle


class Worker(EventEmitter):

    def __init__(self, client, url, logEntryAdded):
        super().__init__()
        self._client = client
        self.url = url
        self._client.once("Runtime.executionContextCreated")

    async def onceExCc(self, event):
        await self._client.send(
            "Runtime.evaluate",
            dict(
                expression="this",
                returnByValue=False,
                contextId=event["executionContextId"],
            ),
        )
