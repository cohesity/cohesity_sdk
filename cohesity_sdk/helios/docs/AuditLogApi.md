# cohesity_sdk.helios.AuditLogApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_logs**](AuditLogApi.md#create_audit_logs) | **POST** /create-audit-logs | Create cluster audit logs.
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
[**update_filer_audit_log_configs**](AuditLogApi.md#update_filer_audit_log_configs) | **PUT** /audit-logs/filer-configs | Update filer audit log configs.
[**update_helios_audit_log_settings**](AuditLogApi.md#update_helios_audit_log_settings) | **PUT** /mcm/audit-logs/settings | Update Helios Audit Log Settings.


# **create_audit_logs**
> AuditLogsEntityTypes create_audit_logs(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create cluster audit logs.

Create a cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.audit_log import AuditLog
from cohesity_sdk.helios.models.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    body = cohesity_sdk.helios.AuditLog() # AuditLog | Request to create a audit log.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create cluster audit logs.
        api_response = api_instance.create_audit_logs(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AuditLogApi->create_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->create_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditLog**](AuditLog.md)| Request to create a audit log. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AuditLogsEntityTypes**](AuditLogsEntityTypes.md)

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

# **download_helios_audit_logs**
> bytearray download_helios_audit_logs(region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, cluster_identifiers=cluster_identifiers, start_index=start_index, count=count, include_helios_logs=include_helios_logs, include_dmaas_logs=include_dmaas_logs, region_ids=region_ids, service_context=service_context)

Download helios audit logs.

Download helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    search_string = 'search_string_example' # str | Search audit logs by 'entityName' or 'details'. (optional)
    usernames = ['usernames_example'] # List[str] | Specifies a list of usernames, only audit logs made by these users will be returned. (optional)
    domains = ['domains_example'] # List[str] | Specifies a list of domains, only audit logs made by user in these domains will be returned. (optional)
    entity_types = ['entity_types_example'] # List[str] | Specifies a list of entity types, only audit logs containing these entity types will be returned. (optional)
    actions = ['actions_example'] # List[str] | Specifies a list of actions, only audit logs containing these actions will be returned. (optional)
    start_time_usecs = 56 # int | Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. (optional)
    end_time_usecs = 56 # int | Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies a list of tenant ids, only audit logs made by these tenants will be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. (optional)
    start_index = 56 # int | Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. (optional)
    count = 56 # int | Specifies the number of indexed objects to be fetched from the index. (optional)
    include_helios_logs = True # bool | Specifies if helios audit logs need to be fetched or not from the index. (optional)
    include_dmaas_logs = True # bool | Specifies if dmaas audit logs need to be fetched or not from the index. (optional)
    region_ids = ['region_ids_example'] # List[str] | Specifies the list of region ids to filter.  (optional)
    service_context = ['service_context_example'] # List[str] | Returns the audit logs for a list of filter service context. Passing service context only one at a time is supported as of now (optional)

    try:
        # Download helios audit logs.
        api_response = api_instance.download_helios_audit_logs(region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, cluster_identifiers=cluster_identifiers, start_index=start_index, count=count, include_helios_logs=include_helios_logs, include_dmaas_logs=include_dmaas_logs, region_ids=region_ids, service_context=service_context)
        print("The response of AuditLogApi->download_helios_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->download_helios_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **search_string** | **str**| Search audit logs by &#39;entityName&#39; or &#39;details&#39;. | [optional] 
 **usernames** | [**List[str]**](str.md)| Specifies a list of usernames, only audit logs made by these users will be returned. | [optional] 
 **domains** | [**List[str]**](str.md)| Specifies a list of domains, only audit logs made by user in these domains will be returned. | [optional] 
 **entity_types** | [**List[str]**](str.md)| Specifies a list of entity types, only audit logs containing these entity types will be returned. | [optional] 
 **actions** | [**List[str]**](str.md)| Specifies a list of actions, only audit logs containing these actions will be returned. | [optional] 
 **start_time_usecs** | **int**| Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. | [optional] 
 **end_time_usecs** | **int**| Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies a list of tenant ids, only audit logs made by these tenants will be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional] 
 **start_index** | **int**| Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. | [optional] 
 **count** | **int**| Specifies the number of indexed objects to be fetched from the index. | [optional] 
 **include_helios_logs** | **bool**| Specifies if helios audit logs need to be fetched or not from the index. | [optional] 
 **include_dmaas_logs** | **bool**| Specifies if dmaas audit logs need to be fetched or not from the index. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Specifies the list of region ids to filter.  | [optional] 
 **service_context** | [**List[str]**](str.md)| Returns the audit logs for a list of filter service context. Passing service context only one at a time is supported as of now | [optional] 

### Return type

**bytearray**

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
> AuditLogs get_audit_logs(access_cluster_id=access_cluster_id, region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, start_index=start_index, count=count)

Get cluster audit logs.

Get a cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.audit_logs import AuditLogs
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    search_string = 'search_string_example' # str | Search audit logs by 'entityName' or 'details'. (optional)
    usernames = ['usernames_example'] # List[str] | Specifies a list of usernames, only audit logs made by these users will be returned. (optional)
    domains = ['domains_example'] # List[str] | Specifies a list of domains, only audit logs made by user in these domains will be returned. (optional)
    entity_types = ['entity_types_example'] # List[str] | Specifies a list of entity types, only audit logs containing these entity types will be returned. (optional)
    actions = ['actions_example'] # List[str] | Specifies a list of actions, only audit logs containing these actions will be returned. (optional)
    start_time_usecs = 56 # int | Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. (optional)
    end_time_usecs = 56 # int | Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies a list of tenant ids, only audit logs made by these tenants will be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)
    start_index = 56 # int | Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. (optional)
    count = 56 # int | Specifies the number of indexed obejcts to be fetched from the specified start index. (optional)

    try:
        # Get cluster audit logs.
        api_response = api_instance.get_audit_logs(access_cluster_id=access_cluster_id, region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, start_index=start_index, count=count)
        print("The response of AuditLogApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **search_string** | **str**| Search audit logs by &#39;entityName&#39; or &#39;details&#39;. | [optional] 
 **usernames** | [**List[str]**](str.md)| Specifies a list of usernames, only audit logs made by these users will be returned. | [optional] 
 **domains** | [**List[str]**](str.md)| Specifies a list of domains, only audit logs made by user in these domains will be returned. | [optional] 
 **entity_types** | [**List[str]**](str.md)| Specifies a list of entity types, only audit logs containing these entity types will be returned. | [optional] 
 **actions** | [**List[str]**](str.md)| Specifies a list of actions, only audit logs containing these actions will be returned. | [optional] 
 **start_time_usecs** | **int**| Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. | [optional] 
 **end_time_usecs** | **int**| Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies a list of tenant ids, only audit logs made by these tenants will be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional] 
 **start_index** | **int**| Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. | [optional] 
 **count** | **int**| Specifies the number of indexed obejcts to be fetched from the specified start index. | [optional] 

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
> AuditLogsActions get_audit_logs_actions(access_cluster_id=access_cluster_id, region_id=region_id)

Get cluster audit logs actions.

Get all actions of cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.audit_logs_actions import AuditLogsActions
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get cluster audit logs actions.
        api_response = api_instance.get_audit_logs_actions(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AuditLogApi->get_audit_logs_actions:\n")
        pprint(api_response)
    except Exception as e:
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
> AuditLogsEntityTypes get_audit_logs_entity_types(access_cluster_id=access_cluster_id, region_id=region_id)

Get cluster audit logs entity types.

Get all entity types of cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get cluster audit logs entity types.
        api_response = api_instance.get_audit_logs_entity_types(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AuditLogApi->get_audit_logs_entity_types:\n")
        pprint(api_response)
    except Exception as e:
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
> FilerAuditLogConfigs get_filer_audit_log_configs(access_cluster_id=access_cluster_id, region_id=region_id)

Get filer audit log configs.

Get filer audit log configs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get filer audit log configs.
        api_response = api_instance.get_filer_audit_log_configs(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AuditLogApi->get_filer_audit_log_configs:\n")
        pprint(api_response)
    except Exception as e:
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
> HeliosAuditLogSettings get_helios_audit_log_settings(region_id=region_id)

Get Helios Audit Log Settings.

Returns a list of Helios audit log settings.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_audit_log_settings import HeliosAuditLogSettings
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Helios Audit Log Settings.
        api_response = api_instance.get_helios_audit_log_settings(region_id=region_id)
        print("The response of AuditLogApi->get_helios_audit_log_settings:\n")
        pprint(api_response)
    except Exception as e:
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
> HeliosAuditLogs get_helios_audit_logs(region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, entity_ids=entity_ids, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, cluster_identifiers=cluster_identifiers, start_index=start_index, count=count, include_helios_logs=include_helios_logs, include_dmaas_logs=include_dmaas_logs, service_context=service_context, region_ids=region_ids)

Get helios audit logs.

Get helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_audit_logs import HeliosAuditLogs
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    search_string = 'search_string_example' # str | Search audit logs by 'entityName' or 'details'. (optional)
    usernames = ['usernames_example'] # List[str] | Specifies a list of usernames, only audit logs made by these users will be returned. (optional)
    domains = ['domains_example'] # List[str] | Specifies a list of domains, only audit logs made by user in these domains will be returned. (optional)
    entity_types = ['entity_types_example'] # List[str] | Specifies a list of entity types, only audit logs containing these entity types will be returned. (optional)
    entity_ids = ['entity_ids_example'] # List[str] | Specifies a list of entity ids, only audit logs containing these entity ids will be returned. (optional)
    actions = ['actions_example'] # List[str] | Specifies a list of actions, only audit logs containing these actions will be returned. (optional)
    start_time_usecs = 56 # int | Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. (optional)
    end_time_usecs = 56 # int | Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies a list of tenant ids, only audit logs made by these tenants will be returned. These has to be local tenant Id. (optional)
    include_tenants = True # bool | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. (optional)
    start_index = 56 # int | Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. (optional)
    count = 56 # int | Specifies the number of indexed objects to be fetched from the index. (optional)
    include_helios_logs = True # bool | Specifies if helios audit logs need to be fetched or not from the index. This is deprecated. Use serviceContext instead. (optional)
    include_dmaas_logs = True # bool | Specifies if dmaas audit logs need to be fetched or not from the index. This is deprecated. Use serviceContext instead. (optional)
    service_context = ['service_context_example'] # List[str] | Returns the audit logs for a list of filter service context. Passing service context only one at a time is supported as of now (optional)
    region_ids = ['region_ids_example'] # List[str] | Specifies the list of region ids to filter.  (optional)

    try:
        # Get helios audit logs.
        api_response = api_instance.get_helios_audit_logs(region_id=region_id, search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, entity_ids=entity_ids, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, cluster_identifiers=cluster_identifiers, start_index=start_index, count=count, include_helios_logs=include_helios_logs, include_dmaas_logs=include_dmaas_logs, service_context=service_context, region_ids=region_ids)
        print("The response of AuditLogApi->get_helios_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_helios_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **search_string** | **str**| Search audit logs by &#39;entityName&#39; or &#39;details&#39;. | [optional] 
 **usernames** | [**List[str]**](str.md)| Specifies a list of usernames, only audit logs made by these users will be returned. | [optional] 
 **domains** | [**List[str]**](str.md)| Specifies a list of domains, only audit logs made by user in these domains will be returned. | [optional] 
 **entity_types** | [**List[str]**](str.md)| Specifies a list of entity types, only audit logs containing these entity types will be returned. | [optional] 
 **entity_ids** | [**List[str]**](str.md)| Specifies a list of entity ids, only audit logs containing these entity ids will be returned. | [optional] 
 **actions** | [**List[str]**](str.md)| Specifies a list of actions, only audit logs containing these actions will be returned. | [optional] 
 **start_time_usecs** | **int**| Specifies a unix timestamp in microseconds, only audit logs made after this time will be returned. | [optional] 
 **end_time_usecs** | **int**| Specifies a unix timestamp in microseconds, only audit logs made before this time will be returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies a list of tenant ids, only audit logs made by these tenants will be returned. These has to be local tenant Id. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional] 
 **start_index** | **int**| Specifies a start index. The oldest logs before this index will skipped, only audit logs from this index will be fetched. | [optional] 
 **count** | **int**| Specifies the number of indexed objects to be fetched from the index. | [optional] 
 **include_helios_logs** | **bool**| Specifies if helios audit logs need to be fetched or not from the index. This is deprecated. Use serviceContext instead. | [optional] 
 **include_dmaas_logs** | **bool**| Specifies if dmaas audit logs need to be fetched or not from the index. This is deprecated. Use serviceContext instead. | [optional] 
 **service_context** | [**List[str]**](str.md)| Returns the audit logs for a list of filter service context. Passing service context only one at a time is supported as of now | [optional] 
 **region_ids** | [**List[str]**](str.md)| Specifies the list of region ids to filter.  | [optional] 

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
> HeliosAuditLogsActions get_helios_audit_logs_actions(region_id=region_id, service=service)

Get helios audit logs actions.

Get all actions of helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_audit_logs_actions import HeliosAuditLogsActions
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    service = Mcm # str | Get audit logs actions by service. (optional) (default to Mcm)

    try:
        # Get helios audit logs actions.
        api_response = api_instance.get_helios_audit_logs_actions(region_id=region_id, service=service)
        print("The response of AuditLogApi->get_helios_audit_logs_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_helios_audit_logs_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **service** | **str**| Get audit logs actions by service. | [optional] [default to Mcm]

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
> HeliosAuditLogUsers get_helios_audit_logs_cluster_users(region_id=region_id)

Get helios audit logs cluster users.

Get all cluster users of helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_audit_log_users import HeliosAuditLogUsers
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get helios audit logs cluster users.
        api_response = api_instance.get_helios_audit_logs_cluster_users(region_id=region_id)
        print("The response of AuditLogApi->get_helios_audit_logs_cluster_users:\n")
        pprint(api_response)
    except Exception as e:
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
> HeliosAuditLogsEntityTypes get_helios_audit_logs_entity_types(region_id=region_id, service=service)

Get helios audit logs entity types.

Get all entity types of helios audit logs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_audit_logs_entity_types import HeliosAuditLogsEntityTypes
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    service = Mcm # str | Get audit logs entity type by service. (optional) (default to Mcm)

    try:
        # Get helios audit logs entity types.
        api_response = api_instance.get_helios_audit_logs_entity_types(region_id=region_id, service=service)
        print("The response of AuditLogApi->get_helios_audit_logs_entity_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_helios_audit_logs_entity_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **service** | **str**| Get audit logs entity type by service. | [optional] [default to Mcm]

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

# **update_filer_audit_log_configs**
> FilerAuditLogConfigs update_filer_audit_log_configs(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update filer audit log configs.

Update filer audit log configs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    body = cohesity_sdk.helios.FilerAuditLogConfigs() # FilerAuditLogConfigs | Specifies the filer audit log config to update.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update filer audit log configs.
        api_response = api_instance.update_filer_audit_log_configs(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AuditLogApi->update_filer_audit_log_configs:\n")
        pprint(api_response)
    except Exception as e:
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
> HeliosAuditLogSettings update_helios_audit_log_settings(body, region_id=region_id)

Update Helios Audit Log Settings.

Updates Helios audit log settings.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_audit_log_settings import HeliosAuditLogSettings
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AuditLogApi(api_client)
    body = cohesity_sdk.helios.HeliosAuditLogSettings() # HeliosAuditLogSettings | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Helios Audit Log Settings.
        api_response = api_instance.update_helios_audit_log_settings(body, region_id=region_id)
        print("The response of AuditLogApi->update_helios_audit_log_settings:\n")
        pprint(api_response)
    except Exception as e:
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

