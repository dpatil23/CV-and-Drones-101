import cv2
import numpy as np
import glob 


cap = cv2.VideoCapture(0)

num = 0

while True:

    ret, img = cap.read()
    k = cv2.waitKey(5)
    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(r"C:\Users\darsh\OneDrive\Desktop\Class notes of CV and Drones 101\chessimg.jpg" + str(num) + '.png', img)
        print("image saved!")
        num += 1
    cv2.imshow('Img',img)

# Release and destroy all windows before termination
cap.release()

def calibrate_camera(images_folder, pattern_size=(6, 8)):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

    objpoints = []  # 3D points in real world space
    imgpoints = []  # 2D points in image plane

    images = glob.glob(images_folder + '/*.jpg')

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
            img = cv2.drawChessboardCorners(img, pattern_size, corners2, ret)
            cv2.imshow('img', img)
            cv2.waitKey(500)

    cv2.destroyAllWindows()

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    return mtx, dist

def undistort(s, camera_matrix, distortion_coefficients):
    # Read the input image
    img = cv2.imread(s)

    # Undistort the image
    undistorted_img = cv2.undistort(img, camera_matrix, distortion_coefficients)

    # Display the original and undistorted images
    cv2.imshow("Original Image", img)
    cv2.imshow("Undistorted Image", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
images_folder = "C:/Users/darsh/OneDrive/Desktop/chessimg"
camera_matrix, distortion_coefficients = calibrate_camera(images_folder)
image_path = "C:/Users/darsh/OneDrive/Desktop/1.jpg"
undistort(image_path, camera_matrix, distortion_coefficients)
