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
from cohesity_sdk.helios.model.active_directories import ActiveDirectories
from cohesity_sdk.helios.model.active_directory import ActiveDirectory
from cohesity_sdk.helios.model.create_active_directory_request import (
    CreateActiveDirectoryRequest,
)
from cohesity_sdk.helios.model.domain_controllers_response import (
    DomainControllersResponse,
)
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_active_directory_request import (
    UpdateActiveDirectoryRequest,
)


class ActiveDirectoryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_active_directory(self, body, **kwargs):
            """Create an Active Directory.  # noqa: E501

            Create an Active Directory.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_active_directory(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (CreateActiveDirectoryRequest): Specifies the parameters to create an Active Directory.

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
                ActiveDirectory
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

        self.create_active_directory = _Endpoint(
            settings={
                "response_type": (ActiveDirectory,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/active-directories",
                "operation_id": "create_active_directory",
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
                    "body": (CreateActiveDirectoryRequest,),
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
            callable=__create_active_directory,
        )

        def __delete_active_directory(
            self,
            id,
            active_directory_admin_username,
            active_directory_admin_password,
            **kwargs
        ):
            """Delete an Active Directory.  # noqa: E501

            Delete an Active Directory.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_active_directory(id, active_directory_admin_username, active_directory_admin_password, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specifies id of an Active Directory.
                active_directory_admin_username (str): Specifies the username of the Active Directory Admin.
                active_directory_admin_password (str): Specifies the password of the Active Directory Admin.

            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                force_remove (bool): To force delete the Active directory from cluster. This will skip all the checks that prevents cluster from leaving an AD domain.. [optional]
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
            kwargs["id"] = id
            kwargs["active_directory_admin_username"] = active_directory_admin_username
            kwargs["active_directory_admin_password"] = active_directory_admin_password
            return self.call_with_http_info(**kwargs)

        self.delete_active_directory = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/active-directories/{id}",
                "operation_id": "delete_active_directory",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                    "active_directory_admin_username",
                    "active_directory_admin_password",
                    "access_cluster_id",
                    "region_id",
                    "force_remove",
                ],
                "required": [
                    "id",
                    "active_directory_admin_username",
                    "active_directory_admin_password",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (int,),
                    "active_directory_admin_username": (str,),
                    "active_directory_admin_password": (str,),
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                    "force_remove": (bool,),
                },
                "attribute_map": {
                    "id": "id",
                    "active_directory_admin_username": "activeDirectoryAdminUsername",
                    "active_directory_admin_password": "activeDirectoryAdminPassword",
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "force_remove": "forceRemove",
                },
                "location_map": {
                    "id": "path",
                    "active_directory_admin_username": "header",
                    "active_directory_admin_password": "header",
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "force_remove": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__delete_active_directory,
        )

        def __get_active_directory(self, **kwargs):
            """Get the list of Active Directories.  # noqa: E501

            Get the list of Active Directories.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_active_directory(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                domain_names ([str]): Filter by a list of Active Directory domain names.. [optional]
                ids ([int]): Filter by a list of Active Directory Ids.. [optional]
                tenant_ids ([str]): TenantIds contains ids of the tenants for which Active Directories are to be returned.. [optional]
                include_tenants (bool): If true, the response will include Active Directories which were created by all tenants which the current user has permission to see. If false, then only Active Directories created by the current user will be returned.. [optional]
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
                ActiveDirectories
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

        self.get_active_directory = _Endpoint(
            settings={
                "response_type": (ActiveDirectories,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/active-directories",
                "operation_id": "get_active_directory",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "access_cluster_id",
                    "region_id",
                    "domain_names",
                    "ids",
                    "tenant_ids",
                    "include_tenants",
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
                    "domain_names": ([str],),
                    "ids": ([int],),
                    "tenant_ids": ([str],),
                    "include_tenants": (bool,),
                },
                "attribute_map": {
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "domain_names": "domainNames",
                    "ids": "ids",
                    "tenant_ids": "tenantIds",
                    "include_tenants": "includeTenants",
                },
                "location_map": {
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "domain_names": "query",
                    "ids": "query",
                    "tenant_ids": "query",
                    "include_tenants": "query",
                },
                "collection_format_map": {
                    "domain_names": "csv",
                    "ids": "csv",
                    "tenant_ids": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_active_directory,
        )

        def __get_active_directory_by_id(self, id, **kwargs):
            """Get an Active Directory by id.  # noqa: E501

            Get an Active Directory by id.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_active_directory_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specifies id of an Active Directory.

            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                include_centrify_zones (bool): Specifies whether to include Centrify Zones of the Active Directory in response.. [optional]
                include_domain_controllers (bool): Specifies whether to include Domain Controllers of the Active Directory in response.. [optional]
                include_security_principals (bool): Specifies whether to include Security Principals of the Active Directory in response.. [optional]
                prefix (str): Specifies a prefix, only security principals with name or sAMAccountName having this prefix (ignoring cases) will be returned. This field is appliciable and mandatory if 'includeSecurityPrincipals' is set to true.. [optional]
                object_class ([str]): Specifies a list of object classes, only security principals with object class in this list will be returned. This field is appliciable if 'includeSecurityPrincipals' is set to true.. [optional]
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
                ActiveDirectory
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
            kwargs["id"] = id
            return self.call_with_http_info(**kwargs)

        self.get_active_directory_by_id = _Endpoint(
            settings={
                "response_type": (ActiveDirectory,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/active-directories/{id}",
                "operation_id": "get_active_directory_by_id",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                    "access_cluster_id",
                    "region_id",
                    "include_centrify_zones",
                    "include_domain_controllers",
                    "include_security_principals",
                    "prefix",
                    "object_class",
                ],
                "required": [
                    "id",
                ],
                "nullable": [],
                "enum": [
                    "object_class",
                ],
                "validation": [
                    "object_class",
                ],
            },
            root_map={
                "validations": {
                    ("object_class",): {},
                },
                "allowed_values": {
                    ("object_class",): {
                        "USER": "User",
                        "GROUP": "Group",
                        "COMPUTER": "Computer",
                        "WELLKNOWNPRINCIPAL": "WellKnownPrincipal",
                    },
                },
                "openapi_types": {
                    "id": (int,),
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                    "include_centrify_zones": (bool,),
                    "include_domain_controllers": (bool,),
                    "include_security_principals": (bool,),
                    "prefix": (str,),
                    "object_class": ([str],),
                },
                "attribute_map": {
                    "id": "id",
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "include_centrify_zones": "includeCentrifyZones",
                    "include_domain_controllers": "includeDomainControllers",
                    "include_security_principals": "includeSecurityPrincipals",
                    "prefix": "prefix",
                    "object_class": "objectClass",
                },
                "location_map": {
                    "id": "path",
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "include_centrify_zones": "query",
                    "include_domain_controllers": "query",
                    "include_security_principals": "query",
                    "prefix": "query",
                    "object_class": "query",
                },
                "collection_format_map": {
                    "object_class": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_active_directory_by_id,
        )

        def __get_domain_controllers(self, domain_names, **kwargs):
            """Get Domain Controllers of specified domains.  # noqa: E501

            Get Domain Controllers of specified domains.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_domain_controllers(domain_names, async_req=True)
            >>> result = thread.get()

            Args:
                domain_names ([str]): Specifies a list of domain names.

            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                connection_id (int, none_type): Specifies the Id of the connection which the connector belongs to.. [optional]
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
                DomainControllersResponse
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
            kwargs["domain_names"] = domain_names
            return self.call_with_http_info(**kwargs)

        self.get_domain_controllers = _Endpoint(
            settings={
                "response_type": (DomainControllersResponse,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/domain-controllers",
                "operation_id": "get_domain_controllers",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "domain_names",
                    "access_cluster_id",
                    "region_id",
                    "connection_id",
                ],
                "required": [
                    "domain_names",
                ],
                "nullable": [
                    "connection_id",
                ],
                "enum": [],
                "validation": [
                    "domain_names",
                ],
            },
            root_map={
                "validations": {
                    ("domain_names",): {
                        "min_items": 1,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "domain_names": ([str],),
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                    "connection_id": (
                        int,
                        none_type,
                    ),
                },
                "attribute_map": {
                    "domain_names": "domainNames",
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                    "connection_id": "connectionId",
                },
                "location_map": {
                    "domain_names": "query",
                    "access_cluster_id": "header",
                    "region_id": "header",
                    "connection_id": "query",
                },
                "collection_format_map": {
                    "domain_names": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_domain_controllers,
        )

        def __update_active_directory(self, id, body, **kwargs):
            """Update an Active Directory.  # noqa: E501

            Update an Active Directory.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_active_directory(id, body, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Specifies id of an Active Directory.
                body (UpdateActiveDirectoryRequest): Request to update an Active Directory.

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
                ActiveDirectory
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
            kwargs["id"] = id
            kwargs["body"] = body
            return self.call_with_http_info(**kwargs)

        self.update_active_directory = _Endpoint(
            settings={
                "response_type": (ActiveDirectory,),
                "auth": ["TokenHeader", "ClusterId", "APIKeyHeader"],
                "endpoint_path": "/active-directories/{id}",
                "operation_id": "update_active_directory",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                    "body",
                    "access_cluster_id",
                    "region_id",
                ],
                "required": [
                    "id",
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
                    "id": (int,),
                    "body": (UpdateActiveDirectoryRequest,),
                    "access_cluster_id": (int,),
                    "region_id": (str,),
                },
                "attribute_map": {
                    "id": "id",
                    "access_cluster_id": "accessClusterId",
                    "region_id": "regionId",
                },
                "location_map": {
                    "id": "path",
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
            callable=__update_active_directory,
        )
