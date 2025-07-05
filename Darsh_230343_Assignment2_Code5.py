import cv2
import numpy as np
import glob

chessboardSize = (8,6)
frameSize = (640,480)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 20
objp = objp * size_of_chessboard_squares_mm

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob(r"C:\Users\darsh\OneDrive\Desktop\chessimg\calibrated1.png")

for image in images:

    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, chessboardSize, None)

    # If found, add object points, image points (after refining them)
    if ret == True:

        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(0)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, frameSize, None, None)

print("Camera Matrix",mtx)

def pose_estimation(frame, aruco_dict_type, matrix_coefficients, distortion_coefficients):

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	arucoDict=cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
	arucoParams=cv2.aruco.DetectorParameters_create()
	corners, ids, rejected_img_points=cv2.aruco.detectMarkers(gray,arucoDict,parameters=arucoParams)
    
   	 
	if len(corners) > 0:
		for i in range(0, len(ids)):
			rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 50, matrix_coefficients,distortion_coefficients)
			cv2.aruco.drawDetectedMarkers(frame, corners)
			cv2.drawFrameAxes(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 5)
			print(tvec)
	return frame,arucoDict,arucoParams

cap=cv2.VideoCapture(0)
    
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while cap.isOpened():
	ret,img=cap.read()
	h,w,_=img.shape
	width=1000
	height=int(width*(h/w))
	img=cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)
	intrinsic_camera = np.array(((207.66132141,0,251.41218615),(0,205.751007,338.91119239),(0,0,1)))
	distortion = np.array(( 0.07640411,-0.06229856,0.01462332,0.0039293,0.00467759))

	detected_markers=pose_estimation(img,cv2.aruco.DICT_4X4_50,intrinsic_camera,distortion)
	#corners,ids,rejected=cv2.aruco.detectMarkers(img,arucoDict,parameters=arucoParams)
	#detected_markers=aruco_display(corners,ids,rejected,img)
	cv2.imshow("Image",detected_markers)

	key=cv2.waitKey(1)

	if key == 27:
		break
cv2.destroyAllWindows()
cap.release()

def markers(s):
    # Read the input image
    img = cv2.imread(s)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the ArUco dictionary and parameters
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters_create()

    # Detect markers in the image
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None and len(ids) == 1:
        # Draw bounding box for the detected marker
        img = cv2.aruco.drawDetectedMarkers(img, corners, ids)

        # Estimate pose for the detected marker
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 1, mtx, dist)

        # Extract translation and rotation vectors for the first marker
        rvec = rvecs[0][0]
        tvec = tvecs[0][0]

        # Compute the center of the marker
        xc, yc = corners[0][0].mean(axis=0)

        # Compute pose axes for the detected marker
        axis_length = 50
        axis_points, _ = cv2.projectPoints(np.array([[axis_length, 0, 0], [0, axis_length, 0], [0, 0, axis_length]]), rvec, tvec, mtx, dist)
        axis_points = axis_points.astype(int)

        # Draw axes on the image
        img = cv2.line(img, tuple(corners[0][0][0]), tuple(axis_points[0][0]), (0, 0, 255), 5)  # x-axis (red)
        img = cv2.line(img, tuple(corners[0][0][0]), tuple(axis_points[1][0]), (0, 255, 0), 5)  # y-axis (green)
        img = cv2.line(img, tuple(corners[0][0][0]), tuple(axis_points[2][0]), (255, 0, 0), 5)  # z-axis (blue)

        # Display the final output image
        cv2.imshow("Detected Marker", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Return translation vector, rotation vector, and marker center
        return tvec, rvec, xc, yc

    else:
        print("No ArUco marker found in the image or multiple markers detected.")
        return None

# Example usage:
# Provide the path to the camera calibration images or use the mtx and dist obtained from previous calibration
# mtx, dist = calibrate_camera("path/to/calibration/images")
markers(r"C:\Users\darsh\OneDrive\Desktop\aruco.png")
