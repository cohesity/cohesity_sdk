# cohesity_sdk.cluster.RemoteStorageApi

All URIs are relative to *http://localhost/v2*

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete remote storage registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import remote_storage
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_storage.RemoteStorageApi(api_client)
    id = 1 # int | Specifies the registration id of the registered remote storage.

    # example passing only required values which don't have defaults set
    try:
        # Delete Remote Storage Registration
        api_instance.delete_remote_storage_registration(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling RemoteStorageApi->delete_remote_storage_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get summary about list of registered remote storage servers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import remote_storage
from cohesity_sdk.cluster.cohesity.model.registered_remote_storage_list import RegisteredRemoteStorageList
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_storage.RemoteStorageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Registered Remote Storage Servers List
        api_response = api_instance.get_registered_remote_storage_list()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling RemoteStorageApi->get_registered_remote_storage_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegisteredRemoteStorageList**](RegisteredRemoteStorageList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> RemoteStorageInfo get_remote_storage_details(id)

Get remote storage details

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get details of remote storage given by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import remote_storage
from cohesity_sdk.cluster.cohesity.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_storage.RemoteStorageApi(api_client)
    id = 1 # int | Specifies the id of the registered remote storage.
    include_available_space = False # bool | Specifies whether to include available capacity on remote storage. (optional) if omitted the server will use the default value of False
    include_available_data_vips = False # bool | Specifies whether to include available data vips on remote storage. (optional) if omitted the server will use the default value of False
    include_array_info = False # bool | Includes flashblade specific info like name, software os and version of pure flashblade. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get remote storage details
        api_response = api_instance.get_remote_storage_details(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling RemoteStorageApi->get_remote_storage_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get remote storage details
        api_response = api_instance.get_remote_storage_details(id, include_available_space=include_available_space, include_available_data_vips=include_available_data_vips, include_array_info=include_array_info)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling RemoteStorageApi->get_remote_storage_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the registered remote storage. |
 **include_available_space** | **bool**| Specifies whether to include available capacity on remote storage. | [optional] if omitted the server will use the default value of False
 **include_available_data_vips** | **bool**| Specifies whether to include available data vips on remote storage. | [optional] if omitted the server will use the default value of False
 **include_array_info** | **bool**| Includes flashblade specific info like name, software os and version of pure flashblade. | [optional] if omitted the server will use the default value of False

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Register a remote storage to be used for disaggregated storage.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import remote_storage
from cohesity_sdk.cluster.cohesity.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_storage.RemoteStorageApi(api_client)
    body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to register a remote storage management server.

    # example passing only required values which don't have defaults set
    try:
        # Register Remote Storage
        api_response = api_instance.register_new_remote_storage(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling RemoteStorageApi->register_new_remote_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to register a remote storage management server. |

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update Registered Remote Storage Config.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import remote_storage
from cohesity_sdk.cluster.cohesity.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = remote_storage.RemoteStorageApi(api_client)
    id = 1 # int | Specifies the registration id of the registered remote storage.
    body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to update the registration.

    # example passing only required values which don't have defaults set
    try:
        # Update Remote Storage Config
        api_response = api_instance.update_remote_storage_registration(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

