import cv2 as cv

def readVideo(video_path):
    """ 
    Read a video from a given path and return a list of frames
    """
    cap = cv.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frames.append(frame)
        else:
            break
    cap.release()
    return frames

def playVideo(frames):
    """
    Play a video from a list of frames
    """
    for frame in frames:
        cv.imshow('frame', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()