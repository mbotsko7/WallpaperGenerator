import sys
import cv2

video_path = sys.argv[1]
print video_path
video_capture = cv2.VideoCapture(video_path)

success, image = video_capture.read()
yes = video_capture.isOpened()
print yes

count = 0
variance = 0
while success:
	if variance == 11:
		success, image = video_capture.read()
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
		success = video_capture.grab()
		variance += 1

