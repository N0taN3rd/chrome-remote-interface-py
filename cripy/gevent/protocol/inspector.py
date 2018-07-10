__all__ = ["Inspector"]


class Inspector(object):
    def __init__(self, chrome):
        """
        Construct a new Inspector object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disables inspector domain notifications.
        """
        wres = self.chrome.send('Inspector.disable')
        return wres.get()

    def enable(self):
        """
        Enables inspector domain notifications.
        """
        wres = self.chrome.send('Inspector.enable')
        return wres.get()

    def detached(self, fn, once=False):
        """
        Fired when remote debugging connection is about to be terminated. Contains detach reason.
        """
        self.chrome.on("Inspector.detached", fn, once=once)

    def targetCrashed(self, fn, once=False):
        """
        Fired when debugging target has crashed
        """
        self.chrome.on("Inspector.targetCrashed", fn, once=once)

    def targetReloadedAfterCrash(self, fn, once=False):
        """
        Fired when debugging target has reloaded after crash
        """
        self.chrome.on("Inspector.targetReloadedAfterCrash", fn, once=once)


