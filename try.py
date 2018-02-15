import cv2
vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0
ramp_frames=30
for i in xrange(ramp_frames):
  vidcap.read()

success = True
while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1