"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cluster.api_client import ApiClient, Endpoint as _Endpoint
from cohesity_sdk.cluster.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.kerberos_provider import KerberosProvider
from cohesity_sdk.cluster.model.kerberos_providers import KerberosProviders
from cohesity_sdk.cluster.model.register_or_update_kerberos_provider_request import RegisterOrUpdateKerberosProviderRequest
from cohesity_sdk.cluster.model.unregister_kerberos_provider import UnregisterKerberosProvider
from cohesity_sdk.cluster.model.unregister_kerberos_request import UnregisterKerberosRequest


class KerberosProvidersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_kerberos_provider_by_id(
            self,
            id,
            **kwargs
        ):
            """Get the Registered Kerberos Provider by id.  # noqa: E501

            Get the Registered Kerberos Provider by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_kerberos_provider_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id.

            Keyword Args:
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
                KerberosProvider
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_kerberos_provider_by_id = _Endpoint(
            settings={
                'response_type': (KerberosProvider,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/kerberos-providers/{id}',
                'operation_id': 'get_kerberos_provider_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^\d+:\d+:\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
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
            callable=__get_kerberos_provider_by_id
        )

        def __get_kerberos_providers(
            self,
            **kwargs
        ):
            """Get the list of Kerberos Providers.  # noqa: E501

            Get the list of Kerberos Authentication Providers.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_kerberos_providers(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                realm_names ([str]): Filter by a list of realm names.. [optional]
                ids ([int]): Filter by a list of Kerberos Provider Ids.. [optional]
                kdc_servers ([str]): Filter by a list of KDC servers.. [optional]
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
                KerberosProviders
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

        self.get_kerberos_providers = _Endpoint(
            settings={
                'response_type': (KerberosProviders,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/kerberos-providers',
                'operation_id': 'get_kerberos_providers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'realm_names',
                    'ids',
                    'kdc_servers',
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
                    'realm_names':
                        ([str],),
                    'ids':
                        ([int],),
                    'kdc_servers':
                        ([str],),
                },
                'attribute_map': {
                    'realm_names': 'realmNames',
                    'ids': 'ids',
                    'kdc_servers': 'kdcServers',
                },
                'location_map': {
                    'realm_names': 'query',
                    'ids': 'query',
                    'kdc_servers': 'query',
                },
                'collection_format_map': {
                    'realm_names': 'csv',
                    'ids': 'csv',
                    'kdc_servers': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_kerberos_providers
        )

        def __register_kerberos_provider(
            self,
            body,
            **kwargs
        ):
            """Register a Kerberos Authentication Provider.  # noqa: E501

            Register a Kerberos Authentication Provider.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.register_kerberos_provider(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (RegisterOrUpdateKerberosProviderRequest): Specifies the parameters to Register a Kerberos Provider.

            Keyword Args:
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
                KerberosProvider
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

        self.register_kerberos_provider = _Endpoint(
            settings={
                'response_type': (KerberosProvider,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/kerberos-providers/register',
                'operation_id': 'register_kerberos_provider',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
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
                        (RegisterOrUpdateKerberosProviderRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
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
            callable=__register_kerberos_provider
        )

        def __unregister_kerberos_provider(
            self,
            id,
            body,
            **kwargs
        ):
            """Unregister a Kerberos Provider.  # noqa: E501

            Unregister a Kerberos Provider.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.unregister_kerberos_provider(id, body, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Specifies the id.
                body (UnregisterKerberosRequest): Request to unregister a Kerberos Provider.

            Keyword Args:
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
                UnregisterKerberosProvider
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
            kwargs['id'] = \
                id
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.unregister_kerberos_provider = _Endpoint(
            settings={
                'response_type': (UnregisterKerberosProvider,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/kerberos-providers/unregister/{id}',
                'operation_id': 'unregister_kerberos_provider',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'body',
                ],
                'required': [
                    'id',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^\d+:\d+:\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'body':
                        (UnregisterKerberosRequest,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'body': 'body',
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
            callable=__unregister_kerberos_provider
        )

        def __update_kerberos_provider(
            self,
            id,
            body,
            **kwargs
        ):
            """Update the Kerberos Provider Registration.  # noqa: E501

            Update the Kerberos Provider Registration.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_kerberos_provider(id, body, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id.
                body (RegisterOrUpdateKerberosProviderRequest): Request to update a Kerberos Provider.

            Keyword Args:
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
                KerberosProvider
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
            kwargs['id'] = \
                id
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_kerberos_provider = _Endpoint(
            settings={
                'response_type': (KerberosProvider,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/kerberos-providers/{id}',
                'operation_id': 'update_kerberos_provider',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'body',
                ],
                'required': [
                    'id',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^\d+:\d+:\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'body':
                        (RegisterOrUpdateKerberosProviderRequest,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'body': 'body',
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
            callable=__update_kerberos_provider
        )
