# cohesity_sdk.RecoveryApi


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
[**internal_api_create_download_files_and_folders_recovery**](RecoveryApi.md#internal_api_create_download_files_and_folders_recovery) | **POST** /data-protect/recoveries/downloadFilesAndFoldersRecovery | Create a download files and folders recovery.
[**internal_api_download_files_from_recovery**](RecoveryApi.md#internal_api_download_files_from_recovery) | **GET** /data-protect/recoveries/{id}/downloadFiles | Download files from the given download file recovery.
[**internal_api_download_indexed_file**](RecoveryApi.md#internal_api_download_indexed_file) | **GET** /data-protect/snapshots/{snapshotsId}/downloadFile | Download an indexed file.
[**tear_down_recovery_by_id**](RecoveryApi.md#tear_down_recovery_by_id) | **POST** /data-protect/recoveries/{id}/tear-down | Tear down Recovery for a given id.


# **cancel_recovery_by_id**
> cancel_recovery_by_id(id)

Cancel Recovery for a given id.

Cancel Recovery for a given id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of a Recovery.

# example passing only required values which don't have defaults set
try:
	# Cancel Recovery for a given id.
	client.recovery.cancel_recovery_by_id(id)
except ApiException as e:
	print("Exception when calling RecoveryApi->cancel_recovery_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.recovery import Recovery
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.download_files_and_folders_request_params import DownloadFilesAndFoldersRequestParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DownloadFilesAndFoldersRequestParams(
        name="name_example",
        object=CommonRecoverObjectSnapshotParams(
            snapshot_id="snapshot_id_example",
            point_in_time_usecs=1,
            protection_group_id="protection_group_id_example",
            protection_group_name="protection_group_name_example",
            object_info={},
            archival_target_info={},
            recover_from_standby=True,
        ),
        parent_recovery_id="4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026",
        files_and_folders=[
            FilesAndFoldersObject(
                absolute_path="absolute_path_example",
                is_directory=True,
            ),
        ],
        glacier_retrieval_type="kStandard",
    ) # DownloadFilesAndFoldersRequestParams | Specifies the parameters to create a download files and folder recovery.

# example passing only required values which don't have defaults set
try:
	# Create a download files and folders recovery.
	api_response = client.recovery.create_download_files_and_folders_recovery(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RecoveryApi->create_download_files_and_folders_recovery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadFilesAndFoldersRequestParams**](DownloadFilesAndFoldersRequestParams.md)| Specifies the parameters to create a download files and folder recovery. |

### Return type

[**Recovery**](Recovery.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
> Recovery create_recovery(body)

Performs a Recovery.

Performs a Recovery.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.recovery import Recovery
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_recovery_request import CreateRecoveryRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateRecoveryRequest() # CreateRecoveryRequest | Specifies the parameters to create a Recovery.
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

# example passing only required values which don't have defaults set
try:
	# Performs a Recovery.
	api_response = client.recovery.create_recovery(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RecoveryApi->create_recovery: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Performs a Recovery.
	api_response = client.recovery.create_recovery(body, request_initiator_type=request_initiator_type)
	pprint(api_response)
except ApiException as e:
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

[APIKeyHeader](../README.md#APIKeyHeader)

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
> download_files_from_recovery(id)

Download files from the given download file recovery.

Download files from the given download file recovery.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of a Recovery.
start_offset = 1 # int | Specifies the start offset of file chunk to be downloaded. (optional)
length = 1 # int | Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) (optional)
file_type = "fileType_example" # str | Specifies the downloaded type, i.e: error, success_files_list (optional)

# example passing only required values which don't have defaults set
try:
	# Download files from the given download file recovery.
	client.recovery.download_files_from_recovery(id)
except ApiException as e:
	print("Exception when calling RecoveryApi->download_files_from_recovery: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Download files from the given download file recovery.
	client.recovery.download_files_from_recovery(id, start_offset=start_offset, length=length, file_type=file_type)
except ApiException as e:
	print("Exception when calling RecoveryApi->download_files_from_recovery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. |
 **start_offset** | **int**| Specifies the start offset of file chunk to be downloaded. | [optional]
 **length** | **int**| Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) | [optional]
 **file_type** | **str**| Specifies the downloaded type, i.e: error, success_files_list | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
> download_indexed_file(snapshots_id)

Download an indexed file.

Download an indexed file from a snapshot.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


snapshots_id = "snapshotsId_example" # str | Specifies the snapshot id to download from.
file_path = "filePath_example" # str | Specifies the path to the file to download. If no path is specified and snapshot environment is kVMWare, VMX file for VMware will be downloaded. For other snapshot environments, this field must be specified. (optional)
retry_attempt = 1 # int | Specifies the number of attempts the protection run took to create this file. (optional)
start_offset = 1 # int | Specifies the start offset of file chunk to be downloaded. (optional)
length = 1 # int | Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) (optional)

# example passing only required values which don't have defaults set
try:
	# Download an indexed file.
	client.recovery.download_indexed_file(snapshots_id)
except ApiException as e:
	print("Exception when calling RecoveryApi->download_indexed_file: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Download an indexed file.
	client.recovery.download_indexed_file(snapshots_id, file_path=file_path, retry_attempt=retry_attempt, start_offset=start_offset, length=length)
except ApiException as e:
	print("Exception when calling RecoveryApi->download_indexed_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshots_id** | **str**| Specifies the snapshot id to download from. |
 **file_path** | **str**| Specifies the path to the file to download. If no path is specified and snapshot environment is kVMWare, VMX file for VMware will be downloaded. For other snapshot environments, this field must be specified. | [optional]
 **retry_attempt** | **int**| Specifies the number of attempts the protection run took to create this file. | [optional]
 **start_offset** | **int**| Specifies the start offset of file chunk to be downloaded. | [optional]
 **length** | **int**| Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.fetch_uptier_data_response import FetchUptierDataResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


archive_uid = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Archive UID of the current restore.

# example passing only required values which don't have defaults set
try:
	# Fetches the uptier data.
	api_response = client.recovery.fetch_uptier_data(archive_uid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RecoveryApi->fetch_uptier_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_uid** | **str**| Archive UID of the current restore. |

### Return type

[**FetchUptierDataResponse**](FetchUptierDataResponse.md)

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

# **get_recoveries**
> Recoveries get_recoveries()

Lists the Recoveries.

Lists the Recoveries.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.recoveries import Recoveries
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026",
    ] # [str] | Filter Recoveries for given ids. (optional)
return_only_child_recoveries = True # bool | Returns only child recoveries if passed as true. This filter should always be used along with 'ids' filter.  (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the organizations for which recoveries are to be returned. (optional)
include_tenants = True # bool | Specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)
start_time_usecs = 1 # int | Returns the recoveries which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
end_time_usecs = 1 # int | Returns the recoveries which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
storage_domain_id = 1 # int | Filter by Storage Domain id. Only recoveries writing data to this Storage Domain will be returned. (optional)
snapshot_target_type = [
        "Local",
    ] # [str] | Specifies the snapshot's target type from which recovery has been performed. (optional)
archival_target_type = [
        "Tape",
    ] # [str] | Specifies the snapshot's archival target type from which recovery has been performed. This parameter applies only if 'snapshotTargetType' is 'Archival'. (optional)
snapshot_environments = [
        "kVMware",
    ] # [str] | Specifies the list of snapshot environment types to filter Recoveries. If empty, Recoveries related to all environments will be returned. (optional)
status = [
        "Accepted",
    ] # [str] | Specifies the list of run status to filter Recoveries. If empty, Recoveries with all run status will be returned. (optional)
recovery_actions = [
        "RecoverVMs",
    ] # [str] | Specifies the list of recovery actions to filter Recoveries. If empty, Recoveries related to all actions will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Lists the Recoveries.
	api_response = client.recovery.get_recoveries(ids=ids, return_only_child_recoveries=return_only_child_recoveries, tenant_ids=tenant_ids, include_tenants=include_tenants, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, storage_domain_id=storage_domain_id, snapshot_target_type=snapshot_target_type, archival_target_type=archival_target_type, snapshot_environments=snapshot_environments, status=status, recovery_actions=recovery_actions)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RecoveryApi->get_recoveries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Filter Recoveries for given ids. | [optional]
 **return_only_child_recoveries** | **bool**| Returns only child recoveries if passed as true. This filter should always be used along with &#39;ids&#39; filter.  | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the organizations for which recoveries are to be returned. | [optional]
 **include_tenants** | **bool**| Specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **start_time_usecs** | **int**| Returns the recoveries which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional]
 **end_time_usecs** | **int**| Returns the recoveries which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional]
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only recoveries writing data to this Storage Domain will be returned. | [optional]
 **snapshot_target_type** | **[str]**| Specifies the snapshot&#39;s target type from which recovery has been performed. | [optional]
 **archival_target_type** | **[str]**| Specifies the snapshot&#39;s archival target type from which recovery has been performed. This parameter applies only if &#39;snapshotTargetType&#39; is &#39;Archival&#39;. | [optional]
 **snapshot_environments** | **[str]**| Specifies the list of snapshot environment types to filter Recoveries. If empty, Recoveries related to all environments will be returned. | [optional]
 **status** | **[str]**| Specifies the list of run status to filter Recoveries. If empty, Recoveries with all run status will be returned. | [optional]
 **recovery_actions** | **[str]**| Specifies the list of recovery actions to filter Recoveries. If empty, Recoveries related to all actions will be returned. | [optional]

### Return type

[**Recoveries**](Recoveries.md)

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

# **get_recovery_by_id**
> Recovery get_recovery_by_id(id)

Get Recovery for a given id.

Get Recovery for a given id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.recovery import Recovery
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of a Recovery.
include_tenants = True # bool | Specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# Get Recovery for a given id.
	api_response = client.recovery.get_recovery_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RecoveryApi->get_recovery_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Recovery for a given id.
	api_response = client.recovery.get_recovery_by_id(id, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
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

# **get_recovery_debug_logs**
> get_recovery_debug_logs(id)

Get the debug logs for a particular recovery operation.

Get the debug logs for a particular recovery operation.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of a Recovery job.

# example passing only required values which don't have defaults set
try:
	# Get the debug logs for a particular recovery operation.
	client.recovery.get_recovery_debug_logs(id)
except ApiException as e:
	print("Exception when calling RecoveryApi->get_recovery_debug_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery job. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique ID of a Recovery.

# example passing only required values which don't have defaults set
try:
	# Get the CSV of errors/warnings for a given recovery operation.
	client.recovery.get_recovery_errors_report(id)
except ApiException as e:
	print("Exception when calling RecoveryApi->get_recovery_errors_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique ID of a Recovery. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_api_create_download_files_and_folders_recovery**
> Recovery internal_api_create_download_files_and_folders_recovery(body)

Create a download files and folders recovery.

Creates a download files and folders recovery.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.recovery import Recovery
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.download_files_and_folders_request_params import DownloadFilesAndFoldersRequestParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DownloadFilesAndFoldersRequestParams(
        name="name_example",
        object=CommonRecoverObjectSnapshotParams(
            snapshot_id="snapshot_id_example",
            point_in_time_usecs=1,
            protection_group_id="protection_group_id_example",
            protection_group_name="protection_group_name_example",
            object_info={},
            archival_target_info={},
            recover_from_standby=True,
        ),
        parent_recovery_id="4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026",
        files_and_folders=[
            FilesAndFoldersObject(
                absolute_path="absolute_path_example",
                is_directory=True,
            ),
        ],
        glacier_retrieval_type="kStandard",
    ) # DownloadFilesAndFoldersRequestParams | Specifies the parameters to create a download files and folder recovery.

# example passing only required values which don't have defaults set
try:
	# Create a download files and folders recovery.
	api_response = client.recovery.internal_api_create_download_files_and_folders_recovery(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RecoveryApi->internal_api_create_download_files_and_folders_recovery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadFilesAndFoldersRequestParams**](DownloadFilesAndFoldersRequestParams.md)| Specifies the parameters to create a download files and folder recovery. |

### Return type

[**Recovery**](Recovery.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_api_download_files_from_recovery**
> internal_api_download_files_from_recovery(id)

Download files from the given download file recovery.

Download files from the given download file recovery.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of a Recovery.
start_offset = 1 # int | Specifies the start offset of file chunk to be downloaded. (optional)
length = 1 # int | Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) (optional)

# example passing only required values which don't have defaults set
try:
	# Download files from the given download file recovery.
	client.recovery.internal_api_download_files_from_recovery(id)
except ApiException as e:
	print("Exception when calling RecoveryApi->internal_api_download_files_from_recovery: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Download files from the given download file recovery.
	client.recovery.internal_api_download_files_from_recovery(id, start_offset=start_offset, length=length)
except ApiException as e:
	print("Exception when calling RecoveryApi->internal_api_download_files_from_recovery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. |
 **start_offset** | **int**| Specifies the start offset of file chunk to be downloaded. | [optional]
 **length** | **int**| Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_api_download_indexed_file**
> internal_api_download_indexed_file(snapshots_id)

Download an indexed file.

Download an indexed file from a snapshot.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


snapshots_id = "snapshotsId_example" # str | Specifies the snapshot id to download from.
file_path = "filePath_example" # str | Specifies the path to the file to download. If no path is specified and snapshot environment is kVMWare, VMX file for VMware will be downloaded. For other snapshot environments, this field must be specified. (optional)
retry_attempt = 1 # int | Specifies the number of attempts the protection run took to create this file. (optional)
start_offset = 1 # int | Specifies the start offset of file chunk to be downloaded. (optional)
length = 1 # int | Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) (optional)

# example passing only required values which don't have defaults set
try:
	# Download an indexed file.
	client.recovery.internal_api_download_indexed_file(snapshots_id)
except ApiException as e:
	print("Exception when calling RecoveryApi->internal_api_download_indexed_file: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Download an indexed file.
	client.recovery.internal_api_download_indexed_file(snapshots_id, file_path=file_path, retry_attempt=retry_attempt, start_offset=start_offset, length=length)
except ApiException as e:
	print("Exception when calling RecoveryApi->internal_api_download_indexed_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshots_id** | **str**| Specifies the snapshot id to download from. |
 **file_path** | **str**| Specifies the path to the file to download. If no path is specified and snapshot environment is kVMWare, VMX file for VMware will be downloaded. For other snapshot environments, this field must be specified. | [optional]
 **retry_attempt** | **int**| Specifies the number of attempts the protection run took to create this file. | [optional]
 **start_offset** | **int**| Specifies the start offset of file chunk to be downloaded. | [optional]
 **length** | **int**| Specifies the length of bytes to download. This can not be greater than 8MB (8388608 byets) | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of a Recovery.

# example passing only required values which don't have defaults set
try:
	# Tear down Recovery for a given id.
	client.recovery.tear_down_recovery_by_id(id)
except ApiException as e:
	print("Exception when calling RecoveryApi->tear_down_recovery_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of a Recovery. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

