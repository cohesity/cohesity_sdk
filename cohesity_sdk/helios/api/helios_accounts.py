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
from cohesity_sdk.helios.model.helios_accounts import HeliosAccounts
from cohesity_sdk.helios.model.impersonation_action import ImpersonationAction
from cohesity_sdk.helios.model.mcm_tenant_action import McmTenantAction
from cohesity_sdk.helios.model.mcm_tenant_migration_status import McmTenantMigrationStatus
from cohesity_sdk.helios.model.mcm_tenant_profiles import McmTenantProfiles


class HeliosAccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_accounts(
            self,
            **kwargs
        ):
            """Get Accounts  # noqa: E501

            Get Helios Accounts  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_accounts(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                search_string (str, none_type): Filter by accounts which partially match the string.. [optional]
                support_case_id (str, none_type): Filter by Support Case ID. This must be specified if and only if the currently logged in user is a support user.. [optional]
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
                HeliosAccounts
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

        self.get_accounts = _Endpoint(
            settings={
                'response_type': (HeliosAccounts,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/accounts',
                'operation_id': 'get_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'region_id',
                    'search_string',
                    'support_case_id',
                ],
                'required': [],
                'nullable': [
                    'search_string',
                    'support_case_id',
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
                    'search_string':
                        (str, none_type,),
                    'support_case_id':
                        (str, none_type,),
                },
                'attribute_map': {
                    'region_id': 'regionId',
                    'search_string': 'searchString',
                    'support_case_id': 'supportCaseId',
                },
                'location_map': {
                    'region_id': 'header',
                    'search_string': 'query',
                    'support_case_id': 'query',
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
            callable=__get_accounts
        )

        def __mcm_get_tenant_migration_status(
            self,
            **kwargs
        ):
            """Get Tenant Migration Status  # noqa: E501

            Get the migration status for the current tenant.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.mcm_get_tenant_migration_status(async_req=True)
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
                McmTenantMigrationStatus
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

        self.mcm_get_tenant_migration_status = _Endpoint(
            settings={
                'response_type': (McmTenantMigrationStatus,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/tenants/migrations',
                'operation_id': 'mcm_get_tenant_migration_status',
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
            callable=__mcm_get_tenant_migration_status
        )

        def __mcm_get_tenant_profiles(
            self,
            **kwargs
        ):
            """Get Tenant profiles  # noqa: E501

            Get tenant profiles for currently logged in user.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.mcm_get_tenant_profiles(async_req=True)
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
                McmTenantProfiles
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

        self.mcm_get_tenant_profiles = _Endpoint(
            settings={
                'response_type': (McmTenantProfiles,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/tenant-profiles',
                'operation_id': 'mcm_get_tenant_profiles',
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
            callable=__mcm_get_tenant_profiles
        )

        def __mcm_perform_tenant_action(
            self,
            body,
            **kwargs
        ):
            """Perform Mcm Tenant Action  # noqa: E501

            Perform an action on a DMaaS tenant.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.mcm_perform_tenant_action(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (McmTenantAction): Specifies the parameters to perform a tenant action.

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
                McmTenantAction
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

        self.mcm_perform_tenant_action = _Endpoint(
            settings={
                'response_type': (McmTenantAction,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/tenants/actions',
                'operation_id': 'mcm_perform_tenant_action',
                'http_method': 'POST',
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
                        (McmTenantAction,),
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
            callable=__mcm_perform_tenant_action
        )

        def __perform_impersonation_action(
            self,
            body,
            **kwargs
        ):
            """Start or Stop Impersonation Session  # noqa: E501

            Starts or stops an impersonation session for Helios support and sales users.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.perform_impersonation_action(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (ImpersonationAction): Specifies the parameters to perform a tenant action.

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
                ImpersonationAction
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

        self.perform_impersonation_action = _Endpoint(
            settings={
                'response_type': (ImpersonationAction,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/accounts/impersonations/actions',
                'operation_id': 'perform_impersonation_action',
                'http_method': 'POST',
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
                        (ImpersonationAction,),
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
            callable=__perform_impersonation_action
        )
