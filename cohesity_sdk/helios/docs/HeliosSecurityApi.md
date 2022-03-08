# cohesity_sdk.HeliosSecurityApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anomaly_alert_notif_level**](HeliosSecurityApi.md#get_anomaly_alert_notif_level) | **GET** /mcm/security/anomalies | Get the anomaly details.
[**update_anomaly_alert_notif_level**](HeliosSecurityApi.md#update_anomaly_alert_notif_level) | **PUT** /mcm/security/anomalies | Updates the anomaly notification threshold.


# **get_anomaly_alert_notif_level**
> AnomalyAlert get_anomaly_alert_notif_level()

Get the anomaly details.

Get the anomaly details.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.anomaly_alert import AnomalyAlert
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the anomaly details.
	api_response = client.helios_security.get_anomaly_alert_notif_level(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosSecurityApi->get_anomaly_alert_notif_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**AnomalyAlert**](AnomalyAlert.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the response of the notification operation. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_anomaly_alert_notif_level**
> update_anomaly_alert_notif_level(body)

Updates the anomaly notification threshold.

Update the anomaly settings such as notification threshold.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.anomaly_alert import AnomalyAlert
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = AnomalyAlert(
        notification_info=NotificationInfo(
            anomaly_strength_threshold=1,
        ),
        tagging_info=TaggingInfo(
            block_restore=True,
            tag_id=1,
            tag_name="tag_name_example",
        ),
    ) # AnomalyAlert | Specifies the parameters to update an account notification threshold
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Updates the anomaly notification threshold.
	client.helios_security.update_anomaly_alert_notif_level(body)
except ApiException as e:
	print("Exception when calling HeliosSecurityApi->update_anomaly_alert_notif_level: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Updates the anomaly notification threshold.
	client.helios_security.update_anomaly_alert_notif_level(body, region_id=region_id)
except ApiException as e:
	print("Exception when calling HeliosSecurityApi->update_anomaly_alert_notif_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnomalyAlert**](AnomalyAlert.md)| Specifies the parameters to update an account notification threshold |
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
**204** | Updated successfully |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

