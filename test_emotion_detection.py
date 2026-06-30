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
        self.assertEqual(result_1,"joy")

        result_2=emotion_detector("I am really mad about this")
        self.assertEqual(result_2,"anger")

        result_3=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3,"disgust")

        result_4=emotion_detector("I am so sad about this")
        self.assertEqual(result_4,"sadness")

        result_5=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5,"fear")


if __name__ == "main":
    unittest.main()