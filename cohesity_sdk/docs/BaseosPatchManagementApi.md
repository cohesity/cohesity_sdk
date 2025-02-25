# cohesity_sdk.BaseosPatchManagementApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_baseos_patch**](BaseosPatchManagementApi.md#apply_baseos_patch) | **POST** /patch-management/baseos-patch-apply | Applies the given baseos patch.
[**download_baseos_patch**](BaseosPatchManagementApi.md#download_baseos_patch) | **POST** /patch-management/baseos-patch-download | Downloads the given baseos patch.
[**get_baseos_patch_list**](BaseosPatchManagementApi.md#get_baseos_patch_list) | **GET** /patch-management/baseos-patch-list | Get available baseos patches
[**get_baseos_patch_log**](BaseosPatchManagementApi.md#get_baseos_patch_log) | **GET** /patch-management/baseos-patch-log | Get Baseos patch application log
[**remove_baseos_patch**](BaseosPatchManagementApi.md#remove_baseos_patch) | **POST** /patch-management/baseos-patch-remove | Cleans up the given baseos patch files.


# **apply_baseos_patch**
> apply_baseos_patch(body)

Applies the given baseos patch.

Applies the given baseos patch.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.apply_baseos_patch_request import ApplyBaseosPatchRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ApplyBaseosPatchRequest(
        patch_name="patch_name_example",
    ) # ApplyBaseosPatchRequest | Request to apply a baseos patch.

# example passing only required values which don't have defaults set
try:
	# Applies the given baseos patch.
	client.baseos_patch_management.apply_baseos_patch(body)
except ApiException as e:
	print("Exception when calling BaseosPatchManagementApi->apply_baseos_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyBaseosPatchRequest**](ApplyBaseosPatchRequest.md)| Request to apply a baseos patch. |

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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_baseos_patch**
> download_baseos_patch(body)

Downloads the given baseos patch.

Downloads the given baseos patch.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.download_baseos_patch_request import DownloadBaseosPatchRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DownloadBaseosPatchRequest(
        patch_url="patch_url_example",
    ) # DownloadBaseosPatchRequest | Request to download a new baseos patch.

# example passing only required values which don't have defaults set
try:
	# Downloads the given baseos patch.
	client.baseos_patch_management.download_baseos_patch(body)
except ApiException as e:
	print("Exception when calling BaseosPatchManagementApi->download_baseos_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadBaseosPatchRequest**](DownloadBaseosPatchRequest.md)| Request to download a new baseos patch. |

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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baseos_patch_list**
> BaseosPatchList get_baseos_patch_list()

Get available baseos patches

Returns the available baseos patches

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.baseos_patch_list import BaseosPatchList
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
	# Get available baseos patches
	api_response = client.baseos_patch_management.get_baseos_patch_list()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling BaseosPatchManagementApi->get_baseos_patch_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BaseosPatchList**](BaseosPatchList.md)

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

# **get_baseos_patch_log**
> BaseosPatchLog get_baseos_patch_log(patch_name)

Get Baseos patch application log

Returns the log and status of the mentioned patch.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.baseos_patch_log import BaseosPatchLog
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


patch_name = "patchName_example" # str | Name of the hotfix with security patch

# example passing only required values which don't have defaults set
try:
	# Get Baseos patch application log
	api_response = client.baseos_patch_management.get_baseos_patch_log(patch_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling BaseosPatchManagementApi->get_baseos_patch_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_name** | **str**| Name of the hotfix with security patch |

### Return type

[**BaseosPatchLog**](BaseosPatchLog.md)

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

# **remove_baseos_patch**
> remove_baseos_patch(body)

Cleans up the given baseos patch files.

Cleans up the given baseos patch files.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remove_baseos_patch_request import RemoveBaseosPatchRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RemoveBaseosPatchRequest(
        force_remove=True,
        patch_name="patch_name_example",
    ) # RemoveBaseosPatchRequest | Request to remove baseos patch files.

# example passing only required values which don't have defaults set
try:
	# Cleans up the given baseos patch files.
	client.baseos_patch_management.remove_baseos_patch(body)
except ApiException as e:
	print("Exception when calling BaseosPatchManagementApi->remove_baseos_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveBaseosPatchRequest**](RemoveBaseosPatchRequest.md)| Request to remove baseos patch files. |

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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

