import numpy as np
from tqdm import tqdm

SSD = lambda window1, window2: np.sum((window1.astype("float") - window2.astype("float")) ** 2)
SAD = lambda window1, window2: np.sum(np.abs(window1.astype("float") - window2.astype("float")))

def block_matching(img1, img2, window_size=3, max_disparity=16, metric=SSD):
    # Get the shape of the image
    height, width = img1.shape
    # Define the disparity map
    disparity_map = np.zeros((height, width), np.uint8)
    # Define the half window
    half_window = window_size // 2
    # Loop through every pixel in the left image
    for y in range(half_window, height - half_window):
        for x in range(half_window, width - half_window):
            # Get the current window
            window = img1[y - half_window: y + half_window + 1, x - half_window: x + half_window + 1]
            # Define the minimum SSD
            min_metric = 255 * window_size * window_size
            # Define the best disparity
            best_disparity = 0
            # Loop through every possible disparity
            for d in range(max_disparity):
                # Check if we are within the image bounds
                if x - d - half_window >= 0:
                    # Get the current window from the right image
                    current_window = img2[y - half_window: y + half_window + 1, x - d - half_window: x - d + half_window + 1]
                    # Calculate the SSD / SAD
                    m = metric(window, current_window)
                    # Check if the SSD / SAD is smaller than the minimum metric
                    if m < min_metric:
                        # Update the minimum metric
                        min_metric = m
                        # Update the best disparity
                        best_disparity = d
            # Update the disparity map
            disparity_map[y, x] = best_disparity
    return disparity_map


matchCost = lambda pixelL, pixelR, sigma: ((pixelL.astype('float') - pixelR.astype('float'))**2 // sigma**2)

def dp_forwardpass(imgLeft, imgRight, sigma, c0):

    (heightL, widthL), (heightR, widthR) = imgLeft.shape, imgRight.shape
    height = min(heightL, heightR)
    
    # Define the cost matrix
    cost_matrix = np.zeros((height, widthL, widthR), dtype='float16')

    # Computing Forward Pass
    for scanline in tqdm(range(height)):
        # Initializing first row and column of cost matrix
        for i in range(widthL):
            cost_matrix[scanline][i][0] = i*c0
        for i in range(widthR):
            cost_matrix[scanline][0][i] = i*c0

        # Computing optimal cost
        for i in range(1, widthL):
            for j in range(1, widthR):

                costs = [cost_matrix[scanline][i-1][j-1] + matchCost(imgLeft[scanline][i], imgRight[scanline][j], sigma),
                        cost_matrix[scanline][i-1][j] + c0,
                        cost_matrix[scanline][i][j-1] + c0]

                cost_matrix[scanline][i][j] = min(costs)

    return cost_matrix

def dp_backpass(cost_matrix):

    height, widthL, widthR = cost_matrix.shape[0], cost_matrix.shape[1], cost_matrix.shape[2]

    # Define the disparity maps
    disparity_mapL = np.zeros((height, widthL), dtype='float16')
    disparity_mapR = np.zeros((height, widthR), dtype='float16')

    # Computing Back Pass
    for scanline in range(height):
        
        i = widthL-1; j = widthR-1
        while (i > 0 and j > 0):
            _min = np.argmin([cost_matrix[scanline][i-1][j-1], cost_matrix[scanline][i-1][j], cost_matrix[scanline][i][j-1]])
            if _min == 0: # Pixels i and j match
                disparity_mapL[scanline][i] = np.abs(j - i)
                disparity_mapR[scanline][j] = np.abs(j - i)
                i-=1; j-=1
            elif _min == 1: # Pixel i is occluded   
                disparity_mapL[scanline][i] = 0
                i-=1
            else: # Pixel j is occluded
                disparity_mapR[scanline][j] = 0
                j-=1

    return disparity_mapL, disparity_mapR