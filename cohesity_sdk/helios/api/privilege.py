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
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.privileges import Privileges


class PrivilegeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __check_privileges(self, **kwargs):
            """Check if user has a list of privileges  # noqa: E501

            Checks if the current logged in user has the particular privilages or not  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.check_privileges(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                privilege_names ([str]): Filter by a list of Privilege names.. [optional]
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

        self.check_privileges = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/mcm/has-privileges",
                "operation_id": "check_privileges",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "region_id",
                    "privilege_names",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [
                    "privilege_names",
                ],
            },
            root_map={
                "validations": {
                    ("privilege_names",): {
                        "min_items": 1,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "region_id": (str,),
                    "privilege_names": ([str],),
                },
                "attribute_map": {
                    "region_id": "regionId",
                    "privilege_names": "privilegeNames",
                },
                "location_map": {
                    "region_id": "header",
                    "privilege_names": "query",
                },
                "collection_format_map": {
                    "privilege_names": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__check_privileges,
        )

        def __get_privileges(self, **kwargs):
            """Get Privileges.  # noqa: E501

            Get Privileges.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_privileges(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                names ([str]): Filter by a list of Privilege names.. [optional]
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
                Privileges
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

        self.get_privileges = _Endpoint(
            settings={
                "response_type": (Privileges,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/privileges",
                "operation_id": "get_privileges",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "access_cluster_id",
                    "region_id",
                    "names",
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
                    "names": ([str],),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "names": "names",
                },
                "location_map": {
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "names": "query",
                },
                "collection_format_map": {
                    "names": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_privileges,
        )
