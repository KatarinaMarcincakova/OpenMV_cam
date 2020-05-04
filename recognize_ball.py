# Untitled - By: katka - po sep 30 2019

#ball thresholds = ([240, 255, 80, 130, 10, 52 ])


import sensor, image, time, math

threshold_index = 0 # 0 for red, 1 for green, 2 for blue

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green/blue things. You may wish to tune them...
thresholds = [(45, 60, 50, 74, 38, 61)] # generic_ball_thresholds

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" merges all overlapping blobs in the image.

while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds[threshold_index]], pixels_threshold=200, area_threshold=200, merge=True):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
    print(clock.fps())
