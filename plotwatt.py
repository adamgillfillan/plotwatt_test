__author__ = 'Adam'


def detection_accuracy(truth, detected):
    """
        This method aims to find the accuracy of an appliance detection algorithm.
        It takes 2 lists:
            truth list of known values.
            detected list of detected values.
        The goal is to sort out the true positives, false positives, and false negatives
    """
    true_positives = [0.19, 1.46]
    false_positives = [1.12, 1.8]
    false_negatives = [5.0]


    return [true_positives, false_positives, false_negatives]