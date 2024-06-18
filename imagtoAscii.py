from PIL import Image
import math


#---opening image file 
def getimage(path):
    im=Image.open(path)
    return im



#----resizing the image---------
def resizeandgreyfy(im):
    width,height=im.size
    im1=im.resize((math.ceil(width*0.2), math.ceil(height*0.2*0.42)),Image.Resampling.LANCZOS)
    im1=im1.convert('L')
    return im1


#----loading pixel data---------
def pixdata(im2):
    return list(im2.getdata())
    

#----mapping the correspoinding pixel value with text---------
def getting_char(xp):
    line=" `.-:_><+*?pMQ%@"
    # print(xp)
    # print(line[xp//17])
    return line[xp//17]


def imgtoAscii(path):
    image=getimage(path)
    image=resizeandgreyfy(image)
    w,h=image.size
    pixel=pixdata(image)
    ll=[]
    txt=[]
    #-----wiiting in file-------
    for i in range(h):
        for j in range(w):
            x=pixel[i*w+j]
            ll.append(getting_char(x))
        text=''.join(ll)
        txt.append(text)
        ll=[]
    finaltext='\n'.join(txt)
    print(finaltext)


if __name__=='__main__':
    imgtoAscii("images.jpeg")
#     print(imgtoAscii("profile1.jpg"))
    
