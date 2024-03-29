# cohesity_sdk.AuditLogApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**download_helios_audit_logs**](AuditLogApi.md#download_helios_audit_logs) | **GET** /mcm/audit-logs/download | Download helios audit logs.
[**get_audit_logs**](AuditLogApi.md#get_audit_logs) | **GET** /audit-logs | Get cluster audit logs.
[**get_audit_logs_actions**](AuditLogApi.md#get_audit_logs_actions) | **GET** /audit-logs/actions | Get cluster audit logs actions.
[**get_audit_logs_entity_types**](AuditLogApi.md#get_audit_logs_entity_types) | **GET** /audit-logs/entity-types | Get cluster audit logs entity types.
[**get_filer_audit_log_configs**](AuditLogApi.md#get_filer_audit_log_configs) | **GET** /audit-logs/filer-configs | Get filer audit log configs.
[**get_helios_audit_log_settings**](AuditLogApi.md#get_helios_audit_log_settings) | **GET** /mcm/audit-logs/settings | Get Helios Audit Log Settings.
[**get_helios_audit_logs**](AuditLogApi.md#get_helios_audit_logs) | **GET** /mcm/audit-logs | Get helios audit logs.
[**get_helios_audit_logs_actions**](AuditLogApi.md#get_helios_audit_logs_actions) | **GET** /mcm/audit-logs/actions | Get helios audit logs actions.
[**get_helios_audit_logs_cluster_users**](AuditLogApi.md#get_helios_audit_logs_cluster_users) | **GET** /mcm/audit-logs/clusterUsers | Get helios audit logs cluster users.
[**get_helios_audit_logs_entity_types**](AuditLogApi.md#get_helios_audit_logs_entity_types) | **GET** /mcm/audit-logs/entity-types | Get helios audit logs entity types.
[**publish_helios_audit_log**](AuditLogApi.md#publish_helios_audit_log) | **POST** /mcm/audit-logs/publish | Publish helios audit log.
[**update_filer_audit_log_configs**](AuditLogApi.md#update_filer_audit_log_configs) | **PUT** /audit-logs/filer-configs | Update filer audit log configs.
[**update_helios_audit_log_settings**](AuditLogApi.md#update_helios_audit_log_settings) | **PUT** /mcm/audit-logs/settings | Update Helios Audit Log Settings.


# **download_helios_audit_logs**
> file_type download_helios_audit_logs()

Download helios audit logs.

Download helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
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
        "entityTypes_example",
    ] # [str], none_type | Specifies a list of entity types, only audit logs containing these entity types will be returned. (optional)
actions = [
        "actions_example",
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
include_helios_logs = True # bool, none_type | Specifies if helios audit logs need to be fetched or not from the index. (optional)
include_dmaas_logs = True # bool, none_type | Specifies if dmaas audit logs need to be fetched or not from the index. (optional)
region_ids = [
        "us-east-1",
    ] # [str], none_type | Specifies the list of region ids to filter.  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Download helios audit logs.
	api_response = client.audit_log.download_helios_audit_logs(region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, cluster_identifiers=cluster_identifiers, start_index=start_index, count=count, include_helios_logs=include_helios_logs, include_dmaas_logs=include_dmaas_logs, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->download_helios_audit_logs: %s\n" % e)
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
 **include_helios_logs** | **bool, none_type**| Specifies if helios audit logs need to be fetched or not from the index. | [optional]
 **include_dmaas_logs** | **bool, none_type**| Specifies if dmaas audit logs need to be fetched or not from the index. | [optional]
 **region_ids** | **[str], none_type**| Specifies the list of region ids to filter.  | [optional]

### Return type

**file_type**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Download file for Audit Logs. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs**
> AuditLogs get_audit_logs()

Get cluster audit logs.

Get a cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.audit_logs import AuditLogs
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
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
start_index = 1 # int, none_type | Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. (optional)
count = 1 # int, none_type | Specifies the number of indexed obejcts to be fetched from the specified start index. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get cluster audit logs.
	api_response = client.audit_log.get_audit_logs(access_cluster_id=access_cluster_id, region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, start_index=start_index, count=count)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
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
 **start_index** | **int, none_type**| Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. | [optional]
 **count** | **int, none_type**| Specifies the number of indexed obejcts to be fetched from the specified start index. | [optional]

### Return type

[**AuditLogs**](AuditLogs.md)

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

# **get_audit_logs_actions**
> AuditLogsActions get_audit_logs_actions()

Get cluster audit logs actions.

Get all actions of cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.audit_logs_actions import AuditLogsActions
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get cluster audit logs actions.
	api_response = client.audit_log.get_audit_logs_actions(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_audit_logs_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**AuditLogsActions**](AuditLogsActions.md)

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

# **get_audit_logs_entity_types**
> AuditLogsEntityTypes get_audit_logs_entity_types()

Get cluster audit logs entity types.

Get all entity types of cluster audit logs.

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


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get cluster audit logs entity types.
	api_response = client.audit_log.get_audit_logs_entity_types(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_audit_logs_entity_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
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

# **get_filer_audit_log_configs**
> FilerAuditLogConfigs get_filer_audit_log_configs()

Get filer audit log configs.

Get filer audit log configs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get filer audit log configs.
	api_response = client.audit_log.get_filer_audit_log_configs(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_filer_audit_log_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

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
	api_response = client.audit_log.get_helios_audit_log_settings(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_helios_audit_log_settings: %s\n" % e)
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
        "entityTypes_example",
    ] # [str], none_type | Specifies a list of entity types, only audit logs containing these entity types will be returned. (optional)
actions = [
        "actions_example",
    ] # [str], none_type | Specifies a list of actions, only audit logs containing these actions will be returned. (optional)
start_time_usecs = 1 # int, none_type | Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. (optional)
end_time_usecs = 1 # int, none_type | Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str], none_type | Specifies a list of tenant ids, only audit logs made by these tenants will be returned. These has to be local tenant Id. (optional)
include_tenants = True # bool, none_type | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)
cluster_identifiers = [
        "4:072888001528021798096225500850762068629",
    ] # [str], none_type | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. (optional)
start_index = 1 # int, none_type | Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. (optional)
count = 1 # int, none_type | Specifies the number of indexed objects to be fetched from the index. (optional)
include_helios_logs = True # bool, none_type | Specifies if helios audit logs need to be fetched or not from the index. (optional)
include_dmaas_logs = True # bool, none_type | Specifies if dmaas audit logs need to be fetched or not from the index. (optional)
region_ids = [
        "us-east-1",
    ] # [str], none_type | Specifies the list of region ids to filter.  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios audit logs.
	api_response = client.audit_log.get_helios_audit_logs(region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, cluster_identifiers=cluster_identifiers, start_index=start_index, count=count, include_helios_logs=include_helios_logs, include_dmaas_logs=include_dmaas_logs, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_helios_audit_logs: %s\n" % e)
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
 **tenant_ids** | **[str], none_type**| Specifies a list of tenant ids, only audit logs made by these tenants will be returned. These has to be local tenant Id. | [optional]
 **include_tenants** | **bool, none_type**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional]
 **cluster_identifiers** | **[str], none_type**| Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional]
 **start_index** | **int, none_type**| Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. | [optional]
 **count** | **int, none_type**| Specifies the number of indexed objects to be fetched from the index. | [optional]
 **include_helios_logs** | **bool, none_type**| Specifies if helios audit logs need to be fetched or not from the index. | [optional]
 **include_dmaas_logs** | **bool, none_type**| Specifies if dmaas audit logs need to be fetched or not from the index. | [optional]
 **region_ids** | **[str], none_type**| Specifies the list of region ids to filter.  | [optional]

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
service = "Mcm" # str, none_type | Get audit logs actions by service. (optional) if omitted the server will use the default value of "Mcm"

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios audit logs actions.
	api_response = client.audit_log.get_helios_audit_logs_actions(region_id=region_id, service=service)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_helios_audit_logs_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **service** | **str, none_type**| Get audit logs actions by service. | [optional] if omitted the server will use the default value of "Mcm"

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

# **get_helios_audit_logs_cluster_users**
> HeliosAuditLogUsers get_helios_audit_logs_cluster_users()

Get helios audit logs cluster users.

Get all cluster users of helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_audit_log_users import HeliosAuditLogUsers
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios audit logs cluster users.
	api_response = client.audit_log.get_helios_audit_logs_cluster_users(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_helios_audit_logs_cluster_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosAuditLogUsers**](HeliosAuditLogUsers.md)

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
> HeliosAuditLogsEntityTypes get_helios_audit_logs_entity_types()

Get helios audit logs entity types.

Get all entity types of helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_audit_logs_entity_types import HeliosAuditLogsEntityTypes
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
service = "Mcm" # str, none_type | Get audit logs entity type by service. (optional) if omitted the server will use the default value of "Mcm"

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios audit logs entity types.
	api_response = client.audit_log.get_helios_audit_logs_entity_types(region_id=region_id, service=service)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->get_helios_audit_logs_entity_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **service** | **str, none_type**| Get audit logs entity type by service. | [optional] if omitted the server will use the default value of "Mcm"

### Return type

[**HeliosAuditLogsEntityTypes**](HeliosAuditLogsEntityTypes.md)

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

# **publish_helios_audit_log**
> publish_helios_audit_log(body)

Publish helios audit log.

Publish Helios Audit Log

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.publish_helios_audit_log_request import PublishHeliosAuditLogRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = PublishHeliosAuditLogRequest(
        details="details_example",
        entity_name="entity_name_example",
        entity_type="ClusterPartition",
        entity_id="entity_id_example",
        action="Login",
        ip="ip_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        original_tenant_id="original_tenant_id_example",
        original_tenant_name="original_tenant_name_example",
        previous_record={},
        new_record={},
    ) # PublishHeliosAuditLogRequest | Specifies the parameters to publish helios audit log.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Publish helios audit log.
	client.audit_log.publish_helios_audit_log(body)
except ApiException as e:
	print("Exception when calling AuditLogApi->publish_helios_audit_log: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Publish helios audit log.
	client.audit_log.publish_helios_audit_log(body, region_id=region_id)
except ApiException as e:
	print("Exception when calling AuditLogApi->publish_helios_audit_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublishHeliosAuditLogRequest**](PublishHeliosAuditLogRequest.md)| Specifies the parameters to publish helios audit log. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filer_audit_log_configs**
> FilerAuditLogConfigs update_filer_audit_log_configs(body)

Update filer audit log configs.

Update filer audit log configs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = FilerAuditLogConfigs(
        share_permissions=[
            SmbPermission(
                type="Allow",
                mode="FolderSubFoldersAndFiles",
                access="ReadOnly",
                sid="sid_example",
                special_type=1,
                special_access_mask=1,
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
                smb_access="kDisabled",
                s3_access="kDisabled",
            ),
        ],
        override_global_subnet_whitelist=True,
    ) # FilerAuditLogConfigs | Specifies the filer audit log config to update.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update filer audit log configs.
	api_response = client.audit_log.update_filer_audit_log_configs(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->update_filer_audit_log_configs: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update filer audit log configs.
	api_response = client.audit_log.update_filer_audit_log_configs(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->update_filer_audit_log_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)| Specifies the filer audit log config to update. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

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
        role_settings=[
            HeliosAuditLogRoleSetting(
                role_name="role_name_example",
                read_logging=False,
            ),
        ],
        read_logging=False,
        retention_period_days=1,
    ) # HeliosAuditLogSettings | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Helios Audit Log Settings.
	api_response = client.audit_log.update_helios_audit_log_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->update_helios_audit_log_settings: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Helios Audit Log Settings.
	api_response = client.audit_log.update_helios_audit_log_settings(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AuditLogApi->update_helios_audit_log_settings: %s\n" % e)
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

