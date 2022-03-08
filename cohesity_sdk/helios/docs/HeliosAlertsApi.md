# cohesity_sdk.HeliosAlertsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_alerts**](HeliosAlertsApi.md#get_helios_alerts) | **GET** /mcm/alerts | Get list of helios alerts.


# **get_helios_alerts**
> AlertsList get_helios_alerts()

Get list of helios alerts.

Get the list of helios alerts.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.alerts_list import AlertsList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
alert_id_list = [
        "alertIdList_example",
    ] # [str] | Filter by list of alert ids. (optional)
alert_state_list = [
        "alertStateList_example",
    ] # [str] | Filter by list of alert states. (optional)
alert_type_list = [
        1,
    ] # [int] | Filter by list of alert types. (optional)
alert_severity_list = [
        "kCritical",
    ] # [str] | Filter by list of alert severity types. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by list of region ids. (optional)
cluster_identifiers = [
        "clusterIdentifiers_example",
    ] # [str] | Filter by list of cluster ids. (optional)
start_date_usecs = 1 # int | Specifies the start time of the alerts to be returned. All the alerts returned are raised after the specified start time. This value should be in Unix timestamp epoch in microseconds. (optional)
end_date_usecs = 1 # int | Specifies the end time of the alerts to be returned. All the alerts returned are raised before the specified end time. This value should be in Unix timestamp epoch in microseconds. (optional)
max_alerts = 1 # int | Specifies maximum number of alerts to return (optional)
alert_category_list = [
        "kDisk",
    ] # [str, none_type] | Filter by list of alert categories. (optional)
alert_type_bucket_list = [
        "kHardware",
    ] # [str, none_type] | Filter by list of alert type buckets. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of helios alerts.
	api_response = client.helios_alerts.get_helios_alerts(region_id=region_id, alert_id_list=alert_id_list, alert_state_list=alert_state_list, alert_type_list=alert_type_list, alert_severity_list=alert_severity_list, region_ids=region_ids, cluster_identifiers=cluster_identifiers, start_date_usecs=start_date_usecs, end_date_usecs=end_date_usecs, max_alerts=max_alerts, alert_category_list=alert_category_list, alert_type_bucket_list=alert_type_bucket_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAlertsApi->get_helios_alerts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **alert_id_list** | **[str]**| Filter by list of alert ids. | [optional]
 **alert_state_list** | **[str]**| Filter by list of alert states. | [optional]
 **alert_type_list** | **[int]**| Filter by list of alert types. | [optional]
 **alert_severity_list** | **[str]**| Filter by list of alert severity types. | [optional]
 **region_ids** | **[str]**| Filter by list of region ids. | [optional]
 **cluster_identifiers** | **[str]**| Filter by list of cluster ids. | [optional]
 **start_date_usecs** | **int**| Specifies the start time of the alerts to be returned. All the alerts returned are raised after the specified start time. This value should be in Unix timestamp epoch in microseconds. | [optional]
 **end_date_usecs** | **int**| Specifies the end time of the alerts to be returned. All the alerts returned are raised before the specified end time. This value should be in Unix timestamp epoch in microseconds. | [optional]
 **max_alerts** | **int**| Specifies maximum number of alerts to return | [optional]
 **alert_category_list** | [**[str, none_type]**](str, none_type.md)| Filter by list of alert categories. | [optional]
 **alert_type_bucket_list** | [**[str, none_type]**](str, none_type.md)| Filter by list of alert type buckets. | [optional]

### Return type

[**AlertsList**](AlertsList.md)

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

