# cohesity_sdk.cluster.AuditLogApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_logs**](AuditLogApi.md#create_audit_logs) | **POST** /create-audit-logs | Create cluster audit logs.
[**get_audit_logs**](AuditLogApi.md#get_audit_logs) | **GET** /audit-logs | Get cluster audit logs.
[**get_audit_logs_actions**](AuditLogApi.md#get_audit_logs_actions) | **GET** /audit-logs/actions | Get cluster audit logs actions.
[**get_audit_logs_entity_types**](AuditLogApi.md#get_audit_logs_entity_types) | **GET** /audit-logs/entity-types | Get cluster audit logs entity types.
[**get_filer_audit_log_configs**](AuditLogApi.md#get_filer_audit_log_configs) | **GET** /audit-logs/filer-configs | Get filer audit log configs.
[**update_filer_audit_log_configs**](AuditLogApi.md#update_filer_audit_log_configs) | **PUT** /audit-logs/filer-configs | Update filer audit log configs.


# **create_audit_logs**
> AuditLogsEntityTypes create_audit_logs(body)

Create cluster audit logs.

```No Privileges Required``` <br><br>Create a cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import audit_log
from cohesity_sdk.cluster.cohesity.model.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.cluster.cohesity.model.audit_log import AuditLog
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log.AuditLogApi(api_client)
    body = AuditLog(
        action="action_example",
        details="details_example",
        domain="domain_example",
        entity_name="entity_name_example",
        entity_type="entity_type_example",
        ip="ip_example",
        is_impersonation=True,
        new_record="new_record_example",
        original_tenant_id="original_tenant_id_example",
        original_tenant_name="original_tenant_name_example",
        previous_record="previous_record_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        timestamp_usecs=1,
        username="username_example",
    ) # AuditLog | Request to create a audit log.

    # example passing only required values which don't have defaults set
    try:
        # Create cluster audit logs.
        api_response = api_instance.create_audit_logs(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AuditLogApi->create_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditLog**](AuditLog.md)| Request to create a audit log. |

### Return type

[**AuditLogsEntityTypes**](AuditLogsEntityTypes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs**
> AuditLogs get_audit_logs()

Get cluster audit logs.

**Privileges:** ```CLUSTER_AUDIT``` <br><br>Get a cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import audit_log
from cohesity_sdk.cluster.cohesity.model.audit_logs import AuditLogs
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log.AuditLogApi(api_client)
    search_string = "searchString_example" # str, none_type | Search audit logs by 'entityName' or 'details'. (optional)
    usernames = [
        "usernames_example",
    ] # [str], none_type | Specifies a list of usernames, only audit logs made by these users will be returned. (optional)
    domains = [
        "domains_example",
    ] # [str], none_type | Specifies a list of domains, only audit logs made by user in these domains will be returned. (optional)
    entity_types = [
        "ClusterPartition",
    ] # [str], none_type | Specifies a list of entity types, only audit logs containing these entity types will be returned. (optional)
    actions = [
        "Login",
    ] # [str], none_type | Specifies a list of actions, only audit logs containing these actions will be returned. (optional)
    start_time_usecs = 1 # int, none_type | Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. (optional)
    end_time_usecs = 1 # int, none_type | Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str], none_type | Specifies a list of tenant ids, only audit logs made by these tenants will be returned. (optional)
    include_tenants = True # bool, none_type | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)
    start_index = 1 # int, none_type | Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. (optional)
    count = 1 # int, none_type | Specifies the number of indexed obejcts to be fetched from the specified start index. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get cluster audit logs.
        api_response = api_instance.get_audit_logs(search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, start_index=start_index, count=count)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AuditLogApi->get_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str, none_type**| Search audit logs by &#39;entityName&#39; or &#39;details&#39;. | [optional]
 **usernames** | **[str], none_type**| Specifies a list of usernames, only audit logs made by these users will be returned. | [optional]
 **domains** | **[str], none_type**| Specifies a list of domains, only audit logs made by user in these domains will be returned. | [optional]
 **entity_types** | **[str], none_type**| Specifies a list of entity types, only audit logs containing these entity types will be returned. | [optional]
 **actions** | **[str], none_type**| Specifies a list of actions, only audit logs containing these actions will be returned. | [optional]
 **start_time_usecs** | **int, none_type**| Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. | [optional]
 **end_time_usecs** | **int, none_type**| Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. | [optional]
 **tenant_ids** | **[str], none_type**| Specifies a list of tenant ids, only audit logs made by these tenants will be returned. | [optional]
 **include_tenants** | **bool, none_type**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional]
 **start_index** | **int, none_type**| Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. | [optional]
 **count** | **int, none_type**| Specifies the number of indexed obejcts to be fetched from the specified start index. | [optional]

### Return type

[**AuditLogs**](AuditLogs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_actions**
> AuditLogsActions get_audit_logs_actions()

Get cluster audit logs actions.

**Privileges:** ```CLUSTER_AUDIT``` <br><br>Get all actions of cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import audit_log
from cohesity_sdk.cluster.cohesity.model.audit_logs_actions import AuditLogsActions
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log.AuditLogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster audit logs actions.
        api_response = api_instance.get_audit_logs_actions()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AuditLogApi->get_audit_logs_actions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditLogsActions**](AuditLogsActions.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_entity_types**
> AuditLogsEntityTypes get_audit_logs_entity_types()

Get cluster audit logs entity types.

**Privileges:** ```CLUSTER_AUDIT``` <br><br>Get all entity types of cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import audit_log
from cohesity_sdk.cluster.cohesity.model.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log.AuditLogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster audit logs entity types.
        api_response = api_instance.get_audit_logs_entity_types()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AuditLogApi->get_audit_logs_entity_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditLogsEntityTypes**](AuditLogsEntityTypes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filer_audit_log_configs**
> FilerAuditLogConfigs get_filer_audit_log_configs()

Get filer audit log configs.

**Privileges:** ```CLUSTER_AUDIT``` <br><br>Get filer audit log configs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import audit_log
from cohesity_sdk.cluster.cohesity.model.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log.AuditLogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get filer audit log configs.
        api_response = api_instance.get_filer_audit_log_configs()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AuditLogApi->get_filer_audit_log_configs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filer_audit_log_configs**
> FilerAuditLogConfigs update_filer_audit_log_configs(body)

Update filer audit log configs.

**Privileges:** ```CLUSTER_AUDIT``` <br><br>Update filer audit log configs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import audit_log
from cohesity_sdk.cluster.cohesity.model.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_log.AuditLogApi(api_client)
    body = FilerAuditLogConfigs(
        override_global_subnet_whitelist=True,
        share_permissions=[
            SmbPermission(
                access="ReadOnly",
                mode="FolderSubFoldersAndFiles",
                sid="sid_example",
                special_access_mask=1,
                special_type=1,
                type="Allow",
            ),
        ],
        subnet_whitelist=[
            Subnet(
                component="component_example",
                description="description_example",
                gateway="gateway_example",
                id=1,
                ip="ip_example",
                netmask_bits=1,
                netmask_ip4="netmask_ip4_example",
                nfs_access="kDisabled",
                nfs_squash="kNone",
                s3_access="kDisabled",
                smb_access="kDisabled",
            ),
        ],
    ) # FilerAuditLogConfigs | Specifies the filer audit log config to update.

    # example passing only required values which don't have defaults set
    try:
        # Update filer audit log configs.
        api_response = api_instance.update_filer_audit_log_configs(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AuditLogApi->update_filer_audit_log_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)| Specifies the filer audit log config to update. |

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

