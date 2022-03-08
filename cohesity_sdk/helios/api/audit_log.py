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
from cohesity_sdk.helios.model.audit_logs import AuditLogs
from cohesity_sdk.helios.model.audit_logs_actions import AuditLogsActions
from cohesity_sdk.helios.model.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.filer_audit_log_configs import FilerAuditLogConfigs


class AuditLogApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_audit_logs(
            self,
            **kwargs
        ):
            """Get cluster audit logs.  # noqa: E501

            Get a cluster audit logs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_audit_logs(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                access_cluster_id (int): This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios.. [optional]
                region_id (str): This field uniquely represents a region and is used for making Helios calls to a specific region.. [optional]
                search_string (str, none_type): Search audit logs by 'entityName' or 'details'.. [optional]
                usernames ([str], none_type): Specifies a list of usernames, only audit logs made by these users will be returned.. [optional]
                domains ([str], none_type): Specifies a list of domains, only audit logs made by user in these domains will be returned.. [optional]
                entity_types ([str], none_type): Specifies a list of entity types, only audit logs containing these entity types will be returned.. [optional]
                actions ([str], none_type): Specifies a list of actions, only audit logs containing these actions will be returned.. [optional]
                start_time_usecs (int, none_type): Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned.. [optional]
                end_time_usecs (int, none_type): Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned.. [optional]
                tenant_ids ([str], none_type): Specifies a list of tenant ids, only audit logs made by these tenants will be returned.. [optional]
                include_tenants (bool, none_type): If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned.. [optional]
                start_index (int, none_type): Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched.. [optional]
                count (int, none_type): Specifies the number of indexed obejcts to be fetched from the specified start index.. [optional]
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
                AuditLogs
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

        self.get_audit_logs = _Endpoint(
            settings={
                'response_type': (AuditLogs,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/audit-logs',
                'operation_id': 'get_audit_logs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'access_cluster_id',
                    'region_id',
                    'search_string',
                    'usernames',
                    'domains',
                    'entity_types',
                    'actions',
                    'start_time_usecs',
                    'end_time_usecs',
                    'tenant_ids',
                    'include_tenants',
                    'start_index',
                    'count',
                ],
                'required': [],
                'nullable': [
                    'search_string',
                    'usernames',
                    'domains',
                    'entity_types',
                    'actions',
                    'start_time_usecs',
                    'end_time_usecs',
                    'tenant_ids',
                    'include_tenants',
                    'start_index',
                    'count',
                ],
                'enum': [
                    'entity_types',
                    'actions',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('entity_types',): {
                        'None': None,
                        "CLUSTERPARTITION": "ClusterPartition",
                        "STORAGEDOMAIN": "StorageDomain",
                        "VIEW": "View",
                        "SHARE": "Share",
                        "NODE": "Node",
                        "DISK": "Disk",
                        "CLUSTER": "Cluster",
                        "VLAN": "Vlan",
                        "USER": "User",
                        "APIKEY": "ApiKey",
                        "CHASSIS": "Chassis",
                        "SSLCERTIFICATE": "SslCertificate",
                        "PROTECTIONGROUP": "ProtectionGroup",
                        "SOURCE": "Source",
                        "RECOVERYTASK": "RecoveryTask",
                        "SMTPSERVER": "SmtpServer",
                        "ENCRYPTIONKEY": "EncryptionKey",
                        "PROTECTIONPOLICY": "ProtectionPolicy",
                        "ALERT": "Alert",
                        "RESOLUTION": "Resolution",
                        "ALERTNOTIFICATIONRULE": "AlertNotificationRule",
                        "VAULT": "Vault",
                        "REMOTECLUSTER": "RemoteCluster",
                        "ACTIVEDIRECTORY": "ActiveDirectory",
                        "KERBEROSPROVIDER": "KerberosProvider",
                        "LDAP": "Ldap",
                        "ANTIVIRUSSERVICEGROUP": "AntivirusServiceGroup",
                        "INFECTEDFILE": "InfectedFile",
                        "PREFERREDDOMAINCONTROLLER": "PreferredDomainController",
                        "GROUP": "Group",
                        "ROLE": "Role",
                        "PROTECTIONRUN": "ProtectionRun",
                        "SEARCHJOB": "SearchJob",
                        "PHYSICALAGENT": "PhysicalAgent",
                        "CLONETASK": "CloneTask",
                        "CLONEREFRESHTASK": "CloneRefreshTask",
                        "NETWORK": "Network",
                        "INTERFACE": "Interface",
                        "NETWORKINERFACEGROUP": "NetworkInerfaceGroup",
                        "SCHEDULER": "Scheduler",
                        "PROXYSERVER": "ProxyServer",
                        "STATICROUTE": "StaticRoute",
                        "IP": "Ip",
                        "QOS": "Qos",
                        "KMSCONFIGURATION": "KmsConfiguration",
                        "CLOUDSPIN": "CloudSpin",
                        "TENANT": "Tenant",
                        "IDPCONFIGURATION": "IdpConfiguration",
                        "APP": "App",
                        "HELIOSEVENT": "HeliosEvent",
                        "OBJECT": "Object",
                        "CLUSTERSERVICES": "ClusterServices",
                        "ACCESSTOKEN": "AccessToken",
                        "SNMPCONFIG": "SnmpConfig",
                        "IOTIER": "IoTier",
                        "SERVICEFLAG": "ServiceFlag",
                        "SUPPORTSERVER": "SupportServer",
                        "CSR": "Csr",
                        "KEYSTONE": "Keystone",
                        "SWIFTROLES": "SwiftRoles",
                        "TAGS": "Tags",
                        "NIS": "Nis",
                        "SNAPSHOT": "Snapshot",
                        "HYBRIDEXTENDER": "HybridExtender",
                        "DATATIERINGANALYSISGROUP": "DataTieringAnalysisGroup",
                        "DATATIERINGDOWNTIERTASK": "DataTieringDowntierTask",
                        "DATATIERINGUPTIERTASK": "DataTieringUptierTask",
                        "TRUSTEDCA": "TrustedCA",
                        "AMQPTARGETCONFIGURATION": "AMQPTargetConfiguration",
                        "PATCH": "Patch",
                        "HOTFIX": "Hotfix"
                    },
                    ('actions',): {
                        'None': None,
                        "LOGIN": "Login",
                        "LOGOUT": "Logout",
                        "CREATE": "Create",
                        "MODIFY": "Modify",
                        "DELETE": "Delete",
                        "ACTIVATE": "Activate",
                        "DEACTIVATE": "Deactivate",
                        "PAUSE": "Pause",
                        "RESUME": "Resume",
                        "RUNNOW": "RunNow",
                        "CLONE": "Clone",
                        "RECOVER": "Recover",
                        "CANCEL": "Cancel",
                        "REGISTER": "Register",
                        "UNREGISTER": "Unregister",
                        "UPDATE": "Update",
                        "REFRESH": "Refresh",
                        "UPGRADE": "Upgrade",
                        "UPLOAD": "Upload",
                        "DOWNLOAD": "Download",
                        "RENAME": "Rename",
                        "ACCEPT": "Accept",
                        "MARK": "Mark",
                        "CLOSE": "Close",
                        "JOIN": "Join",
                        "DISJOIN": "DisJoin",
                        "OVERWRITE": "Overwrite",
                        "MARKREMOVAL": "MarkRemoval",
                        "CLOUDSPIN": "CloudSpin",
                        "ASSIGN": "Assign",
                        "UNASSIGN": "Unassign",
                        "NOTIFICATIONRULE": "NotificationRule",
                        "SCHEDULEREPORT": "ScheduleReport",
                        "INSTALL": "Install",
                        "UNINSTALL": "Uninstall",
                        "STOP": "Stop",
                        "START": "Start",
                        "RESTART": "Restart",
                        "RUNDIAGNOSTICS": "RunDiagnostics",
                        "APPLY": "Apply",
                        "REVERT": "Revert",
                        "IMPORT": "Import",
                        "VALIDATE": "Validate",
                        "CLUSTEREXPAND": "ClusterExpand"
                    },
                },
                'openapi_types': {
                    'access_cluster_id':
                        (int,),
                    'region_id':
                        (str,),
                    'search_string':
                        (str, none_type,),
                    'usernames':
                        ([str], none_type,),
                    'domains':
                        ([str], none_type,),
                    'entity_types':
                        ([str], none_type,),
                    'actions':
                        ([str], none_type,),
                    'start_time_usecs':
                        (int, none_type,),
                    'end_time_usecs':
                        (int, none_type,),
                    'tenant_ids':
                        ([str], none_type,),
                    'include_tenants':
                        (bool, none_type,),
                    'start_index':
                        (int, none_type,),
                    'count':
                        (int, none_type,),
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                    'search_string': 'searchString',
                    'usernames': 'usernames',
                    'domains': 'domains',
                    'entity_types': 'entityTypes',
                    'actions': 'actions',
                    'start_time_usecs': 'startTimeUsecs',
                    'end_time_usecs': 'endTimeUsecs',
                    'tenant_ids': 'tenantIds',
                    'include_tenants': 'includeTenants',
                    'start_index': 'startIndex',
                    'count': 'count',
                },
                'location_map': {
                    'access_cluster_id': 'header',
                    'region_id': 'header',
                    'search_string': 'query',
                    'usernames': 'query',
                    'domains': 'query',
                    'entity_types': 'query',
                    'actions': 'query',
                    'start_time_usecs': 'query',
                    'end_time_usecs': 'query',
                    'tenant_ids': 'query',
                    'include_tenants': 'query',
                    'start_index': 'query',
                    'count': 'query',
                },
                'collection_format_map': {
                    'usernames': 'csv',
                    'domains': 'csv',
                    'entity_types': 'csv',
                    'actions': 'csv',
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
            callable=__get_audit_logs
        )

        def __get_audit_logs_actions(
            self,
            **kwargs
        ):
            """Get cluster audit logs actions.  # noqa: E501

            Get all actions of cluster audit logs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_audit_logs_actions(async_req=True)
            >>> result = thread.get()


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
                AuditLogsActions
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

        self.get_audit_logs_actions = _Endpoint(
            settings={
                'response_type': (AuditLogsActions,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/audit-logs/actions',
                'operation_id': 'get_audit_logs_actions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'access_cluster_id',
                    'region_id',
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
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                },
                'location_map': {
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
            callable=__get_audit_logs_actions
        )

        def __get_audit_logs_entity_types(
            self,
            **kwargs
        ):
            """Get cluster audit logs entity types.  # noqa: E501

            Get all entity types of cluster audit logs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_audit_logs_entity_types(async_req=True)
            >>> result = thread.get()


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
                AuditLogsEntityTypes
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

        self.get_audit_logs_entity_types = _Endpoint(
            settings={
                'response_type': (AuditLogsEntityTypes,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/audit-logs/entity-types',
                'operation_id': 'get_audit_logs_entity_types',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'access_cluster_id',
                    'region_id',
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
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                },
                'location_map': {
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
            callable=__get_audit_logs_entity_types
        )

        def __get_filer_audit_log_configs(
            self,
            **kwargs
        ):
            """Get filer audit log configs.  # noqa: E501

            Get filer audit log configs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_filer_audit_log_configs(async_req=True)
            >>> result = thread.get()


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
                FilerAuditLogConfigs
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

        self.get_filer_audit_log_configs = _Endpoint(
            settings={
                'response_type': (FilerAuditLogConfigs,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/audit-logs/filer-configs',
                'operation_id': 'get_filer_audit_log_configs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'access_cluster_id',
                    'region_id',
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
                },
                'attribute_map': {
                    'access_cluster_id': 'accessClusterId',
                    'region_id': 'regionId',
                },
                'location_map': {
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
            callable=__get_filer_audit_log_configs
        )

        def __update_filer_audit_log_configs(
            self,
            body,
            **kwargs
        ):
            """Update filer audit log configs.  # noqa: E501

            Update filer audit log configs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_filer_audit_log_configs(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (FilerAuditLogConfigs): Specifies the filer audit log config to update.

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
                FilerAuditLogConfigs
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

        self.update_filer_audit_log_configs = _Endpoint(
            settings={
                'response_type': (FilerAuditLogConfigs,),
                'auth': [
                    'TokenHeader',
                    'ClusterId',
                    'APIKeyHeader'
                ],
                'endpoint_path': '/audit-logs/filer-configs',
                'operation_id': 'update_filer_audit_log_configs',
                'http_method': 'PUT',
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
                        (FilerAuditLogConfigs,),
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
            callable=__update_filer_audit_log_configs
        )
