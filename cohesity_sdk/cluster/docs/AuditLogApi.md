# cohesity_sdk.AuditLogApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](AuditLogApi.md#get_audit_logs) | **GET** /audit-logs | Get cluster audit logs.
[**get_audit_logs_actions**](AuditLogApi.md#get_audit_logs_actions) | **GET** /audit-logs/actions | Get cluster audit logs actions.
[**get_audit_logs_entity_types**](AuditLogApi.md#get_audit_logs_entity_types) | **GET** /audit-logs/entity-types | Get cluster audit logs entity types.
[**get_filer_audit_log_configs**](AuditLogApi.md#get_filer_audit_log_configs) | **GET** /audit-logs/filer-configs | Get filer audit log configs.
[**update_filer_audit_log_configs**](AuditLogApi.md#update_filer_audit_log_configs) | **PUT** /audit-logs/filer-configs | Update filer audit log configs.


# **get_audit_logs**
> AuditLogs get_audit_logs()

Get cluster audit logs.

Get a cluster audit logs.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.audit_logs import AuditLogs
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

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
	api_response = client.audit_log.get_audit_logs(search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, start_index=start_index, count=count)
	pprint(api_response)
except ApiException as e:
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

No authorization required

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

Get all actions of cluster audit logs.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.audit_logs_actions import AuditLogsActions
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


# example, this endpoint has no required or optional parameters
try:
	# Get cluster audit logs actions.
	api_response = client.audit_log.get_audit_logs_actions()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_audit_logs_actions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditLogsActions**](AuditLogsActions.md)

### Authorization

No authorization required

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

Get all entity types of cluster audit logs.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


# example, this endpoint has no required or optional parameters
try:
	# Get cluster audit logs entity types.
	api_response = client.audit_log.get_audit_logs_entity_types()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_audit_logs_entity_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditLogsEntityTypes**](AuditLogsEntityTypes.md)

### Authorization

No authorization required

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

Get filer audit log configs.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


# example, this endpoint has no required or optional parameters
try:
	# Get filer audit log configs.
	api_response = client.audit_log.get_filer_audit_log_configs()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_filer_audit_log_configs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

### Authorization

No authorization required

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

Update filer audit log configs.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

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
	api_response = client.audit_log.update_filer_audit_log_configs(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->update_filer_audit_log_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)| Specifies the filer audit log config to update. |

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

