# cohesity_sdk.RemoteStorageApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_remote_storage_registration**](RemoteStorageApi.md#delete_remote_storage_registration) | **DELETE** /remote-storage/{id} | Delete Remote Storage Registration
[**get_registered_remote_storage_list**](RemoteStorageApi.md#get_registered_remote_storage_list) | **GET** /remote-storage | Get Registered Remote Storage Servers List
[**get_remote_storage_details**](RemoteStorageApi.md#get_remote_storage_details) | **GET** /remote-storage/{id} | Get remote storage details
[**register_new_remote_storage**](RemoteStorageApi.md#register_new_remote_storage) | **POST** /remote-storage | Register Remote Storage
[**update_remote_storage_registration**](RemoteStorageApi.md#update_remote_storage_registration) | **PATCH** /remote-storage/{id} | Update Remote Storage Config


# **delete_remote_storage_registration**
> delete_remote_storage_registration(id)

Delete Remote Storage Registration

Delete remote storage registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteStorageApi(api_client)
    id = 56 # int | Specifies the registration id of the registered remote storage.

    try:
        # Delete Remote Storage Registration
        api_instance.delete_remote_storage_registration(id)
    except Exception as e:
        print("Exception when calling RemoteStorageApi->delete_remote_storage_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. | 

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

# **get_registered_remote_storage_list**
> RegisteredRemoteStorageList get_registered_remote_storage_list()

Get Registered Remote Storage Servers List

Get summary about list of registered remote storage servers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.registered_remote_storage_list import RegisteredRemoteStorageList
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteStorageApi(api_client)

    try:
        # Get Registered Remote Storage Servers List
        api_response = api_instance.get_registered_remote_storage_list()
        print("The response of RemoteStorageApi->get_registered_remote_storage_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteStorageApi->get_registered_remote_storage_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RegisteredRemoteStorageList**](RegisteredRemoteStorageList.md)

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

# **get_remote_storage_details**
> RemoteStorageInfo get_remote_storage_details(id, include_available_space=include_available_space, include_available_data_vips=include_available_data_vips, include_array_info=include_array_info)

Get remote storage details

Get details of remote storage given by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteStorageApi(api_client)
    id = 56 # int | Specifies the id of the registered remote storage.
    include_available_space = False # bool | Specifies whether to include available capacity on remote storage. (optional) (default to False)
    include_available_data_vips = False # bool | Specifies whether to include available data vips on remote storage. (optional) (default to False)
    include_array_info = False # bool | Includes flashblade specific info like name, software os and version of pure flashblade. (optional) (default to False)

    try:
        # Get remote storage details
        api_response = api_instance.get_remote_storage_details(id, include_available_space=include_available_space, include_available_data_vips=include_available_data_vips, include_array_info=include_array_info)
        print("The response of RemoteStorageApi->get_remote_storage_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteStorageApi->get_remote_storage_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the registered remote storage. | 
 **include_available_space** | **bool**| Specifies whether to include available capacity on remote storage. | [optional] [default to False]
 **include_available_data_vips** | **bool**| Specifies whether to include available data vips on remote storage. | [optional] [default to False]
 **include_array_info** | **bool**| Includes flashblade specific info like name, software os and version of pure flashblade. | [optional] [default to False]

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

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

# **register_new_remote_storage**
> RemoteStorageInfo register_new_remote_storage(body)

Register Remote Storage

Register a remote storage to be used for disaggregated storage.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteStorageApi(api_client)
    body = cohesity_sdk.RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to register a remote storage management server.

    try:
        # Register Remote Storage
        api_response = api_instance.register_new_remote_storage(body)
        print("The response of RemoteStorageApi->register_new_remote_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteStorageApi->register_new_remote_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to register a remote storage management server. | 

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

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

# **update_remote_storage_registration**
> RemoteStorageInfo update_remote_storage_registration(id, body)

Update Remote Storage Config

Update Registered Remote Storage Config.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteStorageApi(api_client)
    id = 56 # int | Specifies the registration id of the registered remote storage.
    body = cohesity_sdk.RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to update the registration.

    try:
        # Update Remote Storage Config
        api_response = api_instance.update_remote_storage_registration(id, body)
        print("The response of RemoteStorageApi->update_remote_storage_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteStorageApi->update_remote_storage_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. | 
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to update the registration. | 

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

