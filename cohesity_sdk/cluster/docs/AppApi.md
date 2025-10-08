# cohesity_sdk.AppApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_images_status**](AppApi.md#get_images_status) | **GET** /apps/{appUid}/images/status | Api to get images information.
[**perform_on_demand_service_action**](AppApi.md#perform_on_demand_service_action) | **PUT** /apps/{appUid}/images/action | Enables or disables a service.
[**upload_app_container_image**](AppApi.md#upload_app_container_image) | **POST** /apps/{appUid}/imageUpload | Upload apps container image.


# **get_images_status**
> ImagesStatus get_images_status(app_uid)

Api to get images information.

**Privileges:** ```APPS_MANAGEMENT``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.images_status import ImagesStatus
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


app_uid = 1 # int | Specifies the app Id.

# example passing only required values which don't have defaults set
try:
	# Api to get images information.
	api_response = client.app.get_images_status(app_uid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AppApi->get_images_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uid** | **int**| Specifies the app Id. |

### Return type

[**ImagesStatus**](ImagesStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetImagesStatusResponse specifies response for getting image status |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_on_demand_service_action**
> perform_on_demand_service_action(app_uid, body)

Enables or disables a service.

**Privileges:** ```APPS_MANAGEMENT``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.perform_service_action_parameters import PerformServiceActionParameters
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


app_uid = 1 # int | Specifies the app Id.
body = PerformServiceActionParameters(
        enable=True,
    ) # PerformServiceActionParameters | Request to update app instance settings.

# example passing only required values which don't have defaults set
try:
	# Enables or disables a service.
	client.app.perform_on_demand_service_action(app_uid, body)
except ApiException as e:
	print("Exception when calling AppApi->perform_on_demand_service_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uid** | **int**| Specifies the app Id. |
 **body** | [**PerformServiceActionParameters**](PerformServiceActionParameters.md)| Request to update app instance settings. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_app_container_image**
> upload_app_container_image(app_uid)

Upload apps container image.

**Privileges:** ```APPS_MANAGEMENT``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


app_uid = 1 # int | Specifies the app Id.

# example passing only required values which don't have defaults set
try:
	# Upload apps container image.
	client.app.upload_app_container_image(app_uid)
except ApiException as e:
	print("Exception when calling AppApi->upload_app_container_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uid** | **int**| Specifies the app Id. |

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
**202** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

