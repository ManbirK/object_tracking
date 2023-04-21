# awaaz nahi aa rhi aapki 

import cv2
import time
import math
  

basket_c_x = 500

basket_c_y = 300


trajectory_x = []
trajectory_y = []

video = cv2.VideoCapture("bb3.mp4")


#tracker load

tracker = cv2.TrackerCSRT_create()


# load the first frame of the video
returned, img = video.read()

#Select the bounding box on the image
#cv2.selectROI("Name of the region of interest", Image on which we want to create it )
ball_box = cv2.selectROI("Tracking", img, False)
#ballbox = [x,y,w,h]


#iniialize the tracker

tracker.init(img,ball_box)
print(ball_box)


# draw_box

def drawBox(img,ball_box):

    x,y,w,h = int(ball_box[0]),int(ball_box[1]),int(ball_box[2]),int(ball_box[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
 
#goal track
def goal_track(img,ball_box):
    x,y,w,h = int(ball_box[0]),int(ball_box[1]),int(ball_box[2]),int(ball_box[3])

    c_x = x + int(w/2)

    c_y = y + int(h/2)

    cv2.circle(img,(c_x,c_y),2, (0,255,0),4)

    cv2.circle(img,(int(basket_c_x),int(basket_c_y)),2, (0,255,0),4)

    dist = math.sqrt(((c_x-basket_c_x)**2 ) + ((c_y-basket_c_y)**2 ))
    print(dist)

    if(dist<=25):
        cv2.putText(img,"Goal",(250,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    trajectory_x.append(c_x)
    trajectory_y.append(c_y)   

    for pos in range(len(trajectory_x)-1):
        cv2.circle(img,(trajectory_x[pos],trajectory_y[pos]),2, (0,255,0),4)

     
while True:
    check,img = video.read()   

    success, ball_box = tracker.update(img)

    if success:
        drawBox(img,ball_box)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    goal_track(img,ball_box)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()

