"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 2.0.3
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from ynab_api.api_client import ApiClient, Endpoint as _Endpoint
from ynab_api.model_utils import (  # noqa: F401
    check_allowed_values, check_validations, date, datetime, file_type,
    none_type, validate_and_convert_types)
from ynab_api.model.account_response import AccountResponse
from ynab_api.model.accounts_response import AccountsResponse
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.save_account_wrapper import SaveAccountWrapper


class AccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_account_endpoint = _Endpoint(
            settings={
                'response_type': (AccountResponse, ),
                'auth': ['bearer'],
                'endpoint_path': '/budgets/{budget_id}/accounts',
                'operation_id': 'create_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                    'data',
                ],
                'required': [
                    'budget_id',
                    'data',
                ],
                'nullable': [
                    'budget_id',
                ],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'budget_id': (
                        str,
                        none_type,
                    ),
                    'data': (SaveAccountWrapper, ),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                },
                'location_map': {
                    'budget_id': 'path',
                    'data': 'body',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)
        self.get_account_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (AccountResponse, ),
                'auth': ['bearer'],
                'endpoint_path': '/budgets/{budget_id}/accounts/{account_id}',
                'operation_id': 'get_account_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                    'account_id',
                ],
                'required': [
                    'budget_id',
                    'account_id',
                ],
                'nullable': [
                    'budget_id',
                    'account_id',
                ],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'budget_id': (
                        str,
                        none_type,
                    ),
                    'account_id': (
                        str,
                        none_type,
                    ),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                    'account_id': 'account_id',
                },
                'location_map': {
                    'budget_id': 'path',
                    'account_id': 'path',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)
        self.get_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (AccountsResponse, ),
                'auth': ['bearer'],
                'endpoint_path': '/budgets/{budget_id}/accounts',
                'operation_id': 'get_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'budget_id',
                    'last_knowledge_of_server',
                ],
                'required': [
                    'budget_id',
                ],
                'nullable': [
                    'budget_id',
                    'last_knowledge_of_server',
                ],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'budget_id': (
                        str,
                        none_type,
                    ),
                    'last_knowledge_of_server': (
                        int,
                        none_type,
                    ),
                },
                'attribute_map': {
                    'budget_id': 'budget_id',
                    'last_knowledge_of_server': 'last_knowledge_of_server',
                },
                'location_map': {
                    'budget_id': 'path',
                    'last_knowledge_of_server': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)

    def create_account(self, budget_id, data, **kwargs):
        """Create a new account  # noqa: E501

        Creates a new account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_account(budget_id, data, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str, none_type): The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
            data (SaveAccountWrapper): The account to create.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        kwargs['data'] = \
            data
        return self.create_account_endpoint.call_with_http_info(**kwargs)

    def get_account_by_id(self, budget_id, account_id, **kwargs):
        """Single account  # noqa: E501

        Returns a single account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_by_id(budget_id, account_id, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str, none_type): The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
            account_id (str, none_type): The id of the account

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        kwargs['account_id'] = \
            account_id
        return self.get_account_by_id_endpoint.call_with_http_info(**kwargs)

    def get_accounts(self, budget_id, **kwargs):
        """Account list  # noqa: E501

        Returns all accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_accounts(budget_id, async_req=True)
        >>> result = thread.get()

        Args:
            budget_id (str, none_type): The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).

        Keyword Args:
            last_knowledge_of_server (int, none_type): The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['budget_id'] = \
            budget_id
        return self.get_accounts_endpoint.call_with_http_info(**kwargs)
