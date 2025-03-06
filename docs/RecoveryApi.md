# cohesity_sdk.cluster.RecoveryApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_recovery_by_id**](RecoveryApi.md#cancel_recovery_by_id) | **POST** /data-protect/recoveries/{id}/cancel | Cancel Recovery for a given id.
[**create_download_files_and_folders_recovery**](RecoveryApi.md#create_download_files_and_folders_recovery) | **POST** /data-protect/recoveries/download-files-folders | Create a download files and folders recovery.
[**create_recovery**](RecoveryApi.md#create_recovery) | **POST** /data-protect/recoveries | Performs a Recovery.
[**download_files_from_recovery**](RecoveryApi.md#download_files_from_recovery) | **GET** /data-protect/recoveries/{id}/download-files | Download files from the given download file recovery.
[**download_indexed_file**](RecoveryApi.md#download_indexed_file) | **GET** /data-protect/snapshots/{snapshotsId}/download-file | Download an indexed file.
[**fetch_uptier_data**](RecoveryApi.md#fetch_uptier_data) | **GET** /data-protect/recoveries/fetch-uptier-data | Fetches the uptier data.
[**get_recoveries**](RecoveryApi.md#get_recoveries) | **GET** /data-protect/recoveries | Lists the Recoveries.
[**get_recovery_by_id**](RecoveryApi.md#get_recovery_by_id) | **GET** /data-protect/recoveries/{id} | Get Recovery for a given id.
[**get_recovery_debug_logs**](RecoveryApi.md#get_recovery_debug_logs) | **GET** /data-protect/recoveries/{id}/debug-logs | Get the debug logs for a particular recovery operation.
[**get_recovery_errors_report**](RecoveryApi.md#get_recovery_errors_report) | **GET** /data-protect/recoveries/{id}/download-messages | Get the CSV of errors/warnings for a given recovery operation.
[**tear_down_recovery_by_id**](RecoveryApi.md#tear_down_recovery_by_id) | **POST** /data-protect/recoveries/{id}/tear-down | Tear down Recovery for a given id.


# **cancel_recovery_by_id**
> cancel_recovery_by_id(id)

Cancel Recovery for a given id.

Cancel Recovery for a given id.

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    id = 'id_example' # str | Specifies the id of a Recovery.

    try:
        # Cancel Recovery for a given id.
        api_instance.cancel_recovery_by_id(id)
    except Exception as e:
        print("Exception when calling RecoveryApi->cancel_recovery_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_download_files_and_folders_recovery**
> Recovery create_download_files_and_folders_recovery(body)

Create a download files and folders recovery.

Creates a download files and folders recovery.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.download_files_and_folders_request_params import DownloadFilesAndFoldersRequestParams
from cohesity_sdk.cluster.models.recovery import Recovery
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    body = cohesity_sdk.cluster.DownloadFilesAndFoldersRequestParams() # DownloadFilesAndFoldersRequestParams | Specifies the parameters to create a download files and folder recovery.

    try:
        # Create a download files and folders recovery.
        api_response = api_instance.create_download_files_and_folders_recovery(body)
        print("The response of RecoveryApi->create_download_files_and_folders_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveryApi->create_download_files_and_folders_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadFilesAndFoldersRequestParams**](DownloadFilesAndFoldersRequestParams.md)| Specifies the parameters to create a download files and folder recovery. | 

### Return type

[**Recovery**](Recovery.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recovery**
> Recovery create_recovery(body, request_initiator_type=request_initiator_type)

Performs a Recovery.

Performs a Recovery.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_recovery_request import CreateRecoveryRequest
from cohesity_sdk.cluster.models.recovery import Recovery
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    body = cohesity_sdk.cluster.CreateRecoveryRequest() # CreateRecoveryRequest | Specifies the parameters to create a Recovery.
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    try:
        # Performs a Recovery.
        api_response = api_instance.create_recovery(body, request_initiator_type=request_initiator_type)
        print("The response of RecoveryApi->create_recovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveryApi->create_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRecoveryRequest**](CreateRecoveryRequest.md)| Specifies the parameters to create a Recovery. | 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 

### Return type

[**Recovery**](Recovery.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_files_from_recovery**
> download_files_from_recovery(id, start_offset=start_offset, length=length, file_type=file_type, source_name=source_name, start_time=start_time, include_tenants=include_tenants)

Download files from the given download file recovery.

Download files from the given download file recovery.

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    id = 'id_example' # str | Specifies the id of a Recovery.
    start_offset = 56 # int | Specifies the start offset of file chunk to be downloaded. (optional)
    length = 56 # int | Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) (optional)
    file_type = 'file_type_example' # str | Specifies the downloaded type, i.e: error, success_files_list (optional)
    source_name = 'source_name_example' # str | Specifies the name of the source on which restore is done (optional)
    start_time = 'start_time_example' # str | Specifies the start time of restore task (optional)
    include_tenants = True # bool | Specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)

    try:
        # Download files from the given download file recovery.
        api_instance.download_files_from_recovery(id, start_offset=start_offset, length=length, file_type=file_type, source_name=source_name, start_time=start_time, include_tenants=include_tenants)
    except Exception as e:
        print("Exception when calling RecoveryApi->download_files_from_recovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. | 
 **start_offset** | **int**| Specifies the start offset of file chunk to be downloaded. | [optional] 
 **length** | **int**| Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) | [optional] 
 **file_type** | **str**| Specifies the downloaded type, i.e: error, success_files_list | [optional] 
 **source_name** | **str**| Specifies the name of the source on which restore is done | [optional] 
 **start_time** | **str**| Specifies the start time of restore task | [optional] 
 **include_tenants** | **bool**| Specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_indexed_file**
> download_indexed_file(snapshots_id, file_path=file_path, nvram_file=nvram_file, retry_attempt=retry_attempt, start_offset=start_offset, length=length)

Download an indexed file.

Download an indexed file from a snapshot.

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    snapshots_id = 'snapshots_id_example' # str | Specifies the snapshot id to download from.
    file_path = 'file_path_example' # str | Specifies the path to the file to download. If no path is specified and snapshot environment is kVMWare, VMX file for VMware will be downloaded. For other snapshot environments, this field must be specified. (optional)
    nvram_file = True # bool | Specifies if NVRAM file for VMware should be downloaded. (optional)
    retry_attempt = 56 # int | Specifies the number of attempts the protection run took to create this file. (optional)
    start_offset = 56 # int | Specifies the start offset of file chunk to be downloaded. (optional)
    length = 56 # int | Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) (optional)

    try:
        # Download an indexed file.
        api_instance.download_indexed_file(snapshots_id, file_path=file_path, nvram_file=nvram_file, retry_attempt=retry_attempt, start_offset=start_offset, length=length)
    except Exception as e:
        print("Exception when calling RecoveryApi->download_indexed_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshots_id** | **str**| Specifies the snapshot id to download from. | 
 **file_path** | **str**| Specifies the path to the file to download. If no path is specified and snapshot environment is kVMWare, VMX file for VMware will be downloaded. For other snapshot environments, this field must be specified. | [optional] 
 **nvram_file** | **bool**| Specifies if NVRAM file for VMware should be downloaded. | [optional] 
 **retry_attempt** | **int**| Specifies the number of attempts the protection run took to create this file. | [optional] 
 **start_offset** | **int**| Specifies the start offset of file chunk to be downloaded. | [optional] 
 **length** | **int**| Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_uptier_data**
> FetchUptierDataResponse fetch_uptier_data(archive_uid)

Fetches the uptier data.

Fetches the uptier data for a restore job.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.fetch_uptier_data_response import FetchUptierDataResponse
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    archive_uid = 'archive_uid_example' # str | Archive UID of the current restore.

    try:
        # Fetches the uptier data.
        api_response = api_instance.fetch_uptier_data(archive_uid)
        print("The response of RecoveryApi->fetch_uptier_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveryApi->fetch_uptier_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_uid** | **str**| Archive UID of the current restore. | 

### Return type

[**FetchUptierDataResponse**](FetchUptierDataResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recoveries**
> Recoveries get_recoveries(ids=ids, return_only_child_recoveries=return_only_child_recoveries, tenant_ids=tenant_ids, include_tenants=include_tenants, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, storage_domain_id=storage_domain_id, snapshot_target_type=snapshot_target_type, archival_target_type=archival_target_type, snapshot_environments=snapshot_environments, status=status, recovery_actions=recovery_actions)

Lists the Recoveries.

Lists the Recoveries.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.recoveries import Recoveries
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    ids = ['ids_example'] # List[str] | Filter Recoveries for given ids. (optional)
    return_only_child_recoveries = True # bool | Returns only child recoveries if passed as true. This filter should always be used along with 'ids' filter.  (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the organizations for which recoveries are to be returned. (optional)
    include_tenants = True # bool | Specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)
    start_time_usecs = 56 # int | Returns the recoveries which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
    end_time_usecs = 56 # int | Returns the recoveries which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
    storage_domain_id = 56 # int | Filter by Storage Domain id. Only recoveries writing data to this Storage Domain will be returned. (optional)
    snapshot_target_type = ['snapshot_target_type_example'] # List[str] | Specifies the snapshot's target type from which recovery has been performed. (optional)
    archival_target_type = ['archival_target_type_example'] # List[str] | Specifies the snapshot's archival target type from which recovery has been performed. This parameter applies only if 'snapshotTargetType' is 'Archival'. (optional)
    snapshot_environments = ['snapshot_environments_example'] # List[str] | Specifies the list of snapshot environment types to filter Recoveries. If empty, Recoveries related to all environments will be returned. (optional)
    status = ['status_example'] # List[str] | Specifies the list of run status to filter Recoveries. If empty, Recoveries with all run status will be returned. (optional)
    recovery_actions = ['recovery_actions_example'] # List[str] | Specifies the list of recovery actions to filter Recoveries. If empty, Recoveries related to all actions will be returned. (optional)

    try:
        # Lists the Recoveries.
        api_response = api_instance.get_recoveries(ids=ids, return_only_child_recoveries=return_only_child_recoveries, tenant_ids=tenant_ids, include_tenants=include_tenants, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, storage_domain_id=storage_domain_id, snapshot_target_type=snapshot_target_type, archival_target_type=archival_target_type, snapshot_environments=snapshot_environments, status=status, recovery_actions=recovery_actions)
        print("The response of RecoveryApi->get_recoveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveryApi->get_recoveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| Filter Recoveries for given ids. | [optional] 
 **return_only_child_recoveries** | **bool**| Returns only child recoveries if passed as true. This filter should always be used along with &#39;ids&#39; filter.  | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the organizations for which recoveries are to be returned. | [optional] 
 **include_tenants** | **bool**| Specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 
 **start_time_usecs** | **int**| Returns the recoveries which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional] 
 **end_time_usecs** | **int**| Returns the recoveries which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional] 
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only recoveries writing data to this Storage Domain will be returned. | [optional] 
 **snapshot_target_type** | [**List[str]**](str.md)| Specifies the snapshot&#39;s target type from which recovery has been performed. | [optional] 
 **archival_target_type** | [**List[str]**](str.md)| Specifies the snapshot&#39;s archival target type from which recovery has been performed. This parameter applies only if &#39;snapshotTargetType&#39; is &#39;Archival&#39;. | [optional] 
 **snapshot_environments** | [**List[str]**](str.md)| Specifies the list of snapshot environment types to filter Recoveries. If empty, Recoveries related to all environments will be returned. | [optional] 
 **status** | [**List[str]**](str.md)| Specifies the list of run status to filter Recoveries. If empty, Recoveries with all run status will be returned. | [optional] 
 **recovery_actions** | [**List[str]**](str.md)| Specifies the list of recovery actions to filter Recoveries. If empty, Recoveries related to all actions will be returned. | [optional] 

### Return type

[**Recoveries**](Recoveries.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_by_id**
> Recovery get_recovery_by_id(id, include_tenants=include_tenants)

Get Recovery for a given id.

Get Recovery for a given id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.recovery import Recovery
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    id = 'id_example' # str | Specifies the id of a Recovery.
    include_tenants = True # bool | Specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)

    try:
        # Get Recovery for a given id.
        api_response = api_instance.get_recovery_by_id(id, include_tenants=include_tenants)
        print("The response of RecoveryApi->get_recovery_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecoveryApi->get_recovery_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. | 
 **include_tenants** | **bool**| Specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 

### Return type

[**Recovery**](Recovery.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_debug_logs**
> get_recovery_debug_logs(id)

Get the debug logs for a particular recovery operation.

Get the debug logs for a particular recovery operation.

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    id = 'id_example' # str | Specifies the id of a Recovery job.

    try:
        # Get the debug logs for a particular recovery operation.
        api_instance.get_recovery_debug_logs(id)
    except Exception as e:
        print("Exception when calling RecoveryApi->get_recovery_debug_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery job. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_errors_report**
> get_recovery_errors_report(id)

Get the CSV of errors/warnings for a given recovery operation.

Get a CSV error report for given recovery operation. Each row in CSV report contains the File Path, error/warning code and error/warning message.

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    id = 'id_example' # str | Specifies a unique ID of a Recovery.

    try:
        # Get the CSV of errors/warnings for a given recovery operation.
        api_instance.get_recovery_errors_report(id)
    except Exception as e:
        print("Exception when calling RecoveryApi->get_recovery_errors_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique ID of a Recovery. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tear_down_recovery_by_id**
> tear_down_recovery_by_id(id)

Tear down Recovery for a given id.

Tear down Recovery for a given id.

### Example

* Api Key Authentication (APIKeyHeader):
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.RecoveryApi(api_client)
    id = 'id_example' # str | Specifies the id of a Recovery.

    try:
        # Tear down Recovery for a given id.
        api_instance.tear_down_recovery_by_id(id)
    except Exception as e:
        print("Exception when calling RecoveryApi->tear_down_recovery_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

