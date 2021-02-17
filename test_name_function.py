import unittest
from name_function import *

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        
        formatted_name = get_formatted_name('janis','japlin')
        self.assertEqual(formatted_name,'Janis Japlin')

    def test_first_middle_last_name(self):

        formatted_name = get_formatted_name('janis','joe','japlin')
        self.assertEqual(formatted_name,'Janis Japlin Joe')
    
unittest.main()