import urllib.request
import cv2
import numpy as np
import os


def get_images():
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152 //people
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893 //room
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03663433 //office
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02821627 //bedroom
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03841666 //Office, business office
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03842156 //Office furniture
    negative_images_link1 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    negative_image_urls1 = urllib.request.urlopen(negative_images_link1).read().decode()
    negative_images_link2 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893'
    negative_image_urls2 = urllib.request.urlopen(negative_images_link2).read().decode()
    negative_images_link3 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03663433'
    negative_image_urls3 = urllib.request.urlopen(negative_images_link3).read().decode()
    negative_images_link4 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02821627'
    negative_image_urls4 = urllib.request.urlopen(negative_images_link4).read().decode()
    negative_images_link5 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03841666'
    negative_image_urls5 = urllib.request.urlopen(negative_images_link5).read().decode()
    negative_images_link6 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03842156'
    negative_image_urls6 = urllib.request.urlopen(negative_images_link6).read().decode()

    negative_image_urls = negative_image_urls1 + negative_image_urls2 + negative_image_urls3 + negative_image_urls4 + negative_image_urls5 + negative_image_urls6

    if not os.path.exists('negatives_images'):
        os.makedirs('negatives_images')

    image_number = 1

    for i in negative_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'negatives_images/' + str(image_number) + '.jpg')
            image = cv2.imread('negatives_images/' + str(image_number) + '.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, (100, 100))
            cv2.imwrite('negatives_images/' + str(image_number) + '.jpg', resized_image)
            image_number += 1
        except Exception as e:
            print(str(e))


def find_bad_images():
    for file in ['negatives_images']:
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
    for file in ['negatives_images']:
        for image in os.listdir(file):
            if file == "negatives_images":
                line = file + '/' + image + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

            elif file == 'positive_images':
                line = file + '/' + image + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)


def get_gray_image():
    for file in ['positive_images']:
        for img in os.listdir(file):
            try:
                image = cv2.imread('positive_images/' + str(img), cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(image, (100, 100))
                cv2.imwrite('positive_images/' + str(img), resized_image)
            except Exception as e:
                print(str(e))


# get_images()
# find_bad_images()
# create_pos_n_neg()
# get_gray_image()
