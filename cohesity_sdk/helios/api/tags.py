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
from cohesity_sdk.helios.model.get_tags_result import GetTagsResult
from cohesity_sdk.helios.model.tag import Tag


class TagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_tag(
            self,
            body,
            **kwargs
        ):
            """Create a Tag  # noqa: E501

            Creates a Tag.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_tag(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (Tag): Request to create a Tag.

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
                Tag
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

        self.create_tag = _Endpoint(
            settings={
                'response_type': (Tag,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/tags',
                'operation_id': 'create_tag',
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
                        (Tag,),
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
            callable=__create_tag
        )

        def __delete_tag(
            self,
            id,
            **kwargs
        ):
            """Delete a Tag  # noqa: E501

            Deletes a Tag by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_tag(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Specifies the Id of the tag.

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

        self.delete_tag = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/tags/{id}',
                'operation_id': 'delete_tag',
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
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^\d+:\d+:[A-Z0-9-]+$',  # noqa: E501
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
            callable=__delete_tag
        )

        def __get_tag_by_id(
            self,
            id,
            **kwargs
        ):
            """Get Tag by id.  # noqa: E501

            Get Tag by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_tag_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Specifies the Id of the tag.

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
                Tag
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

        self.get_tag_by_id = _Endpoint(
            settings={
                'response_type': (Tag,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/tags/{id}',
                'operation_id': 'get_tag_by_id',
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
                            'pattern': r'^\d+:\d+:[A-Z0-9-]+$',  # noqa: E501
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
            callable=__get_tag_by_id
        )

        def __get_tags(
            self,
            **kwargs
        ):
            """Get tags based on filters.  # noqa: E501

            If no parameters are specified, all tags are returned.   Specifying parameters filters the results that are returned.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_tags(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                ids ([str]): Filter by a list of Tag Ids. If Ids are mentioned all other fields   will be ignored.. [optional]
                names ([str]): Filter by a list of Tag names.. [optional]
                namespaces ([str]): Filter by a list of Namespaces.. [optional]
                tenant_ids ([str]): TenantIds contains ids of the tenants for which tags are to be   returned.. [optional]
                include_tenants (bool): IncludeTenants specifies if tags of all the tenants under the   hierarchy of the logged in user's organization should be returned.   False, by default.. [optional]
                include_marked_for_deletion (bool): Specifies if tags marked for deletion should be shown. These are   tags which are undergoing deletion. False, by default.. [optional]
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
                GetTagsResult
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

        self.get_tags = _Endpoint(
            settings={
                'response_type': (GetTagsResult,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/tags',
                'operation_id': 'get_tags',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ids',
                    'names',
                    'namespaces',
                    'tenant_ids',
                    'include_tenants',
                    'include_marked_for_deletion',
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
                        ([str],),
                    'names':
                        ([str],),
                    'namespaces':
                        ([str],),
                    'tenant_ids':
                        ([str],),
                    'include_tenants':
                        (bool,),
                    'include_marked_for_deletion':
                        (bool,),
                },
                'attribute_map': {
                    'ids': 'ids',
                    'names': 'names',
                    'namespaces': 'namespaces',
                    'tenant_ids': 'tenantIds',
                    'include_tenants': 'includeTenants',
                    'include_marked_for_deletion': 'includeMarkedForDeletion',
                },
                'location_map': {
                    'ids': 'query',
                    'names': 'query',
                    'namespaces': 'query',
                    'tenant_ids': 'query',
                    'include_tenants': 'query',
                    'include_marked_for_deletion': 'query',
                },
                'collection_format_map': {
                    'ids': 'csv',
                    'names': 'csv',
                    'namespaces': 'csv',
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
            callable=__get_tags
        )

        def __update_tag(
            self,
            id,
            body,
            **kwargs
        ):
            """Update a Tag  # noqa: E501

            Updates a Tag by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_tag(id, body, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Specifies the Id of the tag.
                body (Tag): Request to update a tag.

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
                Tag
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

        self.update_tag = _Endpoint(
            settings={
                'response_type': (Tag,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/tags/{id}',
                'operation_id': 'update_tag',
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
                            'pattern': r'^\d+:\d+:[A-Z0-9-]+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'body':
                        (Tag,),
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
            callable=__update_tag
        )
