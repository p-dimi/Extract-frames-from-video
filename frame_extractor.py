import cv2

import os

#read the video file and assign to the cap variable

vidname = str(input('Video path with extension:'))

cap = cv2.VideoCapture(vidname)

out_folder = 'frames'

#simple counter to count the frames
counter = 0
#read the actual video and save it's frames one by one
while (cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == False:
        break
    try:
        cv2.imwrite(os.path.join(out_folder, 'frame{}.png'.format(counter)), frame)
        counter = counter + 1
    except:
        pass
    print('Frame{} completed'.format(counter))
    
print('Finished')