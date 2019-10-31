import skimage
import numpy as np
import utils


def MaxPool2d(im: np.array,
              kernel_size: int):
    """ A function that max pools an image with size kernel size.
    Assume that the stride is equal to the kernel size, and that the kernel size is even.

    Args:
        im: [np.array of shape [H, W, 3]]
        kernel_size: integer
    Returns:
        im: [np.array of shape [H/kernel_size, W/kernel_size, 3]].
    """
    stride = kernel_size
    ### START YOUR CODE HERE ### (You can change anything inside this block) 

    new_im = np.ndarray([im.shape[0]//stride,im.shape[1]//stride, im.shape[2]])

    for y in range(0,len(im)-kernel_size+1,stride):
        for x in range(0,len(im[0])-kernel_size+1,stride):
            maxpool = [0,0,0]
            for k_y in range(kernel_size):
                for k_x in range(kernel_size):
                    maxpool = [max(m, c) for m, c in zip(maxpool, im[y+k_y][x+k_x])]
            new_im[int(y/stride),int(x/stride)] = maxpool

    return new_im
    ### END YOUR CODE HERE ### 


if __name__ == "__main__":

    # DO NOT CHANGE
    im = skimage.data.chelsea()
    im = utils.uint8_to_float(im)
    max_pooled_image = MaxPool2d(im, 4)

    utils.save_im("chelsea.png", im)
    utils.save_im("chelsea_maxpooled.png", max_pooled_image)

    im = utils.create_checkerboard()
    im = utils.uint8_to_float(im)
    utils.save_im("checkerboard.png", im)
    max_pooled_image = MaxPool2d(im, 2)
    utils.save_im("checkerboard_maxpooled.png", max_pooled_image)
