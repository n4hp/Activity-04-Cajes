import cv2

filepath = 'hutao.jpg'

print (''' Select: 
[1] Color
[2] Grayscale
[3] Unchange
''')

flag = int(input())

if flag == 1:
    xd = 1

elif flag == 2:
    xd = 0

elif flag == 3:
    xd = -1
    

image = cv2.imread(filepath, xd)

cv2.imshow("HUTAO", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
