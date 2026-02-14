import math
import sys
XCord = input(" xcord as number")
YCord = input(" ycord as number")

#convert to float

XCord = float(XCord)
YCord = float (YCord)

xsqr  = XCord * XCord
ysqr  = YCord * YCord

rsqr = xsqr + ysqr 

radius = math.sqrt(rsqr)
print(radius)
quad = 1
if( XCord ==0.0 and YCord == 0.0):
    print("no angle")
    sys.exit(0)

#edge cases like 0,90,180 and 279 degrees 
if XCord == 0.0 or YCord == 0.0: 
    if XCord > 0:
        print("radians 0:")
    if YCord > 0:
        print("radians{}:",format(math.pi/2))
    if XCord < 0:
        print("radians{}:",format(math.pi))
    if YCord < 0:
        print("radians{}:",format(3*math.pi/2))
    sys.exit(0)

Q1Ang = math.sin(math.fabs(XCord)/radius)

if XCord >0 and YCord > 0:
    quad  = 1
    print("quad{}:",format(quad))
    print("radians{}:",format(Q1Ang))
   
if XCord < 0 and YCord > 0:
    quad = 2
    print("quad{}:",format(quad))
    print("radians{}:",format(math.pi-Q1Ang))
   
if XCord < 0 and YCord < 0:
    quad = 3
    print("quad{}:",format(quad))
    print("radians{}:",format(math.pi+Q1Ang))
 
if XCord > 0 and YCord <0:
    quad = 4
    print("quad{}:",format(quad))
    twopi = math.pi*2
    print("radians{}:",format(twopi-Q1Ang))