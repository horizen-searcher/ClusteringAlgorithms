'''
@description: This file contains all the utility functions used in the project
@author: chtholly
@date: 2023-4-22
'''

import cv2
import numpy as np


def read_image(image_path):
    '''
    @description: Read the image from the given path,convert it to RGB and return it
    @param {string} image_path: The path of the image
    @return {numpy.ndarray} image: The image read from the given path
    '''
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def image_to_vector(image):
    '''
    @description: read a image in cv2 format and covert it to a vector using numpy
    @param {img} image: The image to be converted
    @return {numpy.ndarray} image: The image converted to a vector
    '''
    return image.reshape(-1, 3)

def accuracy(y_true, y_pred):
    '''
    @description: Calculate the Mean Square Error of the given prediction
    @param {numpy.ndarray} y_true: The true labels of the data
    @param {numpy.ndarray} y_pred: The predicted labels of the data
    @return {float} accuracy: The MSE of the prediction
    '''
    # Calculate the Mean Square Error of the given prediction
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

