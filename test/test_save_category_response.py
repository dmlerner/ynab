"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

import ynab_api
from ynab_api.model.save_category_response_data import SaveCategoryResponseData

globals()['SaveCategoryResponseData'] = SaveCategoryResponseData
from ynab_api.model.save_category_response import SaveCategoryResponse


class TestSaveCategoryResponse(unittest.TestCase):
    """SaveCategoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSaveCategoryResponse(self):
        """Test SaveCategoryResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SaveCategoryResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
