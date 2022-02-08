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
from cohesity_sdk.cohesity_client_v2.model.create_odp_remote_cluster_params import CreateOdpRemoteClusterParams
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.odp_remote_cluster import OdpRemoteCluster
from cohesity_sdk.cohesity_client_v2.model.odp_remote_clusters import OdpRemoteClusters
from cohesity_sdk.cohesity_client_v2.model.update_odp_remote_cluster_params import UpdateOdpRemoteClusterParams


class RemoteClustersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_odp_remote_cluster(
            self,
            body,
            **kwargs
        ):
            """Create an ODP Remote Cluster config.  # noqa: E501

            Create an ODP Remote Cluster config.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_odp_remote_cluster(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (CreateOdpRemoteClusterParams): Specifies the request to create ODP Remote Cluster config.

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
                OdpRemoteCluster
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

        self.create_odp_remote_cluster = _Endpoint(
            settings={
                'response_type': (OdpRemoteCluster,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/odp-remote-clusters',
                'operation_id': 'create_odp_remote_cluster',
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
                        (CreateOdpRemoteClusterParams,),
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
            callable=__create_odp_remote_cluster
        )

        def __get_odp_remote_cluster_by_id(
            self,
            cluster_id,
            **kwargs
        ):
            """Get ODP Remote Cluster config by id.  # noqa: E501

            Get ODP Remote Cluster config by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_odp_remote_cluster_by_id(cluster_id, async_req=True)
            >>> result = thread.get()

            Args:
                cluster_id (int): Specifies the id of ODP Remote Cluster to fetch.

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
                OdpRemoteCluster
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
            kwargs['cluster_id'] = \
                cluster_id
            return self.call_with_http_info(**kwargs)

        self.get_odp_remote_cluster_by_id = _Endpoint(
            settings={
                'response_type': (OdpRemoteCluster,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/odp-remote-clusters/{clusterId}',
                'operation_id': 'get_odp_remote_cluster_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'cluster_id',
                ],
                'required': [
                    'cluster_id',
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
                    'cluster_id':
                        (int,),
                },
                'attribute_map': {
                    'cluster_id': 'clusterId',
                },
                'location_map': {
                    'cluster_id': 'path',
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
            callable=__get_odp_remote_cluster_by_id
        )

        def __get_odp_remote_clusters(
            self,
            **kwargs
        ):
            """Get ODP Remote Cluster configs.  # noqa: E501

            Get ODP Remote Cluster configs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_odp_remote_clusters(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                cluster_ids ([int]): Specifies a list of ODP Remote Cluster ids to filter.. [optional]
                cluster_names ([str]): Specifies a list of ODP Remote Cluster names to filter.. [optional]
                tenant_ids ([str]): TenantIds contains ids of the tenants for which ODP remote clusters are to be returned.. [optional]
                include_tenants (bool): If true, the response will include ODP remote clusters which were created by all tenants which the current user has permission to see. If false, then only ODP remote clusters created by the current user will be returned.. [optional]
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
                OdpRemoteClusters
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

        self.get_odp_remote_clusters = _Endpoint(
            settings={
                'response_type': (OdpRemoteClusters,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/odp-remote-clusters',
                'operation_id': 'get_odp_remote_clusters',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'cluster_ids',
                    'cluster_names',
                    'tenant_ids',
                    'include_tenants',
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
                    'cluster_ids':
                        ([int],),
                    'cluster_names':
                        ([str],),
                    'tenant_ids':
                        ([str],),
                    'include_tenants':
                        (bool,),
                },
                'attribute_map': {
                    'cluster_ids': 'clusterIds',
                    'cluster_names': 'clusterNames',
                    'tenant_ids': 'tenantIds',
                    'include_tenants': 'includeTenants',
                },
                'location_map': {
                    'cluster_ids': 'query',
                    'cluster_names': 'query',
                    'tenant_ids': 'query',
                    'include_tenants': 'query',
                },
                'collection_format_map': {
                    'cluster_ids': 'csv',
                    'cluster_names': 'csv',
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
            callable=__get_odp_remote_clusters
        )

        def __update_odp_remote_cluster(
            self,
            cluster_id,
            body,
            **kwargs
        ):
            """Update an ODP Remote Cluster config.  # noqa: E501

            Update an ODP Remote Cluster config.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_odp_remote_cluster(cluster_id, body, async_req=True)
            >>> result = thread.get()

            Args:
                cluster_id (int): Specifies the id of ODP Remote Cluster to update.
                body (UpdateOdpRemoteClusterParams): Specifies the request to update ODP Remote Cluster config.

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
                OdpRemoteCluster
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
            kwargs['cluster_id'] = \
                cluster_id
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_odp_remote_cluster = _Endpoint(
            settings={
                'response_type': (OdpRemoteCluster,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/odp-remote-clusters/{clusterId}',
                'operation_id': 'update_odp_remote_cluster',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'cluster_id',
                    'body',
                ],
                'required': [
                    'cluster_id',
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
                    'cluster_id':
                        (int,),
                    'body':
                        (UpdateOdpRemoteClusterParams,),
                },
                'attribute_map': {
                    'cluster_id': 'clusterId',
                },
                'location_map': {
                    'cluster_id': 'path',
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
            callable=__update_odp_remote_cluster
        )
