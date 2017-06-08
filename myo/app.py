from time import sleep
import json
import myo as libmyo
libmyo.init()
import requests
import sys

api_url = 'https://warm-spire-75113.herokuapp.com/api/validate'

# TODO when successfully incremented, return a wait to check api

current_gesture = 0
fails = []
gesture = None
gestures_map = {libmyo.Pose.fist: 'FIST', libmyo.Pose.wave_in: 'LEFT',
                libmyo.Pose.fingers_spread: 'OPEN', libmyo.Pose.wave_out: 'RIGHT'}


def check_gesture():
    print('current_gesture:', current_gesture)

    data = {'current_gesture': current_gesture,
            'gesture': gesture, 'transaction_id': 0}
    payload = json.dumps(data)
    r = requests.put(api_url, data=payload)
    content = r.content
    content_json = json.loads(content)
    result = content_json['result']

    print(result)

    if not result:
        fails.append(True)


class Listener(libmyo.DeviceListener):

    def on_pair(self, myo, timestamp, firmware_version):
        print("Hello, Myo!")

    def on_unpair(self, myo, timestamp):
        print("Goodbye, Myo!")

    def on_pose(self, myo, timestamp, pose):
        global current_gesture
        global fails
        global gesture

        if not (pose == libmyo.Pose.double_tap) and not (pose == libmyo.Pose.rest):
            gesture = gestures_map[pose]

            if len(fails) == 1:
                if fails[0] == True:
                    fails[0] = False
                elif fails[0] == False:
                    current_gesture = current_gesture + 1
                    fails = []
            elif len(fails) == 2:
                # TODO tell parker's website when we hard failed
                print('YOU FAILED')
                sys.exit()
            else:
                current_gesture = current_gesture + 1

            if current_gesture > 3:
                print('success') 
                # TODO print success RIGHT after last gesture instead of after extra gesture
                sys.exit()

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
