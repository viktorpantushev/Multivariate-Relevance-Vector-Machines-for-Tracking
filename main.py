import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

import os

paths = []
for dirname, _, filenames in os.walk("C:/Users/vikto/PycharmProjects/Multivariate-Relevance-Vector-Machines-for-Tracking/images"):
    for filename in filenames:
        paths.append(os.path.join(dirname, filename).replace("\\", "/"))

print(paths)


