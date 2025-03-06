# cohesity_sdk.cluster.PatchManagementApi

All URIs are relative to */v2*

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
> List[ServicePatchLevel] apply_patches(body)

Apply patches

Apply a service patch and its dependencies.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.apply_patches_request import ApplyPatchesRequest
from cohesity_sdk.cluster.models.service_patch_level import ServicePatchLevel
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
    api_instance = cohesity_sdk.cluster.PatchManagementApi(api_client)
    body = cohesity_sdk.cluster.ApplyPatchesRequest() # ApplyPatchesRequest | Request to apply patches.

    try:
        # Apply patches
        api_response = api_instance.apply_patches(body)
        print("The response of PatchManagementApi->apply_patches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchManagementApi->apply_patches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyPatchesRequest**](ApplyPatchesRequest.md)| Request to apply patches. | 

### Return type

[**List[ServicePatchLevel]**](ServicePatchLevel.md)

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

# **get_applied_patches**
> List[AppliedPatch] get_applied_patches(service=service, include_details=include_details)

Get applied patches

Returns a list of currently applied patches that are running on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.applied_patch import AppliedPatch
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
    api_instance = cohesity_sdk.cluster.PatchManagementApi(api_client)
    service = 'service_example' # str | Specifies optional service name whose current patch is returned. If it is not specified, all the applied patches are returned. (optional)
    include_details = True # bool | Specifies whether to return the details of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. (optional)

    try:
        # Get applied patches
        api_response = api_instance.get_applied_patches(service=service, include_details=include_details)
        print("The response of PatchManagementApi->get_applied_patches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchManagementApi->get_applied_patches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Specifies optional service name whose current patch is returned. If it is not specified, all the applied patches are returned. | [optional] 
 **include_details** | **bool**| Specifies whether to return the details of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. | [optional] 

### Return type

[**List[AppliedPatch]**](AppliedPatch.md)

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

# **get_available_patches**
> List[AvailablePatch] get_available_patches(service=service, include_details=include_details)

Get available patches

Returns a list of patches that are available and ready to apply on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.available_patch import AvailablePatch
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
    api_instance = cohesity_sdk.cluster.PatchManagementApi(api_client)
    service = 'service_example' # str | Specifies optional service name whose available patch is returned. If it is not specified, available patches for all the serivces are returned. (optional)
    include_details = True # bool | Specifies whether to return the description of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. (optional)

    try:
        # Get available patches
        api_response = api_instance.get_available_patches(service=service, include_details=include_details)
        print("The response of PatchManagementApi->get_available_patches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchManagementApi->get_available_patches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Specifies optional service name whose available patch is returned. If it is not specified, available patches for all the serivces are returned. | [optional] 
 **include_details** | **bool**| Specifies whether to return the description of all the fixes in the patch. By default, returns only the most recent fix made for the service in the patch. | [optional] 

### Return type

[**List[AvailablePatch]**](AvailablePatch.md)

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

# **get_patch_operation_status**
> PatchOperationStatus get_patch_operation_status(include_details=include_details)

Get patch operation status

Returns the status of the current or the last patch operation. There can be only one active patch operation at any given time.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.patch_operation_status import PatchOperationStatus
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
    api_instance = cohesity_sdk.cluster.PatchManagementApi(api_client)
    include_details = True # bool | Specifies whether to return details of all service patch opertions on all nodes. By default, returns whether there is a patch operation in progress or not. (optional)

    try:
        # Get patch operation status
        api_response = api_instance.get_patch_operation_status(include_details=include_details)
        print("The response of PatchManagementApi->get_patch_operation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchManagementApi->get_patch_operation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_details** | **bool**| Specifies whether to return details of all service patch opertions on all nodes. By default, returns whether there is a patch operation in progress or not. | [optional] 

### Return type

[**PatchOperationStatus**](PatchOperationStatus.md)

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

# **get_patches_history**
> List[PatchOperation] get_patches_history(service=service)

Get patches history

Get the history of all the patch management operations.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.patch_operation import PatchOperation
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
    api_instance = cohesity_sdk.cluster.PatchManagementApi(api_client)
    service = 'service_example' # str | Specifies optional service name whose patch operation history is returned. If it is not specified, patch operations of all the serivces are returned. (optional)

    try:
        # Get patches history
        api_response = api_instance.get_patches_history(service=service)
        print("The response of PatchManagementApi->get_patches_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchManagementApi->get_patches_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Specifies optional service name whose patch operation history is returned. If it is not specified, patch operations of all the serivces are returned. | [optional] 

### Return type

[**List[PatchOperation]**](PatchOperation.md)

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

# **import_patches**
> List[PatchDetail] import_patches(file_name, checksum, patch)

Import patches

Import a patch or a hotfix to the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.patch_detail import PatchDetail
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
    api_instance = cohesity_sdk.cluster.PatchManagementApi(api_client)
    file_name = 'file_name_example' # str | 
    checksum = 'checksum_example' # str | 
    patch = None # bytearray | 

    try:
        # Import patches
        api_response = api_instance.import_patches(file_name, checksum, patch)
        print("The response of PatchManagementApi->import_patches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchManagementApi->import_patches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **checksum** | **str**|  | 
 **patch** | **bytearray**|  | 

### Return type

[**List[PatchDetail]**](PatchDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> List[ServicePatchLevel] revert_patches(body)

Revert patches

Revert an applied service patch and its dependencies.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.revert_patches_request import RevertPatchesRequest
from cohesity_sdk.cluster.models.service_patch_level import ServicePatchLevel
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
    api_instance = cohesity_sdk.cluster.PatchManagementApi(api_client)
    body = cohesity_sdk.cluster.RevertPatchesRequest() # RevertPatchesRequest | Request to revert patches.

    try:
        # Revert patches
        api_response = api_instance.revert_patches(body)
        print("The response of PatchManagementApi->revert_patches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatchManagementApi->revert_patches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevertPatchesRequest**](RevertPatchesRequest.md)| Request to revert patches. | 

### Return type

[**List[ServicePatchLevel]**](ServicePatchLevel.md)

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

