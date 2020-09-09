# Untitled - By: katka - po sep 30 2019

#ball thresholds = ([240, 255, 80, 130, 10, 52 ])


import sensor, image, time, math

def printStatValues():
    print('primary_ball_diameter: ', str(primary_ball_diameter))
    print('primary_ball_distance: ', str(primary_ball_distance))
    print('frame height: ', str(x0))
    print('frame width: ', str(y0))

def printChanValues():
    #print('original x: ', blob.cx(), ' original y: ', blob.cy())
    #print('new x: ', str(x1), ' new y: ', str(y1))
    print('ball_diameter: ', str(ball_diameter))
    print('ball_distance: ', str(ball_distance))
    print('angle: ', str(angle))


threshold_index = 0 # 0 for red, 1 for green, 2 for blue

thresholds = [(43, 78, 27, 75, 14, 65)]

#sensor setup
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

#zakladne parametre
x0 = sensor.width() // 2
y0 = sensor.height()

primary_ball_diameter = 7
primary_ball_distance = 18.5

ball_diameter = 0
ball_distance = 0

angle = 0

while(True):
    clock.tick()
    img = sensor.snapshot()

#finding ball
    for blob in img.find_blobs([thresholds[threshold_index]], pixels_threshold=200, area_threshold=200, merge=True):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())

#position of ball
    x1 = blob.cx() - x0
    y1 = y0 - blob.cy()

#vypocty
    if (y1 ^ 2) != 0 and (x1 ^ 2) != 0:
        anP = math.degrees(math.atan( (y1 ^ 2) / (x1 ^ 2) ))
        if anP > 0:
            angle = 90 - anP
        elif anP < 0:
            angle = - 90 - anP
    else:
        angle = 0
    ball_diameter = blob.h() // 10
    ball_distance = ( ball_diameter * primary_ball_distance ) / primary_ball_diameter
    printChanValues()
