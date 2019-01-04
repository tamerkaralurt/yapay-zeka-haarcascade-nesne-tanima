import urllib.request
import cv2
import numpy as np
import os

def get_images():
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513
    negative_images_link1 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    negative_image_urls1 = urllib.request.urlopen(negative_images_link1).read().decode()
    negative_images_link2 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    negative_image_urls2 = urllib.request.urlopen(negative_images_link2).read().decode()

    if not os.path.exists('negatives_images'):
        os.makedirs('negatives_images')

    image_number = 1

    for i in negative_image_urls1.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'negatives_images/'+str(image_number)+'.jpg')
            image = cv2.imread('negatives_images/'+str(image_number)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, (100,100))
            cv2.imwrite('negatives_images/'+str(image_number)+'.jpg',resized_image)
            image_number += 1
        except Exception as e:
            print(str(e))

    for i in negative_image_urls2.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'negatives_images/'+str(image_number)+'.jpg')
            image = cv2.imread('negatives_images/'+str(image_number)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, (100,100))
            cv2.imwrite('negatives_images/'+str(image_number)+'.jpg',resized_image)
            image_number += 1
        except Exception as e:
            print(str(e))

def find_bad_images():
    for file in ['negatives_images']:
        for image in os.listdir(file):
            for bad in os.listdir('bad_images'):
                try:
                    current_image_path = str(file)+'/'+str(image)
                    bad = cv2.imread('bad_images/'+str(bad))
                    question = cv2.imread(current_image_path)
                    if bad.shape == question.shape and not (np.bitwise_xor(bad,question).any()):
                        print('Bad image!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

def create_pos_n_neg():
    for file in ['negatives_images']:
        for image in os.listdir(file):
            if file == "negatives_images":
                line = file+'/'+image+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

            elif file == 'positive_images':
                line = file+'/'+image+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)

def get_gray_image():
    for file in ['positive_images']:
        for image in os.listdir(file):
            try:
                image = cv2.imread('positive_images/ball.png', cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(image, (100,100))
                cv2.imwrite('positive_images/ball.png',resized_image)
            except Exception as e:
                print(str(e))

# get_images()
# find_bad_images()
# create_pos_n_neg()
# get_gray_image()