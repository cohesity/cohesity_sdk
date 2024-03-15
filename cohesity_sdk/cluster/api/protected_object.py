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
from cohesity_sdk.cluster.model.create_protected_objects_request import CreateProtectedObjectsRequest
from cohesity_sdk.cluster.model.create_protected_objects_response import CreateProtectedObjectsResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_protected_object_response import GetProtectedObjectResponse
from cohesity_sdk.cluster.model.protectd_objects_action_request import ProtectdObjectsActionRequest
from cohesity_sdk.cluster.model.protected_object_action_response import ProtectedObjectActionResponse
from cohesity_sdk.cluster.model.update_protected_objects_request import UpdateProtectedObjectsRequest


class ProtectedObjectApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __perform_action_on_protect_objects(
            self,
            body,
            **kwargs
        ):
            """Perform Actions on Protect Objects.  # noqa: E501

            Perform actions on Protected Objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.perform_action_on_protect_objects(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (ProtectdObjectsActionRequest): Specifies the parameters to perform an action on an already protected object.

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
                ProtectedObjectActionResponse
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

        self.perform_action_on_protect_objects = _Endpoint(
            settings={
                'response_type': (ProtectedObjectActionResponse,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/data-protect/protected-objects/actions',
                'operation_id': 'perform_action_on_protect_objects',
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
                        (ProtectdObjectsActionRequest,),
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
            callable=__perform_action_on_protect_objects
        )

        def __protect_objects_of_any_type(
            self,
            body,
            **kwargs
        ):
            """Create Object Backup.  # noqa: E501

            Create Protect Objects Backup.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.protect_objects_of_any_type(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (CreateProtectedObjectsRequest): Specifies the parameters to protect objects.

            Keyword Args:
                request_initiator_type (str): Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests.. [optional]
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
                CreateProtectedObjectsResponse
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

        self.protect_objects_of_any_type = _Endpoint(
            settings={
                'response_type': (CreateProtectedObjectsResponse,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/data-protect/protected-objects',
                'operation_id': 'protect_objects_of_any_type',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                    'request_initiator_type',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                    'request_initiator_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('request_initiator_type',): {

                        "UIUSER": "UIUser",
                        "UIAUTO": "UIAuto",
                        "HELIOS": "Helios"
                    },
                },
                'openapi_types': {
                    'body':
                        (CreateProtectedObjectsRequest,),
                    'request_initiator_type':
                        (str,),
                },
                'attribute_map': {
                    'request_initiator_type': 'requestInitiatorType',
                },
                'location_map': {
                    'body': 'body',
                    'request_initiator_type': 'header',
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
            callable=__protect_objects_of_any_type
        )

        def __update_protected_objects_of_any_type(
            self,
            id,
            body,
            **kwargs
        ):
            """Update Object Backup.  # noqa: E501

            Update Protected object backup configuration given a object id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_protected_objects_of_any_type(id, body, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specifies the id of the Protected Object.
                body (UpdateProtectedObjectsRequest): Specifies the parameters to perform an update on protected objects.

            Keyword Args:
                request_initiator_type (str): Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests.. [optional]
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
                GetProtectedObjectResponse
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

        self.update_protected_objects_of_any_type = _Endpoint(
            settings={
                'response_type': (GetProtectedObjectResponse,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/data-protect/protected-objects/{id}',
                'operation_id': 'update_protected_objects_of_any_type',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'body',
                    'request_initiator_type',
                ],
                'required': [
                    'id',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                    'request_initiator_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('request_initiator_type',): {

                        "UIUSER": "UIUser",
                        "UIAUTO": "UIAuto",
                        "HELIOS": "Helios"
                    },
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'body':
                        (UpdateProtectedObjectsRequest,),
                    'request_initiator_type':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'request_initiator_type': 'requestInitiatorType',
                },
                'location_map': {
                    'id': 'path',
                    'body': 'body',
                    'request_initiator_type': 'header',
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
            callable=__update_protected_objects_of_any_type
        )
