import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


# Database setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://smartattendancesys-599de-default-rtdb.firebaseio.com/",
    'storageBucket': "smartattendancesys-599de.appspot.com"
})

# Importing the student images
folderPath = 'Images'
pathList=os.listdir(folderPath)
pathList.sort()
print(pathList)
imgList=[]
studentIds=[]

# Extracting the Student ids from the images
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])
#print(studentIds)

    fileName= f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob=bucket.blob(fileName)
    blob.upload_from_filename(fileName)

def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)     # Step 1
        encode=face_recognition.face_encodings(img)[0]    # Step 2
        encodeList.append(encode)

    return encodeList


print("Encoding Started...")
encodeListKnown=findEncodings(imgList)
print(encodeListKnown)
encodeListKnownWithIds=[encodeListKnown,studentIds]
print("Encoding Complete")

# Dumping all the encodings corresponding to the student ids in a pickle file
file=open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File saved")