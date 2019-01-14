import urllib.request
import cv2
import numpy as np
import os

negative_image_number = 1
positive_image_number = 1
test_image_number = 1

def get_images():
    global negative_image_number
    global positive_image_number
    ##Negatives
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152 //people
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893 //room
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03663433 //office
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02821627 //bedroom
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03841666 //Office, business office
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03842156 //Office furniture
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04295881 //Stadium
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n14564779 //Wall
    ##Positives
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04409515 //Tennis Balls

    negative_images_link1 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    negative_image_urls1 = urllib.request.urlopen(negative_images_link1).read().decode()
    # negative_images_link2 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893'
    # negative_image_urls2 = urllib.request.urlopen(negative_images_link2).read().decode()
    negative_images_link3 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03663433'
    negative_image_urls3 = urllib.request.urlopen(negative_images_link3).read().decode()
    # negative_images_link4 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02821627'
    # negative_image_urls4 = urllib.request.urlopen(negative_images_link4).read().decode()
    negative_images_link5 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03841666'
    negative_image_urls5 = urllib.request.urlopen(negative_images_link5).read().decode()
    negative_images_link6 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03842156'
    negative_image_urls6 = urllib.request.urlopen(negative_images_link6).read().decode()
    negative_images_link7 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04295881'
    negative_image_urls7 = urllib.request.urlopen(negative_images_link7).read().decode()
    negative_images_link8 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n14564779'
    negative_image_urls8 = urllib.request.urlopen(negative_images_link8).read().decode()

    positive_images_link1 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04409515'
    positive_image_urls1 = urllib.request.urlopen(positive_images_link1).read().decode()

    negative_image_urls = negative_image_urls1 + negative_image_urls3 + negative_image_urls5 + negative_image_urls6 + negative_image_urls7 + negative_image_urls8
    positive_image_urls = positive_image_urls1

    if not os.path.exists('negatives_images'):
        os.makedirs('negatives_images')

    if not os.path.exists('positive_images'):
        os.makedirs('positive_images')

    for i in positive_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'positive_images/' + str(positive_image_number) + '.bmp')
            image = cv2.imread('positive_images/' + str(positive_image_number) + '.bmp', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, (400, 400))
            cv2.imwrite('positive_images/' + str(positive_image_number) + '.bmp', resized_image)
            positive_image_number += 1
        except Exception as e:
            print(str(e))

    for i in negative_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'negatives_images/' + str(negative_image_number) + '.jpg')
            image = cv2.imread('negatives_images/' + str(negative_image_number) + '.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, (400, 400))
            cv2.imwrite('negatives_images/' + str(negative_image_number) + '.jpg', resized_image)
            negative_image_number += 1
        except Exception as e:
            print(str(e))


def get_test_images():
    global test_image_number
    # Positives
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04409515 //Tennis Balls
    test_images_link1 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04409515'
    test_image_urls1 = urllib.request.urlopen(test_images_link1).read().decode()
    test_image_urls = test_image_urls1
    if not os.path.exists('test_images'):
        os.makedirs('test_images')

    for i in test_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'test_images/' + str(test_image_number) + '.bmp')
            image = cv2.imread('test_images/' + str(test_image_number) + '.bmp', cv2.IMREAD_COLOR)
            resized_image = cv2.resize(image, (400, 400))
            cv2.imwrite('test_images/' + str(test_image_number) + '.bmp', resized_image)
            test_image_number += 1
        except Exception as e:
            print(str(e))

def find_bad_images():
    global negative_image_number
    global positive_image_number

    # for file in ['negatives_images']:
    #    for image in os.listdir(file):
    #        for bad in os.listdir('bad_images'):
    #            try:
    #                current_image_path = str(file) + '/' + str(image)
    #                bad = cv2.imread('bad_images/' + str(bad))
    #                question = cv2.imread(current_image_path)
    #                if bad.shape == question.shape and not (np.bitwise_xor(bad, question).any()):
    #                    print('Bad image!')
    #                    print(current_image_path)
    #                    os.remove(current_image_path)
    #            except Exception as e:
    #                print(str(e))
    #
    # for file in ['positive_images']:
    #     for image in os.listdir(file):
    #         for bad in os.listdir('bad_images'):
    #             try:
    #                 current_image_path = str(file) + '/' + str(image)
    #                 bad = cv2.imread('bad_images/' + str(bad))
    #                 question = cv2.imread(current_image_path)
    #                 if bad.shape == question.shape and not (np.bitwise_xor(bad, question).any()):
    #                     print('Bad image!')
    #                     print(current_image_path)
    #                     os.remove(current_image_path)
    #             except Exception as e:
    #                 print(str(e))

    for file in ['test_images']:
        for image in os.listdir(file):
            for bad in os.listdir('bad_images'):
                try:
                    current_image_path = str(file) + '/' + str(image)
                    bad = cv2.imread('bad_images/' + str(bad))
                    question = cv2.imread(current_image_path)
                    if bad.shape == question.shape and not (np.bitwise_xor(bad, question).any()):
                        print('Bad image!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

def create_pos_n_neg():
    global negative_image_number
    global positive_image_number
    for file in ['negatives_images']:
        for image in os.listdir(file):
            if file == "negatives_images":
                line = file + '/' + image + '\n'
                with open('negative.txt', 'a') as f:
                    f.write(line)

    for file in ['positive_images']:
        for image in os.listdir(file):
            if file == 'positive_images':
                line = file + '/' + image + '\n'
                with open('positive.txt', 'a') as f:
                    f.write(line)


def get_gray_image():
    global negative_image_number
    global positive_image_number
    positive_image_number = 611
    for file in ['pos_alternative_images']:
        for img in os.listdir(file):
            try:
                image = cv2.imread('pos_alternative_images/' + str(img), cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(image, (400, 400))
                cv2.imwrite('positive_images/' + str(positive_image_number)+".bmp", resized_image)
                positive_image_number += 1
            except Exception as e:
                print(str(e))


def sort_by_number():
    number = 1
    for file in ['positive_images']:
        for image in os.listdir(file):
            os.rename(file + "/" + image, file + "/" + str(number) + ".bmp")
            number += 1


# get_images()
# get_gray_image()
# find_bad_images()
# create_pos_n_neg()
# sort_by_number()
# get_test_images()