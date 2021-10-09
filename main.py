import machine
from ws2812 import WS2812
from matrix2812 import matrix2812
import utime
import urandom

#Define the WS1812 nanopixels with 121 lights.
ws = WS2812(machine.Pin(0),121)

#Define the LED matrix as an 11 by 11 grid (starts counting at 0)
myMatrix = matrix2812(10, 10)
daysToLight = []


"""LED Colors"""
white = 0xFFFFFF
green = 0x2FFF00
pure_green = 0x00FF00
dim_green = 0x002000
red = 0xFF0000
dim_red=0x200000
blue = 0x0004FF
dim_blue = 0x000020
purple = 0x8700FB
dim_purple = 0x100020
orange = 0xFF6000
dim_orange = 0x200F00
yellow = 0xFDFF00
dim_yellow = 0x202000
pink = 0xFF00F4
dim_pink = 0x200015
teal = 0x00FFEC
dim_teal = 0x002014
ltblue = 0x009FFF
off = 0x000000
color_seed = 0x000001
very_dim_white = 0x010101
dim_white = 0x404040
mid_white=0x808080
"""clock_color is the color LED you want for the clock display."""
clock_color = mid_white
week_color = dim_blue
day_color = dim_purple
intro_color = blue
intro_color2 = purple


"""Test of list with LED name then color to light it"""
FULL_ARRAY = [0, blue, 1, red, 2, green, 3, off, 4, yellow]

"""Non-Time Words"""
HI = [myMatrix.nameLED(0, 9), intro_color, myMatrix.nameLED(1, 9), intro_color]
BECKY = [myMatrix.nameLED(10, 6), intro_color, myMatrix.nameLED(10, 7), intro_color, myMatrix.nameLED(10, 8), intro_color,  myMatrix.nameLED(10, 9), intro_color, myMatrix.nameLED(10, 10), intro_color]
GOOD = [myMatrix.nameLED(0,8), intro_color2, myMatrix.nameLED(1, 8), intro_color2, myMatrix.nameLED(2, 8), intro_color2, myMatrix.nameLED(3, 8), intro_color2]
DAY = [myMatrix.nameLED(2,9), intro_color2, myMatrix.nameLED(3, 9), intro_color2, myMatrix.nameLED(4, 9), intro_color2]

"""Weekday Matrix"""
SMTWTFS = [myMatrix.nameLED(0, 10), myMatrix.nameLED(1, 10), myMatrix.nameLED(2, 10),  myMatrix.nameLED(3, 10), myMatrix.nameLED(4, 10), myMatrix.nameLED(5, 10), myMatrix.nameLED(6, 10)]


"""Clock Word Definitions"""
IT_IS = [myMatrix.nameLED(0,0), clock_color, myMatrix.nameLED(1, 0), clock_color, myMatrix.nameLED(3, 0), clock_color, myMatrix.nameLED(4, 0), clock_color]
#M_ items are minute words
M_FIVE = [myMatrix.nameLED(7,1), clock_color, myMatrix.nameLED(8, 1), clock_color, myMatrix.nameLED(9, 1), clock_color, myMatrix.nameLED(10, 1), clock_color]
M_TEN =[myMatrix.nameLED(0,3), clock_color, myMatrix.nameLED(1, 3), clock_color, myMatrix.nameLED(2, 3), clock_color]
M_QUARTER = [myMatrix.nameLED(0,2), clock_color, myMatrix.nameLED(1, 2), clock_color, myMatrix.nameLED(2, 2), clock_color, myMatrix.nameLED(3, 2), clock_color, myMatrix.nameLED(4, 2), clock_color, myMatrix.nameLED(5, 2), clock_color, myMatrix.nameLED(6, 2), clock_color]
M_TWENTY = [myMatrix.nameLED(0,1), clock_color, myMatrix.nameLED(1, 1), clock_color, myMatrix.nameLED(2,1), clock_color, myMatrix.nameLED(3, 1), clock_color, myMatrix.nameLED(4, 1), clock_color, myMatrix.nameLED(5, 1), clock_color]
M_TWENTYFIVE = M_TWENTY + M_FIVE
M_HALF = [myMatrix.nameLED(7,2), clock_color, myMatrix.nameLED(8, 2), clock_color, myMatrix.nameLED(9, 2), clock_color, myMatrix.nameLED(10, 2), clock_color]

#before/after the halfway point:
PAST = [myMatrix.nameLED(4,3), clock_color, myMatrix.nameLED(5, 3), clock_color, myMatrix.nameLED(6, 3), clock_color, myMatrix.nameLED(7, 3), clock_color]
TO = [myMatrix.nameLED(7,3), clock_color, myMatrix.nameLED(8, 3), clock_color]

#Hour words:
H_ONE = [myMatrix.nameLED(8,7), clock_color, myMatrix.nameLED(9, 7), clock_color, myMatrix.nameLED(10, 7), clock_color]
H_TWO = [myMatrix.nameLED(6,7), clock_color, myMatrix.nameLED(7, 7), clock_color, myMatrix.nameLED(8, 7), clock_color]
H_THREE = [myMatrix.nameLED(0,5), clock_color, myMatrix.nameLED(1,5), clock_color, myMatrix.nameLED(2,5), clock_color, myMatrix.nameLED(3,5), clock_color, myMatrix.nameLED(4,5), clock_color]
H_FOUR = [myMatrix.nameLED(0,6), clock_color, myMatrix.nameLED(1, 6), clock_color, myMatrix.nameLED(2, 6), clock_color, myMatrix.nameLED(3, 6), clock_color]
H_FIVE = [myMatrix.nameLED(5,8), clock_color, myMatrix.nameLED(8, 8), clock_color, myMatrix.nameLED(7, 8), clock_color, myMatrix.nameLED(9, 8), clock_color]
H_SIX = [myMatrix.nameLED(8,4), clock_color, myMatrix.nameLED(9, 4), clock_color, myMatrix.nameLED(10, 4), clock_color]
H_SEVEN = [myMatrix.nameLED(0,4), clock_color, myMatrix.nameLED(1,4), clock_color, myMatrix.nameLED(2,4), clock_color, myMatrix.nameLED(3,4), clock_color, myMatrix.nameLED(4,4), clock_color]
H_EIGHT = [myMatrix.nameLED(4,5), clock_color, myMatrix.nameLED(5,5), clock_color, myMatrix.nameLED(6,5), clock_color, myMatrix.nameLED(7,5), clock_color, myMatrix.nameLED(8,5), clock_color]
H_NINE = [myMatrix.nameLED(4,4), clock_color, myMatrix.nameLED(5, 4), clock_color, myMatrix.nameLED(6, 4), clock_color, myMatrix.nameLED(7, 4), clock_color]
H_TEN = [myMatrix.nameLED(8,5), clock_color, myMatrix.nameLED(9, 5), clock_color, myMatrix.nameLED(10, 5), clock_color]
H_ELEVEN = [myMatrix.nameLED(0,7), clock_color, myMatrix.nameLED(1,7), clock_color, myMatrix.nameLED(2,7), clock_color, myMatrix.nameLED(3,7), clock_color, myMatrix.nameLED(4,7), clock_color, myMatrix.nameLED(4,7), clock_color]
H_TWELVE = [myMatrix.nameLED(4,6), clock_color, myMatrix.nameLED(5,6), clock_color, myMatrix.nameLED(6,6), clock_color, myMatrix.nameLED(7,6), clock_color, myMatrix.nameLED(8,6), clock_color, myMatrix.nameLED(9,6), clock_color]

OCLOCK = [myMatrix.nameLED(5,9), clock_color, myMatrix.nameLED(6,9), clock_color, myMatrix.nameLED(7,9), clock_color, myMatrix.nameLED(8,9), clock_color, myMatrix.nameLED(9,9), clock_color, myMatrix.nameLED(10,9), clock_color]

"""Variable definitions for time telling from system clock"""
am_pm=0
hour = 0
current_time = utime.localtime()
hour24 =current_time[3]
minute=current_time[4]
second=current_time[5]
weekday=current_time[6]

#year=current_time[0]
#month=current_time[1]
#mday=current_time[2]
#yearday=current_time[7]

""" This function assigns the correct hour word for the current time """
def lightHours(hours, minutes):
    if minutes > 30:
            hours += 1
            if hours == 25:
                hours = 0
    if hours == 0 or hours ==12:
        hourWord = H_TWELVE
        if minutes<3:
            lightDay()
    elif hours == 1 or hours == 13:
        hourWord = H_ONE
    elif hours == 2 or hours == 14:
        hourWord = H_TWO
    elif hours == 3 or hours == 15:
        hourWord = H_THREE
    elif hours == 4 or hours == 16:
        hourWord = H_FOUR
    elif hours == 5 or hours == 17:
        hourWord = H_FIVE
    elif hours == 6 or hours == 18:
        hourWord = H_SIX
    elif hours == 7 or hours == 19:
        hourWord = H_SEVEN
    elif hours == 8 or hours == 20:
        hourWord = H_EIGHT
    elif hours == 9 or hours == 21:
        hourWord = H_NINE
    elif hours == 10 or hours == 22:
        hourWord = H_TEN
    elif hours == 11 or hours == 23:
        hourWord = H_ELEVEN
    return hourWord
    ###

""" This function assigns the correct minute word for the current time """
def lightMinutes(minutes, hours):
    minuteWord = []
    if minutes < 3:
        minuteWord = [] #NOTE: this used to say 0.  I changed it to an empty array in hopes that it would work properly...
    elif minutes < 8:
        minuteWord = M_FIVE + PAST
    elif minutes < 13:
        minuteWord = M_TEN + PAST
    elif minutes < 18:
        minuteWord = M_QUARTER + PAST
    elif minutes < 23:
        minuteWord = M_TWENTY + PAST
    elif minutes < 28:
        minuteWord = M_TWENTYFIVE + PAST
    elif minutes < 33:
        minuteWord = M_HALF + PAST
    elif minutes < 38:
        minuteWord = M_TWENTYFIVE + TO
    elif minutes < 43:
        minuteWord = M_TWENTY + TO
    elif minutes < 48:
        minuteWord = M_QUARTER + TO
    elif minutes < 53:
        minuteWord = M_TEN + TO
    elif minutes < 58:
        minuteWord = M_FIVE + TO
    return minuteWord    
    
        
    
def timeToWords(timeNow):
    wordTime = IT_IS + lightMinutes(timeNow[4], timeNow[3]) + lightHours(timeNow[3], timeNow[4]) + OCLOCK
    #print("Wordtime to light is:", wordTime)
    return wordTime

"""
This function call does "extra" math that really only needs to be done at the first 0-5 minutes.
I *could* make this a little less tricky if I did the function a little different - maybe input the waittime?
So run 1 would input this arithmetic, but subsequent runs the wait time would just be flat 5 minutes.
There would eventually be a few ms drift, but it'd take a long time I think.  Like a really really long time to drift.
"""
def lightTime():
    current_time = utime.localtime()
    #print("current_time:", current_time)
    hour = current_time[3]
    minute = current_time[4]
    am_pm = hour24-12
        
    if minute < 10:
        minute = "0" + str(minute)
    ##The following if loop changes 24 hour time to 12 hour time
    if am_pm < 0:
        am_pm = "am"
        hour = hour24-12
    else:
        am_pm = "pm"
        hour = hour24
    print(str(hour)+":"+str(minute)+" "+ am_pm)
    numsToLight = []  ###This line has cleared out any old lights from the previous array.  I THINK THIS IS NOT NECESSARY.  Delete?
    numsToLight = timeToWords(current_time)
    
    #turnOnMatrix(numsToLight, clock_color)
    pixelLighter(numsToLight)
   
    pixelOff(numsToLight)##DISASTEROUS???
    """This section determines how long the Pico should sleep before updating the clock again.  The initial delay calculation is for
    the first run, and after that it should be just a five minute wait.  I have wondered if I could do this more efficiently, but I
    think this might be as simple as it gets.
    """
    sleepTime = (60-current_time[5])*1000
    
    if current_time[4] % 5 < 3:
            NEWsleepTime = (3 - current_time[4]%5)*60000-current_time[5]*1000
    else:
            NEWsleepTime = (8 - current_time[4]%5)*60000-current_time[5]*1000
    
    #print(sleepTime, NEWsleepTime)
    print("The time to update is:", (NEWsleepTime/1000-NEWsleepTime/1000%60)/60, "minutes and", (NEWsleepTime/1000%60), "secs")
    utime.sleep_ms(NEWsleepTime)#sleep until next minute flips over

def lightDay():
    current_time = utime.localtime()
    #print("current time returns:", current_time)
    weekday = current_time[6] + 2
    if weekday == 7:
        weekday = 0#This compensates for the day of week being goofy...
    elif weekday == 8:
        weekday = 1
    #print("Weekday returns:", weekday) #weekday is 0-6 Mon-Sun in the docs, but today is Sun and it returns 5. Monday returns 6.  Hmm.  Have to add one????  Or is it Tues-Mon??
 
    for i in range(len(SMTWTFS)):
        x=2*i
        daysToLight[x]=SMTWTFS[i]
        if i==weekday:
            daysToLight[x+1]=day_color  #If the day of the week is the correct one, light it the alternate color
        else:
            daysToLight[x+1]=week_color #otherwise, light it main color
   
    
    pixelLighter(daysToLight)

    

    
"""****DEPRICATED**** This function takes an array of LED numbers as an argument, and lights all of the given numbers the clock_color defined above.
In the future, I wonder if I should have the array also hold info to tell us what color each light should be.
def turnOnMatrix(numbersArray, color):
    ##This first loop makes sure all lights in the array are set to off so that we don't accidentally keep old words lit up.  It's not a problem
    ##if the new array is longer than the old one, I think, but it comes into play frequently.
    for x in range(121):  #I dropped this from 121 to 114 so that this does not overwrite the day of the week...probably a mistake.
        ws[x]=off
    #print("Current ws:", ws)
    for i in range(len(numbersArray)):
        #print("Setting ws number: ", i, "to", numbersArray[i])
        ws[numbersArray[i]] = color
    print("Writing new ws:", ws)
    ws.write()
    """

def pixelLighter(pixelList):
    #print(len(pixelList))
    #print("blue=", blue)
    #for i in range(len(pixelList)):
        #print(pixelList[i])
    for i in range(0, len(pixelList), 2):
        #print("i=", i, "i+1=", i+1)
        ws[pixelList[i]] = pixelList[i+1]
        #print("Just set ws[",i,"] to", ws[i+1])
    #print("pixelLighter starting:", ws)
    ws.write()

"""pixelOff switches a set of lights to color "off" for the next update.
     It does NOT send that update to the LEDs, but prepared the ws2812 object to not leave lights on at the next update."""
def pixelOff(pixelList):
    for i in range(0, len(pixelList), 2):
        ws[pixelList[i]] = off

"""bootUpMessage runs before the word clock begins.
It is a space for any messages to be displayed on startup."""
def bootUpMessage():
    pixelLighter(HI+BECKY)
    utime.sleep(3)
    pixelOff(HI+BECKY)
    pixelLighter(GOOD + DAY)
    utime.sleep(2)
    pixelOff(GOOD+DAY)
    lightDay()

"""MAIN PROGRAM"""
print(hour24, ':', minute, ':', second, 'start time') #gives me the time when the program begins

for i in range(14):
    #print("seting daysToLight of", i, "zero.")
    daysToLight.append("TEST")
    
bootUpMessage()
#pixelLighter(IT_IS)


while True:
    #current_time = utime.localtime()
    #only print the new time if the minute switches over
    
    lightTime()
