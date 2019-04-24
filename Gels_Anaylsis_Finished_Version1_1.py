"""
Author: Kuan-Lin Chen
Last Edited Date: 2019.04.24
Project: Image Analysis For Florescent Hydrogel Area Tracking
Info:
    This is the final project of the software carpentry, in which I'm writing a code for my research about the shape-controlled DNA-integrated hydrogel.

    We try to swell and contract the hygrogels with dna hairpins by inserting the hairpins into the polymer network, and observe their area change by taking time-lapse photo and further tracking them with image analysis and plotting their swelling curve using the code developed.

Tips:
    1. Command+Ctrl+G to select all same words

To Add:
    1. Video Creating Function (ADDED!)
    2. Edge detection (Ex. Sobel filter)
    3. Fix the problem of area calculation = 0 for all png files
    4. Add checking for Area Calculation
"""

import os
import time
import cv2
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt


def Gel_Cropping(GEL_NUM = 1, PIC_NUM = 1, START_NUM = 1, MASK = 100, data_folder = "Data_To_Be_Analyzed", image_name = "subImage", file_type = ".tif", output_type = ".tif"):
    """
    This function opens the series of gel figures and crop out different gels, creates  a folder for each gels and save the figure for each cropped gels.

    **Important**
        When selecting, left clicks can be used to remove unwanted clicks!

    Each figures are cropped from the middle of the selected point, and cropped with a square with pixel numbers specified by the parameter "MASK". If the gels are pretty big, increase the mask size, but note that this will take a longer cropping time.

    Note that you may also specify what format the output file wanted.

    **Parameters**
        GEL_NUM *int*
            number of gels you want to analyze.
        PIC_NUM *int*
            number of images you want to analyze.
        START_NUM *int*
            the starting number of the gel.
        MASK *int*
            the size of maks you're using for analysis.
        data_folder *string*
            the name of the mother folder where all your images resides in.
        image_name *string*
            the name of the images starts with.
        file_type *string*
            the type of file of the figures analyzing.
        output_type *string*
            the output format for the figures saved.

    **Returns**
        Not returning anything, but gives a print statement when the cropping is done.
    """

    # Parameter Setting and subfolder creating
    start_time = time.time()
    pic = img.imread("/".join([data_folder,image_name+str(1)+ file_type]))
    shapey = pic.shape; NROWS, NCOLS = shapey[:2]
    plt.imshow(pic, cmap = plt.cm.gray)
    gel_pos = plt.ginput(GEL_NUM, timeout = 0, show_clicks = True, mouse_add = 1, mouse_pop = 3)
    plt.close()
    gel_x, gel_y = [], []

    for i in range(GEL_NUM):
        folder_name = "/".join([os.getcwd(),data_folder,"gel_"+str(START_NUM + i)])
        gel_x.append(int(gel_pos[i][0]))
        gel_y.append(int(gel_pos[i][1]))
        os.mkdir(folder_name)

    # Image Reading and Cropping
    for which_pic in range(PIC_NUM):
        for which_gel in range(GEL_NUM):
            fig = img.imread("/".join([data_folder,image_name+str(which_pic+1)+ file_type]))
            xvals = range(max(0, gel_x[which_gel] - MASK), min(gel_x[which_gel] + MASK + 1, NCOLS))
            yvals = range(max(0, gel_y[which_gel] - MASK), min(gel_y[which_gel] + MASK + 1, NROWS))
            cropped = fig[np.ix_(yvals, xvals)]
            plt.imshow(cropped, cmap=plt.cm.gray)
            plt.axis('off') # Important! Otherwise, will have additional axis
            cropped_name = "/".join([os.getcwd(), data_folder, "gel_"+str(which_gel + START_NUM), image_name + str(which_pic + 1) + output_type])
            plt.savefig(cropped_name, bbox_inches = "tight", pad_inches = -0.5)
    end_time = time.time()

    # End of the process
    print("%d gels cropped in %.2f sec " %(GEL_NUM, (end_time - start_time)))

def Gel_Cropping_txt(GEL_NUM = 1, PIC_NUM = 1, START_NUM = 1, MASK = 100, data_folder = "Data_To_Be_Analyzed", image_name = "subImage", file_type = ".tif"):
    """
    This function opens the series of gel figures and crop out different gels, creates  a folder for each gels and save the image information in a txt file for each cropped gels.

    **Important**
        When selecting, left clicks can be used to remove unwanted clicks!

    This is a txt version of the Gel_Cropping function, and because it saves a txt file instead, it is much much faster. However, trade-off is that you will be unable to view the images directly, so you won't know what's wrong if the curve and images are naughty.

    Each figures are cropped from the middle of the selected point, and cropped with a square with pixel numbers specified by the parameter "MASK". If the gels are pretty big, increase the mask size, but note that this will take a longer cropping time.

    **Parameters**
        GEL_NUM *int*
            number of gels you want to analyze.
        PIC_NUM *int*
            number of images you want to analyze.
        START_NUM *int*
            the starting number of the gel.
        MASK *int*
            the size of maks you're using for analysis.
        data_folder *string*
            the name of the mother folder where all your images resides in.
        image_name *string*
            the name of the images starts with.
        file_type *string*
            the type of file of the figures analyzing.

    **Returns**
        Not returning anything, but gives a print statement when the cropping is done.
    """

    # Parameter Setting and subfolder creating
    start_time = time.time()
    pic = img.imread("/".join([data_folder,image_name+str(1)+ file_type]))
    shapey = pic.shape; NROWS, NCOLS = shapey[:2]
    plt.imshow(pic, cmap = plt.cm.gray)
    gel_pos = plt.ginput(GEL_NUM, timeout = 0, show_clicks = True, mouse_add = 1, mouse_pop = 3)
    plt.close()
    gel_x, gel_y = [], []
    for i in range(GEL_NUM):
        folder_name = "/".join([os.getcwd(),data_folder,"gel_"+str(START_NUM + i)+"_txt"])
        gel_x.append(int(gel_pos[i][0]))
        gel_y.append(int(gel_pos[i][1]))
        os.mkdir(folder_name)

    # Image Reading and Cropping
    for which_pic in range(PIC_NUM):
        for which_gel in range(GEL_NUM):
            fig = img.imread("/".join([data_folder,image_name+str(which_pic+1)+ file_type]))
            xvals = range(max(0, gel_x[which_gel] - MASK), min(gel_x[which_gel] + MASK + 1, NCOLS))
            yvals = range(max(0, gel_y[which_gel] - MASK), min(gel_y[which_gel] + MASK + 1, NROWS))
            cropped = fig[np.ix_(yvals, xvals)]
            cropped_name = "/".join([os.getcwd(), data_folder, "gel_"+str(which_gel + START_NUM)+"_txt", image_name + str(which_pic + 1) + ".txt"])
            np.savetxt(cropped_name, cropped, fmt = "%d")
    end_time = time.time()

    # End of the process
    print("%d gels cropped in %.2f sec " %(GEL_NUM, (end_time - start_time)))


def Area_Calculation(PIC_NUM = 1, DELTA = 100, data_folder = "Data_To_Be_Analyzed", gel_folder = "gel_1" , image_name = "subImage", file_type = ".tif"):
    """
    Reads in the series of cropped gel images and calculates the area of the gels and save the list of the area into a txt file. Note that the value are all normalized with the first value of the gel.

    **Important**
        Does not work with png files yet, need to fix that!

    **Parameters**
        PIC_NUM *int*
            number of images you want to analyze.
        DELTA *int*
            the intensity difference tolerance of the algorithm.
        data_folder *string*
            the name of the mother folder where all your sub folders resides in.
        gel_folder *string*
            the name of the sub folder where all your images resides in.
        image_name *string*
            the name of the images starts with.
        file_type *string*
            the type of file of the figures analyzing.

    **Returns**
        Not returning anything, but gives a print statement when the area calculation is done.
    """

    def area_sum(pic, rows, cols, delta, brightest):
        """
        The algorithm for calculating the gel area.

        The area is detected up by comparing the intensity of every single pixel inside the figure, and by comparing them to a manually selected intensity, and sum up all those pixels that have similar intensity with the selected brightness.

        However, this causes a problem when there are some random bright spot in the figure, thinking of using the sobel filter!
        """

        area_pixels = 0
        for i in range(rows):
            for j in range(cols):
                if abs(np.average(pic[i][j]) - brightest) < delta:
                    area_pixels += 1
        return area_pixels

    # Selecting a standard intensity
    start_time = time.time()
    working_file = "/".join([os.getcwd(),data_folder,gel_folder,image_name + str(1) + file_type])
    pic = img.imread(working_file)
    shapey = pic.shape; NROWS, NCOLS = shapey[:2]
    plt.imshow(pic, cmap=plt.cm.gray)
    brightest = plt.ginput()
    x = int(brightest[0][0]); y = int(brightest[0][1])
    brightest_val = np.average(pic[y][x])
    plt.close()

    # Area Calculation and Normalization
    area_list = []
    unswell_area = area_sum(pic, rows = NROWS, cols = NCOLS, delta = DELTA, brightest = brightest_val)
    for num in range(PIC_NUM):
        area_pixels = 0
        working_file = "/".join([os.getcwd(),data_folder,gel_folder,image_name + str(num + 1) + file_type])
        pic = img.imread(working_file)
        area_list.append(((float(area_sum(pic, rows = NROWS, cols = NCOLS, delta = DELTA, brightest = brightest_val)) / unswell_area) - 1) * 100)

    # Saving a txt file containing the list
    saving_file = "/".join([os.getcwd(),data_folder,gel_folder,gel_folder + ".txt"])
    f = open (saving_file, "w")
    f.writelines(["%.2f\n" % item  for item in area_list])
    f.close()
    end_time = time.time()

    # End of the process
    print("Curve is saved in %.2f secs for %s" %(end_time - start_time,gel_folder))

def Area_Calculation_txt(PIC_NUM = 120, DELTA = 5000, data_folder = "Data_To_Be_Analyzed_2", gel_folder = "gel_1" , image_name = "subImage", AUTO = False):
    """
    Reads in the series of cropped gel image arrays and calculates the area of the gels and save the list of the area into a txt file. Note that the value are all normalized with the first value of the gel.

    Note that this function includes an auto flag, that allows users to automatically calculate the area without specifying a standard brightness for each gels. As it automatically finds out the brightest spot and use that as the standard brightness value, for this algorithm, the delta becomes 3.5 standard deviation to accurately include all gel-like brightness.

    **Parameters**
        PIC_NUM *int*
            number of images you want to analyze.
        DELTA *int*
            the intensity difference tolerance of the algorithm.
        data_folder *string*
            the name of the mother folder where all your sub folders resides in.
        gel_folder *string*
            the name of the sub folder where all your images resides in.
        image_name *string*
            the name of the images starts with.
        file_type *string*
            the type of file of the figures analyzing.
        AUTO *boolyn*
            If true, runs the function without specifying a standard brightness for each gels

    **Returns**
        Not returning anything, but gives a print statement when the area calculation is done.
    """

    def area_sum(pic, rows, cols, delta, brightest):
        """
        The algorithm for calculating the gel area. The area is detected up by comparing the intensity of every single pixel inside the figure, and by comparing them to a manually selected intensity, and sum up all those pixels that have similar intensity with the selected brightness.

        """
        area_pixels = 0
        for i in range(rows):
            for j in range(cols):
                if abs(pic[i][j] - brightest) < delta:
                    area_pixels += 1
        return area_pixels

    # Selecting a standard intensity
    start_time = time.time()
    working_file = "/".join([os.getcwd(),data_folder,gel_folder,image_name + str(1) + ".txt"])
    pic = np.loadtxt(working_file)
    shapey = pic.shape; NROWS, NCOLS = shapey[:2]
    if AUTO == False:
        plt.imshow(pic, cmap=plt.cm.gray)
        brightest = plt.ginput()
        x = int(brightest[0][0]); y = int(brightest[0][1])
        brightest_val = pic[y][x]
        plt.close()
    else:
        brightest_val = pic.max()
        DELTA = 3.5 * pic.std()

    # Area Calculation
    area_list = []
    unswell_area = area_sum(pic, rows = NROWS, cols = NCOLS, delta = DELTA, brightest = brightest_val)
    for num in range(PIC_NUM):
        area_pixels = 0
        working_file = "/".join([os.getcwd(),data_folder,gel_folder,image_name + str(num + 1) + ".txt"])
        pic = np.loadtxt(working_file)
        area_list.append(((float(area_sum(pic, rows = NROWS, cols = NCOLS, delta = DELTA, brightest = brightest_val)) / unswell_area)- 1)* 100)

    # Saving a txt file containing the list
    saving_file = "/".join([os.getcwd(),data_folder,gel_folder,gel_folder + ".txt"])
    f = open (saving_file, "w")
    f.writelines(["%.2f\n" % item  for item in area_list])
    f.close()
    end_time = time.time()

    # End of the process
    print("Curve is saved in %.2f secs for %s" %(end_time - start_time,gel_folder))


def Curve_Merging(PIC_NUM = 120, data_folder = "Data_To_Be_Analyzed", dir_of_curves = ["gel_1", "gel_2", "gel_3"]):
    """
    This function is used when you are doing experiments for a lot of gels and you want to merge the curves to decrease the noise and also show the error.

    The function reads in different lists of swelling curve, calculates the average swelling degree and standard deviation at each time point. Then returns an array containing the average swelling curve and two more curves containg the average (+/-) std as the upper and lower bound of the swelling behavior of the gel.

    **Parameters**
        PIC_NUM *int*
            number of images you used to analyze.
        data_folder *string*
            the name of the mother folder where all your sub folders resides in.
        dir_of_curves *string*
            a list containing all the curves that you want to merge.

    **Returns**
        merged_data *numpy array*
            an array containing the swelling curve within one std deviation.
            merged_data[0] = average swelling + std (upper bound)
            merged_data[1] = average swelling
            merged_data[2] = average swelling + std (lower bound)
    """

    curve_num = len(dir_of_curves)
    merged_data = np.zeros(shape = (curve_num + 3,PIC_NUM))

    for num in range(curve_num):
        working_file = "/".join([os.getcwd(), data_folder, dir_of_curves[num], dir_of_curves[num] + ".txt"])
        file = open(working_file, "r")
        data_read = file.read()
        file.close()
        curve = []
        for i in data_read.split():
            curve.append(i)
        merged_data[num] = curve

    avg_list = []; upper_lst = []; lower_lst = [] #  std_list = [];
    for i in range(PIC_NUM):
        avg_list.append(np.average([merged_data[j][i] for j in range(curve_num)]))
        area_deviation = np.std([merged_data[j][i] for j in range(curve_num)])
        upper_lst.append(avg_list[i] + area_deviation)
        lower_lst.append(avg_list[i] - area_deviation)

    merged_data[-3] = lower_lst; merged_data[-2] = avg_list; merged_data[-1] = upper_lst

    return merged_data[-3:]

def Curve_Plotting(gel_data, time_diff = 0.5, PIC_NUM = 60, color_name = "chocolate", label_name = "20uM Hairpin"):
    """
    Plot the actual curve, the upper bound and lower bound of the curve and fill in the area in between showing the swelling error.

    **Parameters**
        gel_data *array*
            the array containing the upper bound, actual curve and lower bound.
        time_diff *float*
            unit: hr
            the time difference between each picture.
        PIC_NUM *int*
            the total amount of images analyzed.
        color_name *string*
            the color of the line wished to be plotted.
        label_name *string*
            the name of the line, usually named after the experimental condition.

    **Returns**
        Returns nothing.
    """

    time_lst = np.linspace(0,(PIC_NUM-1) * time_diff, PIC_NUM)
    plt.plot(time_lst, gel_data[0],color = color_name ,alpha = 0.1)
    plt.plot(time_lst, gel_data[1],color = color_name , alpha = 1, label = label_name)
    plt.plot(time_lst, gel_data[2],color = color_name , alpha = 0.1)
    plt.fill_between(time_lst, gel_data[0], gel_data[2],color = color_name ,alpha = 0.1)

def video_creation(time_diff = 0.5, PIC_NUM = 50, data_folder = "Data_To_Be_Analyzed", gel_folder = "gel_3" , image_name = "subImage",file_type = ".tif"):
    """
    Creates the video of the swelling reaction of the gels from a series of the gel images.

    ** Parameters**
        time_diff *float*
            unit: hr
            the time difference between each picture.
        PIC_NUM *int*
            number of images you want to analyze.
        data_folder *string*
            the name of the mother folder where all your sub folders resides in.
        gel_folder *string*
            the name of the sub folder where all your images resides in.
        image_name *string*
            the name of the images starts with.
        file_type *string*
            the type of file of the figures analyzing.

    **Returns**
        does not returns anything
    """

    # Parameter Setting
    start_time = time.time()
    video_name = gel_folder + ".avi"
    image_folder = "/".join([os.getcwd(),data_folder,gel_folder])
    num = 0.0; images = []
    for i in range(PIC_NUM):
        images.append(image_folder + "/" + image_name + str(i + 1) + file_type)
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Video Creating
    video = cv2.VideoWriter(video_name, 0, 5, (width,height))
    # cv2.VideoWriter(video_name, code, frame, (width,height))
    # Increase the frame = increase fps, makes the video faster
    for image in images:
        temp_img = cv2.imread(image)
        word = "t = %.1fhr" %num
        num += 0.5
        cv2.putText(temp_img,word,(0,30), font, 1, (255,255,255), 2, cv2.LINE_AA)
        video.write(temp_img)
    cv2.destroyAllWindows()
    video.release()
    end_time = time.time()

    # End of the process
    print("Video created in %.2f sec " %(end_time - start_time))

if __name__ == "__main__":

    Gel_Cropping(GEL_NUM = 1, PIC_NUM = 100, START_NUM = 1, MASK = 100, data_folder = "TS1", image_name = "subImage", file_type = ".tif", output_type = ".tif")

    Gel_Cropping_txt(GEL_NUM = 2, PIC_NUM = 100, MASK = 100, data_folder = "TS1", image_name = "subImage", file_type = ".tif", START_NUM = 2)

    Area_Calculation(PIC_NUM = 100, DELTA = 100, data_folder = "TS1", gel_folder = "gel_1" , image_name = "subImage", file_type = ".tif")

    for gels in ["gel_" + str(i+2) + "_txt" for i in range(2)]:
        Area_Calculation_txt(PIC_NUM = 100, data_folder = "TS1", gel_folder = gels , image_name = "subImage", AUTO = True, DELTA = 2000)

    gel_data_1 = Curve_Merging(PIC_NUM = 100 ,dir_of_curves =  ["gel_1", "gel_2_txt", "gel_3_txt"], data_folder = "TS1")

    Curve_Plotting(gel_data_1, time_diff = 0.5, PIC_NUM = 100, color_name = "blue", label_name = "[HP] = 20uM")

    video_creation(time_diff = 0.5, PIC_NUM = 100, data_folder = "TS1", gel_folder = "gel_1" , image_name = "subImage",file_type = ".tif")

    # # Plotting Settings
    plt.title("Swelling Curve of DNA-integrated Hydrogel")
    plt.grid(alpha = 0.1)
    plt.xlabel('time(hr)')
    plt.ylabel(r'$\Delta Area$' + "(%)")
    # plt.legend(loc = 4)
    plt.legend()

    # # Optional Settings
    # # plt.xlim((0,60))
    # # plt.ylim((90,130))
    # plt.axis('square')
    plt.show()












