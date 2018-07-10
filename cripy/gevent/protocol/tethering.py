__all__ = ["Tethering"]


class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """

    def __init__(self, chrome):
        """
        Construct a new Tethering object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def bind(self, port):
        """
        Request browser port binding.

        :param port: Port number to bind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        wres = self.chrome.send('Tethering.bind', msg_dict)
        return wres.get()

    def unbind(self, port):
        """
        Request browser port unbinding.

        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        wres = self.chrome.send('Tethering.unbind', msg_dict)
        return wres.get()

    def accepted(self, fn, once=False):
        """
        Informs that port was successfully bound and got a specified connection id.
        """
        self.chrome.on("Tethering.accepted", fn, once=once)


