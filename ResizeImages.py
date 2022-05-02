from PIL import Image

def resizeImage(imageName):
    basewidth = 100
    img = Image.open(imageName)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(imageName)
    
l = ['a', 'b', 'c', 'd', 'f', 'g', 'k', 'o', 'p', 'y']

for i in range(0, 1001):
    for j in range(len(l)):
        resizeImage("Dataset/" + l[j] +"Images/" + l[j] +"_" + str(i) + '.png')
        

for i in range(0, 101):
    for j in range(len(l)):
        resizeImage("Dataset/" + l[j] +"Test/" + l[j] +"_" + str(i) + '.png')


