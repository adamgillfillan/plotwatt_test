**This problem aims to find the accuracy of an appliance detection algorithm**

##### Setup:
We are given whole home energy data and a truth set of appliances defined by their wattage in Kilo Watts (kW)

##### Example:
A home has a fridge (200W), an electric vehicle (1500W) and a dryer (5000W) --> 
```
truth set: [ 0.2, 5.0, 1.5 ]
```
After this data is analyzed a "detected" appliance set is created --> 
```
detected set: [ 0.19, 1.46, 1.12 ]
```

##### Problem:
Find the **True Positives** (Detected correctly), 
**False Positives** (Detected incorrectly) and
**False Negatives** (Did not detect)

A detected appliance is considered correct if it is **within 10%** of the truth.

In the above example 
```
True Positives = [ 0.2 (0.19), 1.5 (1.46) ]   ---> Detected Fridge and Electric Vehicle Correctly
False Positives = [  _ (1.12) ]               ---> Detected a 1.12 kW appliance that was not present
False Negatives = [ 5.0 (_) ]                 ---> Failed to detect a 5.0 kW dryer
```

Write a simple python library for algorithm developers to use when measuring the performance of their appliance detection algorithms.

##### Notes:

* Be sure to consider edge cases.  Use your best judgement and the provided context to decide on how to deal with them.
* Use a public version control system such as github or bitbucket and check in with enough frequency that we can get a rough idea of the time spent working on the solution.
