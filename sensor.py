from SimpleCV import *
import time
from time import gmtime, strftime
count = 0
cam = Camera()
threshold = 4.0 # if mean exceeds this amount do something

while True:
        previous = cam.getImage() #grab a frame
        time.sleep(0.1) #wait for 0.1 second
        current = cam.getImage() #grab another frame
        diff = current - previous
        matrix = diff.getNumpy()
        mean = matrix.mean()

        diff.show()
        current.show()
        if mean >= threshold:
                print "Motion Detected"
		while True:
		    print 'Saving : ',
		    print "image"+str(count)+".png"
		    dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		    date = dt.split(' ')[0]
		    time1 = dt.split(' ')[1]
	            current.drawText(date, 520, 430,(0, 0, 255), 24)
		    current.drawText(time1, 520, 450,(0, 0, 255), 24)
		    current.save("motionp/image"+str(count)+".bmp")
		    current.show()
   		    count += 1
	            #time.sleep(0.1)
   	            current = cam.getImage() #grab another frame
