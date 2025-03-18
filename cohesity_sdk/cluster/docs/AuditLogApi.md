# cohesity_sdk.cluster.AuditLogApi

All URIs are relative to */v2*

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

Create a cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.audit_log import AuditLog
from cohesity_sdk.cluster.models.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AuditLogApi(api_client)
    body = cohesity_sdk.cluster.AuditLog() # AuditLog | Request to create a audit log.

    try:
        # Create cluster audit logs.
        api_response = api_instance.create_audit_logs(body)
        print("The response of AuditLogApi->create_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->create_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditLog**](AuditLog.md)| Request to create a audit log. | 

### Return type

[**AuditLogsEntityTypes**](AuditLogsEntityTypes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> AuditLogs get_audit_logs(search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, start_index=start_index, count=count)

Get cluster audit logs.

Get a cluster audit logs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.audit_logs import AuditLogs
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AuditLogApi(api_client)
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
        api_response = api_instance.get_audit_logs(search_string=search_string, usernames=usernames, domains=domains, entity_types=entity_types, actions=actions, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, start_index=start_index, count=count)
        print("The response of AuditLogApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.audit_logs_actions import AuditLogsActions
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AuditLogApi(api_client)

    try:
        # Get cluster audit logs actions.
        api_response = api_instance.get_audit_logs_actions()
        print("The response of AuditLogApi->get_audit_logs_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_logs_actions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditLogsActions**](AuditLogsActions.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.audit_logs_entity_types import AuditLogsEntityTypes
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AuditLogApi(api_client)

    try:
        # Get cluster audit logs entity types.
        api_response = api_instance.get_audit_logs_entity_types()
        print("The response of AuditLogApi->get_audit_logs_entity_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_logs_entity_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuditLogsEntityTypes**](AuditLogsEntityTypes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AuditLogApi(api_client)

    try:
        # Get filer audit log configs.
        api_response = api_instance.get_filer_audit_log_configs()
        print("The response of AuditLogApi->get_filer_audit_log_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_filer_audit_log_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.filer_audit_log_configs import FilerAuditLogConfigs
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AuditLogApi(api_client)
    body = cohesity_sdk.cluster.FilerAuditLogConfigs() # FilerAuditLogConfigs | Specifies the filer audit log config to update.

    try:
        # Update filer audit log configs.
        api_response = api_instance.update_filer_audit_log_configs(body)
        print("The response of AuditLogApi->update_filer_audit_log_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->update_filer_audit_log_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)| Specifies the filer audit log config to update. | 

### Return type

[**FilerAuditLogConfigs**](FilerAuditLogConfigs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

