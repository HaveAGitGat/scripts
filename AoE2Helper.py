import keys as k
from grabscreen import grab_screen
import cv2

import time

import numpy as np

import time  #for delays


#for text to speech
import pyttsx3
engine = pyttsx3.init()


from tkinter import * 

# import the necessary packages for image to text
from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


keys = k.Keys({})

#stats box width is 392 width, 24 height
# WIDTH = 392
# HEIGHT= 24



RESIZE_FACTOR = 0.5 #Screen resize factor 
SHOW_CAPTURE = True #Set to false if you don't want to see the captured screen


wood_Value = 0
food_Value = 0
gold_Value = 0
stone_Value = 0


wood_QuoFloor = 0
food_QuoFloor = 0
gold_QuoFloor = 0
stone_QuoFloor = 0



wood_OldTime = time.monotonic()
wood_OldValue = 0

food_OldTime = time.monotonic()
food_OldValue = 0

gold_OldTime = time.monotonic()
gold_OldValue = 0

stone_OldTime = time.monotonic()
stone_OldValue = 0



temp = 0

# a = time.monotonic()
# b = time.monotonic()
# print(b-a)



while True:

#edge of stats box is 10 to 397

    def readStats(Material,StartWidth,EndWidth):

        WIDTH = EndWidth - StartWidth
        #default
        HEIGHT= 15

        #test
        #HEIGHT= 200

        screen = cv2.resize(grab_screen(region=(StartWidth,5,(StartWidth+WIDTH),(5+HEIGHT))), (int((WIDTH-0)/RESIZE_FACTOR),int((HEIGHT-0)/RESIZE_FACTOR)))

        #screen = cv2.resize(grab_screen(region=(10,145,397,(145+24))),(2,2))

        image_np = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

        image_np = cv2.bitwise_not(image_np)

        image_np_expanded = np.expand_dims(image_np, axis=0)



        if SHOW_CAPTURE:

            cv2.imshow('Press q to quit',image_np)

        # load the example image and convert it to grayscale
        image = image_np

        # lower_white = np.array([255,255,255])
        # upper_white = np.array([255,255,255])

        #gray = cv2.inRange(image, lower_white, upper_white)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # gray = cv2.medianBlur(gray, 3)
    
        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        text = pytesseract.image_to_string(Image.open(filename))
        #os.remove(filename)


        print(text+" "+Material)
        #test
        # engine.say(text+" "+Material)
        # engine.runAndWait() 
     
        if Material=="Wood":

            global wood_QuoFloor
            temp = wood_QuoFloor

            try:
                wood_Value = int(text)
                wood_QuoFloor = int(wood_Value/100)


                global wood_OldTime    
                TimeDifference = time.monotonic() - wood_OldTime

                if TimeDifference >= 10:                

                    wood_OldTime = time.monotonic()
                    global wood_OldValue
                    MaterialDifference = wood_Value - wood_OldValue
                    wood_OldValue = wood_Value


                    MaterialPerMin =((float(MaterialDifference)/TimeDifference)*(60))
                    MaterialPerMin = str(round(MaterialPerMin, 2))


                    file = open(r"D:\Stats\woodPerMin.txt","w") 
                    file.write(MaterialPerMin)
                    file.close() 



            except:    
                print("Something went wrong with wood stats")  


            if wood_QuoFloor != temp:
                engine.say(text+" "+Material)
                engine.runAndWait() 





        if Material=="Food":
            global food_QuoFloor
            temp = food_QuoFloor

            try:
                food_Value = int(text)
                food_QuoFloor = int(food_Value/100)

            except:    
                print("Something went wrong")  


            if food_QuoFloor != temp:
                engine.say(text+" "+Material)
                engine.runAndWait() 







        if Material=="Gold":
            global gold_QuoFloor
            temp = gold_QuoFloor

            try:
                gold_Value = int(text)
                gold_QuoFloor = int(gold_Value/100)

            except:    
                print("Something went wrong")  


            if gold_QuoFloor != temp:
                engine.say(text+" "+Material)
                engine.runAndWait()  









        if Material=="Stone":
            global stone_QuoFloor
            temp = stone_QuoFloor

            try:
                stone_Value = int(text)
                stone_QuoFloor = int(stone_Value/100)

            except:    
                 print("Something went wrong")  


            if stone_QuoFloor != temp:
                engine.say(text+" "+Material)
                engine.runAndWait() 



        if Material=="Pop":

          

            
            try:
                print("h1")


                pop_Value = text
                pop_Value = pop_Value.split('/')

                print("h2")

                pop_Value1= pop_Value[0].strip()
                pop_Value2= pop_Value[1].strip()
                
                
                print("P1-"+pop_Value1)
                print("P2-"+pop_Value2)

            

                pop_Value1= int(pop_Value1)
                pop_Value2= int(pop_Value2)

  

           # print("P1-"+pop_Value1)
           # print("P2-"+pop_Value2)

            

                if (pop_Value2 - pop_Value1) <= 5:
                    engine.say("Build a house")
                    engine.runAndWait()  

                    #keys.directKey("h")
                    #keys.directKey("a")


            except:    
                print("Could not convert pop to int")


                

    readStats("Wood",29,75) 
    readStats("Food",108,152) 
    readStats("Gold",201,229) 
    readStats("Stone",259,305)   
    readStats("Pop",340,385) 


    #readStats("Pop",325,385)   


    #test
    #readStats("Pop",0,500) 

    if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break  


