import code
import tkinter as tk
import time
import csv 
import codetiming

list1 = [1,2,3,4,5,6,7,8,9,10]

import cv2

root = tk.Tk()

root.title("Race Builder version 0.1")
root.minsize= (800,400)

def startrace():
    
     Window1 = tk.Tk()
     Window1.title("Race Builder version 0.1 ")
     time.sleep(1)
     button2 = tk.Button(Window1, text="add particpant", command=add1).pack()
     ask = input("Ask")
     while True: 
         if ask == "et":
            exit()
        
button1 = tk.Button(root, text="Start Race", width=10, command=startrace).pack()

def add1():
        
    

        
        
        
        
        


        codetiming.Timer.start()
        def video_reader():
            cam = cv2.VideoCapture(0)
            detector = cv2.QRCodeDetector()
            while True:
                
                
                
                _, img = cam.read()
                data, bbox, _ = detector.detectAndDecode(img)
                if data:
                    
                    print("QR Code detected-->", data)
                    with open('Race1.csv', mode='a') as iris:
                        

                        ttime = codetiming.Timer.last
                        iris_writer = csv.writer(iris, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        iris_writer.writerow([data, "place not verified" ,ttime])

                        time.sleep(1)
                        
                        
                
                cv2.imshow("img", img) 

                if cv2.waitKey(1) & 0xFF == ord("Q"):
                        break
            
            
        video_reader()  
tk.mainloop()
