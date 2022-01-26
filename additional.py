import numpy,cv2,imutils,os
discard=15
flag0="line-crossing-Exit="
flag1="line-crossing-Entry="
def capture_frame(name):
    global discard
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Couldn't initiate a videocapture object from the camera.\nExiting current app...")
    else:
        print("Camera correctly opened")

    print("=======================================\nDiscarding initial frames")
    while discard:
        success,frame=cap.read()
        if not success:
            print("Couldn't open the selected camera.\nExiting current app...")
            break
        else:
            discard-=1
    frame=cv2.resize(frame,(640,480),interpolation=cv2.INTER_CUBIC)
    filename=os.path.join(os.getcwd(),f"{name}.png")
    cv2.imwrite(filename=filename, img=frame)
    print(f"Saved the file: {filename}")
    cap.release()
    cv2.destroyAllWindows()

def change_content(path,p1,p2):
    print(f"Modifying the file in: {path} with the following points parameters \np1->{p1}\np2->{p2}\n\n\n====================================================================================\n")
    file=open(path,"r")
    newfile=f"{path[:-4]}_2.txt"
    file2=open(newfile,"w")
    data=file.readlines()
    for l in data:
        if flag0 in l:
            file2.write(flag0)
            for i in p1:
                file2.write(f"{i[0]};{i[1]};")
            file2.write(f"\n")
        elif flag1 in l:
            file2.write(flag0)
            for i in p2:
                file2.write(f"{i[0]};{i[1]};")
            file2.write("\n")
            
        else:
            file2.write(f"{l}\n")
    file.close()
    file2.close()
    os.remove(path)
    os.rename(newfile, path)
    print("File correctly formatted")
    return
