import sys
sys.path.append('../')
import unittest
from src.Event import *
# I have tested the beginningOfWorld function in the Event class below.
#

class EventTests(unittest.TestCase):

    def test_beginningOfWorld_True(self):
        self.assertTrue(Event.beginningOfWorld(0))

    def test_beginningOfWorld_False(self):
        self.assertFalse(Event.beginningOfWorld(1))

    def test_beginningOfWorld_Negative(self):
        self.assertTrue(Event.beginningOfWorld(-1))

if __name__ == "__main__":
    unittest.main()
