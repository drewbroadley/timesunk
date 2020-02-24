import time
import socket
import urllib.request
import json
import re
import pdb
import timecode
import datetime

import os
import time
from goprocam import GoProCamera, constants as GoProCameraConstants


class TimeSunkStatus:

    GoProCameraInstance = None

    def __init__(self, GoProCamera):

        self.GoProCameraInstance = GoProCamera

    def get(self):

        return self.GoProCameraInstance.infoCamera()

    def overview(self):

        return self.GoProCameraInstance.overview()
