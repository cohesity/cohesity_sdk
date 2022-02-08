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
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.node_group_request import NodeGroupRequest
from cohesity_sdk.cohesity_client_v2.model.node_group_response import NodeGroupResponse


class NodeGroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_node_group(
            self,
            body,
            **kwargs
        ):
            """Create a Node Group.  # noqa: E501

            Create the Node Group and returns the newly created node group object.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_node_group(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (NodeGroupRequest): Request to create a Node Group.

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
                NodeGroupResponse
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

        self.create_node_group = _Endpoint(
            settings={
                'response_type': (NodeGroupResponse,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/nodeGroups',
                'operation_id': 'create_node_group',
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
                        (NodeGroupRequest,),
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
            callable=__create_node_group
        )

        def __delete_node_group(
            self,
            group_name,
            **kwargs
        ):
            """Delete a Node Group.  # noqa: E501

            Deletes a Node Group based on given node group name.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_node_group(group_name, async_req=True)
            >>> result = thread.get()

            Args:
                group_name (str): Specifies a unique name of the Node Group to delete.

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
            kwargs['group_name'] = \
                group_name
            return self.call_with_http_info(**kwargs)

        self.delete_node_group = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/nodeGroups/{groupName}',
                'operation_id': 'delete_node_group',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_name',
                ],
                'required': [
                    'group_name',
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
                    'group_name':
                        (str,),
                },
                'attribute_map': {
                    'group_name': 'groupName',
                },
                'location_map': {
                    'group_name': 'path',
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
            callable=__delete_node_group
        )

        def __get_node_group_by_name(
            self,
            group_name,
            **kwargs
        ):
            """List Node Groups for a given Group Name.  # noqa: E501

            Returns Node Group for given Group Name.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_node_group_by_name(group_name, async_req=True)
            >>> result = thread.get()

            Args:
                group_name (str): Specifies a unique id of Node Group to return.

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
                NodeGroupResponse
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
            kwargs['group_name'] = \
                group_name
            return self.call_with_http_info(**kwargs)

        self.get_node_group_by_name = _Endpoint(
            settings={
                'response_type': (NodeGroupResponse,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/nodeGroups/{groupName}',
                'operation_id': 'get_node_group_by_name',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_name',
                ],
                'required': [
                    'group_name',
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
                    'group_name':
                        (str,),
                },
                'attribute_map': {
                    'group_name': 'groupName',
                },
                'location_map': {
                    'group_name': 'path',
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
            callable=__get_node_group_by_name
        )

        def __get_node_groups(
            self,
            **kwargs
        ):
            """List Node Groups based on provided filtering parameters.  # noqa: E501

            List node groups.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_node_groups(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                group_names ([str]): Filter node groups by a list of node group names.. [optional]
                group_type (int): Filter node groups by a node group type.. [optional]
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
                NodeGroupResponse
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

        self.get_node_groups = _Endpoint(
            settings={
                'response_type': (NodeGroupResponse,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/nodeGroups',
                'operation_id': 'get_node_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_names',
                    'group_type',
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
                    'group_names':
                        ([str],),
                    'group_type':
                        (int,),
                },
                'attribute_map': {
                    'group_names': 'groupNames',
                    'group_type': 'groupType',
                },
                'location_map': {
                    'group_names': 'query',
                    'group_type': 'query',
                },
                'collection_format_map': {
                    'group_names': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_node_groups
        )

        def __update_node_group(
            self,
            group_name,
            body,
            **kwargs
        ):
            """Update a Node Group.  # noqa: E501

            Specifies the request to update the existing Node Group. On successful update, returns the updated node group object.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_node_group(group_name, body, async_req=True)
            >>> result = thread.get()

            Args:
                group_name (str): Specifies a unique name of the Node Group to update.
                body (NodeGroupRequest): Request to update a Node Group.

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
                NodeGroupResponse
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
            kwargs['group_name'] = \
                group_name
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_node_group = _Endpoint(
            settings={
                'response_type': (NodeGroupResponse,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/nodeGroups/{groupName}',
                'operation_id': 'update_node_group',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_name',
                    'body',
                ],
                'required': [
                    'group_name',
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
                    'group_name':
                        (str,),
                    'body':
                        (NodeGroupRequest,),
                },
                'attribute_map': {
                    'group_name': 'groupName',
                },
                'location_map': {
                    'group_name': 'path',
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
            callable=__update_node_group
        )
