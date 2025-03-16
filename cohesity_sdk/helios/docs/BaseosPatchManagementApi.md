# cohesity_sdk.helios.BaseosPatchManagementApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_baseos_patch**](BaseosPatchManagementApi.md#apply_baseos_patch) | **POST** /patch-management/baseos-patch-apply | Applies the given baseos patch.
[**download_baseos_patch**](BaseosPatchManagementApi.md#download_baseos_patch) | **POST** /patch-management/baseos-patch-download | Downloads the given baseos patch.
[**get_baseos_patch_list**](BaseosPatchManagementApi.md#get_baseos_patch_list) | **GET** /patch-management/baseos-patch-list | Get available baseos patches
[**get_baseos_patch_log**](BaseosPatchManagementApi.md#get_baseos_patch_log) | **GET** /patch-management/baseos-patch-log | Get Baseos patch application log
[**remove_baseos_patch**](BaseosPatchManagementApi.md#remove_baseos_patch) | **POST** /patch-management/baseos-patch-remove | Cleans up the given baseos patch files.


# **apply_baseos_patch**
> apply_baseos_patch(body, access_cluster_id=access_cluster_id, region_id=region_id)

Applies the given baseos patch.

Applies the given baseos patch.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.apply_baseos_patch_request import ApplyBaseosPatchRequest
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
    api_instance = cohesity_sdk.helios.BaseosPatchManagementApi(api_client)
    body = cohesity_sdk.helios.ApplyBaseosPatchRequest() # ApplyBaseosPatchRequest | Request to apply a baseos patch.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Applies the given baseos patch.
        api_instance.apply_baseos_patch(body, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling BaseosPatchManagementApi->apply_baseos_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyBaseosPatchRequest**](ApplyBaseosPatchRequest.md)| Request to apply a baseos patch. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_baseos_patch**
> download_baseos_patch(body, access_cluster_id=access_cluster_id, region_id=region_id)

Downloads the given baseos patch.

Downloads the given baseos patch.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.download_baseos_patch_request import DownloadBaseosPatchRequest
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
    api_instance = cohesity_sdk.helios.BaseosPatchManagementApi(api_client)
    body = cohesity_sdk.helios.DownloadBaseosPatchRequest() # DownloadBaseosPatchRequest | Request to download a new baseos patch.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Downloads the given baseos patch.
        api_instance.download_baseos_patch(body, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling BaseosPatchManagementApi->download_baseos_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadBaseosPatchRequest**](DownloadBaseosPatchRequest.md)| Request to download a new baseos patch. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baseos_patch_list**
> List[BaseosPatchListItem] get_baseos_patch_list(access_cluster_id=access_cluster_id, region_id=region_id)

Get available baseos patches

Returns the available baseos patches

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.baseos_patch_list_item import BaseosPatchListItem
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
    api_instance = cohesity_sdk.helios.BaseosPatchManagementApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get available baseos patches
        api_response = api_instance.get_baseos_patch_list(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of BaseosPatchManagementApi->get_baseos_patch_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaseosPatchManagementApi->get_baseos_patch_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**List[BaseosPatchListItem]**](BaseosPatchListItem.md)

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
> BaseosPatchLog get_baseos_patch_log(patch_name, access_cluster_id=access_cluster_id, region_id=region_id)

Get Baseos patch application log

Returns the log and status of the mentioned patch.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.baseos_patch_log import BaseosPatchLog
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
    api_instance = cohesity_sdk.helios.BaseosPatchManagementApi(api_client)
    patch_name = 'patch_name_example' # str | Name of the hotfix with security patch
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Baseos patch application log
        api_response = api_instance.get_baseos_patch_log(patch_name, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of BaseosPatchManagementApi->get_baseos_patch_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaseosPatchManagementApi->get_baseos_patch_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_name** | **str**| Name of the hotfix with security patch | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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
> remove_baseos_patch(body, access_cluster_id=access_cluster_id, region_id=region_id)

Cleans up the given baseos patch files.

Cleans up the given baseos patch files.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.remove_baseos_patch_request import RemoveBaseosPatchRequest
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
    api_instance = cohesity_sdk.helios.BaseosPatchManagementApi(api_client)
    body = cohesity_sdk.helios.RemoveBaseosPatchRequest() # RemoveBaseosPatchRequest | Request to remove baseos patch files.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Cleans up the given baseos patch files.
        api_instance.remove_baseos_patch(body, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling BaseosPatchManagementApi->remove_baseos_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveBaseosPatchRequest**](RemoveBaseosPatchRequest.md)| Request to remove baseos patch files. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

