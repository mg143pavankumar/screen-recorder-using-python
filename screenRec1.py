# importing the required packages
import pyautogui
import cv2
import numpy as np
import datetime


# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"{time_stamp}.mp4"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 10.0


# Creating a VideoWriter object
out = cv2.VideoWriter(file_name, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

# X and Y coordinates of mouse pointer
Xs = [0, 8, 6, 14, 12, 4, 2, 0]
Ys = [0, 2, 4, 12, 14, 6, 8, 0]


while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    mouseX, mouseY = pyautogui.position()
    mouseX *= 1
    mouseY *= 1

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Synthesize mouse pointer
    Xthis = [3.5*x+mouseX for x in Xs]
    Ythis = [3.5*y+mouseY for y in Ys]
    points = list(zip(Xthis, Ythis))
    points = np.array(points, 'int32')
    cv2.fillPoly(frame, [points], color=[255, 255, 255])

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
