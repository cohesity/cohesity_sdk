# cohesity_sdk.StatsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_throttling_stats**](StatsApi.md#fetch_throttling_stats) | **GET** /mcm/stats/{registrationId}/throttling | Fetch the throttling stats of a source.
[**get_cluster_storage_stats**](StatsApi.md#get_cluster_storage_stats) | **GET** /stats/cluster-storage | Get Cluster Storage Stats.
[**get_files_stats**](StatsApi.md#get_files_stats) | **GET** /stats/files | Get Stats of Files.
[**get_protection_runs_stats**](StatsApi.md#get_protection_runs_stats) | **GET** /stats/protection-runs | Get statistics of protection runs.
[**get_time_series_stats**](StatsApi.md#get_time_series_stats) | **GET** /stats/time-series-stats | Get Time Series Stats.
[**get_view_client_stats**](StatsApi.md#get_view_client_stats) | **GET** /stats/view-clients | Get Stats of View Clients
[**get_views_stats**](StatsApi.md#get_views_stats) | **GET** /stats/views | Get Views Stats.
[**mcm_get_policy_last_run_stats**](StatsApi.md#mcm_get_policy_last_run_stats) | **GET** /mcm/stats/policies/last-run | Compute stats of last Protection Run of Protection Policies.
[**mcm_get_protection_run_last_run_stats**](StatsApi.md#mcm_get_protection_run_last_run_stats) | **GET** /mcm/stats/protection-runs/last-run | Compute stats of last Protection Run across all objects.


# **fetch_throttling_stats**
> FetchThrottlingStatsResponseBody fetch_throttling_stats(registration_id, source_id)

Fetch the throttling stats of a source.

Compute the throttling stats for a source and return time series data.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.fetch_throttling_stats_response_body import FetchThrottlingStatsResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


registration_id = "registrationId_example" # str, none_type | Specifies the registration id of the protected source. It is of the format {clusterID}:{IncarnationId}:{EntityId}.
source_id = "sourceId_example" # str, none_type | Specifies the source name for which throttling stats are needed. In case of Office365, it is the domain name which is unique.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
start_time_usecs = 1 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
end_time_usecs = 1 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
workload_type = [
        "kO365Exchange",
    ] # [str], none_type | Specifies the list of workload types within the source for which throttling stats are needed. (optional)
api_type = [
        "kEWS",
    ] # [str], none_type | Specifies the list of api type within the source for which throttling stats are needed. (optional)

# example passing only required values which don't have defaults set
try:
	# Fetch the throttling stats of a source.
	api_response = client.stats.fetch_throttling_stats(registration_id, source_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->fetch_throttling_stats: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Fetch the throttling stats of a source.
	api_response = client.stats.fetch_throttling_stats(registration_id, source_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, workload_type=workload_type, api_type=api_type)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->fetch_throttling_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str, none_type**| Specifies the registration id of the protected source. It is of the format {clusterID}:{IncarnationId}:{EntityId}. |
 **source_id** | **str, none_type**| Specifies the source name for which throttling stats are needed. In case of Office365, it is the domain name which is unique. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional]
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional]
 **workload_type** | **[str], none_type**| Specifies the list of workload types within the source for which throttling stats are needed. | [optional]
 **api_type** | **[str], none_type**| Specifies the list of api type within the source for which throttling stats are needed. | [optional]

### Return type

[**FetchThrottlingStatsResponseBody**](FetchThrottlingStatsResponseBody.md)

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

# **get_cluster_storage_stats**
> ClusterStorageStats get_cluster_storage_stats()

Get Cluster Storage Stats.

Get Cluster Storage Stats.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.cluster_storage_stats import ClusterStorageStats
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Cluster Storage Stats.
	api_response = client.stats.get_cluster_storage_stats(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_cluster_storage_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClusterStorageStats**](ClusterStorageStats.md)

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

# **get_files_stats**
> FilesStats get_files_stats()

Get Stats of Files.

Get Stats of files.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.files_stats import FilesStats
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
entity_type = "kCluster" # str | Specifies the entity type based on which the files stats are calculated. By default stats are calculated based on Cluster (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Stats of Files.
	api_response = client.stats.get_files_stats(access_cluster_id=access_cluster_id, region_id=region_id, entity_type=entity_type)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_files_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **entity_type** | **str**| Specifies the entity type based on which the files stats are calculated. By default stats are calculated based on Cluster | [optional]

### Return type

[**FilesStats**](FilesStats.md)

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

# **get_protection_runs_stats**
> GetProtectionRunsStatusResponseBody get_protection_runs_stats()

Get statistics of protection runs.

Get statistics of protection runs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.get_protection_runs_status_response_body import GetProtectionRunsStatusResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
start_time_usecs = 1 # int | Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be counted. By default it is current time minus a day. (optional)
end_time_usecs = 1 # int | Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be counted. By default it is current time. (optional)
run_status = [
        "Running",
    ] # [str] | Specifies a list of status, runs matching the status will be returned. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Failed' indicates that the run has failed. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get statistics of protection runs.
	api_response = client.stats.get_protection_runs_stats(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_protection_runs_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_time_series_stats**
> TimeSeriesStats get_time_series_stats(schema_name, metric_names, entity_id, start_time_msecs)

Get Time Series Stats.

Get Time Series Stats.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.time_series_stats import TimeSeriesStats
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


schema_name = "schemaName_example" # str | Specifies the schema name.
metric_names = [
        "metricNames_example",
    ] # [str] | Specifies a list of metric names.
entity_id = "entityId_example" # str | Specifies the entity id.
start_time_msecs = 1 # int | Specifies the start time of series stats.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
end_time_msecs = 1 # int | Specifies the end time of series stats, by default it is current time. (optional)
rollup_function = "kSum" # str | Specifies the rollup function to apply to the data points for the time interval specified by rollupInternalSecs. (optional)
rollup_interval_secs = 1 # int | Specifies the time interval granularity for the specified rollup function. (optional)

# example passing only required values which don't have defaults set
try:
	# Get Time Series Stats.
	api_response = client.stats.get_time_series_stats(schema_name, metric_names, entity_id, start_time_msecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_time_series_stats: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Time Series Stats.
	api_response = client.stats.get_time_series_stats(schema_name, metric_names, entity_id, start_time_msecs, access_cluster_id=access_cluster_id, region_id=region_id, end_time_msecs=end_time_msecs, rollup_function=rollup_function, rollup_interval_secs=rollup_interval_secs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_time_series_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**| Specifies the schema name. |
 **metric_names** | **[str]**| Specifies a list of metric names. |
 **entity_id** | **str**| Specifies the entity id. |
 **start_time_msecs** | **int**| Specifies the start time of series stats. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **end_time_msecs** | **int**| Specifies the end time of series stats, by default it is current time. | [optional]
 **rollup_function** | **str**| Specifies the rollup function to apply to the data points for the time interval specified by rollupInternalSecs. | [optional]
 **rollup_interval_secs** | **int**| Specifies the time interval granularity for the specified rollup function. | [optional]

### Return type

[**TimeSeriesStats**](TimeSeriesStats.md)

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.view_clients_stats import ViewClientsStats
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
metric = "kNumBytesRead" # str, none_type | Specifies the metric to which stats has to be sorted. (optional)
num_top_view_clients = 1 # int, none_type | Specifies the number of view clients for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view clients will be returned. If metric is not specified, this parameter must also not be specified. (optional)
last_hours = 1 # int, none_type | Specifies the last hours of stats to sort. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Stats of View Clients
	api_response = client.stats.get_view_client_stats(access_cluster_id=access_cluster_id, region_id=region_id, metric=metric, num_top_view_clients=num_top_view_clients, last_hours=last_hours)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_view_client_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_views_stats**
> ViewsStats get_views_stats()

Get Views Stats.

Get Views Stats.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.views_stats import ViewsStats
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
metric = "kNumBytesRead" # str, none_type | Specifies the metric to which stats has to be sorted. (optional)
protocol = "kAny" # str, none_type | Specifies the protocol to sort. (optional)
num_top_views = 1 # int, none_type | Specifies the number of view for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view will be returned. If metric is not specified, this parameter must also not be specified. (optional)
last_hours = 1 # int, none_type | Specifies the last hours of stats to sort. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Views Stats.
	api_response = client.stats.get_views_stats(access_cluster_id=access_cluster_id, region_id=region_id, metric=metric, protocol=protocol, num_top_views=num_top_views, last_hours=last_hours)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_views_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **metric** | **str, none_type**| Specifies the metric to which stats has to be sorted. | [optional]
 **protocol** | **str, none_type**| Specifies the protocol to sort. | [optional]
 **num_top_views** | **int, none_type**| Specifies the number of view for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view will be returned. If metric is not specified, this parameter must also not be specified. | [optional]
 **last_hours** | **int, none_type**| Specifies the last hours of stats to sort. | [optional]

### Return type

[**ViewsStats**](ViewsStats.md)

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

# **mcm_get_policy_last_run_stats**
> McmGetPolicyLastRunStatsResponseBody mcm_get_policy_last_run_stats()

Compute stats of last Protection Run of Protection Policies.

Compute stats of last Protection Run of Protection Policies.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_get_policy_last_run_stats_response_body import McmGetPolicyLastRunStatsResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Compute stats of last Protection Run of Protection Policies.
	api_response = client.stats.mcm_get_policy_last_run_stats(region_id=region_id, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->mcm_get_policy_last_run_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]

### Return type

[**McmGetPolicyLastRunStatsResponseBody**](McmGetPolicyLastRunStatsResponseBody.md)

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

# **mcm_get_protection_run_last_run_stats**
> McmGetProtectionLastRunStatsResponseBody mcm_get_protection_run_last_run_stats()

Compute stats of last Protection Run across all objects.

Compute stats of last Protection Run across all objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_get_protection_last_run_stats_response_body import McmGetProtectionLastRunStatsResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Compute stats of last Protection Run across all objects.
	api_response = client.stats.mcm_get_protection_run_last_run_stats(region_id=region_id, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->mcm_get_protection_run_last_run_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]

### Return type

[**McmGetProtectionLastRunStatsResponseBody**](McmGetProtectionLastRunStatsResponseBody.md)

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

