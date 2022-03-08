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
from cohesity_sdk.helios.model.ldap_status import LdapStatus
from cohesity_sdk.helios.model.ldaps import Ldaps


class LDAPApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_ldap_connection_status(
            self,
            id,
            **kwargs
        ):
            """Get LDAP connection status.  # noqa: E501

            Get LDAP connection status.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_ldap_connection_status(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specifies the LDAP id.

            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
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
                LdapStatus
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

        self.get_ldap_connection_status = _Endpoint(
            settings={
                'response_type': (LdapStatus,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/ldap/{id}/connection-status',
                'operation_id': 'get_ldap_connection_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'access_cluster_id',
                    'region_id',
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
                    'access_cluster_id':
                        (int,),
                    'region_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                },
                'location_map': {
                    'id': 'path',
                    'access_cluster_id': 'header',
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
            callable=__get_ldap_connection_status
        )

        def __get_ldaps(
            self,
            **kwargs
        ):
            """Get Groups.  # noqa: E501

            Get LDAPs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_ldaps(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                ids ([int]): Specifies a list of ids to filter.. [optional]
                tenant_ids ([str]): TenantIds contains ids of the tenants for which LDAPs are to be returned.. [optional]
                include_tenants (bool): IncludeTenants specifies if LDAPs of all the tenants under the hierarchy of the logged in user's organization should be returned.. [optional]
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
                Ldaps
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

        self.get_ldaps = _Endpoint(
            settings={
                'response_type': (Ldaps,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/ldap',
                'operation_id': 'get_ldaps',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'access_cluster_id',
                    'region_id',
                    'ids',
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
                    'access_cluster_id':
                        (int,),
                    'region_id':
                        (str,),
                    'ids':
                        ([int],),
                    'tenant_ids':
                        ([str],),
                    'include_tenants':
                        (bool,),
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                    'ids': 'ids',
                    'tenant_ids': 'tenantIds',
                    'include_tenants': 'includeTenants',
                },
                'location_map': {
                    'access_cluster_id': 'header',
                    'region_id': 'header',
                    'ids': 'query',
                    'tenant_ids': 'query',
                    'include_tenants': 'query',
                },
                'collection_format_map': {
                    'ids': 'csv',
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
            callable=__get_ldaps
        )
