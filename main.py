from imutils import paths
import argparse
import cv2
import shutil
import BlurDetection
import logging
import BlurDetection.scripts
import BlurDetection.FocusMask
#main code
#process command line input
logger = logging.getLogger('main')

#loop over input images
"""
for imagePath in paths.list_images("Test"):
	print imagePath
	msk, res, blurry = FocusMask.blur_mask(img)
                    img_msk = cv2.bitwise_and(img, img, mask=msk)
                    if args.display:
                        scripts.display('res', img_msk)
                        scripts.display('msk', msk)
                        scripts.display('img', img)
                        cv2.waitKey(0)
	if fm < 100.0:
		shutil.move(imagePath, "Test/Blurry/"+str(imagePath[14:]))  #  text = "Blurry"
	else:
		shutil.move(imagePath, "Test/NotBlurry/"+str(imagePath[14:]))
		"""
logger = scripts.get_logger(quite=False, debug=False)
for path in paths.list_images("Test"):
    for img_path in scripts.find_images(path):
        logger.debug('evaluating {0}'.format(img_path))
        img = cv2.imread(img_path)
        if isinstance(img, numpy.ndarray):
            msk, res, blurry = FocusMask.blur_mask(img) #RES IS RESULT
            print res
            img_msk = cv2.bitwise_and(img, img, mask=msk)
            scripts.display('res', img_msk)
            cv2.waitKey(0)

def autoanalyze():
    #args = scripts.get_args() #retrieves args
    logger = scripts.get_logger(quite=False, debug=False)
    for path in args.image_paths:
        for img_path in scripts.find_images(path):
            logger.debug('evaluating {0}'.format(img_path))
            img = cv2.imread(img_path)
            if isinstance(img, numpy.ndarray):
                msk, res, blurry = FocusMask.blur_mask(img) #RES IS RESULT
                print res
                img_msk = cv2.bitwise_and(img, img, mask=msk)
                scripts.display('res', img_msk)
                cv2.waitKey(0)