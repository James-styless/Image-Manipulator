from email.mime import image
from PIL import Image,  ImageFilter
import os   

nbanameplayers_list = ['michaeljordan', 'scottskiles', 'yutawantanbe', 'shaq', 'mauricecheeks', 'stevekerr','yaoming','billwennington','jeremylin']
type_list = ['rotate', 'resize', 'png', 'blur', 'blackandwhite']
def display(x):
    for i in x:
        print (i)
    print("")


def ChangeImage():
    while True:
        ChangeImage = input("Do you want to change the image? (y/n): ")
        if ChangeImage.lower() == "y":
            print("")
            break
        elif ChangeImage.lower() == "n":
            userImageChoice = None
            return False
        else:
            print("Invalid input, please try again and enter a valid input.")
    return True


       
def runimage():
    while True:
        global userImageChoice
        userImageChoice = None
        print("Saved images: ")
        display(nbanameplayers_list)
        userImageChoice = input("Which image do you want to change and choose a different mode? or (q) to quit: ")
        userImageChoice.lower()  
        if userImageChoice == "q":
            break     
        elif userImageChoice in nbanameplayers_list:
            Choosetheimage = Image.open(f"{userImageChoice}.jpg")
            Choosetheimage.show()
            x = ChangeImage()
            if x == False:
                continue
            elif x == True: 
                ChangeAndChooseImage()
        else:
            print("Invalid input, please try again please.")
    
    

def ChangeAndChooseImage():
    while True:
        print("Do you want to switch and change your image: ")
        display(type_list)
        userChoice = input("How would you like to change your image?: ")
        userChoice.lower()
        if userChoice in nbanameplayers_list:
            if ChangeImage() == True:
                if userChoice == type_list[0]:
                    rotateImage()
                    break
                elif userChoice == type_list[1]:
                    resizeImage()
                    break
                elif userChoice == type_list[2]:
                    pngImage()
                    break
                elif userChoice == type_list[3]:
                    BlackWhiteImage()
                    break
                elif userChoice == type_list[4]:
                    blurImage()   
                    break
        else:
            print("Invalid input\n")


#This function changes the image's position and can let you choose which way you will like the image to be
def rotateImage():
    while True:
        try:
            userDegrees = int(input("How much would you like to rotate the image by? (Degrees): "))
            break
        except ValueError:
            print("Invalid input\n")
    im = Image.open(f"{userImageChoice}.jpg")
    im.rotate(userDegrees).save('rotation folder/'+userImageChoice+'Rotated.jpg')
    print("You have succesfully rotated the image.")


#This function will create a thumbnail to your image of it's size
def resizeImage():
    size100 = (100,100)
    size200 = (200,200)
    size300 = (300,300)
    while True:
        sizeofImage = int(input("Do you want it to be 100, 200, 300: "))
        im = Image.open(f"{userImageChoice}.jpg")
        if sizeofImage== 100:
            image.thumbnailPicture(size100)
            image.save('100 jpeg/'+userImageChoice+'100.jpg')
            print("Your image has been resized successfully by 100 pixels/pixels")
            break
        elif sizeofImage== 200:
            image.thumbnailPicture(size200)
            image.save('200 jpeg/'+userImageChoice+'200.jpg')
            print("Your image has been resized successfully by 200/200 pixels.")
            break
        elif sizeofImage == 300:
            image.thumbnailPicture(size300)
            image.save('300 jpeg/'+userImageChoice+'300.jpg')
            print("Your image has been resized successfully by 300/300 pixels.")
            break
        else:
            print("Invalid input, please try again. ")



def pngImage():
    png = Image.open(f"{userImageChoice}.jpg")
    fn, fext = os.path.splitext(f"{userImageChoice}.jpg")
    Image.save('png folder/{}.png'.format(fn))
    print("Saved in png folder\n")


def BlackWhiteImage():
    ImageChoice = Image.open(f"{userImageChoice}.jpg")
    ImageConvert= image.convert("L")
    Image.saveFolder('bw folder/'+userImageChoice+'BW.jpg')
    print("Saved in bw folder\n")
    
  
#This function will blur the image and you can choose a number to blur your image by.
def blurImage():
    while True:
        try:
            BlurImage = float(input("How much do you want to blur the image by? (Please Choose a number)?: "))
            break
        except ValueError:
            print("Invalid input\n")
    """ImageOpen = Image.open(fr"{userImageChoice}.jpg")"""    
    FilterImage = Image.filter(ImageFilter.GaussianBlur(BlurImage))
    Image.save('blur folder/'+userImageChoice+'Blur.jpg')
    print("Your image has successfully been blurred and changed.")
    runimage()