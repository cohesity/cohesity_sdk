# cohesity_sdk.StatsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_protection_runs_stats**](StatsApi.md#get_protection_runs_stats) | **GET** /stats/protection-runs | Get statistics of protection runs.


# **get_protection_runs_stats**
> GetProtectionRunsStatusResponseBody get_protection_runs_stats()

Get statistics of protection runs.

Get statistics of protection runs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_protection_runs_status_response_body import GetProtectionRunsStatusResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
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
	api_response = client.[class Tag {
    name: Stats
    description: null
    externalDocs: null
}].get_protection_runs_stats(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)
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

