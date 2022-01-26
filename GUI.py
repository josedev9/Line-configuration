import numpy,cv2,os,sys
points_line_1=[]
count=0
frame=None

def click_function(event, x, y, flags, param):
    global points_line_1,count,frame
    if event==cv2.EVENT_LBUTTONDOWN:
        if count<4:
            points_line_1.append((x,y))
            cv2.circle(frame,(x,y),10,thickness=-1, color=(0,255,0))
        if count==3:
            cv2.line(frame, points_line_1[2], points_line_1[3], color=(0,0,255),thickness=3)
        cv2.imshow("Line configuration", frame)
        count+=1
            
            

def create_window(file):
    global points_line_1,frame
    frame=cv2.imread(file)
    print("====================================================================================")
    if frame.size==0:
        print("\n\nCouldn't open the image saved\nExiting current app...\n\n")
        sys.exit()
    else:
        print("Image correctly opened")
        initial_frame=frame.copy()
        cv2.resize(frame, (640,480),cv2.INTER_CUBIC)
        cv2.namedWindow("Line configuration")
        cv2.setMouseCallback("Line configuration", click_function)
        while True:
                cv2.imshow("Line configuration", frame)
                key=cv2.waitKey(0) & 0XFF
                if key == ord('q'):
                    points_line_2=points_line_1.copy() #I hate python sometimes
                    points_line_2[0],points_line_2[1]=points_line_2[1],points_line_2[0]
                    cv2.destroyAllWindows()
                    return points_line_1,points_line_2
                elif key==ord('r'):
                    frame=initial_frame.copy()
                    points_line_1.clear()
