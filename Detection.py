import cv2
import pydirectinput
import time

pydirectinput.PAUSE = 0


def click_object(needle, haystack):
    search_img = cv2.imread(needle, cv2.IMREAD_UNCHANGED)
    # full_img = cv2.imread(haystack, cv2.IMREAD_UNCHANGED)
    full_img = haystack
    result = cv2.matchTemplate(full_img,search_img,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.85
    if max_val >= threshold:
        print("Found image")
    else:
        print("Image not detected")

    search_img_w = search_img.shape[1]
    search_img_h = search_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + search_img_w, top_left[1] + search_img_h)
    center_click = ((top_left[0] + search_img_w)//2, top_left[1] + search_img_h // 2)

    return center_click

    # Highlight image
    # cv2.rectangle(full_img, top_left, bottom_right, color=(0,255,0), thickness=2,lineType=cv2.LINE_4)
