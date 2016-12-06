from question2 import validIPforScanning
import unittest

class test_question2(unittest.TestCase):
  def test_invalid_network_address(self):
    #invalid network address
    self.assertFalse(validIPforScanning('192.1313.224.2332/24',['192.168.1.12','192.168.2.12']))
  def test_empty_input_list(self):
    #empty input list
    self.assertFalse(validIPforScanning('192.168.1.0/24',[]))
  def test_invalid_subnet_mask(self):
    #invalid subnet mask
    self.assertFalse(validIPforScanning('192.168.1.0/214',['192.168.1.12','192.168.2.12']))
  def test_invalid_address_format(self):
    #invalid IP address format
    self.assertFalse(validIPforScanning('192.168.1.041ascsc/214',['192.168.1.12','192.168.2.12']))
  def test_input_set_not_in_network_range(self):
    # Input data list contains IP addresses not in the network range
    self.assertFalse(validIPforScanning('192.168.1.0/24',['192.168.1.12','192.168.2.12','124.31.13.131']))
  def test_invalid_IP_address_format_in_input_list(self):
    # Input data list has invalid IP address format
    self.assertFalse(validIPforScanning('192.168.1.0/24',['192.168.2sas1.12','192.168.2.12']))
    
  def test_correct1(self):
    self.assertTrue(validIPforScanning('192.168.1.0/24',['192.168.1.12','192.168.1.14']))
  def test_correct2(self):
    self.assertTrue(validIPforScanning('129.186.2.0/24',['129.186.2.12','129.186.2.14']))
  def test_correct3(self):
    self.assertTrue(validIPforScanning('10.8.123.0/24',['10.8.123.12','10.8.123.14','10.8.123.123']))
    
    
    
    
    
    
if __name__ == "__main__":
  unittest.main(exit=False)
