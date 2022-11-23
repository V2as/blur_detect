import cv2 as cv
import numpy as np


image = cv.imread('Rebra.png', cv.IMREAD_COLOR)
grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blr = 1

def normalize(img, size=60):
    global image, grayscale


    (h, w) = img.shape
    (cX, cY) = (int(w / 2.0), int(h / 2.0))

    fft = np.fft.fft2(img)
    fftShift = np.fft.fftshift(fft)
    fftShift[cY - size:cY + size, cX - size:cX + size] = 0
    fftShift = np.fft.ifftshift(fftShift)
    recon = np.fft.ifft2(fftShift)
    magnitude = 20 * np.log(np.abs(recon))
    mean = np.mean(magnitude)
    print(mean)
    # while mean < 15:

    if mean < 15:
        print('Image is blurry')
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        fix = cv.filter2D(img, -1, kernel=kernel)
        image = fix
        grayscale = fix
        print('FIXED')
    else:
        print('Normal')



def blur (img, param):
    global image, grayscale
    blur = cv.blur(img, (param, param))
    image = blur
    grayscale = blur

while True:
    cv.namedWindow("Show")
    cv.imshow("Show", image)

    k = cv.waitKey(1) & 0xFF
    if k == ord('n'):
        normalize(grayscale, size=60)
    if k == ord('b'):
        blur(grayscale, blr)
        blr += 5
    if k == ord('q'):
        print ('QUIT')
        break


cv.destroyAllWindows()

