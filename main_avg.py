# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:30:42 2017

@author: Mauro

"""

# Define Imports

# matplotlib imports
import matplotlib.pyplot as plt

# My imports
from AvgFolder_class import AvgFolder


if __name__ == "__main__":
    print("START AVERAGING SCRIPT")
    
    mypath = "../silentcam/dataset29/"
    avg = AvgFolder(mypath)
    avg.gather_pictures()
    avg.c2gscale()
    avg.squareit()
    avg.binning(0)    
    avg.transpose()
    avg.normalize() 
    
    avg.save_imgs()

        
    avg.generate_template("UseFirstImage")
    avg.save_template()
    
    avg.template.show_image()
    plt.show()  
    
    avg.template.inspect()
    
    correlate = True
    if correlate:
        # aling dataset
        avg.align_images()
        avg.save_algimgs()
        avg.save_corrs()
        avg.save_shifts()
        
        avg.average()
        avg.save_avg()
        avg.avg.show_image()
        plt.show()    