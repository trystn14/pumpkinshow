import board
import time
import neopixel
import random

NUM_PIXELS = 10
np = neopixel.NeoPixel(board.NEOPIXEL, NUM_PIXELS, auto_write = False, brightness=0.2)

#These global constants set the colors and speed of the flame. 
fcolors = [(255, 0, 0), (255, 50, 0), (255, 20, 0), (255, 63, 0), (0, 0, 0)]
speed = [(0.072), (0.09), (0.067), (0.075), (0.083)]
'''
Function: fire

Description: This function simulates a candle flame burning. 

Parameters: num_times- This is how long the function will last.

Return value: none.
'''
def fire(num_times = 50):
    for i in range(num_times):
        np.fill(fcolors[2])
        for j in range(NUM_PIXELS):
            rand_int = random.randrange(0, NUM_PIXELS)
            np[rand_int] = random.choice(fcolors)
        np.show()
        time.sleep(random.choice(speed))
        np[rand_int] = fcolors[2]
        np.show()

'''These globals set the random values needed for lightning. This includes
    the colors for the flash, number of flashes, time between flashes, and the time the
    flashes are on'''
back = ((17, 7, 22))
lcolors = [(255, 255, 255), (200, 200, 255), (120, 120, 120)]
num_flash = [i + 1 for i in range(4)]
timeb = random.randint(4, 10)
timeo = [(0.1), (0.07), (0.17), (0.2), (0.24)]
'''
Function: lightning

Description: This function simulates what lightning would look like. 

Parameters: numtimes- This is how many actual flash seqences you will see.

Return value: Prints the number of flash sequences.
'''
def lightning(numtimes = 5):
    for i in range(numtimes):
        np.fill(back)
        np.show()
        time.sleep(timeb)#time in between
        for j in range(random.choice(num_flash)):
            np.fill(random.choice(lcolors))
            np.show()
            time.sleep(random.choice(timeo))#time on
            np.fill(back)
            np.show()
        print(i)
        
'''
Function: sparkle

Description: This function has a background color and then a random neopixel sparkles. 

Parameters: spark_color- color of the sparkle, back_color- color of the background,
    speed- this is the speed that the sparkles sparkle, num_sparkles- how many sparkles.

Return value: none.
'''
def sparkle(spark_color = [255, 255, 255], back_color = [0, 0, 0], speed = 0.05, num_sparkles = 1):
    for i in range(50):
        np.fill(back_color)
        for j in range(num_sparkles):
            rand_int = random.randrange(0, 10)
            np[rand_int] = spark_color
        np.show()
        time.sleep(speed)
        np[rand_int] = back_color
        np.show()

defcolor = (255, 255, 255)
color1 = [defcolor[0], defcolor[1], defcolor[2]]
'''
Function: fade_out

Description: this function fades out with the color.

Parameters: defaultcolor- what color fades out, speed- how fast the color fades out.

Return value: this function prints the values of red, green, and blue.
'''
def fade_out(defaultcolor, delay = 0.005):
    fadeR = defaultcolor[0]/256.0
    fadeG = defaultcolor[1]/256.0
    fadeB = defaultcolor[2]/256.0
    for i in range(256):
        color1[0] = int (defaultcolor[0] - (fadeR*i))
        color1[1] = int (defaultcolor[1] - (fadeG*i))
        color1[2] = int (defaultcolor[2] - (fadeB*i))
        np.fill(color1)
        time.sleep(delay)
        np.show()
        
'''
Function: fade_in

Description: this function fades in with the color.

Parameters: defaultcolor- what color fades in, speed- how fast the color fades in.

Return value: this function prints the values of red, green, and blue.
'''
def fade_in(defaultcolor, delay = 0.005):
    fadeR = defaultcolor[0]/256.0
    fadeG = defaultcolor[1]/256.0
    fadeB = defaultcolor[2]/256.0
    for i in range(256):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        time.sleep(delay)
        np.show()
        
while True:
    fire()
    fade_in([0, 175, 0])
    time.sleep(1)
    fade_out([0, 175, 0])
    time.sleep(.05)
    fade_in([100, 0, 175])
    time.sleep(1)
    fade_out([100, 0, 175])
    time.sleep(.05)
    sparkle([100, 0, 175], [0, 255, 0], 0.05, 3)
    for i in range(5):
        fade_in([255, 63, 0])
        time.sleep(1)
        fade_out([255, 20, 0])
        time.sleep(.05)
    lightning()
        
