from time import sleep
import json
import myo as libmyo
import requests
import sys

API_URL = 'https://warm-spire-75113.herokuapp.com/api/validate'
GESTURES_MAP = {libmyo.Pose.fist: 'FIST', libmyo.Pose.wave_in: 'LEFT',
                libmyo.Pose.fingers_spread: 'OPEN', libmyo.Pose.wave_out: 'RIGHT'}

current_gesture = 0
fails = []
gesture = None

libmyo.init()


def check_gesture():
    print('current_gesture:', current_gesture)

    data = {'current_gesture': current_gesture,
            'gesture': gesture, 'transaction_id': 0}
    payload = json.dumps(data)
    r = requests.put(API_URL, data=payload)
    content = r.content
    content_json = json.loads(content)
    result = content_json['result']

    print(result)

    if not result:
        fails.append(True)

        if len(fails) == 2:
            print('failure')
            sys.exit()
    elif current_gesture == 3:
        print('success')
        sys.exit()


class Listener(libmyo.DeviceListener):

    def on_pair(self, myo, timestamp, firmware_version):
        print('Hello, Myo!')

    def on_unpair(self, myo, timestamp):
        print('Goodbye, Myo!')

    def on_pose(self, myo, timestamp, pose):
        global current_gesture
        global fails
        global gesture

        if not (pose == libmyo.Pose.double_tap) and not (pose == libmyo.Pose.rest):
            gesture = GESTURES_MAP[pose]

            if len(fails) == 1:
                if fails[0] == True:
                    fails[0] = False
                elif fails[0] == False:
                    current_gesture = current_gesture + 1
                    fails = []
            else:
                current_gesture = current_gesture + 1

            myo.vibrate('short')

            check_gesture()

hub = libmyo.Hub()
hub.run(1000, Listener())

try:
    while True:
        sleep(0.5)
except KeyboardInterrupt:
    print('\nQuit')
finally:
    hub.shutdown()  # !! crucial
