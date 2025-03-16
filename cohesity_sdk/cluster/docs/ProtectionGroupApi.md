# cohesity_sdk.cluster.ProtectionGroupApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_protection_group**](ProtectionGroupApi.md#create_protection_group) | **POST** /data-protect/protection-groups | Create a Protection Group.
[**create_protection_group_run**](ProtectionGroupApi.md#create_protection_group_run) | **POST** /data-protect/protection-groups/{id}/runs | Create a new protection run.
[**delete_protection_group**](ProtectionGroupApi.md#delete_protection_group) | **DELETE** /data-protect/protection-groups/{id} | Delete a Protection Group.
[**get_protection_group_by_id**](ProtectionGroupApi.md#get_protection_group_by_id) | **GET** /data-protect/protection-groups/{id} | List details about single Protection Group.
[**get_protection_group_run**](ProtectionGroupApi.md#get_protection_group_run) | **GET** /data-protect/protection-groups/{id}/runs/{runId} | Get a run for a Protection Group.
[**get_protection_group_runs**](ProtectionGroupApi.md#get_protection_group_runs) | **GET** /data-protect/protection-groups/{id}/runs | Get the list of runs for a Protection Group.
[**get_protection_groups**](ProtectionGroupApi.md#get_protection_groups) | **GET** /data-protect/protection-groups | Get the list of Protection Groups.
[**get_protection_run_progress**](ProtectionGroupApi.md#get_protection_run_progress) | **GET** /data-protect/runs/{runId}/progress | Get the progress of a run.
[**get_protection_run_stats**](ProtectionGroupApi.md#get_protection_run_stats) | **GET** /data-protect/runs/{runId}/stats | Get the stats for a run.
[**get_protection_runs**](ProtectionGroupApi.md#get_protection_runs) | **GET** /data-protect/runs/summary | Get the list of runs.
[**get_run_debug_logs**](ProtectionGroupApi.md#get_run_debug_logs) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/debug-logs | Get the debug logs for a run from a Protection Group.
[**get_run_debug_logs_for_object**](ProtectionGroupApi.md#get_run_debug_logs_for_object) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/objects/{objectId}/debug-logs | Get the debug logs for a particular object in a run from a Protection Group.
[**get_run_messages_report**](ProtectionGroupApi.md#get_run_messages_report) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/objects/{objectId}/download-messages | Get the CSV of various Proto Messages for a given run and an object.
[**get_runs_report**](ProtectionGroupApi.md#get_runs_report) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/objects/{objectId}/downloadFiles | Get the CSV of errors/warnings for a given run and an object.
[**perform_action_on_protection_group_run**](ProtectionGroupApi.md#perform_action_on_protection_group_run) | **POST** /data-protect/protection-groups/{id}/runs/actions | Actions on protection group run.
[**update_protection_group**](ProtectionGroupApi.md#update_protection_group) | **PUT** /data-protect/protection-groups/{id} | Update a Protection Group.
[**update_protection_group_run**](ProtectionGroupApi.md#update_protection_group_run) | **PUT** /data-protect/protection-groups/{id}/runs | Update runs for a particular Protection Group.
[**update_protection_groups_state**](ProtectionGroupApi.md#update_protection_groups_state) | **POST** /data-protect/protection-groups/states | Perform an action like pause, resume, active, deactivate on all specified Protection Groups.


# **create_protection_group**
> ProtectionGroup create_protection_group(body)

Create a Protection Group.

Create a Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.cluster.models.protection_group import ProtectionGroup
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    body = cohesity_sdk.cluster.CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to create a Protection Group.

    try:
        # Create a Protection Group.
        api_response = api_instance.create_protection_group(body)
        print("The response of ProtectionGroupApi->create_protection_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->create_protection_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to create a Protection Group. | 

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_protection_group_run**
> CreateProtectionGroupRunResponseBody create_protection_group_run(id, body)

Create a new protection run.

Create a new protection run. This can be used to start a run for a Protection Group on demand, ignoring the schedule and retention specified in the protection policy.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_protection_group_run_request import CreateProtectionGroupRunRequest
from cohesity_sdk.cluster.models.create_protection_group_run_response_body import CreateProtectionGroupRunResponseBody
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    body = cohesity_sdk.cluster.CreateProtectionGroupRunRequest() # CreateProtectionGroupRunRequest | Specifies the parameters to start a protection run.

    try:
        # Create a new protection run.
        api_response = api_instance.create_protection_group_run(id, body)
        print("The response of ProtectionGroupApi->create_protection_group_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->create_protection_group_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **body** | [**CreateProtectionGroupRunRequest**](CreateProtectionGroupRunRequest.md)| Specifies the parameters to start a protection run. | 

### Return type

[**CreateProtectionGroupRunResponseBody**](CreateProtectionGroupRunResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_protection_group**
> delete_protection_group(id, delete_snapshots=delete_snapshots)

Delete a Protection Group.

Returns Success if the Protection Group is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    delete_snapshots = True # bool | Specifies if Snapshots generated by the Protection Group should also be deleted when the Protection Group is deleted. (optional)

    try:
        # Delete a Protection Group.
        api_instance.delete_protection_group(id, delete_snapshots=delete_snapshots)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->delete_protection_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **delete_snapshots** | **bool**| Specifies if Snapshots generated by the Protection Group should also be deleted when the Protection Group is deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protection_group_by_id**
> ProtectionGroup get_protection_group_by_id(id, request_initiator_type=request_initiator_type, include_last_run_info=include_last_run_info, prune_excluded_source_ids=prune_excluded_source_ids, prune_source_ids=prune_source_ids)

List details about single Protection Group.

Returns the Protection Group corresponding to the specified Group id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.protection_group import ProtectionGroup
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    include_last_run_info = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)
    prune_excluded_source_ids = True # bool | If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. (optional)
    prune_source_ids = True # bool | If true, the response will exclude the list of source IDs within the group specified. (optional)

    try:
        # List details about single Protection Group.
        api_response = api_instance.get_protection_group_by_id(id, request_initiator_type=request_initiator_type, include_last_run_info=include_last_run_info, prune_excluded_source_ids=prune_excluded_source_ids, prune_source_ids=prune_source_ids)
        print("The response of ProtectionGroupApi->get_protection_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_protection_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **include_last_run_info** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional] 
 **prune_excluded_source_ids** | **bool**| If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. | [optional] 
 **prune_source_ids** | **bool**| If true, the response will exclude the list of source IDs within the group specified. | [optional] 

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **get_protection_group_run**
> CommonProtectionGroupRunResponseParameters get_protection_group_run(id, run_id, request_initiator_type=request_initiator_type, tenant_ids=tenant_ids, include_tenants=include_tenants, include_object_details=include_object_details, use_cached_data=use_cached_data)

Get a run for a Protection Group.

Get a run for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.common_protection_group_run_response_parameters import CommonProtectionGroupRunResponseParameters
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    run_id = 'run_id_example' # str | Specifies a unique run id of the Protection Group run.
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which the run is to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it's not specified, it is true by default. (optional)
    include_object_details = True # bool | Specifies if the result includes the object details for a protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)

    try:
        # Get a run for a Protection Group.
        api_response = api_instance.get_protection_group_run(id, run_id, request_initiator_type=request_initiator_type, tenant_ids=tenant_ids, include_tenants=include_tenants, include_object_details=include_object_details, use_cached_data=use_cached_data)
        print("The response of ProtectionGroupApi->get_protection_group_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_protection_group_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. | 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which the run is to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it&#39;s not specified, it is true by default. | [optional] 
 **include_object_details** | **bool**| Specifies if the result includes the object details for a protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 

### Return type

[**CommonProtectionGroupRunResponseParameters**](CommonProtectionGroupRunResponseParameters.md)

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

# **get_protection_group_runs**
> ProtectionGroupRuns get_protection_group_runs(id, request_initiator_type=request_initiator_type, run_id=run_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, run_types=run_types, include_object_details=include_object_details, local_backup_run_status=local_backup_run_status, replication_run_status=replication_run_status, archival_run_status=archival_run_status, cloud_spin_run_status=cloud_spin_run_status, num_runs=num_runs, exclude_non_restorable_runs=exclude_non_restorable_runs, run_tags=run_tags, use_cached_data=use_cached_data, filter_by_end_time=filter_by_end_time, snapshot_target_types=snapshot_target_types, only_return_successful_copy_run=only_return_successful_copy_run, filter_by_copy_task_end_time=filter_by_copy_task_end_time, max_result_count=max_result_count, pagination_cookie=pagination_cookie)

Get the list of runs for a Protection Group.

Get the runs for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.protection_group_runs import ProtectionGroupRuns
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    run_id = 'run_id_example' # str | Specifies the protection run id. (optional)
    start_time_usecs = 56 # int | Start time for time range filter. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be returned. By default it is endTimeUsecs minus an hour. (optional)
    end_time_usecs = 56 # int | End time for time range filter. Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be returned. By default it is current time. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. (optional)
    run_types = ['run_types_example'] # List[str] | Filter by run type. Only protection run matching the specified types will be returned. (optional)
    include_object_details = True # bool | Specifies if the result includes the object details for each protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. (optional)
    local_backup_run_status = ['local_backup_run_status_example'] # List[str] | Specifies a list of local backup status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    replication_run_status = ['replication_run_status_example'] # List[str] | Specifies a list of replication status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    archival_run_status = ['archival_run_status_example'] # List[str] | Specifies a list of archival status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    cloud_spin_run_status = ['cloud_spin_run_status_example'] # List[str] | Specifies a list of cloud spin status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    num_runs = 56 # int | Specifies the max number of runs. If not specified, at most 100 runs will be returned. (optional)
    exclude_non_restorable_runs = False # bool | Specifies whether to exclude non restorable runs. Run is treated restorable only if there is atleast one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. (optional) (default to False)
    run_tags = ['run_tags_example'] # List[str] | Specifies a list of tags for protection runs. If this is specified, only the runs which match these tags will be returned. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)
    filter_by_end_time = True # bool | If true, the runs with backup end time within the specified time range will be returned. Otherwise, the runs with start time in the time range are returned. (optional)
    snapshot_target_types = ['snapshot_target_types_example'] # List[str] | Specifies the snapshot's target type which should be filtered. Note: this field is only considered when, filterByCopyTaskEndTime is set to true, or else it is ignored. (optional)
    only_return_successful_copy_run = True # bool | If set to false, all copy_tasks in any given valid state will be considered. If left empty or set to true, only successful copy_tasks would be considered. Note: this field is only considered when, filterByCopyTaskEndTime is set to true, or else it is ignored. (optional)
    filter_by_copy_task_end_time = True # bool | If true, then the details of the runs for which any copyTask completed in the given timerange will be returned. Only one of filterByEndTime and filterByCopyTaskEndTime can be set. (optional)
    max_result_count = 56 # int | Identifies the max number of items to be returned. This is specifically to be used with pagination. (optional)
    pagination_cookie = 'pagination_cookie_example' # str | Specifies the cookie to fetch the next page of results (optional)

    try:
        # Get the list of runs for a Protection Group.
        api_response = api_instance.get_protection_group_runs(id, request_initiator_type=request_initiator_type, run_id=run_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, run_types=run_types, include_object_details=include_object_details, local_backup_run_status=local_backup_run_status, replication_run_status=replication_run_status, archival_run_status=archival_run_status, cloud_spin_run_status=cloud_spin_run_status, num_runs=num_runs, exclude_non_restorable_runs=exclude_non_restorable_runs, run_tags=run_tags, use_cached_data=use_cached_data, filter_by_end_time=filter_by_end_time, snapshot_target_types=snapshot_target_types, only_return_successful_copy_run=only_return_successful_copy_run, filter_by_copy_task_end_time=filter_by_copy_task_end_time, max_result_count=max_result_count, pagination_cookie=pagination_cookie)
        print("The response of ProtectionGroupApi->get_protection_group_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_protection_group_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **run_id** | **str**| Specifies the protection run id. | [optional] 
 **start_time_usecs** | **int**| Start time for time range filter. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be returned. By default it is endTimeUsecs minus an hour. | [optional] 
 **end_time_usecs** | **int**| End time for time range filter. Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be returned. By default it is current time. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. | [optional] 
 **run_types** | [**List[str]**](str.md)| Filter by run type. Only protection run matching the specified types will be returned. | [optional] 
 **include_object_details** | **bool**| Specifies if the result includes the object details for each protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. | [optional] 
 **local_backup_run_status** | [**List[str]**](str.md)| Specifies a list of local backup status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **replication_run_status** | [**List[str]**](str.md)| Specifies a list of replication status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **archival_run_status** | [**List[str]**](str.md)| Specifies a list of archival status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **cloud_spin_run_status** | [**List[str]**](str.md)| Specifies a list of cloud spin status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **num_runs** | **int**| Specifies the max number of runs. If not specified, at most 100 runs will be returned. | [optional] 
 **exclude_non_restorable_runs** | **bool**| Specifies whether to exclude non restorable runs. Run is treated restorable only if there is atleast one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. | [optional] [default to False]
 **run_tags** | [**List[str]**](str.md)| Specifies a list of tags for protection runs. If this is specified, only the runs which match these tags will be returned. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
 **filter_by_end_time** | **bool**| If true, the runs with backup end time within the specified time range will be returned. Otherwise, the runs with start time in the time range are returned. | [optional] 
 **snapshot_target_types** | [**List[str]**](str.md)| Specifies the snapshot&#39;s target type which should be filtered. Note: this field is only considered when, filterByCopyTaskEndTime is set to true, or else it is ignored. | [optional] 
 **only_return_successful_copy_run** | **bool**| If set to false, all copy_tasks in any given valid state will be considered. If left empty or set to true, only successful copy_tasks would be considered. Note: this field is only considered when, filterByCopyTaskEndTime is set to true, or else it is ignored. | [optional] 
 **filter_by_copy_task_end_time** | **bool**| If true, then the details of the runs for which any copyTask completed in the given timerange will be returned. Only one of filterByEndTime and filterByCopyTaskEndTime can be set. | [optional] 
 **max_result_count** | **int**| Identifies the max number of items to be returned. This is specifically to be used with pagination. | [optional] 
 **pagination_cookie** | **str**| Specifies the cookie to fetch the next page of results | [optional] 

### Return type

[**ProtectionGroupRuns**](ProtectionGroupRuns.md)

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

# **get_protection_groups**
> ProtectionGroups get_protection_groups(request_initiator_type=request_initiator_type, ids=ids, names=names, policy_ids=policy_ids, storage_domain_id=storage_domain_id, include_groups_with_datalock_only=include_groups_with_datalock_only, environments=environments, office365_workloads=office365_workloads, is_active=is_active, is_deleted=is_deleted, is_paused=is_paused, last_run_local_backup_status=last_run_local_backup_status, last_run_replication_status=last_run_replication_status, last_run_archival_status=last_run_archival_status, last_run_cloud_spin_status=last_run_cloud_spin_status, last_run_any_status=last_run_any_status, is_last_run_sla_violated=is_last_run_sla_violated, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, prune_excluded_source_ids=prune_excluded_source_ids, prune_source_ids=prune_source_ids, use_cached_data=use_cached_data, source_ids=source_ids, max_result_count=max_result_count, pagination_cookie=pagination_cookie)

Get the list of Protection Groups.

Get the list of Protection Groups.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.protection_groups import ProtectionGroups
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    ids = ['ids_example'] # List[str] | Filter by a list of Protection Group ids. (optional)
    names = ['names_example'] # List[str] | Filter by a list of Protection Group names. (optional)
    policy_ids = ['policy_ids_example'] # List[str] | Filter by Policy ids that are associated with Protection Groups. Only Protection Groups associated with the specified Policy ids, are returned. (optional)
    storage_domain_id = 56 # int | Filter by Storage Domain id. Only Protection Groups writing data to this Storage Domain will be returned. (optional)
    include_groups_with_datalock_only = True # bool | Whether to only return Protection Groups with a datalock. (optional)
    environments = ['environments_example'] # List[str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protection Groups protecting the specified environment types are returned. (optional)
    office365_workloads = ['office365_workloads_example'] # List[str] |  (optional)
    is_active = True # bool | Filter by Inactive or Active Protection Groups. If not set, all Inactive and Active Protection Groups are returned. If true, only Active Protection Groups are returned. If false, only Inactive Protection Groups are returned. When you create a Protection Group on a Primary Cluster with a replication schedule, the Cluster creates an Inactive copy of the Protection Group on the Remote Cluster. In addition, when an Active and running Protection Group is deactivated, the Protection Group becomes Inactive. (optional)
    is_deleted = True # bool | If true, return only Protection Groups that have been deleted but still have Snapshots associated with them. If false, return all Protection Groups except those Protection Groups that have been deleted and still have Snapshots associated with them. A Protection Group that is deleted with all its Snapshots is not returned for either of these cases. (optional)
    is_paused = True # bool | Filter by paused or non paused Protection Groups, If not set, all paused and non paused Protection Groups are returned. If true, only paused Protection Groups are returned. If false, only non paused Protection Groups are returned. (optional)
    last_run_local_backup_status = ['last_run_local_backup_status_example'] # List[str] | Filter by last local backup run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    last_run_replication_status = ['last_run_replication_status_example'] # List[str] | Filter by last remote replication run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    last_run_archival_status = ['last_run_archival_status_example'] # List[str] | Filter by last cloud archival run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    last_run_cloud_spin_status = ['last_run_cloud_spin_status_example'] # List[str] | Filter by last cloud spin run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    last_run_any_status = ['last_run_any_status_example'] # List[str] | Filter by last any run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    is_last_run_sla_violated = True # bool | If true, return Protection Groups for which last run SLA was violated. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)
    include_last_run_info = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)
    prune_excluded_source_ids = True # bool | If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. (optional)
    prune_source_ids = True # bool | If true, the response will exclude the list of source IDs within the group specified. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)
    source_ids = [56] # List[int] | Filter by Source ids that are associated with Protection Groups. Only Protection Groups associated with the specified Source ids, are returned. (optional)
    max_result_count = 56 # int | Identifies the max number of items to be returned. This is specifically to be used with pagination. (optional)
    pagination_cookie = 'pagination_cookie_example' # str | Specifies the cookie to fetch the set page of results (optional)

    try:
        # Get the list of Protection Groups.
        api_response = api_instance.get_protection_groups(request_initiator_type=request_initiator_type, ids=ids, names=names, policy_ids=policy_ids, storage_domain_id=storage_domain_id, include_groups_with_datalock_only=include_groups_with_datalock_only, environments=environments, office365_workloads=office365_workloads, is_active=is_active, is_deleted=is_deleted, is_paused=is_paused, last_run_local_backup_status=last_run_local_backup_status, last_run_replication_status=last_run_replication_status, last_run_archival_status=last_run_archival_status, last_run_cloud_spin_status=last_run_cloud_spin_status, last_run_any_status=last_run_any_status, is_last_run_sla_violated=is_last_run_sla_violated, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, prune_excluded_source_ids=prune_excluded_source_ids, prune_source_ids=prune_source_ids, use_cached_data=use_cached_data, source_ids=source_ids, max_result_count=max_result_count, pagination_cookie=pagination_cookie)
        print("The response of ProtectionGroupApi->get_protection_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_protection_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **ids** | [**List[str]**](str.md)| Filter by a list of Protection Group ids. | [optional] 
 **names** | [**List[str]**](str.md)| Filter by a list of Protection Group names. | [optional] 
 **policy_ids** | [**List[str]**](str.md)| Filter by Policy ids that are associated with Protection Groups. Only Protection Groups associated with the specified Policy ids, are returned. | [optional] 
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only Protection Groups writing data to this Storage Domain will be returned. | [optional] 
 **include_groups_with_datalock_only** | **bool**| Whether to only return Protection Groups with a datalock. | [optional] 
 **environments** | [**List[str]**](str.md)| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protection Groups protecting the specified environment types are returned. | [optional] 
 **office365_workloads** | [**List[str]**](str.md)|  | [optional] 
 **is_active** | **bool**| Filter by Inactive or Active Protection Groups. If not set, all Inactive and Active Protection Groups are returned. If true, only Active Protection Groups are returned. If false, only Inactive Protection Groups are returned. When you create a Protection Group on a Primary Cluster with a replication schedule, the Cluster creates an Inactive copy of the Protection Group on the Remote Cluster. In addition, when an Active and running Protection Group is deactivated, the Protection Group becomes Inactive. | [optional] 
 **is_deleted** | **bool**| If true, return only Protection Groups that have been deleted but still have Snapshots associated with them. If false, return all Protection Groups except those Protection Groups that have been deleted and still have Snapshots associated with them. A Protection Group that is deleted with all its Snapshots is not returned for either of these cases. | [optional] 
 **is_paused** | **bool**| Filter by paused or non paused Protection Groups, If not set, all paused and non paused Protection Groups are returned. If true, only paused Protection Groups are returned. If false, only non paused Protection Groups are returned. | [optional] 
 **last_run_local_backup_status** | [**List[str]**](str.md)| Filter by last local backup run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **last_run_replication_status** | [**List[str]**](str.md)| Filter by last remote replication run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **last_run_archival_status** | [**List[str]**](str.md)| Filter by last cloud archival run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **last_run_cloud_spin_status** | [**List[str]**](str.md)| Filter by last cloud spin run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **last_run_any_status** | [**List[str]**](str.md)| Filter by last any run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **is_last_run_sla_violated** | **bool**| If true, return Protection Groups for which last run SLA was violated. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional] 
 **include_last_run_info** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional] 
 **prune_excluded_source_ids** | **bool**| If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. | [optional] 
 **prune_source_ids** | **bool**| If true, the response will exclude the list of source IDs within the group specified. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
 **source_ids** | [**List[int]**](int.md)| Filter by Source ids that are associated with Protection Groups. Only Protection Groups associated with the specified Source ids, are returned. | [optional] 
 **max_result_count** | **int**| Identifies the max number of items to be returned. This is specifically to be used with pagination. | [optional] 
 **pagination_cookie** | **str**| Specifies the cookie to fetch the set page of results | [optional] 

### Return type

[**ProtectionGroups**](ProtectionGroups.md)

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

# **get_protection_run_progress**
> GetProtectionRunProgressBody get_protection_run_progress(run_id, objects=objects, tenant_ids=tenant_ids, include_tenants=include_tenants, include_finished_tasks=include_finished_tasks, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_tasks_num=max_tasks_num, exclude_object_details=exclude_object_details, include_event_logs=include_event_logs, max_log_level=max_log_level, run_task_path=run_task_path, object_task_paths=object_task_paths)

Get the progress of a run.

Get the progress of a run.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_protection_run_progress_body import GetProtectionRunProgressBody
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    run_id = 'run_id_example' # str | Specifies a unique run id of the Protection Run.
    objects = [56] # List[int] | Specifies the objects whose progress will be returned. This only applies to protection group runs and will be ignored for object runs. If the objects are specified, the run progress will not be returned and only the progress of the specified objects will be returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which the run is to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it's not specified, it is true by default. (optional)
    include_finished_tasks = True # bool | Specifies whether to return finished tasks. By default only active tasks are returned. (optional)
    start_time_usecs = 56 # int | Specifies the time after which the progress task starts in Unix epoch Timestamp(in microseconds). (optional)
    end_time_usecs = 56 # int | Specifies the time before which the progress task ends in Unix epoch Timestamp(in microseconds). (optional)
    max_tasks_num = 56 # int | Specifies the maximum number of tasks to return. (optional)
    exclude_object_details = True # bool | Specifies whether to return objects. By default all the task tree are returned. (optional)
    include_event_logs = True # bool | Specifies whether to include event logs (optional)
    max_log_level = 56 # int | Specifies the number of levels till which to fetch the event logs. This is applicable only when includeEventLogs is true. (optional)
    run_task_path = 'run_task_path_example' # str | Specifies the task path of the run or object run. This is applicable only if progress of a protection group with one or more object is required.If provided this will be used to fetch progress details directly without looking actual task path of the object. Objects field is stil expected else it changes the response format. (optional)
    object_task_paths = ['object_task_paths_example'] # List[str] | Specifies the object level task path. This relates to the objectID. If provided this will take precedence over the objects, and will be used to fetch progress details directly without looking actuall task path of the object. (optional)

    try:
        # Get the progress of a run.
        api_response = api_instance.get_protection_run_progress(run_id, objects=objects, tenant_ids=tenant_ids, include_tenants=include_tenants, include_finished_tasks=include_finished_tasks, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_tasks_num=max_tasks_num, exclude_object_details=exclude_object_details, include_event_logs=include_event_logs, max_log_level=max_log_level, run_task_path=run_task_path, object_task_paths=object_task_paths)
        print("The response of ProtectionGroupApi->get_protection_run_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_protection_run_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Specifies a unique run id of the Protection Run. | 
 **objects** | [**List[int]**](int.md)| Specifies the objects whose progress will be returned. This only applies to protection group runs and will be ignored for object runs. If the objects are specified, the run progress will not be returned and only the progress of the specified objects will be returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which the run is to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it&#39;s not specified, it is true by default. | [optional] 
 **include_finished_tasks** | **bool**| Specifies whether to return finished tasks. By default only active tasks are returned. | [optional] 
 **start_time_usecs** | **int**| Specifies the time after which the progress task starts in Unix epoch Timestamp(in microseconds). | [optional] 
 **end_time_usecs** | **int**| Specifies the time before which the progress task ends in Unix epoch Timestamp(in microseconds). | [optional] 
 **max_tasks_num** | **int**| Specifies the maximum number of tasks to return. | [optional] 
 **exclude_object_details** | **bool**| Specifies whether to return objects. By default all the task tree are returned. | [optional] 
 **include_event_logs** | **bool**| Specifies whether to include event logs | [optional] 
 **max_log_level** | **int**| Specifies the number of levels till which to fetch the event logs. This is applicable only when includeEventLogs is true. | [optional] 
 **run_task_path** | **str**| Specifies the task path of the run or object run. This is applicable only if progress of a protection group with one or more object is required.If provided this will be used to fetch progress details directly without looking actual task path of the object. Objects field is stil expected else it changes the response format. | [optional] 
 **object_task_paths** | [**List[str]**](str.md)| Specifies the object level task path. This relates to the objectID. If provided this will take precedence over the objects, and will be used to fetch progress details directly without looking actuall task path of the object. | [optional] 

### Return type

[**GetProtectionRunProgressBody**](GetProtectionRunProgressBody.md)

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

# **get_protection_run_stats**
> GetProtectionRunStatsBody get_protection_run_stats(run_id, objects=objects, tenant_ids=tenant_ids, include_tenants=include_tenants, include_finished_tasks=include_finished_tasks, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_tasks_num=max_tasks_num, exclude_object_details=exclude_object_details, run_task_path=run_task_path, object_task_paths=object_task_paths)

Get the stats for a run.

Get the stats for a run.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_protection_run_stats_body import GetProtectionRunStatsBody
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    run_id = 'run_id_example' # str | Specifies a unique run id of the Protection Run.
    objects = [56] # List[int] | Specifies the objects whose stats will be returned. This only applies to protection group runs and will be ignored for object runs. If the objects are specified, the run stats will not be returned and only the stats of the specified objects will be returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which the run is to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it's not specified, it is true by default. (optional)
    include_finished_tasks = True # bool | Specifies whether to return finished tasks. By default only active tasks are returned. (optional)
    start_time_usecs = 56 # int | Specifies the time after which the stats task starts in Unix epoch Timestamp(in microseconds). (optional)
    end_time_usecs = 56 # int | Specifies the time before which the stats task ends in Unix epoch Timestamp(in microseconds). (optional)
    max_tasks_num = 56 # int | Specifies the maximum number of tasks to return. (optional)
    exclude_object_details = True # bool | Specifies whether to return objects. By default all the task tree are returned. (optional)
    run_task_path = 'run_task_path_example' # str | Specifies the task path of the run or object run. This is applicable only if stats of a protection group with one or more object is required. If provided this will be used to fetch stats details directly without looking actual task path of the object. Objects field is stil expected else it changes the response format. (optional)
    object_task_paths = ['object_task_paths_example'] # List[str] | Specifies the object level task path. This relates to the objectID. If provided this will take precedence over the objects, and will be used to fetch stats details directly without looking actuall task path of the object. (optional)

    try:
        # Get the stats for a run.
        api_response = api_instance.get_protection_run_stats(run_id, objects=objects, tenant_ids=tenant_ids, include_tenants=include_tenants, include_finished_tasks=include_finished_tasks, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_tasks_num=max_tasks_num, exclude_object_details=exclude_object_details, run_task_path=run_task_path, object_task_paths=object_task_paths)
        print("The response of ProtectionGroupApi->get_protection_run_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_protection_run_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Specifies a unique run id of the Protection Run. | 
 **objects** | [**List[int]**](int.md)| Specifies the objects whose stats will be returned. This only applies to protection group runs and will be ignored for object runs. If the objects are specified, the run stats will not be returned and only the stats of the specified objects will be returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which the run is to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it&#39;s not specified, it is true by default. | [optional] 
 **include_finished_tasks** | **bool**| Specifies whether to return finished tasks. By default only active tasks are returned. | [optional] 
 **start_time_usecs** | **int**| Specifies the time after which the stats task starts in Unix epoch Timestamp(in microseconds). | [optional] 
 **end_time_usecs** | **int**| Specifies the time before which the stats task ends in Unix epoch Timestamp(in microseconds). | [optional] 
 **max_tasks_num** | **int**| Specifies the maximum number of tasks to return. | [optional] 
 **exclude_object_details** | **bool**| Specifies whether to return objects. By default all the task tree are returned. | [optional] 
 **run_task_path** | **str**| Specifies the task path of the run or object run. This is applicable only if stats of a protection group with one or more object is required. If provided this will be used to fetch stats details directly without looking actual task path of the object. Objects field is stil expected else it changes the response format. | [optional] 
 **object_task_paths** | [**List[str]**](str.md)| Specifies the object level task path. This relates to the objectID. If provided this will take precedence over the objects, and will be used to fetch stats details directly without looking actuall task path of the object. | [optional] 

### Return type

[**GetProtectionRunStatsBody**](GetProtectionRunStatsBody.md)

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

# **get_protection_runs**
> ProtectionRunsSummary get_protection_runs(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)

Get the list of runs.

Get a list of protection runs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.protection_runs_summary import ProtectionRunsSummary
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    start_time_usecs = 56 # int | Start time for time range filter. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be returned. By default it is endTimeUsecs minus an hour. (optional)
    end_time_usecs = 56 # int | End time for time range filter. Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be returned. By default it is current time. (optional)
    run_status = ['run_status_example'] # List[str] | Specifies a list of status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Skipped' indicates that the run was skipped. (optional)

    try:
        # Get the list of runs.
        api_response = api_instance.get_protection_runs(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)
        print("The response of ProtectionGroupApi->get_protection_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_protection_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_usecs** | **int**| Start time for time range filter. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be returned. By default it is endTimeUsecs minus an hour. | [optional] 
 **end_time_usecs** | **int**| End time for time range filter. Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be returned. By default it is current time. | [optional] 
 **run_status** | [**List[str]**](str.md)| Specifies a list of status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

### Return type

[**ProtectionRunsSummary**](ProtectionRunsSummary.md)

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

# **get_run_debug_logs**
> get_run_debug_logs(id, run_id, object_id=object_id)

Get the debug logs for a run from a Protection Group.

Get the debug logs for all objects of a run for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    run_id = 'run_id_example' # str | Specifies a unique run id of the Protection Group run.
    object_id = 'object_id_example' # str | Specifies the id of the object for which debug logs are to be returned.  (optional)

    try:
        # Get the debug logs for a run from a Protection Group.
        api_instance.get_run_debug_logs(id, run_id, object_id=object_id)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_run_debug_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. | 
 **object_id** | **str**| Specifies the id of the object for which debug logs are to be returned.  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_debug_logs_for_object**
> get_run_debug_logs_for_object(id, run_id, object_id)

Get the debug logs for a particular object in a run from a Protection Group.

Get the debug logs for a particular object of a run for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    run_id = 'run_id_example' # str | Specifies a unique run id of the Protection Group run.
    object_id = 'object_id_example' # str | Specifies the id of the object for which debug logs are to be returned. 

    try:
        # Get the debug logs for a particular object in a run from a Protection Group.
        api_instance.get_run_debug_logs_for_object(id, run_id, object_id)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_run_debug_logs_for_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. | 
 **object_id** | **str**| Specifies the id of the object for which debug logs are to be returned.  | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_messages_report**
> get_run_messages_report(id, run_id, object_id, file_type=file_type, name=name)

Get the CSV of various Proto Messages for a given run and an object.

Get an CSV report for given objectId and run id. Each row in CSV report contains the fields from correspoinding proto message.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    run_id = 'run_id_example' # str | Specifies a unique run id of the Protection Group run.
    object_id = 'object_id_example' # str | Specifies the id of the object for which errors/warnings are to be returned. 
    file_type = 'file_type_example' # str | Specifies the downloaded type, i.e: inclusion_exclusion_reports, error_files_list. default: error_files_list (optional)
    name = 'name_example' # str | Specifies the name of the source being backed up (optional)

    try:
        # Get the CSV of various Proto Messages for a given run and an object.
        api_instance.get_run_messages_report(id, run_id, object_id, file_type=file_type, name=name)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_run_messages_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. | 
 **object_id** | **str**| Specifies the id of the object for which errors/warnings are to be returned.  | 
 **file_type** | **str**| Specifies the downloaded type, i.e: inclusion_exclusion_reports, error_files_list. default: error_files_list | [optional] 
 **name** | **str**| Specifies the name of the source being backed up | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runs_report**
> get_runs_report(id, run_id, object_id, file_type=file_type, name=name)

Get the CSV of errors/warnings for a given run and an object.

Get an CSV report for given objectId and run id. Report will depend on the query parameter fileType, default will be: success_files_list where each row contains the name of file backedup successfully.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    run_id = 'run_id_example' # str | Specifies a unique run id of the Protection Group run.
    object_id = 'object_id_example' # str | Specifies the id of the object for which errors/warnings are to be returned. 
    file_type = 'file_type_example' # str | Specifies the downloaded type, i.e: success_files_list, default: success_files_list (optional)
    name = 'name_example' # str | Specifies the name of the source being backed up (optional)

    try:
        # Get the CSV of errors/warnings for a given run and an object.
        api_instance.get_runs_report(id, run_id, object_id, file_type=file_type, name=name)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->get_runs_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. | 
 **object_id** | **str**| Specifies the id of the object for which errors/warnings are to be returned.  | 
 **file_type** | **str**| Specifies the downloaded type, i.e: success_files_list, default: success_files_list | [optional] 
 **name** | **str**| Specifies the name of the source being backed up | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_action_on_protection_group_run**
> PerformRunActionResponse perform_action_on_protection_group_run(id, body)

Actions on protection group run.

Perform various actions on a Protection Group run.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.perform_action_on_protection_group_run_request import PerformActionOnProtectionGroupRunRequest
from cohesity_sdk.cluster.models.perform_run_action_response import PerformRunActionResponse
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    body = cohesity_sdk.cluster.PerformActionOnProtectionGroupRunRequest() # PerformActionOnProtectionGroupRunRequest | Specifies the parameters to perform an action on a protection run.

    try:
        # Actions on protection group run.
        api_response = api_instance.perform_action_on_protection_group_run(id, body)
        print("The response of ProtectionGroupApi->perform_action_on_protection_group_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->perform_action_on_protection_group_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **body** | [**PerformActionOnProtectionGroupRunRequest**](PerformActionOnProtectionGroupRunRequest.md)| Specifies the parameters to perform an action on a protection run. | 

### Return type

[**PerformRunActionResponse**](PerformRunActionResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_protection_group**
> ProtectionGroup update_protection_group(id, body)

Update a Protection Group.

Update the specified Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.cluster.models.protection_group import ProtectionGroup
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies the id of the Protection Group.
    body = cohesity_sdk.cluster.CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to update a Protection Group.

    try:
        # Update a Protection Group.
        api_response = api_instance.update_protection_group(id, body)
        print("The response of ProtectionGroupApi->update_protection_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->update_protection_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Group. | 
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to update a Protection Group. | 

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **update_protection_group_run**
> UpdateProtectionGroupRunResponseBody update_protection_group_run(id, body)

Update runs for a particular Protection Group.

Update runs for a particular Protection Group. A user can perform the following actions: 1. Extend or reduce retention of a local, replication and archival snapshots. 2. Can perform resync operation on failed copy snapshots attempts in this Run. 3. Add new replication and archival snapshot targets to the Run. 4. Add or remove legal hold on the snapshots. Only a user with DSO role can perform this operation. 5. Delete the snapshots that were created as a part of this Run. 6. Apply datalock on existing snapshots where a user cannot manually delete snapshots before the expiry time. 

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.update_protection_group_run_request_body import UpdateProtectionGroupRunRequestBody
from cohesity_sdk.cluster.models.update_protection_group_run_response_body import UpdateProtectionGroupRunResponseBody
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Group.
    body = cohesity_sdk.cluster.UpdateProtectionGroupRunRequestBody() # UpdateProtectionGroupRunRequestBody | Specifies the parameters to update a Protection Group Run.

    try:
        # Update runs for a particular Protection Group.
        api_response = api_instance.update_protection_group_run(id, body)
        print("The response of ProtectionGroupApi->update_protection_group_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->update_protection_group_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. | 
 **body** | [**UpdateProtectionGroupRunRequestBody**](UpdateProtectionGroupRunRequestBody.md)| Specifies the parameters to update a Protection Group Run. | 

### Return type

[**UpdateProtectionGroupRunResponseBody**](UpdateProtectionGroupRunResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_protection_groups_state**
> UpdateProtectionGroupsState update_protection_groups_state(body)

Perform an action like pause, resume, active, deactivate on all specified Protection Groups.

Perform an action like pause, resume, active, deactivate on all specified Protection Groups. Note that the pause or resume actions will take effect from next Protection Run. Also, user can specify only one type of action on all the Protection Groups. Deactivate and activate actions are independent of pause and resume state. Deactivate and activate actions are useful in case of failover situations. Returns success if the state of all the Protection Groups state is changed successfully.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.update_protection_groups_state import UpdateProtectionGroupsState
from cohesity_sdk.cluster.models.update_protection_groups_state_request import UpdateProtectionGroupsStateRequest
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
    api_instance = cohesity_sdk.cluster.ProtectionGroupApi(api_client)
    body = cohesity_sdk.cluster.UpdateProtectionGroupsStateRequest() # UpdateProtectionGroupsStateRequest | Specifies the parameters to perform an action of list of Protection Groups.

    try:
        # Perform an action like pause, resume, active, deactivate on all specified Protection Groups.
        api_response = api_instance.update_protection_groups_state(body)
        print("The response of ProtectionGroupApi->update_protection_groups_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectionGroupApi->update_protection_groups_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProtectionGroupsStateRequest**](UpdateProtectionGroupsStateRequest.md)| Specifies the parameters to perform an action of list of Protection Groups. | 

### Return type

[**UpdateProtectionGroupsState**](UpdateProtectionGroupsState.md)

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

