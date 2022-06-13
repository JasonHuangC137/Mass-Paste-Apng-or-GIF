# Mass-Paste-Apng-or-GIF
When you need to paste a png or gif to a massive amount of picture. GIF only support  8 bit color option, not 24 bit as png does.

Purpose of this app? 
When you need to paste a mass amount of gif or apng (usually with transparant background), you can use this app

Require depedency: 
PIL for python image processing
$ pip install pillow 
Apng $
pip install apng

Setup

1. put all the picture that you wanna use as a base image into the 'base' folder
2. put the gif or apng you wanna paste on, at the root folder
3. Set up all the varaibles in mpapng.py :
    location basepath='base/' -> where you keep your base image 
    outpath='Output/' -> where you wanna output your file 
    target_apng='' -> the gif or apng to paste onto the base image 
    temp='temp/' -> just a tempory file, you can ignore
4. use the script setter to set the script or just paste your script as following form 
    file=[('frame1.png = int, duration = int),(frame2, duration2)....] you can use a "apng JS" to analyze your apng or other gif frame data
5. run mpapng.py and you will see all the out at the Output folder
