# FloroHydrogel_Tracking

This is the final project of the software carpentry, in which I'm writing a code for my research about the shape-controlled DNA-integrated hydrogel.

We try to swell and contract the hygrogels with dna hairpins by inserting the hairpins into the polymer network, and observe their area change by taking time-lapse photo and further tracking them with image analysis and plotting their swelling curve using the code developed.

To run the code, make sure the main code is in the same directory with the folders of gels (ex:TS1), it has several functions that cuts the analysis into several steps:

In step 1, we use Gel_Cropping to crop out each individual gels from the big picture before start workin on it.

Then, step 2 is the actual analysis part, in which we use Area_Calculation to calculate the area in each picture and output a txt file containing the list of areas of different time.

Step 3, would be the merging and plotting part. We use Curve_Merging to merge the curves and Curve_Plotting to plot them.

Finally, there is a video_creation function that creates a video by combining the time lapse images of the gels.

The code is developed by Kuan-Lin Chen, and is used for research purpose, please do not use for commercial purpose.
The author thanks Dr. Henry Herbol, Dr. Joshua Fern, and Hsiang-Yun Chien for insightsul advices and helps.
