# Multivariate-Relevance-Vector-Machines-for-Tracking
Imitating the results from "Multivariate Relevance Vector Machines for Tracking" from A. Tayananthan et al. 

 <br>

My Steps:  
1.  Use Canny Edges to extract Outlines of Hand-Poses.
2.  Make a hierarchy (tree ‘grid-based’ filter)

 <br>
 
How to replicate:
1.  Download and save from https://www.kaggle.com/code/stpeteishii/hand-gestures-mediapipe-images/input as "/images"
2.  I recommend reading https://mi.eng.cam.ac.uk/~cipolla/publications/inproceedings/2003-ICCV-Stenger-filtering.pdf
 
<br>

Problems & Solutions:
1.  How should I create the hierarchy?

-> The highest level of the tree will represent the coarsest partition, thus the lowest level represents the finest partition