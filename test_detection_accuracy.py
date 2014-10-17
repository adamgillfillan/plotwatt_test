__author__ = 'Adam'
import unittest
import plotwatt


class TestDetectionAccuracy(unittest.TestCase):
    def setUp(self):
        self.truth = [0.2, 5.0, 1.5]
        self.detected = [0.19, 1.46, 1.8, 1.12]

        self.true_positives = [0.19, 1.46]
        self.false_positives = [1.8, 1.12]
        self.false_negatives = [5.0]

    def test_detection_accuracy(self):
        self.assertEquals(plotwatt.detection_accuracy(self.truth, self.detected),
                          [self.true_positives,
                          self.false_positives,
                          self.false_negatives])