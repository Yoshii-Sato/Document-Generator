import json
import pathlib, os

import cv2 as cv
import numpy as np

input_dict = json.load(open(os.path.join(pathlib.Path(__file__).parent, 'result.json'), 'r'))

height = input_dict['image_shape']['height']
width = input_dict['image_shape']['width']

blank = np.zeros((height, width,3), dtype= 'uint8')
blank.fill(255)

background = np.zeros((height, width, 3), dtype= 'uint8')

def convert_dict_to_np_list (points):
    points_array = []
    for point in points:
        points_array.append([point['x'], point['y']])
    np_array = np.array([points_array])
    return np_array, points_array

def return_all_text (input):
    for lines in input['coordinates']:
        for line in lines['lines']:
            print(line['ocr_result']['pred'])
    

for sets in input_dict['coordinates']:
    if 'points' in sets:
        np_array, points_array = convert_dict_to_np_list(sets['points'])
        cv.drawContours(background, np_array, -1, (255,1,1), thickness = -1)
        cv.putText(blank, sets['label'], points_array[3], cv.FONT_HERSHEY_COMPLEX, .5, (255,0,0), thickness=1)

    for line in sets['lines']:
        np_array, points_array = convert_dict_to_np_list(line['points'])
        x = points_array[0][0]
        y = 0
        for point in points_array:
            if point[0] < x:
                x = point[0]
            if point[1] > y:
                y = point[1]
        cv.drawContours(blank, np_array, -1, (0,255,0), thickness = 1)
        cv.putText(blank, line['ocr_result']['pred'], (x,y), cv.FONT_HERSHEY_COMPLEX, .24, (0,0,0), thickness = 1 )

page = blank.copy()
mask = background.astype(bool)
alpha = .7
page[mask] = cv.addWeighted(blank, alpha, background, 1 - alpha, 1.0)[mask]

return_all_text(input_dict)

# cv.imshow('background', background)
# cv.imshow('blank', blank)
cv.imshow('final page', page)

cv.waitKey(0)
