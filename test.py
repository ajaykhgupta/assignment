import unittest

def get_result(marks):
  if marks < 35:
    result = 'Not cleared'
  else:
    result = 'Congrats!! Passed'             
  return result


class NearestExitTests(unittest.TestCase):

  def test_val_1(self):
    self.assertEqual(get_result(32), 'Not cleared')
    
 
  def test_val_2(self):
    self.assertEqual(get_result(45), 'Congrats!! Passed')
    

unittest.main()