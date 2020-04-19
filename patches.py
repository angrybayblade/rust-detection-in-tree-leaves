from glob import glob
from time import sleep
from os import system

import cv2


images = glob("./patches/*.jpg")

print (len(images))

for i in images:
    img = cv2.imread(i)
    cv2.imshow("s",img)

    key = cv2.waitKey(25000) & 0xFF

    if key == ord('q') or key == 27:
        break
    elif key == 13:
        system(f"rm {i}")
    elif key == ord('s'):
        cv2.imwrite(f"./patches_clean/{i.split('/')[-1]}",img)
        system(f"rm {i}")
    else:
        print (key)

cv2.destroyAllWindows()