from imutils import paths
import argparse
import cv2
import shutil
import logging
import scripts
import FocusMask
import numpy
#main code
#process command line input
logger = logging.getLogger('main')

def evaluate(img_col):
    numpy.seterr(all='ignore')
    assert isinstance(img_col, numpy.ndarray), 'img_col must be a numpy array'
    assert img_col.ndim == 3, 'img_col must be a color image ({0} dimensions currently)'.format(img_col.ndim)
    #assert isinstance(args, argparse.Namespace), 'args must be of type argparse.Namespace not {0}'.format(type(args))
    img_gry = cv2.cvtColor(img_col, cv2.COLOR_RGB2GRAY)
    rows, cols = img_gry.shape
    crow, ccol = rows/2, cols/2
    f = numpy.fft.fft2(img_gry)
    fshift = numpy.fft.fftshift(f)
    fshift[crow-75:crow+75, ccol-75:ccol+75] = 0
    f_ishift = numpy.fft.ifftshift(fshift)
    img_fft = numpy.fft.ifft2(f_ishift)
    img_fft = 20*numpy.log(numpy.abs(img_fft))
    """
    if args.display and not args.testing:
        cv2.destroyAllWindows()
        scripts.display('img_fft', img_fft)
        scripts.display('img_col', img_col)
        cv2.waitKey(0)
        """
    result = numpy.mean(img_fft)
    return img_fft, result, result < 10
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
for path in paths.list_images("../Test"):
    #print path
    for img_path in scripts.find_images(path):
        logger.debug('evaluating {0}'.format(img_path))
        img = cv2.imread(img_path)
        if isinstance(img, numpy.ndarray):
            msk, res, blurry = FocusMask.blur_mask(img) #RES IS RESULT
            img_fft, result, val = evaluate(img)
            print res
            print result
            img_msk = cv2.bitwise_and(img, img, mask=msk)
            scripts.display('img', img)
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