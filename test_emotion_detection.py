"""
Unit tests for the emotion detection application.
"""

import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetecton(unittest.TestCase):
    """
    Test cases for emotion detection dominant emotions.
    """

    def test_emotion_detection(self):

        result_1=emotion_detector("I am glad this happened")
        self.assertEqual(result_1,)