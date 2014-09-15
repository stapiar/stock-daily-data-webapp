'''
Script that run the units test defined in the tests/ folder.
'''
import unittest

all_tests = unittest.TestLoader().discover("tests", pattern="*.py")
unittest.TextTestRunner().run(all_tests)

