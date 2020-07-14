import praw
import pprint
from datetime import datetime
from urllib.request import urlopen
import imutils
import numpy as np
import cv2
import csv
import progressbar

SUBREDDIT="gaybrosgonemild"

def determine_white_skin_color(image):
    # define the upper and lower boundaries of the HSV pixel
    # intensities to be considered 'skin'
    lowerHSV = np.array([0, 48, 80], dtype = "uint8")
    upperHSV = np.array([20, 255, 255], dtype = "uint8")

    # resize the frame, convert it to the HSV color space,
    # and determine the HSV pixel intensities that fall into
    # the speicifed upper and lower boundaries
    image = imutils.resize(image, width=400)
    converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lowerHSV, upperHSV)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

    # blur the mask to help remove noise, then apply the
    # mask to the frame
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    skin = cv2.bitwise_and(image, image, mask = skinMask)

    return skin

def determine_face(image):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = imutils.resize(image, width=400)
    # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    maxX = 0
    maxY = 0
    maxW = 0
    maxH = 0
    aria = -1
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        temp_aria = (x+w) * (y+h)
        if (temp_aria >= aria):
            aria = temp_aria
            maxX = x
            maxY = y
            maxW = w
            maxH = h
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    crop_image = image[maxY:maxY+maxH, maxX:maxX+maxW]
    # Display the output
    return crop_image

def determine_skin_color(url):
    req = urlopen(url)
    image = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(image, -1)

    image = determine_face(image)
    image = determine_white_skin_color(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if cv2.countNonZero(gray) == 0:
        return 0

    # show the skin in the image along with the mask
    # cv2.imshow("images", image)
    return 1

def main(args):
    reddit = praw.Reddit("bot1", config_interpolation="basic")

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter = '|', quoting=csv.QUOTE_NONNUMERIC)
        subreddit = reddit.subreddit(SUBREDDIT)
        writer.writerow(["ID", "author", "is_white", "score", "upvote_ratio", "comments", "created", "created_utc"])
        whitePerson = 0;
        for submission in progressbar.progressbar(subreddit.top("year", limit=1000)):
            row = []
            row.append(submission.id)
            row.append(submission.author)
            try:
                skinColor = determine_skin_color(submission.url)
            except:
                skinColor = 0
            row.append(skinColor)
            row.append(submission.score)
            row.append(submission.upvote_ratio)
            row.append(submission.comments.__len__())
            row.append(datetime.utcfromtimestamp(submission.created_utc).strftime("%Y-%m-%d %H:%M:%S"))
            row.append(submission.created_utc)
            writer.writerow(row)
            whitePerson = whitePerson + skinColor;
        pprint.pprint("From 1 000 posts there have been " + str(whitePerson) + "white people that I could detect.")
