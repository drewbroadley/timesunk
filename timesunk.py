#!/usr/local/bin/python3.7

"""
from setuptools import setup
setup(
    app=["timesunk.py"],
    setup_requires=["py2app"],
)
"""
# Install notes
# sudo visudo
#   Paste at bottom:
#   drewbroadley    ALL = NOPASSWD: /usr/bin/sntp
#   Replacing "drewbroadley" with your Mac OSX username
# brew install python3
# brew install ntp
# pip3 install goprocam
# pip3 install timecode
# pip3 install python-ltc

from TimeSunk.Connect import TimeSunkConnect
from TimeSunk.DateTime import TimeSunkDateTime
from TimeSunk.Settings import TimeSunkSettings
from TimeSunk.Status import TimeSunkStatus

import time, os
import subprocess
import datetime
from timecode import Timecode
from goprocam import GoProCamera, constants as GoProCameraConstants
from timecode import Timecode

GoProWifiNetworks = [
    ["GP55465027", "canoe7667"]
]

"""
GoProWifiNetworks = [
    ["helm narrow", "sport0544"],
    ["chesty cam", "sail2567"],
    ["LokiHero4S", "lokifilm"],
    ["GP24595375", "fpn-Fcr-4qr"]
]
"""

settings = {
    "fps": 50,
    "mode": "video",
    "resolution": "1080p",
    "low_light": True,
    "protune_video": True,
    "protune_audio": True,
    "white_balance": "auto",
    "color": "flat",
    "aspect_ratio": "16:9",
    "audio_mode": "auto",
    "spot_meter": True,
    "video_stabilised": True,
    "sharpness": "auto",
    "iso_max": 400,
    "ev": 0.0
}

print("CPU: Syncing computer time")
CPUNetworkTime = "/usr/bin/sudo /usr/local/bin/sntp -sS time.apple.com"
CPUNetworkTimeOutput = subprocess.run(CPUNetworkTime, stdout=subprocess.PIPE, shell=True)
print("CPU: time synced!")


for GoProCameraWifi in GoProWifiNetworks:

    print("%s: Connecting... " % (GoProCameraWifi[0]))

    GoProConnect = TimeSunkConnect(GoProCameraWifi)
    GoProCameraInstance = GoProConnect.set()

    if (GoProCameraInstance is None):
        print('%s: Error connecting - tried 5 times, skipping... ' % (GoProCameraWifi[0]))
    else:
        try:
            GoProID = "GoPro:" + GoProCameraInstance.getStatus('status', '30')

            print('%s: Connected' % (GoProID))

            GoProDateTime = TimeSunkDateTime(GoProCameraInstance)
            GoProSettings = TimeSunkSettings(GoProCameraInstance, settings)
            GoProStatus = TimeSunkStatus(GoProCameraInstance)

            datetime_before = GoProDateTime.get()

            print('%s: Time: %s ' % (GoProID, datetime_before))

            # Setting time four times to ensure time is up to date
            GoProDateTime.set()
            GoProDateTime.set()
            GoProDateTime.set()
            GoProDateTime.set()

            print('%s: Time synced' % (GoProID))

            datetime_after = GoProDateTime.get()

            print('%s: Time: %s ' % (GoProID, datetime_after))

            GoProSettings.set()

            print('%s: Settings synced' % (GoProID))

            print('%s: Updated.' % (GoProID))

        except Exception as e:
           print("%s: Couldn't sync/send settings" % (GoProID))

# Setting null instance to do Timecode
GoProDateTime = TimeSunkDateTime({})

print('Timecode:')

while (1):
    print(GoProDateTime.timecode(settings["fps"]), end='\r\n')
    time.sleep(1 / settings["fps"])

# GoProCameraInstance = GoProCamera.GoPro(ip='10.5.5.9',constants.auth)

# print GoProCameraInstance.syncTime()

# print GoProCameraInstance.infoCamera("model_name")


