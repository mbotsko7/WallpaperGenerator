import sys
sys.path.insert(0, "/usr/local/lib/python2.7/site-packages")
import cv2

vidcap = cv2.VideoCapture('home/botsko/Videos/Captain America_The Winter Soldier.m4v')
vidcap.open()
success, image = vidcap.read()
yes = vidcap.isOpened()
count = 0
variance = 0
while success:
	if variance == 11:
		success, image = vidcap.read()

		if count % 100 == 0:
			print str(count)

		params = list()
		params.append(cv2.cv.CV_IMWRITE_PNG_COMPRESSION)
		params.append(0)
		path = "./frames/frame_"+str(count)+".png"
		cv2.imwrite(path, image, params)
		count += 1
		if cv2.waitKey(10) == 27:
			break
		variance = 0
	else:
		success = vidcap.grab()
		variance += 1
