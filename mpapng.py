import fileinput
import pwd
from traceback import print_tb
from PIL import Image,ImageSequence
from apng import APNG
import os 

basepath='base/'
outpath='/Users/jasonhuang/Desktop/untitled folder/Output/'
target_apng='eza.png' #set this by yourself 
temp='temp/'

#ascript uncomment to use 
file= [('1.png', 100), ('2.png', 100), ('3.png', 100), ('4.png', 100), ('5.png', 100), ('6.png', 100), ('7.png', 100), ('8.png', 100), ('9.png', 100), ('10.png', 100), ('11.png', 100), ('12.png', 100), ('13.png', 100), ('14.png', 100), ('15.png', 100), ('16.png', 100), ('17.png', 100), ('18.png', 100), ('19.png', 100), ('20.png', 100), ('21.png', 100), ('22.png', 100), ('23.png', 100), ('24.png', 100), ('25.png', 100), ('26.png', 100), ('27.png', 100), ('28.png', 2000), ('29.png', 100), ('30.png', 100), ('31.png', 100), ('32.png', 100), ('33.png', 100), ('34.png', 100), ('35.png', 100), ('36.png', 100), ('37.png', 100), ('38.png', 100), ('39.png', 100), ('40.png', 2000)]
 
#bscript & Cscript uncomment to use 
#file = [('1.png', 100), ('2.png', 100), ('3.png', 100), ('4.png', 100), ('5.png', 100), ('6.png', 100), ('7.png', 100), ('8.png', 100), ('9.png', 100), ('10.png', 100), ('11.png', 100), ('12.png', 100), ('13.png', 100), ('14.png', 100), ('15.png', 100), ('16.png', 100), ('17.png', 100), ('18.png', 100), ('19.png', 100), ('20.png', 100), ('21.png', 100), ('22.png', 100), ('23.png', 100), ('24.png', 100), ('25.png', 100), ('26.png', 100), ('27.png', 100), ('28.png', 100), ('29.png', 100), ('30.png', 100), ('31.png', 100), ('32.png', 2000), ('33.png', 100), ('34.png', 100), ('35.png', 100), ('36.png', 100), ('37.png', 100), ('38.png', 100), ('39.png', 100), ('40.png', 100), ('41.png', 100), ('42.png', 100), ('43.png', 100), ('44.png', 2000)]




def pastegif(baseimg):
    print(f"Now Processing {baseimg}" )
    transparent_foreground = Image.open(basepath+"/"+baseimg)
    animated_gif = Image.open(target_apng)
    fmc=1
    for frame in ImageSequence.Iterator(animated_gif):
        out = transparent_foreground.copy()
        out.convert("RGBA")
        frame=frame.convert("RGBA")
        out.paste(frame,(0,0),frame)
        out.save(temp+str(fmc)+'.png')
        fmc+=1


# im = []
# bm=[]
# for file in os.listdir('src/'):
#     if file.endswith('.png'):
#         a=str(file)[0:-4]
#         a=int(a)
#         bm.append(file)

# for num in sorted(bm):
#     a=str(num)+".png"
#     im.append(a)

# im[0].save('out.gif', save_all=True, append_images=im[1:], optimize=False, duration=300, loop=0)


# split fram from apng
# sp = APNG.open("eza.png")
# for i, (png, control) in enumerate(sp.frames):
#   png.save("{i}.png".format(i=i))



#create frmae detail and frame name, apng script
# aframe = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000]
# bile=["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png","11.png","12.png","13.png","14.png","15.png","16.png","17.png","18.png","19.png","20.png","21.png","22.png","23.png","24.png","25.png","26.png","27.png","28.png","29.png","30.png","31.png","32.png","33.png","34.png","35.png","36.png","37.png","38.png","39.png","40.png"]
# file=[]
# count=0
# for i in bile:
#     fmdetail= (i,aframe[count])
#     file.append(fmdetail)
#     count+=1


#save the apng from temp, this funtion will go in to the temp folder and craeting a apng from all pngs along the the script
def saveapng(outname):
    global file
    os.chdir(temp)
    c = APNG()
    for file, delay in file:
        c.append_file(file, delay=delay)
        c.save(outpath+outname)
    os.chdir('..')



def main():
    for png in os.listdir(basepath):
        pastegif(png) #split gif into frame and paste on then output to temp/
        saveapng(png)
    print("""

  ______                                     __              __               
 /      \                                   /  |            /  |              
/$$$$$$  |  ______   _____  ____    ______  $$ |  ______   _$$ |_     ______  
$$ |  $$/  /      \ /     \/    \  /      \ $$ | /      \ / $$   |   /      \ 
$$ |      /$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |$$ |/$$$$$$  |$$$$$$/   /$$$$$$  |
$$ |   __ $$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$    $$ |  $$ | __ $$    $$ |
$$ \__/  |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$ |$$$$$$$$/   $$ |/  |$$$$$$$$/ 
$$    $$/ $$    $$/ $$ | $$ | $$ |$$    $$/ $$ |$$       |  $$  $$/ $$       |
 $$$$$$/   $$$$$$/  $$/  $$/  $$/ $$$$$$$/  $$/  $$$$$$$/    $$$$/   $$$$$$$/ 
                                  $$ |                                        
                                  $$ |                                        
                                  $$/                                         

"""
)




if __name__ == '__main__':
    main()





#bframe =[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000]
#cframe =[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000]
#aframe =[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 2000]

