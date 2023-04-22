import Utilities as util
import cv2
import matplotlib.pyplot as plt
import kmeans as km
import numpy as np
import agglomerative as agg

def kmeans_test():
    img = util.read_image('test.jpg')
    # convert the image to grayscale
    vectorized = util.image_to_vector(img)

    
    # run the kmeans algorithm
    kmeans = km.kmeans(dim = 3, k = 2, data = vectorized)
    kmeans.run()
    res = kmeans.process_data([0,255])
    centroids = kmeans.centroids
    
    res1 = np.zeros((vectorized.shape[0],3))
    # am array as long as the number of pixels in the image
    # if the pixel is in the first cluster, the value is as same as the first centroid, otherwise the value is as same as the second centroid
    for i in range(res.shape[0]):
        if res[i] == 0:
            res1[i] = centroids[0]
        else:
            res1[i] = centroids[1]
    # display the image in rgb space again
    # if the culster is 0, set the color same as the first centroid, otherwise set the color same as the second centroid
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(vectorized[:,0],vectorized[:,1],vectorized[:,2],c=res1/255)
    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')
    # set the color of the axis label
    ax.xaxis.label.set_color('red')
    ax.yaxis.label.set_color('green')
    ax.zaxis.label.set_color('blue')
    plt.show()
    
    
    # reshape the result
    res = res.reshape(img.shape[0],img.shape[1])
    # save the result  as a image
    cv2.imwrite('result.jpg',res)
    
def agglomerative_test():
    # random generate a data in dim 3(rgb) and 1000 points
    data = np.random.randint(0,255,(100,3))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0],data[:,1],data[:,2],c=data/255)
    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')
    # set the color of the axis label
    ax.xaxis.label.set_color('red')
    ax.yaxis.label.set_color('green')
    ax.zaxis.label.set_color('blue')
    plt.show()
    
    # run the agglomerative algorithm, and set the number of clusters to 3
    agglomerative = agg.AgglomerativeClustering( k = 10, data = data)
    agglomerative.fit()
    # get the result
    res = agglomerative.get_result()
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0],data[:,1],data[:,2],c=res/255)
    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')
    # set the color of the axis label
    ax.xaxis.label.set_color('red')
    ax.yaxis.label.set_color('green')
    ax.zaxis.label.set_color('blue')
    plt.show()
    
if __name__ == '__main__':
    # kmeans_test()
    agglomerative_test()