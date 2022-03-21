# cohesity_sdk.AlertApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_summary**](AlertApi.md#get_alert_summary) | **GET** /alerts-summary | Get alerts summary.
[**get_helios_alerts**](AlertApi.md#get_helios_alerts) | **GET** /mcm/alerts | Get list of helios alerts.
[**get_helios_alerts_summary**](AlertApi.md#get_helios_alerts_summary) | **GET** /mcm/stats/alerts-summary | Get alerts summary on Helios.


# **get_alert_summary**
> AlertsSummaryResponse get_alert_summary()

Get alerts summary.

Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.alerts_summary_response import AlertsSummaryResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
start_time_usecs = 1 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
end_time_usecs = 1 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
include_tenants = True # bool, none_type | IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str], none_type | TenantIds contains ids of the tenants for which alerts are to be used to compute summary. (optional)
states_list = [
        "kResolved",
    ] # [str], none_type | Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get alerts summary.
	api_response = client.alert.get_alert_summary(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alert_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional]
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional]
 **include_tenants** | **bool, none_type**| IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user&#39;s organization should be used to compute summary. | [optional]
 **tenant_ids** | **[str], none_type**| TenantIds contains ids of the tenants for which alerts are to be used to compute summary. | [optional]
 **states_list** | **[str], none_type**| Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. | [optional]

### Return type

[**AlertsSummaryResponse**](AlertsSummaryResponse.md)

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
	api_response = client.alert.get_helios_alerts(region_id=region_id, alert_id_list=alert_id_list, alert_state_list=alert_state_list, alert_type_list=alert_type_list, alert_severity_list=alert_severity_list, region_ids=region_ids, cluster_identifiers=cluster_identifiers, start_date_usecs=start_date_usecs, end_date_usecs=end_date_usecs, max_alerts=max_alerts, alert_category_list=alert_category_list, alert_type_bucket_list=alert_type_bucket_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_helios_alerts: %s\n" % e)
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

# **get_helios_alerts_summary**
> AlertsSummaryResponse get_helios_alerts_summary()

Get alerts summary on Helios.

Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.alerts_summary_response import AlertsSummaryResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
cluster_identifiers = [
        "clusterIdentifiers_example",
    ] # [str], none_type | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. (optional)
start_time_usecs = 1 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
end_time_usecs = 1 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
states_list = [
        "kResolved",
    ] # [str], none_type | Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get alerts summary on Helios.
	api_response = client.alert.get_helios_alerts_summary(region_id=region_id, cluster_identifiers=cluster_identifiers, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, states_list=states_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_helios_alerts_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **cluster_identifiers** | **[str], none_type**| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. | [optional]
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional]
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional]
 **states_list** | **[str], none_type**| Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. | [optional]

### Return type

[**AlertsSummaryResponse**](AlertsSummaryResponse.md)

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

