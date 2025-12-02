# cohesity_sdk.StatsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_storage_stats**](StatsApi.md#get_cluster_storage_stats) | **GET** /stats/cluster-storage | Get Cluster Storage Stats.
[**get_files_stats**](StatsApi.md#get_files_stats) | **GET** /stats/files | Get Stats of Files.
[**get_protection_runs_stats**](StatsApi.md#get_protection_runs_stats) | **GET** /stats/protection-runs | Get statistics of protection runs.
[**get_replication_backlog_stats**](StatsApi.md#get_replication_backlog_stats) | **GET** /stats/replication-backlog | Get Time Series Stats for Replication Backlog.
[**get_replication_clusters**](StatsApi.md#get_replication_clusters) | **GET** /stats/replication-clusters | 
[**get_replication_data_trend**](StatsApi.md#get_replication_data_trend) | **GET** /stats/replication-data-trend | 
[**get_replication_objects**](StatsApi.md#get_replication_objects) | **GET** /stats/replication-objects | 
[**get_replication_objects_trend**](StatsApi.md#get_replication_objects_trend) | **GET** /stats/replication-objects-trend | 
[**get_restore_stats**](StatsApi.md#get_restore_stats) | **GET** /stats/recoveries | Compute the statistics on the Restore tasks on the cluster.
[**get_time_series_stats**](StatsApi.md#get_time_series_stats) | **GET** /stats/time-series-stats | Get Time Series Stats.
[**get_top_views_stats**](StatsApi.md#get_top_views_stats) | **GET** /stats/top-views | Get stats for the top views, which are the views with largest value of &#39;stats.valueInLastHours&#39; for a given combination of &#39;metric&#39;, &#39;protocol&#39; &amp; &#39;lastHours&#39; params. The API uses suitable defaults if any of the parameters are not specified.
[**get_view_client_stats**](StatsApi.md#get_view_client_stats) | **GET** /stats/view-clients | Get Stats of View Clients
[**get_views_stats**](StatsApi.md#get_views_stats) | **GET** /stats/views | Get stats for the top views, which are the views with largest value of &#39;stats.valueInLastHours&#39; for a given combination of &#39;metric&#39;, &#39;protocol&#39; &amp; &#39;lastHours&#39; params. The API uses suitable defaults if any of the parameters are not specified.
[**get_workload_stats**](StatsApi.md#get_workload_stats) | **GET** /stats/workload-stats | Get Workload Stats Schema.


# **get_cluster_storage_stats**
> ClusterStorageStats get_cluster_storage_stats()

Get Cluster Storage Stats.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get Cluster Storage Stats.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_storage_stats import ClusterStorageStats
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
	# Get Cluster Storage Stats.
	api_response = client.stats.get_cluster_storage_stats()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_cluster_storage_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStorageStats**](ClusterStorageStats.md)

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

# **get_files_stats**
> FilesStats get_files_stats()

Get Stats of Files.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get Stats of files.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.files_stats import FilesStats
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


entity_type = "kCluster" # str | Specifies the entity type based on which the files stats are calculated. By default stats are calculated based on Cluster (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Stats of Files.
	api_response = client.stats.get_files_stats(entity_type=entity_type)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_files_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Specifies the entity type based on which the files stats are calculated. By default stats are calculated based on Cluster | [optional]

### Return type

[**FilesStats**](FilesStats.md)

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

# **get_protection_runs_stats**
> GetProtectionRunsStatusResponseBody get_protection_runs_stats()

Get statistics of protection runs.

**Privileges:** ```PROTECTION_VIEW``` <br><br>Get statistics of protection runs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_protection_runs_status_response_body import GetProtectionRunsStatusResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **get_replication_backlog_stats**
> ReplicationBacklogStats get_replication_backlog_stats()

Get Time Series Stats for Replication Backlog.

**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW, STORAGE_DOMAIN_VIEW, STORAGE_VIEW, PROTECTION_VIEW``` <br><br>Get Replication Backlog Stats.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.replication_backlog_stats import ReplicationBacklogStats
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
is_in_bound = True # bool | Specifies whether to get inbound or outbound replication backlog stats. Default is false. (optional)
target_cluster_list = [
        1,
    ] # [int] | Filters stats to only include entities that were replicated to the specified target remote cluster IDs. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Time Series Stats for Replication Backlog.
	api_response = client.stats.get_replication_backlog_stats(include_tenants=include_tenants, is_in_bound=is_in_bound, target_cluster_list=target_cluster_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_backlog_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **is_in_bound** | **bool**| Specifies whether to get inbound or outbound replication backlog stats. Default is false. | [optional]
 **target_cluster_list** | **[int]**| Filters stats to only include entities that were replicated to the specified target remote cluster IDs. | [optional]

### Return type

[**ReplicationBacklogStats**](ReplicationBacklogStats.md)

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

# **get_replication_clusters**
> ReplicationClustersResponse get_replication_clusters(start_time_msecs, rollup_interval_secs, target_cluster_list)



**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW, STORAGE_DOMAIN_VIEW, STORAGE_VIEW, PROTECTION_VIEW``` <br><br>Get list of clusters with total data replicated for each.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.replication_clusters_response import ReplicationClustersResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_msecs = 1 # int | Specifies the start time of series stats.
rollup_interval_secs = 1 # int | Specifies the time interval granularity for the specified rollup function.
target_cluster_list = [
        1,
    ] # [int] | List of cluster IDs for which replication data should be retrieved. Must include at least one cluster.
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
is_in_bound = True # bool | Specifies whether to get inbound or outbound replication backlog stats. Default is false. (optional)
prorate_data_points = True # bool | Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. (optional)
end_time_msecs = 1 # int | Specifies the end time of series stats, by default it is current time. (optional)

# example passing only required values which don't have defaults set
try:
	api_response = client.stats.get_replication_clusters(start_time_msecs, rollup_interval_secs, target_cluster_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_clusters: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	api_response = client.stats.get_replication_clusters(start_time_msecs, rollup_interval_secs, target_cluster_list, include_tenants=include_tenants, is_in_bound=is_in_bound, prorate_data_points=prorate_data_points, end_time_msecs=end_time_msecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_msecs** | **int**| Specifies the start time of series stats. |
 **rollup_interval_secs** | **int**| Specifies the time interval granularity for the specified rollup function. |
 **target_cluster_list** | **[int]**| List of cluster IDs for which replication data should be retrieved. Must include at least one cluster. |
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **is_in_bound** | **bool**| Specifies whether to get inbound or outbound replication backlog stats. Default is false. | [optional]
 **prorate_data_points** | **bool**| Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. | [optional]
 **end_time_msecs** | **int**| Specifies the end time of series stats, by default it is current time. | [optional]

### Return type

[**ReplicationClustersResponse**](ReplicationClustersResponse.md)

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

# **get_replication_data_trend**
> TimeSeriesStats get_replication_data_trend(start_time_msecs, rollup_interval_secs)



**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW, STORAGE_DOMAIN_VIEW, STORAGE_VIEW, PROTECTION_VIEW``` <br><br>Get replication data trends over time for all entities in the given schema.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.time_series_stats import TimeSeriesStats
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_msecs = 1 # int | Specifies the start time of series stats.
rollup_interval_secs = 1 # int | Specifies the time interval granularity for the specified rollup function.
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
is_in_bound = True # bool | Specifies whether to get inbound or outbound replication backlog stats. Default is false. (optional)
prorate_data_points = True # bool | Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. (optional)
end_time_msecs = 1 # int | Specifies the end time of series stats, by default it is current time. (optional)
target_cluster_list = [
        1,
    ] # [int] | Filters stats to only include entities that were replicated to the specified target remote cluster IDs. (optional)

# example passing only required values which don't have defaults set
try:
	api_response = client.stats.get_replication_data_trend(start_time_msecs, rollup_interval_secs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_data_trend: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	api_response = client.stats.get_replication_data_trend(start_time_msecs, rollup_interval_secs, include_tenants=include_tenants, is_in_bound=is_in_bound, prorate_data_points=prorate_data_points, end_time_msecs=end_time_msecs, target_cluster_list=target_cluster_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_data_trend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_msecs** | **int**| Specifies the start time of series stats. |
 **rollup_interval_secs** | **int**| Specifies the time interval granularity for the specified rollup function. |
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **is_in_bound** | **bool**| Specifies whether to get inbound or outbound replication backlog stats. Default is false. | [optional]
 **prorate_data_points** | **bool**| Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. | [optional]
 **end_time_msecs** | **int**| Specifies the end time of series stats, by default it is current time. | [optional]
 **target_cluster_list** | **[int]**| Filters stats to only include entities that were replicated to the specified target remote cluster IDs. | [optional]

### Return type

[**TimeSeriesStats**](TimeSeriesStats.md)

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

# **get_replication_objects**
> ReplicationObjectsList get_replication_objects()



**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW, STORAGE_DOMAIN_VIEW, STORAGE_VIEW, PROTECTION_VIEW``` <br><br>Get list of all replicated objects in the given time range

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.replication_objects_list import ReplicationObjectsList
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_msecs = 1 # int | Specifies the start time of series stats. (optional)
end_time_msecs = 1 # int | Specifies the end time of series stats, by default it is current time. (optional)
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
is_in_bound = True # bool | Specifies whether to get inbound or outbound replication backlog stats. Default is false. (optional)
target_cluster_list = [
        1,
    ] # [int] | Filters stats to only include entities that were replicated to the specified target remote cluster IDs. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	api_response = client.stats.get_replication_objects(start_time_msecs=start_time_msecs, end_time_msecs=end_time_msecs, include_tenants=include_tenants, is_in_bound=is_in_bound, target_cluster_list=target_cluster_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_msecs** | **int**| Specifies the start time of series stats. | [optional]
 **end_time_msecs** | **int**| Specifies the end time of series stats, by default it is current time. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **is_in_bound** | **bool**| Specifies whether to get inbound or outbound replication backlog stats. Default is false. | [optional]
 **target_cluster_list** | **[int]**| Filters stats to only include entities that were replicated to the specified target remote cluster IDs. | [optional]

### Return type

[**ReplicationObjectsList**](ReplicationObjectsList.md)

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

# **get_replication_objects_trend**
> TimeSeriesStats get_replication_objects_trend(start_time_msecs, rollup_interval_secs)



**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW, STORAGE_DOMAIN_VIEW, STORAGE_VIEW, PROTECTION_VIEW``` <br><br>Get replication object trends over time for all entities in the given schema.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.time_series_stats import TimeSeriesStats
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_msecs = 1 # int | Specifies the start time of series stats.
rollup_interval_secs = 1 # int | Specifies the time interval granularity for the specified rollup function.
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
prorate_data_points = True # bool | Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. (optional)
end_time_msecs = 1 # int | Specifies the end time of series stats, by default it is current time. (optional)
target_cluster_list = [
        1,
    ] # [int] | Filters stats to only include entities that were replicated to the specified target remote cluster IDs. (optional)

# example passing only required values which don't have defaults set
try:
	api_response = client.stats.get_replication_objects_trend(start_time_msecs, rollup_interval_secs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_objects_trend: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	api_response = client.stats.get_replication_objects_trend(start_time_msecs, rollup_interval_secs, include_tenants=include_tenants, prorate_data_points=prorate_data_points, end_time_msecs=end_time_msecs, target_cluster_list=target_cluster_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_replication_objects_trend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_msecs** | **int**| Specifies the start time of series stats. |
 **rollup_interval_secs** | **int**| Specifies the time interval granularity for the specified rollup function. |
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **prorate_data_points** | **bool**| Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. | [optional]
 **end_time_msecs** | **int**| Specifies the end time of series stats, by default it is current time. | [optional]
 **target_cluster_list** | **[int]**| Filters stats to only include entities that were replicated to the specified target remote cluster IDs. | [optional]

### Return type

[**TimeSeriesStats**](TimeSeriesStats.md)

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

# **get_restore_stats**
> RestoreStats get_restore_stats(start_time_usecs, end_time_usecs)

Compute the statistics on the Restore tasks on the cluster.

**Privileges:** ```RESTORE_VIEW``` <br><br>Compute the statistics on the Restore tasks on the cluster based on the provided time interval.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.restore_stats import RestoreStats
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_usecs = 1 # int | Specifies the start time Unix time epoch in microseconds from which the restore stats are computed.
end_time_usecs = 1 # int | Specifies the end time Unix time epoch in microseconds to which the restore stats are computed.

# example passing only required values which don't have defaults set
try:
	# Compute the statistics on the Restore tasks on the cluster.
	api_response = client.stats.get_restore_stats(start_time_usecs, end_time_usecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_restore_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_usecs** | **int**| Specifies the start time Unix time epoch in microseconds from which the restore stats are computed. |
 **end_time_usecs** | **int**| Specifies the end time Unix time epoch in microseconds to which the restore stats are computed. |

### Return type

[**RestoreStats**](RestoreStats.md)

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

# **get_time_series_stats**
> TimeSeriesStats get_time_series_stats(schema_name, metric_names, start_time_msecs)

Get Time Series Stats.

**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW, STORAGE_DOMAIN_VIEW, STORAGE_VIEW, PROTECTION_VIEW``` <br><br>Get Time Series Stats.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.time_series_stats import TimeSeriesStats
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


schema_name = "schemaName_example" # str | Specifies the schema name.
metric_names = [
        "metricNames_example",
    ] # [str] | Specifies a list of metric names.
start_time_msecs = 1 # int | Specifies the start time of series stats.
entity_id = "entityId_example" # str | Specifies the entity id. (optional)
entity_id_list = [
        "entityIdList_example",
    ] # [str] | Specifies an entity id list represented as a string. The stats result will be the sum over all these entities. Duplicate id's will be ignored. If both EntityIdList and EntityId are specified, EntityId will be ignored. (optional)
prorate_data_points = True # bool | Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. This should be used only when rollup function is provided. (optional)
include_growth_change = True # bool | Specifies if the response should return the difference of a data point with the previous datapoint. Used for determining the change in growth rate. Datapoint could be +x, 0, -x showing the growth is up, no change or down respectively. (optional)
end_time_msecs = 1 # int | Specifies the end time of series stats, by default it is current time. (optional)
rollup_function = "kSum" # str | Specifies the rollup function to apply to the data points for the time interval specified by rollupInternalSecs. (optional)
rollup_interval_secs = 1 # int | Specifies the time interval granularity for the specified rollup function. (optional)

# example passing only required values which don't have defaults set
try:
	# Get Time Series Stats.
	api_response = client.stats.get_time_series_stats(schema_name, metric_names, start_time_msecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_time_series_stats: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Time Series Stats.
	api_response = client.stats.get_time_series_stats(schema_name, metric_names, start_time_msecs, entity_id=entity_id, entity_id_list=entity_id_list, prorate_data_points=prorate_data_points, include_growth_change=include_growth_change, end_time_msecs=end_time_msecs, rollup_function=rollup_function, rollup_interval_secs=rollup_interval_secs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_time_series_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**| Specifies the schema name. |
 **metric_names** | **[str]**| Specifies a list of metric names. |
 **start_time_msecs** | **int**| Specifies the start time of series stats. |
 **entity_id** | **str**| Specifies the entity id. | [optional]
 **entity_id_list** | **[str]**| Specifies an entity id list represented as a string. The stats result will be the sum over all these entities. Duplicate id&#39;s will be ignored. If both EntityIdList and EntityId are specified, EntityId will be ignored. | [optional]
 **prorate_data_points** | **bool**| Specifies to create pro rated data point for every rollup interval instead of returning the actual raw data points. This should be used only when rollup function is provided. | [optional]
 **include_growth_change** | **bool**| Specifies if the response should return the difference of a data point with the previous datapoint. Used for determining the change in growth rate. Datapoint could be +x, 0, -x showing the growth is up, no change or down respectively. | [optional]
 **end_time_msecs** | **int**| Specifies the end time of series stats, by default it is current time. | [optional]
 **rollup_function** | **str**| Specifies the rollup function to apply to the data points for the time interval specified by rollupInternalSecs. | [optional]
 **rollup_interval_secs** | **int**| Specifies the time interval granularity for the specified rollup function. | [optional]

### Return type

[**TimeSeriesStats**](TimeSeriesStats.md)

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

# **get_top_views_stats**
> ViewsStats get_top_views_stats()

Get stats for the top views, which are the views with largest value of 'stats.valueInLastHours' for a given combination of 'metric', 'protocol' & 'lastHours' params. The API uses suitable defaults if any of the parameters are not specified.

**Privileges:** ```STORAGE_VIEW``` <br><br>Get stats for the top views, which are the views with largest value of 'stats.valueInLastHours' for a given combination of 'metric', 'protocol' & 'lastHours' params. The API uses suitable defaults if any of the parameters are not specified.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.views_stats import ViewsStats
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


metric = "kNumBytesRead" # str, none_type | Specifies the metric to which stats has to be sorted. Defaults to kNumBytesRead. (optional) if omitted the server will use the default value of "kNumBytesRead"
protocol = "kAny" # str, none_type | Specifies the protocol to sort. Defaults to kAny. (optional) if omitted the server will use the default value of "kAny"
num_top_views = 100 # int, none_type | Specifies the number of view for which stats has to be computed. Returned Views will be sorted in descending order based on the 'metric' param. Minimum value has to be 1. Defaults to 100. (optional) if omitted the server will use the default value of 100
last_hours = 24 # int, none_type | Specifies the last hours of stats to sort. Defaults to 24. (optional) if omitted the server will use the default value of 24

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get stats for the top views, which are the views with largest value of 'stats.valueInLastHours' for a given combination of 'metric', 'protocol' & 'lastHours' params. The API uses suitable defaults if any of the parameters are not specified.
	api_response = client.stats.get_top_views_stats(metric=metric, protocol=protocol, num_top_views=num_top_views, last_hours=last_hours)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_top_views_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str, none_type**| Specifies the metric to which stats has to be sorted. Defaults to kNumBytesRead. | [optional] if omitted the server will use the default value of "kNumBytesRead"
 **protocol** | **str, none_type**| Specifies the protocol to sort. Defaults to kAny. | [optional] if omitted the server will use the default value of "kAny"
 **num_top_views** | **int, none_type**| Specifies the number of view for which stats has to be computed. Returned Views will be sorted in descending order based on the &#39;metric&#39; param. Minimum value has to be 1. Defaults to 100. | [optional] if omitted the server will use the default value of 100
 **last_hours** | **int, none_type**| Specifies the last hours of stats to sort. Defaults to 24. | [optional] if omitted the server will use the default value of 24

### Return type

[**ViewsStats**](ViewsStats.md)

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

# **get_view_client_stats**
> ViewClientsStats get_view_client_stats()

Get Stats of View Clients

**Privileges:** ```STORAGE_VIEW``` <br><br>Get Stats of View Clients.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.view_clients_stats import ViewClientsStats
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **get_views_stats**
> ViewsStats get_views_stats()

Get stats for the top views, which are the views with largest value of 'stats.valueInLastHours' for a given combination of 'metric', 'protocol' & 'lastHours' params. The API uses suitable defaults if any of the parameters are not specified.

**Privileges:** ```STORAGE_VIEW``` <br><br>This api will be deprecated. Use the API '/stats/top-views' instead.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.views_stats import ViewsStats
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


metric = "kNumBytesRead" # str, none_type | Specifies the metric to which stats has to be sorted. Defaults to kNumBytesRead. (optional) if omitted the server will use the default value of "kNumBytesRead"
protocol = "kAny" # str, none_type | Specifies the protocol to sort. Defaults to kAny. (optional) if omitted the server will use the default value of "kAny"
num_top_views = 100 # int, none_type | Specifies the number of view for which stats has to be computed. Returned Views will be sorted in descending order based on the 'metric' param. Minimum value has to be 1. Defaults to 100. (optional) if omitted the server will use the default value of 100
last_hours = 24 # int, none_type | Specifies the last hours of stats to sort. Defaults to 24. (optional) if omitted the server will use the default value of 24

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get stats for the top views, which are the views with largest value of 'stats.valueInLastHours' for a given combination of 'metric', 'protocol' & 'lastHours' params. The API uses suitable defaults if any of the parameters are not specified.
	api_response = client.stats.get_views_stats(metric=metric, protocol=protocol, num_top_views=num_top_views, last_hours=last_hours)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_views_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str, none_type**| Specifies the metric to which stats has to be sorted. Defaults to kNumBytesRead. | [optional] if omitted the server will use the default value of "kNumBytesRead"
 **protocol** | **str, none_type**| Specifies the protocol to sort. Defaults to kAny. | [optional] if omitted the server will use the default value of "kAny"
 **num_top_views** | **int, none_type**| Specifies the number of view for which stats has to be computed. Returned Views will be sorted in descending order based on the &#39;metric&#39; param. Minimum value has to be 1. Defaults to 100. | [optional] if omitted the server will use the default value of 100
 **last_hours** | **int, none_type**| Specifies the last hours of stats to sort. Defaults to 24. | [optional] if omitted the server will use the default value of 24

### Return type

[**ViewsStats**](ViewsStats.md)

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

# **get_workload_stats**
> WorkloadStatsSummary get_workload_stats()

Get Workload Stats Schema.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get Workload Stats Schema. API will provide the high level information about different Workloads on Cohesity cluster along with their Entity Ids.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.workload_stats_summary import WorkloadStatsSummary
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
	# Get Workload Stats Schema.
	api_response = client.stats.get_workload_stats()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StatsApi->get_workload_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkloadStatsSummary**](WorkloadStatsSummary.md)

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

