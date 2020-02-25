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



    GoProCameraInstance = None

    """
         quik_capture=True,
        led=False, gps=True, lcd_brightness=0.1, beeps=False, video_format="PAL", auto_off="Never", screen_saver="Never",
         aspect_ratio="16:9",
        
    """

    def __init__(self, GoProCamera, settings):
        self.GoProCameraInstance = GoProCamera
        self.mode = settings["mode"] if "mode" in settings else "video"
        self.fps = settings["fps"] if "fps" in settings else 24
        self.resolution = settings["resolution"] if "resolution" in settings else "1080p"
        self.fov = settings["fov"] if "fov" in settings else "wide"
        self.low_light = settings["low_light"] if "low_light" in settings else True
        self.protune_video = settings["protune_video"] if "protune_video" in settings else True
        self.protune_audio = settings["protune_audio"] if "protune_audio" in settings else True
        self.white_balance = settings["white_balance"] if "white_balance" in settings else "auto"
        self.color = settings["color"] if "color" in settings else "flat"
        self.aspect_ratio = settings["color"] if "color" in settings else "16:9"
        self.audio_mode = settings["audio_mode"] if "audio_mode" in settings else "auto"
        self.spot_meter = settings["spot_meter"] if "spot_meter" in settings else True
        self.video_stabilised = settings["video_stabilised"] if "video_stabilised" in settings else True
        self.sharpness = settings["sharpness"] if "sharpness" in settings else "auto"
        self.iso_max = settings["iso_max"] if "iso_max" in settings else 800
        self.ev = settings["ev"] if "ev" in settings else 0.0

    def set(self):

        # Setting mode
        if (self.mode == "video"):
            self.GoProCameraInstance.mode(GoProCameraConstants.Mode.VideoMode)

            # Set Protune Audio
            if (self.protune_audio):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.PROTUNE_AUDIO,
                                                      GoProCameraConstants.Video.ProtuneAudio.ON)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.PROTUNE_AUDIO,
                                                      GoProCameraConstants.Video.ProtuneAudio.OFF)

            # Set Video Stabilisation
            if (self.video_stabilised):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.VIDEO_EIS,
                                                      GoProCameraConstants.Video.VideoEIS.ON)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.VIDEO_EIS,
                                                      GoProCameraConstants.Video.VideoEIS.OFF)

            # Set Spot Meter
            if (self.spot_meter):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.SPOT_METER,
                                                      GoProCameraConstants.Video.SpotMeter.ON)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.SPOT_METER,
                                                      GoProCameraConstants.Video.SpotMeter.OFF)

            # Set Audio Mode
            if (self.audio_mode == "wind"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.AUDIO_MODE,
                                                      GoProCameraConstants.Video.AudioMode.Wind)
            elif (self.audio_mode == "stereo"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.AUDIO_MODE,
                                                      GoProCameraConstants.Video.AudioMode.Stereo)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.AUDIO_MODE,
                                                      GoProCameraConstants.Video.AudioMode.Auto)

            # Set Aspect Ratio
            if (self.aspect_ratio == "4:3"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ASPECT_RATION,
                                                      GoProCameraConstants.Video.AspectRatio.AP4by3)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ASPECT_RATION,
                                                      GoProCameraConstants.Video.AspectRatio.AP16by9)

            # Set Color
            if (self.color == "flat"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.COLOR,
                                                      GoProCameraConstants.Video.Color.Flat)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.COLOR,
                                                      GoProCameraConstants.Video.Color.GOPRO)

            # Set Sharpness
            if (self.sharpness == "high"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.SHARPNESS,
                                                      GoProCameraConstants.Video.Sharpness.High)
            elif (self.sharpness == "low"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.SHARPNESS,
                                                      GoProCameraConstants.Video.Sharpness.Low)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.SHARPNESS,
                                                      GoProCameraConstants.Video.Sharpness.Med)

            # Set ProTune Video
            if (self.protune_video):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.PROTUNE_VIDEO,
                                                      GoProCameraConstants.Video.ProTune.ON)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.PROTUNE_VIDEO,
                                                      GoProCameraConstants.Video.ProTune.OFF)

            # Set Low Light
            if (self.low_light):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.LOW_LIGHT,
                                                      GoProCameraConstants.Video.LowLight.ON)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.LOW_LIGHT,
                                                      GoProCameraConstants.Video.LowLight.OFF)

            # Set White Balance
            if (self.white_balance == "native"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WBNative)
            elif (self.white_balance == "2300K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB2300k)
            elif (self.white_balance == "2800K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB2800k)
            elif (self.white_balance == "3000K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB3000k)
            elif (self.white_balance == "3200K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB3200k)
            elif (self.white_balance == "4000K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB4000k)
            elif (self.white_balance == "4500K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB4500k)
            elif (self.white_balance == "4800K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB4800k)
            elif (self.white_balance == "5000K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB5000k)
            elif (self.white_balance == "5500K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB5500k)
            elif (self.white_balance == "6000K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB6000k)
            elif (self.white_balance == "6500K"):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WB6500k)
            else:
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.WHITE_BALANCE,
                                                      GoProCameraConstants.Video.WhiteBalance.WBAuto)

            # Set ISO Max
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
                elif (self.iso_max == 1600):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ISO_LIMIT,
                                                          GoProCameraConstants.Video.IsoLimit.ISO1600)
                elif (self.iso_max == 3200):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ISO_LIMIT,
                                                          GoProCameraConstants.Video.IsoLimit.ISO3200)
                else:
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.ISO_LIMIT,
                                                          GoProCameraConstants.Video.IsoLimit.ISO6400)

            if (self.ev):
                if (self.ev == 0.5):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.M0_5)
                elif (self.ev == 1):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.M1)
                elif (self.ev == 1.5):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.M1_5)
                elif (self.ev == -0.5):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.P0_5)
                elif (self.ev == -1.0):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.P1)
                elif (self.ev == -1.5):
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.P1_5)
                else:
                    self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.EVCOMP, GoProCameraConstants.Video.EvComp.Zero)

            # Setting FPS
            if (self.fps):
                self.GoProCameraInstance.gpControlSet(GoProCameraConstants.Video.FRAME_RATE, self.fps)

            # Setting resolution
            if (self.resolution == "960p"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R960p
                )
            elif (self.resolution == "1440p"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R1440p
                )
            elif (self.resolution == "2k"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R2k
                )
            elif (self.resolution == "720p"):
                if (self.fov == "wide"):
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R720p
                    )
            elif (self.resolution == "4K"):
                if (self.fov == "wide"):
                    self.GoProCameraInstance.gpControlSet(
                        GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R4k
                    )
            else:
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.RESOLUTION, GoProCameraConstants.Video.Resolution.R1080p
                )

            # Setting FOV
            if (self.fov == "wide"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.FOV, GoProCameraConstants.Video.Fov.Wide
                )
            elif (self.fov == "medium"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.FOV, GoProCameraConstants.Video.Fov.Medium
                )
            elif (self.fov == "narrow"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.FOV, GoProCameraConstants.Video.Fov.Narrow
                )
            elif (self.fov == "superview"):
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.FOV, GoProCameraConstants.Video.Fov.SuperView
                )
            else:
                self.GoProCameraInstance.gpControlSet(
                    GoProCameraConstants.Video.FOV, GoProCameraConstants.Video.Fov.Linear
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
