import cv2 
import dropbox
import time
import random
starttime = time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while result:
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        starttime+=time.time()
        result=False
        
    return imageName
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def uploadFile(imageName):
    accessToken="sl.A3OOhJ01u45Z4_vjOcmYv5LZErzCRaw4G1vb4sz_6Pwpq5mGk0JHlq7Q9t-DV55OISek8pdos0AEgdAGehQ9KrjWvYveLbEylFpAFxy5Un-EG4z7cCFBt2BBA7_nVcMg_yeBHto"
    file=imageName
    fileFrom=file
    fileTo="/folder2/"+imageName
    dbx=dropbox.Dropbox(accessToken)
    with open(fileFrom,"rb")as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded successfully")
        
def main():
    while True:
        if((time.time()-starttime)>=5):
            name=takeSnapshot()
            uploadFile(name)

main()