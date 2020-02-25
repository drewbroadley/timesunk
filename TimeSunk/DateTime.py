import datetime


class TimeSunkDateTime:

    GoProCameraInstance = None

    def __init__(self, GoProCamera):

        self.GoProCameraInstance = GoProCamera

    def get(self):
        GoProCameraStatusDateTime = self.GoProCameraInstance.getStatus('status', '40')

        d = [];

        for item in GoProCameraStatusDateTime[1:].split('%'):
            d.append(int(item, 16))

        d = datetime.datetime(d[0] + 2000, d[1], d[2], d[3], d[4], d[5])

        return d

    def set(self):
        d = self.GoProCameraInstance.syncTime()

        return d

    def timecode(self, fps):
        microseconds_fps = 1000000 / fps
        d = datetime.datetime.now()
        t = d.time()
        microseconds = int(t.strftime('%f'))
        timecode_fps = str(int(microseconds/microseconds_fps))
        value = t.strftime('%H:%M:%S:') + timecode_fps
        return value
