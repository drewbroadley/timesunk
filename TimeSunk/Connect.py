import datetime
from goprocam import GoProCamera, constants as GoProCameraConstants
import time, os
import subprocess

class TimeSunkConnect:

    GoProCameraInstance = None
    GoProWifiSSID = None
    GoProWifiPassword = None

    def __init__(self, GoProCameraWifi):

        self.GoProWifiSSID = GoProCameraWifi[0]
        self.GoProWifiPassword = GoProCameraWifi[1]

        print('%s: Set WIFI password %s ' % (GoProCameraWifi[0], GoProCameraWifi[1]))

    def set(self, attempt=1):

        if (attempt > 5):
            return None

        try:
            print('%s: Connection attempt #%d ' % (self.GoProWifiSSID, attempt))

            GoProNetworkSetup = "/usr/sbin/networksetup -setairportnetwork en0 '%s' '%s'" % (self.GoProWifiSSID, self.GoProWifiPassword)
            GoProNetworkSetupOutput = subprocess.run(GoProNetworkSetup, stdout=subprocess.PIPE, shell=True)

            # Settle to allow WIFI to connect to GoPro
            time.sleep(10)

            GoProNetworkGetSSID = "/usr/sbin/networksetup -listallhardwareports | /usr/bin/awk '/Wi-Fi/{getline; print $2}' | /usr/bin/xargs /usr/sbin/networksetup -getairportnetwork | /usr/bin/awk -F\"Network: \" '/Network:/{print $2}'"
            GoProNetworkGetSSIDOutput = subprocess.run(GoProNetworkGetSSID, stdout=subprocess.PIPE, shell=True)

            if (GoProNetworkGetSSIDOutput.stdout.strip().decode("utf-8") != self.GoProWifiSSID):
                raise Exception("Incorrect WIFI")
            # Connect to GoPro
            self.GoProCameraInstance = GoProCamera.GoPro()

            return self.GoProCameraInstance

        except Exception as e:
            return self.set((attempt+1))