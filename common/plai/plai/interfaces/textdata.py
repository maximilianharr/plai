"""@package textdata

  @brief Helper functions to convert text data (e.g. csv etc)
  
  @author Maximilian Harr <maximilian.harr@gmail.com>
  @date 29.05.2020

  @bug
  @warning
  @todo
 
"""

## IMPORTS #######################################################################################
import numpy as np
import scipy.io
from skimage import io, exposure
import matplotlib.pyplot as plt

## CLASSES ######################################################################################

## FUNCTIONS #####################################################################################

def get_array_from_string(datastring: str) -> np.array([]):
    """
    get_array_from_string Reads array from string and returns it as np.array
        @param array_str: string of arrays, e.g. "[1, 2, 3]"
        @return: np.array
    """

    # Check input parameter
    if not type(datastring) == str:
        raise ValueError('Wrong datatype provided')
    
    # Extract paranthesis from string
    datastring = datastring.replace("[", "")
    datastring = datastring.replace("]", "")

    data_array = np.array([])
    data_array = datastring.split(",")
    
    # Convert to float
    data_array = [float(e) for e in data_array]
    
    return data_array

# @brief Get bbox arrays from (cropped) pandas (train.csv)
# @param data 
# @return np.array with bounding boxe
def get_img_bbox(data):
    """
    get_array_from_string Reads array from string and returns it as np.array
        @param array_str: string of arrays, e.g. "[1, 2, 3]"
        @return: np.array
    """
    bbox_all = np.array([])
    
    # Iterate boxes
    for index, row in data.iterrows():
        bbox_f = get_array_from_string( row['bbox'] )
        bbox_all = np.concatenate([bbox_all, bbox_f])

    return bbox_all

# @brief Plot image with bounding boxes
# @param image_string image name without *.jpg ending
def plot_boundingbox(data_box, image_str):
    
    # Get image and it's bounding boxes
    image = io.imread(image_str)
    bbox_all = get_img_bbox(data_box[data_box.image_id == image_str])
    
    # Plot data
    fig, ax = plt.subplots(1)
    ax.imshow(image)
    
    for bbox in bbox_all.reshape(-1,4):
        rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3],linewidth=1,edgecolor='r',facecolor='none')                    
        ax.add_patch(rect)
    
    plt.show()
