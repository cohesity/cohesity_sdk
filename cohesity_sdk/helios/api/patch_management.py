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
    validate_and_convert_types,
)
from cohesity_sdk.helios.model.applied_patches import AppliedPatches
from cohesity_sdk.helios.model.apply_patches_request import ApplyPatchesRequest
from cohesity_sdk.helios.model.available_patches import AvailablePatches
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.patch_operation_status import PatchOperationStatus
from cohesity_sdk.helios.model.patches_details import PatchesDetails
from cohesity_sdk.helios.model.patches_history import PatchesHistory
from cohesity_sdk.helios.model.revert_patches_request import RevertPatchesRequest
from cohesity_sdk.helios.model.service_patch_levels import ServicePatchLevels


class PatchManagementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __apply_patches(self, body, **kwargs):
            """Apply patches  # noqa: E501

            Apply a service patch and its dependencies.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.apply_patches(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (ApplyPatchesRequest): Request to apply patches.

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
                ServicePatchLevels
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["body"] = body
            return self.call_with_http_info(**kwargs)

        self.apply_patches = _Endpoint(
            settings={
                "response_type": (ServicePatchLevels,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/patch-management/available-patches",
                "operation_id": "apply_patches",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                    "access_cluster_id",
                    "region_id",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (ApplyPatchesRequest,),
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                },
                "location_map": {
                    "body": "body",
                    "access_cluster_id": "header",
                    "region_id": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__apply_patches,
        )

        def __get_applied_patches(self, **kwargs):
            """Get applied patches  # noqa: E501

            Returns a list of currently applied patches that are running on the cluster.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_applied_patches(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                service (str): Specifies optional service name whose current patch is returned. If it is not specified, all the applied patches are returned.. [optional]
                include_details (bool): Specifies whether to return the details of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch.. [optional]
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
                AppliedPatches
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.get_applied_patches = _Endpoint(
            settings={
                "response_type": (AppliedPatches,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/patch-management/applied-patches",
                "operation_id": "get_applied_patches",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "access_cluster_id",
                    "region_id",
                    "service",
                    "include_details",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                    "service": (str,),
                    "include_details": (bool,),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "service": "service",
                    "include_details": "includeDetails",
                },
                "location_map": {
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "service": "query",
                    "include_details": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_applied_patches,
        )

        def __get_available_patches(self, **kwargs):
            """Get available patches  # noqa: E501

            Returns a list of patches that are available and ready to apply on the cluster.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_available_patches(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                service (str): Specifies optional service name whose available patch is returned. If it is not specified, available patches for all the serivces are returned.. [optional]
                include_details (bool): Specifies whether to return the description of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch.. [optional]
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
                AvailablePatches
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.get_available_patches = _Endpoint(
            settings={
                "response_type": (AvailablePatches,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/patch-management/available-patches",
                "operation_id": "get_available_patches",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "access_cluster_id",
                    "region_id",
                    "service",
                    "include_details",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                    "service": (str,),
                    "include_details": (bool,),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "service": "service",
                    "include_details": "includeDetails",
                },
                "location_map": {
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "service": "query",
                    "include_details": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_available_patches,
        )

        def __get_patch_operation_status(self, **kwargs):
            """Get patch operation status  # noqa: E501

            Returns the status of the current or the last patch operation. There can be only one active patch operation at any given time.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_patch_operation_status(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                include_details (bool): Specifies whether to return details of all service patch opertions on all nodes. By default, returns whether there is a patch operation in progress or not.. [optional]
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
                PatchOperationStatus
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.get_patch_operation_status = _Endpoint(
            settings={
                "response_type": (PatchOperationStatus,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/patch-management/operation-status",
                "operation_id": "get_patch_operation_status",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "access_cluster_id",
                    "region_id",
                    "include_details",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                    "include_details": (bool,),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "include_details": "includeDetails",
                },
                "location_map": {
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "include_details": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_patch_operation_status,
        )

        def __get_patches_history(self, **kwargs):
            """Get patches history  # noqa: E501

            Get the history of all the patch management operations.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_patches_history(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                service (str): Specifies optional service name whose patch operation history is returned. If it is not specified, patch operations of all the serivces are returned.. [optional]
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
                PatchesHistory
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.get_patches_history = _Endpoint(
            settings={
                "response_type": (PatchesHistory,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/patch-management/patches-history",
                "operation_id": "get_patches_history",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "access_cluster_id",
                    "region_id",
                    "service",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                    "service": (str,),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "service": "service",
                },
                "location_map": {
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "service": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_patches_history,
        )

        def __import_patches(self, file_name, checksum, patch, **kwargs):
            """Import patches  # noqa: E501

            Import a patch or a hotfix to the cluster.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.import_patches(file_name, checksum, patch, async_req=True)
            >>> result = thread.get()

            Args:
                file_name (str):
                checksum (str):
                patch (file_type):

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
                PatchesDetails
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["file_name"] = file_name
            kwargs["checksum"] = checksum
            kwargs["patch"] = patch
            return self.call_with_http_info(**kwargs)

        self.import_patches = _Endpoint(
            settings={
                "response_type": (PatchesDetails,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/patch-management/available-patches",
                "operation_id": "import_patches",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "file_name",
                    "checksum",
                    "patch",
                    "access_cluster_id",
                    "region_id",
                ],
                "required": [
                    "file_name",
                    "checksum",
                    "patch",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "file_name": (str,),
                    "checksum": (str,),
                    "patch": (file_type,),
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                },
                "attribute_map": {
                    "file_name": "fileName",
                    "checksum": "checksum",
                    "patch": "patch",
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                },
                "location_map": {
                    "file_name": "form",
                    "checksum": "form",
                    "patch": "form",
                    "access_cluster_id": "header",
                    "region_id": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["multipart/form-data"],
            },
            api_client=api_client,
            callable=__import_patches,
        )

        def __revert_patches(self, body, **kwargs):
            """Revert patches  # noqa: E501

            Revert an applied service patch and its dependencies.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.revert_patches(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (RevertPatchesRequest): Request to revert patches.

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
                ServicePatchLevels
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["body"] = body
            return self.call_with_http_info(**kwargs)

        self.revert_patches = _Endpoint(
            settings={
                "response_type": (ServicePatchLevels,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/patch-management/applied-patches",
                "operation_id": "revert_patches",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                    "access_cluster_id",
                    "region_id",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (RevertPatchesRequest,),
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                },
                "location_map": {
                    "body": "body",
                    "access_cluster_id": "header",
                    "region_id": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__revert_patches,
        )
