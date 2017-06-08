from time import sleep
from myo import init, Hub, DeviceListener

# run export DYLD_LIBRARY_PATH=/Users/kas/Downloads/sdk/myo.framework

class Listener(DeviceListener):
    def on_pair(self, myo, timestamp, firmware_version):
        print("Hello, Myo!")

    def on_unpair(self, myo, timestamp):
        print("Goodbye, Myo!")

    def on_pose(self, myo, timestamp, pose):
        print(pose)

init()
hub = Hub()
hub.run(1000, Listener())
try:
    while True:
        sleep(0.5)
except KeyboardInterrupt:
    print('\nQuit')
finally:
    hub.shutdown()  # !! crucial
