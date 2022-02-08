"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cohesity_client_v2.api_client import ApiClient, Endpoint as _Endpoint
from cohesity_sdk.cohesity_client_v2.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cohesity_sdk.cohesity_client_v2.model.create_storage_domain_param import CreateStorageDomainParam
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.storage_domain import StorageDomain
from cohesity_sdk.cohesity_client_v2.model.storage_domains import StorageDomains
from cohesity_sdk.cohesity_client_v2.model.update_storage_domain_param import UpdateStorageDomainParam


class StorageDomainsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_storage_domain(
            self,
            body,
            **kwargs
        ):
            """Create a Storage Domain.  # noqa: E501

            Create a Storage Domain.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_storage_domain(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (CreateStorageDomainParam): Specified the request to create a Storage Domain.

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
                StorageDomain
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

        self.create_storage_domain = _Endpoint(
            settings={
                'response_type': (StorageDomain,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/storage-domains',
                'operation_id': 'create_storage_domain',
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
                        (CreateStorageDomainParam,),
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
            callable=__create_storage_domain
        )

        def __delete_storage_domain(
            self,
            id,
            **kwargs
        ):
            """Delete a Storage Domain.  # noqa: E501

            Delete a Storage Domain.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_storage_domain(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specified the Storage Domain id to delete.

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
                None
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

        self.delete_storage_domain = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/storage-domains/{id}',
                'operation_id': 'delete_storage_domain',
                'http_method': 'DELETE',
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
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
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
            callable=__delete_storage_domain
        )

        def __get_storage_domain_by_id(
            self,
            id,
            **kwargs
        ):
            """Get a Storage Domain by id.  # noqa: E501

            Get a Storage Domain by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_storage_domain_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specified the Storage Domain id to fetch.

            Keyword Args:
                include_stats (bool): Whether to include Storage Domain stats in response.. [optional]
                include_time_series_schema (bool): Whether to include Storage Domain time series schema in response.. [optional]
                include_file_count_by_size (bool): Whether to include Storage Domain file count by size.. [optional]
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
                StorageDomain
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

        self.get_storage_domain_by_id = _Endpoint(
            settings={
                'response_type': (StorageDomain,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/storage-domains/{id}',
                'operation_id': 'get_storage_domain_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'include_stats',
                    'include_time_series_schema',
                    'include_file_count_by_size',
                ],
                'required': [
                    'id',
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
                    'id':
                        (int,),
                    'include_stats':
                        (bool,),
                    'include_time_series_schema':
                        (bool,),
                    'include_file_count_by_size':
                        (bool,),
                },
                'attribute_map': {
                    'id': 'id',
                    'include_stats': 'includeStats',
                    'include_time_series_schema': 'includeTimeSeriesSchema',
                    'include_file_count_by_size': 'includeFileCountBySize',
                },
                'location_map': {
                    'id': 'path',
                    'include_stats': 'query',
                    'include_time_series_schema': 'query',
                    'include_file_count_by_size': 'query',
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
            callable=__get_storage_domain_by_id
        )

        def __get_storage_domains(
            self,
            **kwargs
        ):
            """Get Storage Domains.  # noqa: E501

            Get Storage Domains.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_storage_domains(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                ids ([int]): Filter by a list of Storage Domain ids.. [optional]
                names ([str]): Filter by a list of Storage Domain names.. [optional]
                cluster_partition_ids ([int]): Filter by a list of cluster partition ids.. [optional]
                tenant_ids ([str]): TenantIds contains ids of the tenants for which Storage Domains are to be returned.. [optional]
                include_tenants (bool): IncludeTenants specifies if Storage Domains of all the tenants under the hierarchy of the logged in user's organization should be returned.. [optional]
                include_stats (bool): Whether to include Storage Domain stats in response.. [optional]
                include_time_series_schema (bool): Whether to include Storage Domain time series schema in response.. [optional]
                include_file_count_by_size (bool): Whether to include Storage Domain file count by size.. [optional]
                match_partial_names (bool): If true, the names in viewNames are matched by any partial rather than exactly matched.. [optional]
                view_template_id (int): Specifies a view template id for Storage Domain. Storage Domains with same deduplication and compression settings will be recommended.. [optional]
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
                StorageDomains
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

        self.get_storage_domains = _Endpoint(
            settings={
                'response_type': (StorageDomains,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/storage-domains',
                'operation_id': 'get_storage_domains',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ids',
                    'names',
                    'cluster_partition_ids',
                    'tenant_ids',
                    'include_tenants',
                    'include_stats',
                    'include_time_series_schema',
                    'include_file_count_by_size',
                    'match_partial_names',
                    'view_template_id',
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
                    'ids':
                        ([int],),
                    'names':
                        ([str],),
                    'cluster_partition_ids':
                        ([int],),
                    'tenant_ids':
                        ([str],),
                    'include_tenants':
                        (bool,),
                    'include_stats':
                        (bool,),
                    'include_time_series_schema':
                        (bool,),
                    'include_file_count_by_size':
                        (bool,),
                    'match_partial_names':
                        (bool,),
                    'view_template_id':
                        (int,),
                },
                'attribute_map': {
                    'ids': 'ids',
                    'names': 'names',
                    'cluster_partition_ids': 'clusterPartitionIds',
                    'tenant_ids': 'tenantIds',
                    'include_tenants': 'includeTenants',
                    'include_stats': 'includeStats',
                    'include_time_series_schema': 'includeTimeSeriesSchema',
                    'include_file_count_by_size': 'includeFileCountBySize',
                    'match_partial_names': 'matchPartialNames',
                    'view_template_id': 'viewTemplateId',
                },
                'location_map': {
                    'ids': 'query',
                    'names': 'query',
                    'cluster_partition_ids': 'query',
                    'tenant_ids': 'query',
                    'include_tenants': 'query',
                    'include_stats': 'query',
                    'include_time_series_schema': 'query',
                    'include_file_count_by_size': 'query',
                    'match_partial_names': 'query',
                    'view_template_id': 'query',
                },
                'collection_format_map': {
                    'ids': 'csv',
                    'names': 'csv',
                    'cluster_partition_ids': 'csv',
                    'tenant_ids': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_storage_domains
        )

        def __update_storage_domain(
            self,
            id,
            body,
            **kwargs
        ):
            """Update a Storage Domain.  # noqa: E501

            Update a Storage Domain.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_storage_domain(id, body, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specified the Storage Domain id to update.
                body (UpdateStorageDomainParam): Specified the request to update a Storage Domain.

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
                StorageDomain
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

        self.update_storage_domain = _Endpoint(
            settings={
                'response_type': (StorageDomain,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/storage-domains/{id}',
                'operation_id': 'update_storage_domain',
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
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'body':
                        (UpdateStorageDomainParam,),
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
            callable=__update_storage_domain
        )
