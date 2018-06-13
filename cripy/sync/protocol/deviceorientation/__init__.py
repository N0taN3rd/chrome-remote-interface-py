
__all__ = ["DeviceOrientation"]


class DeviceOrientation(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def clearDeviceOrientationOverride(self):
        self.chrome.send('DeviceOrientation.clearDeviceOrientationOverride')


    def setDeviceOrientationOverride(self, alpha, beta, gamma):
        """
        :param alpha: Mock alpha
        :type alpha: float
        :param beta: Mock beta
        :type beta: float
        :param gamma: Mock gamma
        :type gamma: float
        """
        msg_dict = dict()
        if alpha is not None:
            msg_dict['alpha'] = alpha
        if beta is not None:
            msg_dict['beta'] = beta
        if gamma is not None:
            msg_dict['gamma'] = gamma
        self.chrome.send('DeviceOrientation.setDeviceOrientationOverride', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return None

