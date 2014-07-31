## This problem aims to find the accuracy of an appliance detection algorithm

Setup:
We are given whole home energy data and a truth set of appliances defined by their wattage in Kilo Watts (kW)

Example:
A home has a fridge (200W), an electric vehicle (1500W) and a dryer (5000W) --> truth set  [ 0.2, 5.0, 1.5 ]

After this data is analyzed a "detected" appliance set is created --> detected set [ 0.19, 1.46, 1.12 ]

Problem:
Find the True Positives (Detected correctly), False Positives (Detected incorrectly) and
False Negatives (Did not detect)

A detected appliances is considered correct if it is _within 10%_ of the truth.

In the above example 

True Positives = [ 0.2 (0.19), 1.5 (1.46) ]   ---> Detected Fridge and Electric Vehicle Correctly
False Positives = [  _ (1.12) ]               ---> Detected a 1.12 kW appliance that was not present
False Negatives = [ 5.0 (_) ]                 ---> Failed to detect a 5.0 kW dryer