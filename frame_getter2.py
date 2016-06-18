import sys
sys.path.insert(0, "/usr/local/lib/python2.7/site-packages")
import cv2

vidcap = cv2.VideoCapture('Independence Day.mp4')
#vidcap.open(1)
success, image = vidcap.read()
yes = vidcap.isOpened()
#print yes

count = 0
variance = 0
while success:
	if variance == 11:
		success, image = vidcap.read()

		if count % 100 == 0:
			print str(count)

		params = list()
		params.append(16)
		params.append(0)
		path = "test_frames/frame_"+str(count)+".png"
		cv2.imwrite(path, image, params)
		count += 1
		if cv2.waitKey(10) == 27:
			break
		variance = 0
	else:
		success = vidcap.grab()
		variance += 1

