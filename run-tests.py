import unittest
import re
import numpy as np
import pandas as pd
from model import model_predict,model_train
from datetime import date

class TestModel(unittest.TestCase):

    # example test method
    def test_uk(self):
        out = model_predict("united_kingdom","2018","06","09")
        print(out)
        self.assertEqual(abs(195732.10533-out['y_pred'][0]) < 0.001, True )

    def test_all(self):
        out = model_predict("all","2018","06","09")
        print(out)
        self.assertEqual(abs(211410.32333-out['y_pred'][0]) < 0.001, True )

class TestLogging(unittest.TestCase):

    def test_log(self):
        today = date.today()
        logfile = "predict-{}-{}.log".format(today.year, today.month)
        beforecount  = len(pd.read_csv(logfile))
        out = model_predict("all","2018","06","09")
        aftercount = len(pd.read_csv(logfile))
        print(beforecount,aftercount)
        self.assertEqual(beforecount < aftercount,True)

class TestAPI(unittest.TestCase):

    @unittest.expectedFailure
    def test_no_date(self):
        self.assertRaises(Exception, model_predict("all"))

    @unittest.expectedFailure
    def test_date_out_of_range(self):
        self.assertRaises(Exception, model_predict("all","2016","06","09"))

if __name__ == '__main__':
    unittest.main()
