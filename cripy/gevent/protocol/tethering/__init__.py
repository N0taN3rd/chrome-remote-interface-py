from cripy.gevent.protocol.tethering import events as Events

__all__ = ["Tethering"] + Events.__all__


class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    def bind(self, port):
        """
        :param port: Port number to bind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict["port"] = port
        wres = self.chrome.send("Tethering.bind", msg_dict)
        return wres.get()

    def unbind(self, port):
        """
        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict["port"] = port
        wres = self.chrome.send("Tethering.unbind", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
