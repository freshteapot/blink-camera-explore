import os
from blinkpy import blinkpy

username=os.getenv('BLINK_USERNAME', 'fake')
password=os.getenv('BLINK_PASSWORD', 'fake')

blink = blinkpy.Blink(username=username, password=password, refresh_rate=30)
blink.start()
blink.refresh()

for name, camera in blink.cameras.items():
  print(name)                   # Name of the camera
  print('Temp is {}'.format(camera.temperature_c))

camera_name = os.getenv('BLINK_CAMERA_NAME', 'Main Garden')
camera = blink.cameras[camera_name]
camera.snap_picture()
blink.refresh()

# Hard code saving of file, this assumes docker in use. Might want to change this.
camera.image_to_file('/data/bob.jpg')
