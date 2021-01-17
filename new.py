import time
import dropbox
import cv2
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(1,100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot taken")
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = 'RZSCy2zyE_YAAAAAAAAAAf6OvC8czkqOFLqZ4N7miDA7lEFC7RGK4DLCShnX5sFo'
    file = img_name
    file_from = file
    file_to = '/test/'+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()