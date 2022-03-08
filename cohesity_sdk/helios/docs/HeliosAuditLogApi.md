# cohesity_sdk.HeliosAuditLogApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_audit_log_settings**](HeliosAuditLogApi.md#get_helios_audit_log_settings) | **GET** /mcm/audit-logs/settings | Get Helios Audit Log Settings.
[**get_helios_audit_logs**](HeliosAuditLogApi.md#get_helios_audit_logs) | **GET** /mcm/audit-logs | Get helios audit logs.
[**get_helios_audit_logs_actions**](HeliosAuditLogApi.md#get_helios_audit_logs_actions) | **GET** /mcm/audit-logs/actions | Get helios audit logs actions.
[**get_helios_audit_logs_entity_types**](HeliosAuditLogApi.md#get_helios_audit_logs_entity_types) | **GET** /mcm/audit-logs/entity-types | Get helios audit logs entity types.
[**update_helios_audit_log_settings**](HeliosAuditLogApi.md#update_helios_audit_log_settings) | **PUT** /mcm/audit-logs/settings | Update Helios Audit Log Settings.


# **get_helios_audit_log_settings**
> HeliosAuditLogSettings get_helios_audit_log_settings()

Get Helios Audit Log Settings.

Returns a list of Helios audit log settings.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_audit_log_settings import HeliosAuditLogSettings
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Helios Audit Log Settings.
	api_response = client.helios_audit_log.get_helios_audit_log_settings(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAuditLogApi->get_helios_audit_log_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosAuditLogSettings**](HeliosAuditLogSettings.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helios_audit_logs**
> HeliosAuditLogs get_helios_audit_logs()

Get helios audit logs.

Get helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_audit_logs import HeliosAuditLogs
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
cluster_identifiers = [
        "4:072888001528021798096225500850762068629",
    ] # [str], none_type | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. (optional)
start_index = 1 # int, none_type | Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. (optional)
count = 1 # int, none_type | Specifies the number of indexed objects to be fetched from the index. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios audit logs.
	api_response = client.helios_audit_log.get_helios_audit_logs(region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, cluster_identifiers=cluster_identifiers, start_index=start_index, count=count)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAuditLogApi->get_helios_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **search_string** | **str, none_type**| Search audit logs by &#39;entityName&#39; or &#39;details&#39;. | [optional]
 **usernames** | **[str], none_type**| Specifies a list of usernames, only audit logs made by these users will be returned. | [optional]
 **domains** | **[str], none_type**| Specifies a list of domains, only audit logs made by user in these domains will be returned. | [optional]
 **entity_types** | **[str], none_type**| Specifies a list of entity types, only audit logs containing these entity types will be returned. | [optional]
 **actions** | **[str], none_type**| Specifies a list of actions, only audit logs containing these actions will be returned. | [optional]
 **start_time_usecs** | **int, none_type**| Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. | [optional]
 **end_time_usecs** | **int, none_type**| Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. | [optional]
 **tenant_ids** | **[str], none_type**| Specifies a list of tenant ids, only audit logs made by these tenants will be returned. | [optional]
 **include_tenants** | **bool, none_type**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional]
 **cluster_identifiers** | **[str], none_type**| Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional]
 **start_index** | **int, none_type**| Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. | [optional]
 **count** | **int, none_type**| Specifies the number of indexed objects to be fetched from the index. | [optional]

### Return type

[**HeliosAuditLogs**](HeliosAuditLogs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helios_audit_logs_actions**
> HeliosAuditLogsActions get_helios_audit_logs_actions()

Get helios audit logs actions.

Get all actions of helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_audit_logs_actions import HeliosAuditLogsActions
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios audit logs actions.
	api_response = client.helios_audit_log.get_helios_audit_logs_actions(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAuditLogApi->get_helios_audit_logs_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosAuditLogsActions**](HeliosAuditLogsActions.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helios_audit_logs_entity_types**
> AuditLogsEntityTypes get_helios_audit_logs_entity_types()

Get helios audit logs entity types.

Get all entity types of helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios audit logs entity types.
	api_response = client.helios_audit_log.get_helios_audit_logs_entity_types(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAuditLogApi->get_helios_audit_logs_entity_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**AuditLogsEntityTypes**](AuditLogsEntityTypes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_helios_audit_log_settings**
> HeliosAuditLogSettings update_helios_audit_log_settings(body)

Update Helios Audit Log Settings.

Updates Helios audit log settings.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_audit_log_settings import HeliosAuditLogSettings
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = HeliosAuditLogSettings(
        user_settings=[
            HeliosAuditLogUserSetting(
                user_sid="user_sid_example",
                read_logging=False,
            ),
        ],
        read_logging=False,
    ) # HeliosAuditLogSettings | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Helios Audit Log Settings.
	api_response = client.helios_audit_log.update_helios_audit_log_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAuditLogApi->update_helios_audit_log_settings: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Helios Audit Log Settings.
	api_response = client.helios_audit_log.update_helios_audit_log_settings(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAuditLogApi->update_helios_audit_log_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosAuditLogSettings**](HeliosAuditLogSettings.md)|  |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosAuditLogSettings**](HeliosAuditLogSettings.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

