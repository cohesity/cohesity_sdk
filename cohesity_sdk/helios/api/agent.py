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
from cohesity_sdk.helios.model.agent_upgrade_task_action_object import AgentUpgradeTaskActionObject
from cohesity_sdk.helios.model.agent_upgrade_task_action_request import AgentUpgradeTaskActionRequest
from cohesity_sdk.helios.model.agent_upgrade_task_state import AgentUpgradeTaskState
from cohesity_sdk.helios.model.agent_upgrade_task_states import AgentUpgradeTaskStates
from cohesity_sdk.helios.model.create_upgrade_task_request import CreateUpgradeTaskRequest
from cohesity_sdk.helios.model.download_agent_request_params import DownloadAgentRequestParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_agent_images_response import McmAgentImagesResponse


class AgentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_upgrade_task(
            self,
            body,
            **kwargs
        ):
            """Create an upgrade task  # noqa: E501

            Create a schedule based agent upgrade task.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_upgrade_task(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (CreateUpgradeTaskRequest): Specifies parameters to create a schedule based agent upgrade task.

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
                AgentUpgradeTaskState
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

        self.create_upgrade_task = _Endpoint(
            settings={
                'response_type': (AgentUpgradeTaskState,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/data-protect/agents/upgrade-tasks',
                'operation_id': 'create_upgrade_task',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                    'access_cluster_id',
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
                        (CreateUpgradeTaskRequest,),
                    'access_cluster_id':
                        (int,),
                    'region_id':
                        (str,),
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                },
                'location_map': {
                    'body': 'body',
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
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_upgrade_task
        )

        def __download_agent(
            self,
            body,
            **kwargs
        ):
            """Download agent  # noqa: E501

            Download agent for different hosts.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.download_agent(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (DownloadAgentRequestParams): Specifies agent details.

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
                file_type
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

        self.download_agent = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/data-protect/agents/download',
                'operation_id': 'download_agent',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                    'access_cluster_id',
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
                        (DownloadAgentRequestParams,),
                    'access_cluster_id':
                        (int,),
                    'region_id':
                        (str,),
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                },
                'location_map': {
                    'body': 'body',
                    'access_cluster_id': 'header',
                    'region_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__download_agent
        )

        def __get_upgrade_tasks(
            self,
            **kwargs
        ):
            """Get upgrade tasks  # noqa: E501

            Get the list of agent upgrade tasks.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_upgrade_tasks(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                ids ([int]): Specifies IDs of tasks to be fetched.. [optional]
                tenant_ids ([str]): TenantIds contains ids of the tenants for which objects are to be returned.. [optional]
                include_tenants (bool): If true, the response will include upgrade tasks which were created by all tenants which the current user has permission to see. If false, then only upgrade tasks created by the current user will be returned.. [optional]
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
                AgentUpgradeTaskStates
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

        self.get_upgrade_tasks = _Endpoint(
            settings={
                'response_type': (AgentUpgradeTaskStates,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/data-protect/agents/upgrade-tasks',
                'operation_id': 'get_upgrade_tasks',
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
            callable=__get_upgrade_tasks
        )

        def __mcm_get_agent_image_details(
            self,
            **kwargs
        ):
            """Get agent images details.  # noqa: E501

            Get agent information on Helios.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.mcm_get_agent_image_details(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                platform (str): Specifies a platform for which agent information need to be fetched.. [optional]
                package_type (str): Specifies a package type for which agent information need to be fetched.. [optional]
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
                McmAgentImagesResponse
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

        self.mcm_get_agent_image_details = _Endpoint(
            settings={
                'response_type': (McmAgentImagesResponse,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/mcm/data-protect/agents/images',
                'operation_id': 'mcm_get_agent_image_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'region_id',
                    'platform',
                    'package_type',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'platform',
                    'package_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('platform',): {

                        "WINDOWS": "Windows",
                        "LINUX": "Linux",
                        "SOLARIS": "Solaris"
                    },
                    ('package_type',): {

                        "SCRIPT": "Script",
                        "RPM": "RPM",
                        "SUSERPM": "SuseRPM",
                        "DEB": "DEB"
                    },
                },
                'openapi_types': {
                    'region_id':
                        (str,),
                    'platform':
                        (str,),
                    'package_type':
                        (str,),
                },
                'attribute_map': {
                    'region_id': 'regionId',
                    'platform': 'platform',
                    'package_type': 'packageType',
                },
                'location_map': {
                    'region_id': 'header',
                    'platform': 'query',
                    'package_type': 'query',
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
            callable=__mcm_get_agent_image_details
        )

        def __perform_action_on_agent_upgrade_task(
            self,
            body,
            **kwargs
        ):
            """Perform action on an upgrade task.  # noqa: E501

            Perform actions on an agent upgrade task.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.perform_action_on_agent_upgrade_task(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (AgentUpgradeTaskActionRequest): Specifies the parameters to perform an action on an agent upgrade task.

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
                AgentUpgradeTaskActionObject
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

        self.perform_action_on_agent_upgrade_task = _Endpoint(
            settings={
                'response_type': (AgentUpgradeTaskActionObject,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/data-protect/agents/upgrade-tasks/actions',
                'operation_id': 'perform_action_on_agent_upgrade_task',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                    'access_cluster_id',
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
                        (AgentUpgradeTaskActionRequest,),
                    'access_cluster_id':
                        (int,),
                    'region_id':
                        (str,),
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                },
                'location_map': {
                    'body': 'body',
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
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__perform_action_on_agent_upgrade_task
        )