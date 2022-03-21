# cohesity_sdk.HeliosNotificationsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_notifications**](HeliosNotificationsApi.md#get_helios_notifications) | **GET** /mcm/dashboard/notifications | Get helios notifications


# **get_helios_notifications**
> Notifications get_helios_notifications()

Get helios notifications

Get all types of notifications.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.notifications import Notifications
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get helios notifications
	api_response = client.helios_notifications.get_helios_notifications(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosNotificationsApi->get_helios_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Notifications**](Notifications.md)

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

