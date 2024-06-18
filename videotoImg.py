
import cv2 
import os 

# Read the video from specified path 
def convert(path):
    cam = cv2.VideoCapture(path) 
    try: 
        # creating a folder named data 
        if not os.path.exists('data'): 
            os.makedirs('data') 

    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 

    # frame 
    currentframe = 0
    counter=0
    while(True): 
        
        # reading from frame 
        ret,frame = cam.read() 
    
        if ret: 
            counter+=1
            if counter==1:
                name = './data/frame' + str(currentframe) + '.jpg'
                print ('Creating...' + name) 
                cv2.imwrite(name, frame) 
                currentframe += 1
                counter=0
        else: 
            break
    cam.release() 
    cv2.destroyAllWindows() 

