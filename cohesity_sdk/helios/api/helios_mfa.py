"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.helios.api_client import ApiClient, Endpoint as _Endpoint
from cohesity_sdk.helios.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_mfa import HeliosMfa


class HeliosMfaApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_mfa_preferences(
            self,
            **kwargs
        ):
            """Get MFA Preferences  # noqa: E501

            Gets the Multi Factor Authentication configuration for the account.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_mfa_preferences(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
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
                HeliosMfa
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_mfa_preferences = _Endpoint(
            settings={
                'response_type': (HeliosMfa,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/mfa',
                'operation_id': 'get_mfa_preferences',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'region_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'region_id':
                        (str,),
                },
                'attribute_map': {
                    'region_id': 'regionId',
                },
                'location_map': {
                    'region_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_mfa_preferences
        )

        def __update_mfa_preferences(
            self,
            body,
            **kwargs
        ):
            """Update MFA Preferences  # noqa: E501

            Updates the Multi Factor Authentication configuration for the account.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_mfa_preferences(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (HeliosMfa): Specifies the parameters to support MFA.

            Keyword Args:
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
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
                HeliosMfa
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_mfa_preferences = _Endpoint(
            settings={
                'response_type': (HeliosMfa,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/mfa',
                'operation_id': 'update_mfa_preferences',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                    'region_id',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (HeliosMfa,),
                    'region_id':
                        (str,),
                },
                'attribute_map': {
                    'region_id': 'regionId',
                },
                'location_map': {
                    'body': 'body',
                    'region_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_mfa_preferences
        )
