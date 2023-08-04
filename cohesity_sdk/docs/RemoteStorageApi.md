# cohesity_sdk.RemoteStorageApi


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
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the registration id of the registered remote storage.

# example passing only required values which don't have defaults set
try:
	# Delete Remote Storage Registration
	client.remote_storage.delete_remote_storage_registration(id)
except ApiException as e:
	print("Exception when calling RemoteStorageApi->delete_remote_storage_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. |

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

# **get_registered_remote_storage_list**
> RegisteredRemoteStorageList get_registered_remote_storage_list()

Get Registered Remote Storage Servers List

Get summary about list of registered remote storage servers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.registered_remote_storage_list import RegisteredRemoteStorageList
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
	# Get Registered Remote Storage Servers List
	api_response = client.remote_storage.get_registered_remote_storage_list()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteStorageApi->get_registered_remote_storage_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegisteredRemoteStorageList**](RegisteredRemoteStorageList.md)

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

# **get_remote_storage_details**
> RemoteStorageInfo get_remote_storage_details(id)

Get remote storage details

Get details of remote storage given by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the registered remote storage.
include_available_space = False # bool | Specifies whether to include available capacity on remote storage. (optional) if omitted the server will use the default value of False
include_available_data_vips = False # bool | Specifies whether to include available data vips on remote storage. (optional) if omitted the server will use the default value of False
include_array_info = False # bool | Includes flashblade specific info like name, software os and version of pure flashblade. (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
try:
	# Get remote storage details
	api_response = client.remote_storage.get_remote_storage_details(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteStorageApi->get_remote_storage_details: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get remote storage details
	api_response = client.remote_storage.get_remote_storage_details(id, include_available_space=include_available_space, include_available_data_vips=include_available_data_vips, include_array_info=include_array_info)
	pprint(api_response)
except ApiException as e:
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

# **register_new_remote_storage**
> RemoteStorageInfo register_new_remote_storage(body)

Register Remote Storage

Register a remote storage to be used for disaggregated storage.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to register a remote storage management server.

# example passing only required values which don't have defaults set
try:
	# Register Remote Storage
	api_response = client.remote_storage.register_new_remote_storage(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteStorageApi->register_new_remote_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to register a remote storage management server. |

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

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

# **update_remote_storage_registration**
> RemoteStorageInfo update_remote_storage_registration(id, body)

Update Remote Storage Config

Update Registered Remote Storage Config.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the registration id of the registered remote storage.
body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to update the registration.

# example passing only required values which don't have defaults set
try:
	# Update Remote Storage Config
	api_response = client.remote_storage.update_remote_storage_registration(id, body)
	pprint(api_response)
except ApiException as e:
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

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

