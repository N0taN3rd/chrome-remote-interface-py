from cripy.sync.client import EventEmitter


class It(EventEmitter):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    ee = It()
    ee.on('it', lambda *args: print('it event', *args))
    ee.emit('it', 1)
