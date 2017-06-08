from time import sleep
import json
import myo as libmyo; libmyo.init()
import requests

api_url = 'https://warm-spire-75113.herokuapp.com/api/validate'

gesture = None
gestures_map = {libmyo.Pose.fist:'FIST', libmyo.Pose.wave_in:'LEFT', libmyo.Pose.fingers_spread:'OPEN', libmyo.Pose.wave_out:'RIGHT'}

def check_gesture(current_gesture):
    print('current_gesture:', current_gesture)

    data = {'current_gesture':current_gesture, 'gesture':gesture, 'transaction_id':0}
    payload = json.dumps(data)
    r = requests.put(api_url, data=payload)
    content = r.content
    content_json = json.loads(content)
    result = content_json['result']

    print(result)

class Listener(libmyo.DeviceListener):
    def __init__(self):
        self.current_gesture = 0

    def on_pair(self, myo, timestamp, firmware_version):
        print("Hello, Myo!")

    def on_unpair(self, myo, timestamp):
        print("Goodbye, Myo!")

    def on_pose(self, myo, timestamp, pose):
        if not (pose == libmyo.Pose.rest) and not (pose == libmyo.Pose.double_tap):
            if self.current_gesture >= 3:
                self.current_gesture = 0

            gesture = gestures_map[pose]
            self.current_gesture = self.current_gesture + 1

            myo.vibrate('short')

            check_gesture(self.current_gesture)

hub = libmyo.Hub()
hub.run(1000, Listener())
try:
    while True:
        sleep(0.5)
except KeyboardInterrupt:
    print('\nQuit')
finally:
    hub.shutdown()  # !! crucial
