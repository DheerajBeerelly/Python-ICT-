'''

Name : Dheeraj Mahanidhi Beerelly
Date: 08/16/2022
Course: ICT-4370-1
Week 10: DISCUSSION B - TESTING APPLIED


'''

import unittest




class Stock():

    def __init__(self,symbol,number_of_shares,purchase_price):
        self.symbol = symbol
        self.number_of_shares = number_of_shares
        self.purchase_price = purchase_price
  
class UnitTestSample(unittest.TestCase):
      
    # Returns True if the symbol contains GOOG.
    def test_symbol(self):
        o = Stock('GOOG', 100,123.12)
        self.assertEqual( o.symbol, 'GOOG')

    def test_numberofshares(self):
        o = Stock('GOOG', 100,123.12)
        self.assertEqual( o.number_of_shares, 100)

    def test_purchaseprice(self):
        o = Stock('GOOG', 100,123.12)
        self.assertEqual( o.purchase_price, 123.12)
  
    
  
if __name__ == '__main__':
    unittest.main()
