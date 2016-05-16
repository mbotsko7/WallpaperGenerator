from imutils import paths
import argparse
import cv2
import shutil

def variance_of_lapacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required = True,
				help = "path to input directory of images")
ap.add_argument("-t", "--threshold", type = float, default = 100.0,
				help = "focus measures that fall below this value will be considered 'blurry'")
gs = vars(ap.parse_args())

#loop over input images
x = paths.list_images("../StarWars")
print x
y = "Hi"

for imagePath in paths.list_images("StarWars_Test"):
	print imagePath
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_lapacian(gray)
	text = "Not Blurry"

	if fm < 100.0:
		shutil.move(imagePath, "Blurry/"+str(imagePath[14:]))  #  text = "Blurry"
	else:
		shutil.move(imagePath, "NotBlurry/"+str(imagePath[14:]))
	# cv2.putText(image, "{}: {:.2f}".format(text, fm), (10,30),
	# 			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 3)
	# cv2.imshow("Image", image)
	# key = cv2.waitKey(0)