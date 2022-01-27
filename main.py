from math import sqrt
import cv2
import numpy as np

def euclidean_distance(row1, row2):
    distance = sqrt((row2[0] - row1[0])*(row2[0] - row1[0])+(row2[1] - row1[1])*(row2[1] - row1[1]))
    return distance

def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    a=[]
    for train_row in train:
        dist = euclidean_distance(train_row, test_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
        a.append(distances[i][1])
    return neighbors,a


def click_event(event, x, y,
                flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.circle(img, (x, y), 4, (0, 0, 255), -1)
        neighbors,a = get_neighbors(points, (x, y), 5)
        print(a)
        for neighbor in neighbors:
            cv2.circle(img, neighbor, 4, (0, 0, 255), -1)
            print(neighbor)
        for i in a:
            cv2.circle(img, (x, y), int(i), (255, 0, 0), 1)
        cv2.imshow('image', img)


def draw_grid(img, line_color=(255, 255, 0), thickness=1, type_=cv2.LINE_AA, pxstep=50):
    x = pxstep
    y = pxstep
    while x < img.shape[1]:
        cv2.line(
            img, (x, 0), (x, img.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        x += pxstep
    while y < img.shape[0]:
        cv2.line(img, (0, y), (img.shape[1], y),
                 color=line_color, lineType=type_, thickness=thickness)
        y += pxstep


def createRandomPoint(num1, num2, num3, img):
    for i in range(num3):
        X = np.random.randint(num1, num2, size=2)
        Tuple_1 = tuple(X)
        cv2.circle(img, Tuple_1, 4, (0, 255, 0), -1)
        points.append(Tuple_1)
        i = i+1


def createnewPoint(img):
    xCords = input("istenilen noktanin x cord: ")
    yCords = input("istenilen noktanin x cord: ")
    cv2.circle(img, (xCords, yCords), 4, (0, 255, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)

draw_grid(img)
points = []

# show the image
createRandomPoint(15, 490, 50, img)
cv2.imshow('image', img)

cv2.setMouseCallback('image',
                     click_event)
cv2.waitKey(0)

cv2.destroyAllWindows()
