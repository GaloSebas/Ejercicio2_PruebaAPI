import unittest
import HtmlTestRunner

from api_automation_example import api_example_petstore

# Generate the test suite
def test_suite():
    suite = unittest.TestSuite()
    # Add each TC to define an execution order
    suite.addTest(api_example_petstore('test_add_pet'))
    suite.addTest(api_example_petstore('test_get_pet_by_id'))
    suite.addTest(api_example_petstore('test_update_pet'))
    suite.addTest(api_example_petstore('test_get_pet_by_status'))
    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='Reports', report_name='e2e_Results_Report', verbosity=2)
    runner.run(test_suite())
    
