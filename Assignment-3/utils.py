import numpy as np

SSD = lambda window1, window2: np.sum((window1.astype("float") - window2.astype("float")) ** 2)
SAD = lambda window1, window2: np.sum(np.abs(window1.astype("float") - window2.astype("float")))

def block_matching(img1, img2, window_size=3, max_disparity=16, metric=SSD):
    # Get the shape of the image
    height, width = img1.shape
    # Define the disparity map
    disparity_map = np.zeros((height, width), np.uint8)
    # Define the half window
    half_window = window_size // 2
    # Loop through every pixel in the left image progress bar
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

