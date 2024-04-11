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
from cohesity_sdk.cluster.model.antivirus_service_group import AntivirusServiceGroup
from cohesity_sdk.cluster.model.antivirus_service_groups import AntivirusServiceGroups
from cohesity_sdk.cluster.model.create_antivirus_service_group_params import CreateAntivirusServiceGroupParams
from cohesity_sdk.cluster.model.delete_infected_files import DeleteInfectedFiles
from cohesity_sdk.cluster.model.delete_infected_files_parameters import DeleteInfectedFilesParameters
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.icap_uri_connection_status_list import IcapUriConnectionStatusList
from cohesity_sdk.cluster.model.infected_files import InfectedFiles
from cohesity_sdk.cluster.model.update_infected_files_list import UpdateInfectedFilesList
from cohesity_sdk.cluster.model.update_infected_files_parameters import UpdateInfectedFilesParameters


class AntivirusServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_antivirus_group(
            self,
            body,
            **kwargs
        ):
            """Create an Antivirus Service group.  # noqa: E501

            Create Antivirus Service group.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_antivirus_group(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (CreateAntivirusServiceGroupParams): Specifies the parameters to create antivirus service group.

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
                AntivirusServiceGroup
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

        self.create_antivirus_group = _Endpoint(
            settings={
                'response_type': (AntivirusServiceGroup,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/groups',
                'operation_id': 'create_antivirus_group',
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
                        (CreateAntivirusServiceGroupParams,),
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
            callable=__create_antivirus_group
        )

        def __delete_antivirus_group(
            self,
            id,
            **kwargs
        ):
            """Delete an Antivirus Service group  # noqa: E501

            Deletes an Antivirus service group based on given id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_antivirus_group(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specifies a unique id of the Antivirus Group to delete.

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

        self.delete_antivirus_group = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/groups/{id}',
                'operation_id': 'delete_antivirus_group',
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
            callable=__delete_antivirus_group
        )

        def __delete_infected_files(
            self,
            body,
            **kwargs
        ):
            """Delete infected files.  # noqa: E501

            Delete infected files.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_infected_files(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (DeleteInfectedFilesParameters): Specifies the parameters of infected files to be deleted.

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
                DeleteInfectedFiles
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

        self.delete_infected_files = _Endpoint(
            settings={
                'response_type': (DeleteInfectedFiles,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/infected-files',
                'operation_id': 'delete_infected_files',
                'http_method': 'DELETE',
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
                        (DeleteInfectedFilesParameters,),
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
            callable=__delete_infected_files
        )

        def __get_antivirus_service_groups(
            self,
            **kwargs
        ):
            """Get Antivirus Service groups.  # noqa: E501

            Get Antivirus Service groups.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_antivirus_service_groups(async_req=True)
            >>> result = thread.get()


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
                AntivirusServiceGroups
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

        self.get_antivirus_service_groups = _Endpoint(
            settings={
                'response_type': (AntivirusServiceGroups,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/groups',
                'operation_id': 'get_antivirus_service_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
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
            callable=__get_antivirus_service_groups
        )

        def __get_icap_uri_connection_status(
            self,
            **kwargs
        ):
            """Get ICAP Uri connection status.  # noqa: E501

            Get ICAP Uri connection status.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_icap_uri_connection_status(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                uris ([str]): Specifies a list of URIs to check connection status.. [optional]
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
                IcapUriConnectionStatusList
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

        self.get_icap_uri_connection_status = _Endpoint(
            settings={
                'response_type': (IcapUriConnectionStatusList,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/icap-uri-connection-status',
                'operation_id': 'get_icap_uri_connection_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uris',
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
                    'uris':
                        ([str],),
                },
                'attribute_map': {
                    'uris': 'uris',
                },
                'location_map': {
                    'uris': 'query',
                },
                'collection_format_map': {
                    'uris': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_icap_uri_connection_status
        )

        def __get_infected_files(
            self,
            **kwargs
        ):
            """Get infected files.  # noqa: E501

            Get infected files.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_infected_files(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                view_ids ([int]): Specifies a list of view ids. Only infected files from these views will be returned.. [optional]
                path (str): Specifies the file path.. [optional]
                states ([str]): Specifies the file states.. [optional]
                max_count (int): Specifies the max number of files to be returned.. [optional]
                cookie (str): Specifies the pagination cookie.. [optional]
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
                InfectedFiles
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

        self.get_infected_files = _Endpoint(
            settings={
                'response_type': (InfectedFiles,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/infected-files',
                'operation_id': 'get_infected_files',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_ids',
                    'path',
                    'states',
                    'max_count',
                    'cookie',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'states',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('states',): {

                        "QUARANTINED": "Quarantined",
                        "UNQUARANTINED": "Unquarantined"
                    },
                },
                'openapi_types': {
                    'view_ids':
                        ([int],),
                    'path':
                        (str,),
                    'states':
                        ([str],),
                    'max_count':
                        (int,),
                    'cookie':
                        (str,),
                },
                'attribute_map': {
                    'view_ids': 'viewIds',
                    'path': 'path',
                    'states': 'states',
                    'max_count': 'maxCount',
                    'cookie': 'cookie',
                },
                'location_map': {
                    'view_ids': 'query',
                    'path': 'query',
                    'states': 'query',
                    'max_count': 'query',
                    'cookie': 'query',
                },
                'collection_format_map': {
                    'view_ids': 'csv',
                    'states': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_infected_files
        )

        def __update_antivirus_group(
            self,
            id,
            body,
            **kwargs
        ):
            """Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.  # noqa: E501

            Update an Antivirus Service group.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_antivirus_group(id, body, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specifies a unique id of the Antivirus Group to update.
                body (AntivirusServiceGroup): Specifies the parameters to update antivirus service group.

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
                AntivirusServiceGroup
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

        self.update_antivirus_group = _Endpoint(
            settings={
                'response_type': (AntivirusServiceGroup,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/groups/{id}',
                'operation_id': 'update_antivirus_group',
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
                        (AntivirusServiceGroup,),
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
            callable=__update_antivirus_group
        )

        def __update_infected_files(
            self,
            body,
            **kwargs
        ):
            """Update infected files state.  # noqa: E501

            Update infected files state.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_infected_files(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (UpdateInfectedFilesParameters): Specifies the parameters of infected files to be updated.

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
                UpdateInfectedFilesList
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

        self.update_infected_files = _Endpoint(
            settings={
                'response_type': (UpdateInfectedFilesList,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/antivirus-service/infected-files',
                'operation_id': 'update_infected_files',
                'http_method': 'PUT',
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
                        (UpdateInfectedFilesParameters,),
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
            callable=__update_infected_files
        )
