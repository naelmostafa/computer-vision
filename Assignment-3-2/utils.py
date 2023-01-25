import cv2
import numpy as np
import os
import imageio


def get_rectangle(frame):
    """
    Select ROI on certain image by marking it with a rectangle
    Returns rectangle coordinates as [x,y,w,h]
    """
    # Define a variable to store the coordinates of the rectangle
    rect = [0, 0, 0, 0]
    
    # Make a copy of the frame
    img = frame.copy()
    
    # Define the mouse callback function
    def select_rectangle(event, x, y, flags, param):
        nonlocal rect
        if event == cv2.EVENT_LBUTTONDOWN:
            rect[0] = x
            rect[1] = y
        elif event == cv2.EVENT_LBUTTONUP:
            rect[2] = x - rect[0]
            rect[3] = y - rect[1]

    # Set the mouse callback function for the window
    cv2.namedWindow("Select rectangle")
    cv2.setMouseCallback("Select rectangle", select_rectangle)
    # draw rectangle
    
    
    while(True):
        # Show the frame
        cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 2)
        cv2.imshow("Select rectangle", img)

        # Exit if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the display window
    cv2.destroyAllWindows()
    
    return rect


def play_video(frames, type='array'):
    """
    Play a video from a list of frames or np array
    """

    frame_count = lambda : frames.shape[-1] if type == 'array' else len(frames)
    frame_idx = lambda i: frames[...,i] if type == 'array' else frames[i]

    print("Playing video ....")
    print("Press q to exit")
    for i in range(frame_count()):
        cv2.imshow('frame', frame_idx(i))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()



def getWarpMat(p):
    """
    Returns (2x3) affine transformation matrix given 6 transform parameters
    """
    W = np.array([[1 + p[0],     p[2],  p[4]],
                  [    p[1], 1 + p[3],  p[5]]])
    return W 


def getUnrolledPts(Image, ROI):
    """
    Flattens 2D region of image into 1D array based on ROI provided
    """
    x, y, w, h = ROI
    # Array to store flattened pixel locations, each element consists of [x, y, 1]
    unrolledPts = np.empty([h*w,3])

    n = 0
    for i in range(x, x+w):
        for j in range(y, y+h):
            unrolledPts[n,0] = i
            unrolledPts[n,1] = j
            unrolledPts[n,2] = 1
            n+=1

    # Array to store flattened pixel values, each element consists of intensity value from original image
    unrolledIntensity = np.empty(h*w)
    for i, pt in enumerate(unrolledPts):
        unrolledIntensity[i] = Image[int(pt[1]),int(pt[0])]

    return unrolledPts, unrolledIntensity
    

def warpPoints(Image, warpMat, templatePts, gradientX, gradientY):
    """
    Performs affine warp on a given set of points using a given warp matrix
    Returns warped pixel locations, warped pixel values, and warped gradient values
    """
    h, w = Image.shape

    # Warping points
    warpedImgPts = np.matmul(warpMat, templatePts.T).astype(int)

    # Clipping points out of image dimensions
    warpedImgPts[1,:] = np.clip(warpedImgPts[1,:], 0, h-1)
    warpedImgPts[0,:] = np.clip(warpedImgPts[0,:], 0, w-1)

    # Assigning Intensities and gradients to warped points
    warpedImgIntensities = Image[warpedImgPts[1,:].astype(int),warpedImgPts[0,:].astype(int)]
    gradXValues = gradientX[warpedImgPts[1,:].astype(int),warpedImgPts[0,:].astype(int)]
    gradYValues = gradientY[warpedImgPts[1,:].astype(int),warpedImgPts[0,:].astype(int)]
     
    return warpedImgPts, warpedImgIntensities, gradXValues, gradYValues


def getJacobian(templatePts):
    """
    Returns jacobian matrix based on given set of [x,y] corrdinates
    """

    x = np.array(templatePts[...,0])
    y = np.array(templatePts[...,1])

    ones = np.ones(templatePts.shape[0])
    zeros = np.zeros(templatePts.shape[0])

    row1 = np.stack((x, zeros, y, zeros, ones, zeros), axis=1)
    row2 = np.stack((zeros, x, zeros, y, zeros, ones), axis=1)
    jacob = np.stack((row1, row2), axis=1)

    return jacob

def save_as_npy(frames, filename):
    """
    Saves a list of frames as a npy file
    """
    if os.path.exists(filename):
        print("File already exists")
        return
    np.save(filename, frames)
    print("Saved as", filename)

def save_as_gif(frames, filename, fps=10, duration=0.02):
    """
    Saves a list of frames as a gif file
    """
    if os.path.exists(filename):
        print("File already exists")
        return
    frames = frames[::2]
    # reduce the resolution of the frames
    frames = [cv2.resize(frame, (0,0), fx=0.5, fy=0.5) for frame in frames]
    imageio.mimsave(filename, frames, fps=fps, duration=duration, subrectangles=True)
    print("Saved as", filename)
