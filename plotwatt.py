__author__ = 'Adam'


def detection_accuracy(truth, detected):
    """
        This method aims to find the accuracy of an appliance detection algorithm.
        It takes 2 lists:
            truth list of known values.
            detected list of detected values.
        The goal is to sort out the true positives, false positives, and false negatives
        A value in the detected list is a true positive if it is within 10% of a value in the truth list
        A value is a false positive if it is greater than 10%
        A value is a false negative if it was not detected
    """
    true_positives = []
    false_positives = []
    false_negatives = []
    temp_false_negatives = []

    # edge cases


    # determine true positives
    for detected_element in detected:
        for truth_element in truth:
            value = round(abs(truth_element - detected_element), 2)
            # if value is within 10%, it is a true positive
            if value * 100 <= 10:
                if detected_element not in true_positives:
                    true_positives.append(detected_element)
                    # we know that the truth element was matched, so add it to a temporary false_negatives array. later
                    # we can compare this to the truth array and difference them resulting in our false_negatives
                    if truth_element not in temp_false_negatives:
                        temp_false_negatives.append(truth_element)

    # determine false positives
    for detected_element in detected:
        for truth_element in truth:
            value = round(abs(truth_element - detected_element), 2)
            # if value is within 10%, it is a true positive
            if value * 100 > 10:
                if detected_element not in false_positives and detected_element not in true_positives:
                    false_positives.append(detected_element)
                    if truth_element not in temp_false_negatives:
                        temp_false_negatives.append(truth_element)

    # determine false negatives by taking the difference of temp_false_negatives and truth values
    for truth_element in truth:
        if truth_element not in temp_false_negatives:
            false_negatives.append(truth_element)

    # Consider the case where a negative value may have slipped in. This should not be allowed.
    true_positives = [x for x in true_positives if x > 0]
    false_positives = [x for x in false_positives if x > 0]
    false_negatives = [x for x in false_negatives if x > 0]

    return [true_positives, false_positives, false_negatives]


truth_1 = [0.2, 5.0, 1.5]
detected_1 = [1.8, 1.46, .19, 1.12]

print(detection_accuracy(truth_1, detected_1))