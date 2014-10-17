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
    temp_false_negatives = []

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
                    if truth_element not in false_negatives:
                        temp_false_negatives.append(truth_element)

    # determine false positives
    for detected_element in detected:
        for truth_element in truth:
            value = round(abs(truth_element - detected_element), 2)
            # if value is within 10%, it is a true positive
            if value * 100 > 10:
                if detected_element not in false_positives and detected_element not in true_positives:
                    false_positives.append(detected_element)
                    if truth_element not in false_negatives:
                        temp_false_negatives.append(truth_element)

    # determine false negatives by taking the difference of temp_false_negatives and truth values
    for truth_element in truth:
        if truth_element not in temp_false_negatives:
            false_negatives.append(truth_element)

    return [true_positives, false_positives, false_negatives]


truth_1 = [0.2, 5.0, 1.5]
detected_1 = [1.8, 1.46, .19, 1.12]

print(detection_accuracy(truth_1, detected_1))