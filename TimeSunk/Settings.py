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

class TimeSunkSettings:

    resolution = "1080p"
    mode = "video"
    fps = "50"
    fov = "wide"
    low_light = True
    protune = True
    white_balance = "auto"
    color = "flat"
    shutter = "auto"
    iso_max = "400"
    ev = 0.0
    rotation = "auto"
    default_mode = "video"
    quik_capture = True
    led = False
    gps = True
    lcd_brightness = 0.1
    beeps = False
    video_format = "PAL"
    auto_off = "Never"
    screen_saver = "Never"
    language = "English"
    language_voice = "English - US"

    GoProCameraInstance = None

    def __init__(self, GoProCamera):

        self.GoProCameraInstance = GoProCamera

    def set(self):

        # Setting mode
        if (self.mode == "video"):
            self.GoProCameraInstance.mode(GoProCameraConstants.Mode.VideoMode)

            if (self.iso_max):
                if (self.iso_max == 100):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ISO_LIMIT,
                                                          GoProCameraConstants.Video.IsoLimit.ISO100)
                elif (self.iso_max == 200):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ISO_LIMIT,
                                                          GoProCameraConstants.Video.IsoLimit.ISO200)
                elif (self.iso_max == 800):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ISO_LIMIT,
                                                          GoProCameraConstants.Video.IsoLimit.ISO800)
                
                else:
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ISO_LIMIT,
                                                          GoProCameraConstants.Video.IsoLimit.ISO1600)

            if (self.ev):
                if (self.ev == 0):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.Zero)
                elif (self.ev == 0):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.Zero)
                elif (self.ev == 0):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.Zero)
                elif (self.ev == 0):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.Zero)
                elif (self.ev == 0):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.Zero)


            # Setting FPS
            if (self.fps):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.FRAME_RATE, self.fps)

            # Setting resolution
            if (self.resolution == "1080p"):
                if (self.fov == "wide"):
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R1080pSV
                    )
                else:
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R1080p
                    )
            elif (self.resolution == "2k"):
                if (self.fov == "wide"):
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R2k
                    )
                else:
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R2kSV
                    )
            elif (self.resolution == "720p"):
                if (self.fov == "wide"):
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R720pSV
                    )
                else:
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R720p
                    )
            elif (self.resolution == "4K"):
                if (self.fov == "wide"):
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R4kSV
                    )
                else:
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R4k
                    )

        elif (self.mode == "photo"):
            self.GoProCameraInstance.mode(GoProCameraConstants.Mode.PhotoMode)

            if (self.resolution == "12MP"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Photo.RESOLUTION, GoProCameraConstants.Photo.Resolution.R12L
                )
            elif (self.resolution == "7MP"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Photo.RESOLUTION, GoProCameraConstants.Photo.Resolution.R7M
                )


        #elif (self.mode == "multi"):
        #    InternalGoProCameraInstance.mode(GoProCameraConstants.Mode.MultiShotMode)

        return None
