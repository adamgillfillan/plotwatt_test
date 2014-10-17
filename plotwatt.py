__author__ = 'Adam'


def detection_accuracy(truth, detected):
    """
        This method aims to find the accuracy of an appliance detection algorithm.
        It takes 2 lists:
            truth list of known values.
            detected list of detected values.
        The goal is to sort out the true positives, false positives, and false negatives
    """
    true_positives = []
    false_positives = []
    false_negatives = []

    for detected_element in detected:
        for truth_element in truth:
            value = round(abs(truth_element - detected_element), 2)
            if value * 100 <= 10:
                true_positives.append(detected_element)
            if value * 100 > 10:
                false_negatives.append(detected_element)


    return [true_positives, false_positives, false_negatives]