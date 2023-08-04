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
from cohesity_sdk.cluster.model.static_route_params import StaticRouteParams
from cohesity_sdk.cluster.model.static_routes import StaticRoutes


class RoutesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_static_route(
            self,
            body,
            **kwargs
        ):
            """Configure a static route  # noqa: E501

            Configure a static route on an interface.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_static_route(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (StaticRouteParams): Specifies the parameters to configure a static route on an interface.

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
                StaticRouteParams
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

        self.add_static_route = _Endpoint(
            settings={
                'response_type': (StaticRouteParams,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/network/routes',
                'operation_id': 'add_static_route',
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
                        (StaticRouteParams,),
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
            callable=__add_static_route
        )

        def __delete_static_route(
            self,
            route_id,
            **kwargs
        ):
            """Delete a static route  # noqa: E501

            Delete a static route on a network interface.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_static_route(route_id, async_req=True)
            >>> result = thread.get()

            Args:
                route_id (str): Specify the unique identifier for the route.

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
            kwargs['route_id'] = \
                route_id
            return self.call_with_http_info(**kwargs)

        self.delete_static_route = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/network/routes/{routeId}',
                'operation_id': 'delete_static_route',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'route_id',
                ],
                'required': [
                    'route_id',
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
                    'route_id':
                        (str,),
                },
                'attribute_map': {
                    'route_id': 'routeId',
                },
                'location_map': {
                    'route_id': 'path',
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
            callable=__delete_static_route
        )

        def __list_static_routes(
            self,
            **kwargs
        ):
            """List all static routes  # noqa: E501

            List the static routes for the Cohesity Cluster.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_static_routes(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                interface_groups ([str]): Specifies the network interfaces name to filter.. [optional]
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
                StaticRoutes
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

        self.list_static_routes = _Endpoint(
            settings={
                'response_type': (StaticRoutes,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/network/routes',
                'operation_id': 'list_static_routes',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'interface_groups',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'interface_groups',
                ]
            },
            root_map={
                'validations': {
                    ('interface_groups',): {

                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'interface_groups':
                        ([str],),
                },
                'attribute_map': {
                    'interface_groups': 'interfaceGroups',
                },
                'location_map': {
                    'interface_groups': 'query',
                },
                'collection_format_map': {
                    'interface_groups': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_static_routes
        )

        def __update_static_route(
            self,
            route_id,
            body,
            **kwargs
        ):
            """Update a static route  # noqa: E501

            Update static route details.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_static_route(route_id, body, async_req=True)
            >>> result = thread.get()

            Args:
                route_id (str): Specify the unique identifier for the route.
                body (StaticRouteParams): Specifies the update request parameters.

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
                StaticRouteParams
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
            kwargs['route_id'] = \
                route_id
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.update_static_route = _Endpoint(
            settings={
                'response_type': (StaticRouteParams,),
                'auth': [
                    'TokenHeader',
        
                    'APIKeyHeader'
                ],
                'endpoint_path': '/network/routes/{routeId}',
                'operation_id': 'update_static_route',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'route_id',
                    'body',
                ],
                'required': [
                    'route_id',
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
                    'route_id':
                        (str,),
                    'body':
                        (StaticRouteParams,),
                },
                'attribute_map': {
                    'route_id': 'routeId',
                },
                'location_map': {
                    'route_id': 'path',
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
            callable=__update_static_route
        )