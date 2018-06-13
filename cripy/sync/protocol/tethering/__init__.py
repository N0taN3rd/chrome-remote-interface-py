from cripy.sync.protocol.tethering import events as Events

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
            msg_dict['port'] = port
        self.chrome.send('Tethering.bind', params=msg_dict)


    def unbind(self, port):
        """
        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        self.chrome.send('Tethering.unbind', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

