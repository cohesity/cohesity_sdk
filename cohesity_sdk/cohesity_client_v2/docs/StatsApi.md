# cohesity_sdk.StatsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_protection_runs_stats**](StatsApi.md#get_protection_runs_stats) | **GET** /stats/protection-runs | Get statistics of protection runs.
[**get_view_client_stats**](StatsApi.md#get_view_client_stats) | **GET** /stats/view-clients | Get Stats of View Clients


# **get_protection_runs_stats**
> GetProtectionRunsStatusResponseBody get_protection_runs_stats()

Get statistics of protection runs.

Get statistics of protection runs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.get_protection_runs_status_response_body import GetProtectionRunsStatusResponseBody
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_usecs = 1 # int | Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be counted. By default it is current time minus a day. (optional)
end_time_usecs = 1 # int | Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be counted. By default it is current time. (optional)
run_status = [
        "Running",
    ] # [str] | Specifies a list of status, runs matching the status will be returned. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Failed' indicates that the run has failed. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get statistics of protection runs.
	api_response = client.stats.get_protection_runs_stats(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_protection_runs_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_usecs** | **int**| Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be counted. By default it is current time minus a day. | [optional]
 **end_time_usecs** | **int**| Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be counted. By default it is current time. | [optional]
 **run_status** | **[str]**| Specifies a list of status, runs matching the status will be returned. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional]

### Return type

[**GetProtectionRunsStatusResponseBody**](GetProtectionRunsStatusResponseBody.md)

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

# **get_view_client_stats**
> ViewClientsStats get_view_client_stats()

Get Stats of View Clients

Get Stats of View Clients.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view_clients_stats import ViewClientsStats
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


metric = "kNumBytesRead" # str, none_type | Specifies the metric to which stats has to be sorted. (optional)
num_top_view_clients = 1 # int, none_type | Specifies the number of view clients for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view clients will be returned. If metric is not specified, this parameter must also not be specified. (optional)
last_hours = 1 # int, none_type | Specifies the last hours of stats to sort. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Stats of View Clients
	api_response = client.stats.get_view_client_stats(metric=metric, num_top_view_clients=num_top_view_clients, last_hours=last_hours)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_view_client_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str, none_type**| Specifies the metric to which stats has to be sorted. | [optional]
 **num_top_view_clients** | **int, none_type**| Specifies the number of view clients for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view clients will be returned. If metric is not specified, this parameter must also not be specified. | [optional]
 **last_hours** | **int, none_type**| Specifies the last hours of stats to sort. | [optional]

### Return type

[**ViewClientsStats**](ViewClientsStats.md)

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

