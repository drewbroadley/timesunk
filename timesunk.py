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

from TimeSunk.DateTime import TimeSunkDateTime
from TimeSunk.Settings import TimeSunkSettings
from TimeSunk.Status import TimeSunkStatus

import time, os

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

print("CPU: Syncing computer time")
os.system("sudo sntp -sS time.apple.com")
print("CPU: time synced!")

for GoProCameraWifi in GoProWifiNetworks:

    print("%s: Connecting... " % (GoProCameraWifi[0]))
    GoProNetworkSetup = "networksetup -setairportnetwork en0 '%s' '%s'" % (GoProCameraWifi[0], GoProCameraWifi[1])

    print("%s: Trying `%s`" % (GoProCameraWifi[0], GoProNetworkSetup))
    os.system(GoProNetworkSetup)

    print("%s: Settling for 10 seconds.." % (GoProCameraWifi[0]))
    time.sleep(10)

    try:

        GoProCameraInstance = GoProCamera.GoPro()

        GoProWifiSSID = "GoPro:" + GoProCameraInstance.getStatus('status', '30')

        GoProDateTime = TimeSunkDateTime(GoProCameraInstance)
        GoProSettings = TimeSunkSettings(GoProCameraInstance)
        GoProStatus = TimeSunkStatus(GoProCameraInstance)

        datetime_before = GoProDateTime.get()

        print('%s: Time: %s ' % (GoProWifiSSID, datetime_before))

        GoProDateTime.set()
        GoProDateTime.set()
        GoProDateTime.set()
        GoProDateTime.set()

        print('%s: Time synced' % (GoProWifiSSID))

        datetime_after = GoProDateTime.get()

        print('%s: Time: %s ' % (GoProWifiSSID, datetime_after))

        GoProSettings.set()

        print('%s: Settings synced' % (GoProWifiSSID))

        print('%s: Updated.' % (GoProWifiSSID))

        print(GoProStatus.overview())

    except Exception as e:
       print("%s: Couldn't connect to Camera" % (GoProCameraWifi[0]))


# GoProCameraInstance = GoProCamera.GoPro(ip='10.5.5.9',constants.auth)

# print GoProCameraInstance.syncTime()

# print GoProCameraInstance.infoCamera("model_name")


