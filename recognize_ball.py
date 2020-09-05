# Untitled - By: katka - po sep 30 2019

#ball thresholds = ([240, 255, 80, 130, 10, 52 ])


import sensor, image, time, math

threshold_index = 0 # 0 for red, 1 for green, 2 for blue

thresholds = [(45, 60, 50, 74, 38, 61)]

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

x0 = sensor.width() // 2
y0 = sensor.height()

print('vyska: ', str(x0))
print('sirka: ', str(y0))

while(True):
    clock.tick()
    img = sensor.snapshot()

#finding ball
    for blob in img.find_blobs([thresholds[threshold_index]], pixels_threshold=200, area_threshold=200, merge=True):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())

#position of ball
    print('original x: ', blob.cx(), ' original y: ', blob.cy())
    x1 = blob.cx() - x0
    y1 = y0 - blob.cy()
    print('nove x: ', str(x1), ' nove y: ', str(y1))
