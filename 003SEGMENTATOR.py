from SimpleCV import Camera, Display, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab

def classify(im, K, show=False):
    """ classify    - classify an image using k-means algorithm.

    Arguments:
        * im            - an image (ndarray) or a filename.
        * K             - number of classes.
        * show  = False - if True, display the image and the classes.

    Return:
        * imClasses     - the classes of the image (ndarray, 2D).

    See also:
        * kMeans        - K-means algorithm.
    """
    a = Image(im)
    a = a.histogram(255)
    
    # Load image
    if type(im) is str:
        im = plt.imread(im)

    # Reshape and apply k-mean
    values = im.reshape((im.shape[0] * im.shape[1], -1))
    centers, classes = kMeans(values, K)
    imClasses = classes.reshape((im.shape[0], im.shape[1]))
##    imClasses.save("imClassesH.png")
##    imClassesHl=image("imClassesH.png")
##    imClassHisto=imClassesH1.histogram(255)
    
    
    # Display
    if show:
                
        cmap = 'gray' if im.ndim < 3 else None
        plt.subplot(221), plt.imshow(im, cmap=cmap), plt.title('Imagen Gray')
        plt.subplot(222), plt.imshow(imClasses), plt.title('Segmentacion por Clases')
        pylab.subplot(223), pylab.plot(a), pylab.draw(), pylab.pause(0.0001), pylab.title('Histograma Img Gray')
        pylab.subplot(224), pylab.plot(a), pylab.draw(), pylab.pause(0.0001), pylab.title('Histograma Img Segmentada')
        plt.show()

    # The end
    return imClasses


def kMeans(Y, K, maxIter=99):
    """ kMeans      - K-means clustering algorithm.

    Arguments:
        * Y                 - data to be classified, row by row (ndarray, 2D).
        * K                 - number of classes.
        * maxIter   = 99    - maximum number of iterations

    Return:
        * X                 - center of the classes, row by row (ndarray, 2D).
        * C                 - classes of the elements in Y (ndarray, 1D).

    See also:
        * nearestNeighbor   - nearest-neighbor classification.
    """

    # Check dimensions
    if Y.ndim != 2:
        raise Exception('data matrix must be a 2D ndarray')

    # Initialize with K values from Y
    X = Y[np.random.permutation(Y.shape[0])[0:K], :]
    C = nearestNeighbor(Y, X)

    # Optimize Y and I alternatively
    for n in range(maxIter):
        X = updateCenters(Y, C)
        old, C = C, nearestNeighbor(Y, X)

        # Stop if convergence
        if all(C == old):
            break

    # Return centers and classes
    return X, C


def nearestNeighbor(Y, X):
    """ nearestNeighbor     - nearest neighbor classification.

    Arguments:
        * Y     - data to be classified, row by row (ndarray, 2D).
        * X     - center of the classes, row by row (ndarray, 2D).

    Return:
        * C     - classes of the data from the nearest neighbor (ndarray, 1D).

    See also:
        * kMeans    - K-means classification.
    """

    # Check dimensions
    if Y.ndim != 2 or X.ndim != 2:
        raise Exception('Y and X matrices must be 2D ndarrays')
    if Y.shape[1] != X.shape[1]:
        raise Exception('Y and X matrices must have the same number of columns')

    # Find c(i) = arg min(j) || Yi - Xj ||
    dist2 = np.sum(Y**2, 1).reshape(-1, 1) + np.sum(X**2, 1).reshape(1, -1) - 2 * np.dot(Y, X.T)
    return dist2.argmin(1)


def updateCenters(Y, C):
    """ updateCenters   - update the centers of the classes (during k-means).

    Arguments:
        * Y     - data to be classified, row by row (ndarray, 2D).
        * C     - classes of the data (ndarray, 1D).

    Return:
        * X     - center of the classes, row by row (ndarray, 2D).

    See also:
        * kMeans            - k-means classification.
        * nearestNeighbor   - nearest neighbor classification.
    """

    # Check dimensions
    if Y.ndim != 2:
        raise Exception('data matrix must be a 2D ndarray')
    if C.ndim != 1:
        raise Exception('classes matrix must be a 1D ndarray')
    if Y.shape[0] != C.shape[0]:
        raise Exception('Y and C matrix must have the same number of rows')

    # Create an empty array
    K = C.max() + 1
    X = np.ndarray((K, Y.shape[1]), Y.dtype)

    # Compute barycenters
    for k in range(K):
        X[k,:] = Y[C == k,:].mean(0)

    # Return them
    return X

a = Image("hola5Gray.png")
b = a.histogram(255)
# If launched as a script
if __name__ == '__main__':
    import sys

    # Display usage if not enough arguments
    if len(sys.argv) != 3:
        print 'Usage:'
        print '   ', sys.argv[0], '<image.png> <K>'

    # Launch example
    else:
        imName, K = sys.argv[1], int(sys.argv[2])
        classify(imName, K, True)
