# cohesity_sdk.PatchManagementApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_patches**](PatchManagementApi.md#apply_patches) | **POST** /patch-management/available-patches | Apply patches
[**get_applied_patches**](PatchManagementApi.md#get_applied_patches) | **GET** /patch-management/applied-patches | Get applied patches
[**get_available_patches**](PatchManagementApi.md#get_available_patches) | **GET** /patch-management/available-patches | Get available patches
[**get_patch_operation_status**](PatchManagementApi.md#get_patch_operation_status) | **GET** /patch-management/operation-status | Get patch operation status
[**get_patches_history**](PatchManagementApi.md#get_patches_history) | **GET** /patch-management/patches-history | Get patches history
[**import_patches**](PatchManagementApi.md#import_patches) | **PUT** /patch-management/available-patches | Import patches
[**revert_patches**](PatchManagementApi.md#revert_patches) | **POST** /patch-management/applied-patches | Revert patches


# **apply_patches**
> ServicePatchLevels apply_patches(body)

Apply patches

Apply a service patch and its dependencies.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.service_patch_levels import ServicePatchLevels
from cohesity_sdk.cluster.model.apply_patches_request import ApplyPatchesRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = ApplyPatchesRequest(
        all=True,
        service="service_example",
    ) # ApplyPatchesRequest | Request to apply patches.

# example passing only required values which don't have defaults set
try:
	# Apply patches
	api_response = client.patch_management.apply_patches(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PatchManagementApi->apply_patches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyPatchesRequest**](ApplyPatchesRequest.md)| Request to apply patches. |

### Return type

[**ServicePatchLevels**](ServicePatchLevels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applied_patches**
> AppliedPatches get_applied_patches()

Get applied patches

Returns a list of currently applied patches that are running on the cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.applied_patches import AppliedPatches
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

service = "service_example" # str | Specifies optional service name whose current patch is returned. If it is not specified, all the applied patches are returned. (optional)
include_details = True # bool | Specifies whether to return the details of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get applied patches
	api_response = client.patch_management.get_applied_patches(service=service, include_details=include_details)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PatchManagementApi->get_applied_patches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Specifies optional service name whose current patch is returned. If it is not specified, all the applied patches are returned. | [optional]
 **include_details** | **bool**| Specifies whether to return the details of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. | [optional]

### Return type

[**AppliedPatches**](AppliedPatches.md)

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

# **get_available_patches**
> AvailablePatches get_available_patches()

Get available patches

Returns a list of patches that are available and ready to apply on the cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.available_patches import AvailablePatches
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

service = "service_example" # str | Specifies optional service name whose available patch is returned. If it is not specified, available patches for all the serivces are returned. (optional)
include_details = True # bool | Specifies whether to return the description of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get available patches
	api_response = client.patch_management.get_available_patches(service=service, include_details=include_details)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PatchManagementApi->get_available_patches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Specifies optional service name whose available patch is returned. If it is not specified, available patches for all the serivces are returned. | [optional]
 **include_details** | **bool**| Specifies whether to return the description of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. | [optional]

### Return type

[**AvailablePatches**](AvailablePatches.md)

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

# **get_patch_operation_status**
> PatchOperationStatus get_patch_operation_status()

Get patch operation status

Returns the status of the current or the last patch operation. There can be only one active patch operation at any given time.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.patch_operation_status import PatchOperationStatus
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

include_details = True # bool | Specifies whether to return details of all service patch opertions on all nodes. By default, returns whether there is a patch operation in progress or not. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get patch operation status
	api_response = client.patch_management.get_patch_operation_status(include_details=include_details)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PatchManagementApi->get_patch_operation_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_details** | **bool**| Specifies whether to return details of all service patch opertions on all nodes. By default, returns whether there is a patch operation in progress or not. | [optional]

### Return type

[**PatchOperationStatus**](PatchOperationStatus.md)

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

# **get_patches_history**
> PatchesHistory get_patches_history()

Get patches history

Get the history of all the patch management operations.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.patches_history import PatchesHistory
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

service = "service_example" # str | Specifies optional service name whose patch operation history is returned. If it is not specified, patch operations of all the serivces are returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get patches history
	api_response = client.patch_management.get_patches_history(service=service)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PatchManagementApi->get_patches_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Specifies optional service name whose patch operation history is returned. If it is not specified, patch operations of all the serivces are returned. | [optional]

### Return type

[**PatchesHistory**](PatchesHistory.md)

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

# **import_patches**
> PatchesDetails import_patches(file_name, checksum, patch)

Import patches

Import a patch or a hotfix to the cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.patches_details import PatchesDetails
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

file_name = "file_name_example" # str | 
checksum = "checksum_example" # str | 
patch = open('/path/to/file', 'rb') # file_type | 

# example passing only required values which don't have defaults set
try:
	# Import patches
	api_response = client.patch_management.import_patches(file_name, checksum, patch)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PatchManagementApi->import_patches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  |
 **checksum** | **str**|  |
 **patch** | **file_type**|  |

### Return type

[**PatchesDetails**](PatchesDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_patches**
> ServicePatchLevels revert_patches(body)

Revert patches

Revert an applied service patch and its dependencies.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.service_patch_levels import ServicePatchLevels
from cohesity_sdk.cluster.model.revert_patches_request import RevertPatchesRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = RevertPatchesRequest(
        patch_level=1,
        service="service_example",
    ) # RevertPatchesRequest | Request to revert patches.

# example passing only required values which don't have defaults set
try:
	# Revert patches
	api_response = client.patch_management.revert_patches(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PatchManagementApi->revert_patches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevertPatchesRequest**](RevertPatchesRequest.md)| Request to revert patches. |

### Return type

[**ServicePatchLevels**](ServicePatchLevels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

