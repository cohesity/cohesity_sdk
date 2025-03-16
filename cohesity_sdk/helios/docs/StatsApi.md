# cohesity_sdk.helios.StatsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_throttling_stats**](StatsApi.md#fetch_throttling_stats) | **GET** /mcm/stats/{registrationId}/throttling | Fetch the throttling stats of a source.
[**get_cluster_storage_stats**](StatsApi.md#get_cluster_storage_stats) | **GET** /stats/cluster-storage | Get Cluster Storage Stats.
[**get_files_stats**](StatsApi.md#get_files_stats) | **GET** /stats/files | Get Stats of Files.
[**get_protection_runs_stats**](StatsApi.md#get_protection_runs_stats) | **GET** /stats/protection-runs | Get statistics of protection runs.
[**get_time_series_stats**](StatsApi.md#get_time_series_stats) | **GET** /stats/time-series-stats | Get Time Series Stats.
[**get_view_client_stats**](StatsApi.md#get_view_client_stats) | **GET** /stats/view-clients | Get Stats of View Clients
[**get_views_stats**](StatsApi.md#get_views_stats) | **GET** /stats/views | Get Views Stats.
[**get_workload_stats**](StatsApi.md#get_workload_stats) | **GET** /stats/workload-stats | Get Workload Stats Schema.
[**mcm_get_policy_last_run_stats**](StatsApi.md#mcm_get_policy_last_run_stats) | **GET** /mcm/stats/policies/last-run | Compute stats of last Protection Run of Protection Policies.
[**mcm_get_protection_run_last_run_stats**](StatsApi.md#mcm_get_protection_run_last_run_stats) | **GET** /mcm/stats/protection-runs/last-run | Compute stats of last Protection Run across all objects.


# **fetch_throttling_stats**
> FetchThrottlingStatsResponseBody fetch_throttling_stats(registration_id, source_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, workload_type=workload_type, api_type=api_type)

Fetch the throttling stats of a source.

Compute the throttling stats for a source and return time series data.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.fetch_throttling_stats_response_body import FetchThrottlingStatsResponseBody
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    registration_id = 'registration_id_example' # str | Specifies the registration id of the protected source. It is of the format {clusterID}:{IncarnationId}:{EntityId}.
    source_id = 'source_id_example' # str | Specifies the source name for which throttling stats are needed. In case of Office365, it is the domain name which is unique.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    start_time_usecs = 56 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
    end_time_usecs = 56 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
    workload_type = ['workload_type_example'] # List[str] | Specifies the list of workload types within the source for which throttling stats are needed. (optional)
    api_type = ['api_type_example'] # List[str] | Specifies the list of api type within the source for which throttling stats are needed. (optional)

    try:
        # Fetch the throttling stats of a source.
        api_response = api_instance.fetch_throttling_stats(registration_id, source_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, workload_type=workload_type, api_type=api_type)
        print("The response of StatsApi->fetch_throttling_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->fetch_throttling_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| Specifies the registration id of the protected source. It is of the format {clusterID}:{IncarnationId}:{EntityId}. | 
 **source_id** | **str**| Specifies the source name for which throttling stats are needed. In case of Office365, it is the domain name which is unique. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional] 
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional] 
 **workload_type** | [**List[str]**](str.md)| Specifies the list of workload types within the source for which throttling stats are needed. | [optional] 
 **api_type** | [**List[str]**](str.md)| Specifies the list of api type within the source for which throttling stats are needed. | [optional] 

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
> ClusterStorageStats get_cluster_storage_stats(access_cluster_id=access_cluster_id, region_id=region_id)

Get Cluster Storage Stats.

Get Cluster Storage Stats.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.cluster_storage_stats import ClusterStorageStats
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Cluster Storage Stats.
        api_response = api_instance.get_cluster_storage_stats(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of StatsApi->get_cluster_storage_stats:\n")
        pprint(api_response)
    except Exception as e:
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
> FilesStats get_files_stats(access_cluster_id=access_cluster_id, region_id=region_id, entity_type=entity_type)

Get Stats of Files.

Get Stats of files.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.files_stats import FilesStats
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    entity_type = 'entity_type_example' # str | Specifies the entity type based on which the files stats are calculated. By default stats are calculated based on Cluster (optional)

    try:
        # Get Stats of Files.
        api_response = api_instance.get_files_stats(access_cluster_id=access_cluster_id, region_id=region_id, entity_type=entity_type)
        print("The response of StatsApi->get_files_stats:\n")
        pprint(api_response)
    except Exception as e:
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
> GetProtectionRunsStatusResponseBody get_protection_runs_stats(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)

Get statistics of protection runs.

Get statistics of protection runs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_protection_runs_status_response_body import GetProtectionRunsStatusResponseBody
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    start_time_usecs = 56 # int | Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be counted. By default it is current time minus a day. (optional)
    end_time_usecs = 56 # int | Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be counted. By default it is current time. (optional)
    run_status = ['run_status_example'] # List[str] | Specifies a list of status, runs matching the status will be returned. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Failed' indicates that the run has failed. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)

    try:
        # Get statistics of protection runs.
        api_response = api_instance.get_protection_runs_stats(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)
        print("The response of StatsApi->get_protection_runs_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_protection_runs_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **start_time_usecs** | **int**| Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be counted. By default it is current time minus a day. | [optional] 
 **end_time_usecs** | **int**| Specify the end time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be counted. By default it is current time. | [optional] 
 **run_status** | [**List[str]**](str.md)| Specifies a list of status, runs matching the status will be returned. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 

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
> TimeSeriesStats get_time_series_stats(schema_name, metric_names, entity_id, start_time_msecs, access_cluster_id=access_cluster_id, region_id=region_id, end_time_msecs=end_time_msecs, rollup_function=rollup_function, rollup_interval_secs=rollup_interval_secs)

Get Time Series Stats.

Get Time Series Stats.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.time_series_stats import TimeSeriesStats
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    schema_name = 'schema_name_example' # str | Specifies the schema name.
    metric_names = ['metric_names_example'] # List[str] | Specifies a list of metric names.
    entity_id = 'entity_id_example' # str | Specifies the entity id.
    start_time_msecs = 56 # int | Specifies the start time of series stats.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    end_time_msecs = 56 # int | Specifies the end time of series stats, by default it is current time. (optional)
    rollup_function = 'rollup_function_example' # str | Specifies the rollup function to apply to the data points for the time interval specified by rollupInternalSecs. (optional)
    rollup_interval_secs = 56 # int | Specifies the time interval granularity for the specified rollup function. (optional)

    try:
        # Get Time Series Stats.
        api_response = api_instance.get_time_series_stats(schema_name, metric_names, entity_id, start_time_msecs, access_cluster_id=access_cluster_id, region_id=region_id, end_time_msecs=end_time_msecs, rollup_function=rollup_function, rollup_interval_secs=rollup_interval_secs)
        print("The response of StatsApi->get_time_series_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_time_series_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**| Specifies the schema name. | 
 **metric_names** | [**List[str]**](str.md)| Specifies a list of metric names. | 
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
> ViewClientsStats get_view_client_stats(access_cluster_id=access_cluster_id, region_id=region_id, metric=metric, num_top_view_clients=num_top_view_clients, last_hours=last_hours)

Get Stats of View Clients

Get Stats of View Clients.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.view_clients_stats import ViewClientsStats
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    metric = 'metric_example' # str | Specifies the metric to which stats has to be sorted. (optional)
    num_top_view_clients = 56 # int | Specifies the number of view clients for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view clients will be returned. If metric is not specified, this parameter must also not be specified. (optional)
    last_hours = 56 # int | Specifies the last hours of stats to sort. (optional)

    try:
        # Get Stats of View Clients
        api_response = api_instance.get_view_client_stats(access_cluster_id=access_cluster_id, region_id=region_id, metric=metric, num_top_view_clients=num_top_view_clients, last_hours=last_hours)
        print("The response of StatsApi->get_view_client_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_view_client_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **metric** | **str**| Specifies the metric to which stats has to be sorted. | [optional] 
 **num_top_view_clients** | **int**| Specifies the number of view clients for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view clients will be returned. If metric is not specified, this parameter must also not be specified. | [optional] 
 **last_hours** | **int**| Specifies the last hours of stats to sort. | [optional] 

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
> ViewsStats get_views_stats(access_cluster_id=access_cluster_id, region_id=region_id, metric=metric, protocol=protocol, num_top_views=num_top_views, last_hours=last_hours)

Get Views Stats.

Get Views Stats.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.views_stats import ViewsStats
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    metric = 'metric_example' # str | Specifies the metric to which stats has to be sorted. (optional)
    protocol = 'protocol_example' # str | Specifies the protocol to sort. (optional)
    num_top_views = 56 # int | Specifies the number of view for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view will be returned. If metric is not specified, this parameter must also not be specified. (optional)
    last_hours = 56 # int | Specifies the last hours of stats to sort. (optional)

    try:
        # Get Views Stats.
        api_response = api_instance.get_views_stats(access_cluster_id=access_cluster_id, region_id=region_id, metric=metric, protocol=protocol, num_top_views=num_top_views, last_hours=last_hours)
        print("The response of StatsApi->get_views_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_views_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **metric** | **str**| Specifies the metric to which stats has to be sorted. | [optional] 
 **protocol** | **str**| Specifies the protocol to sort. | [optional] 
 **num_top_views** | **int**| Specifies the number of view for which stats has to be computed. Specifying this field will return the Views sorted in the descending order on the metric specified. If specified, minimum value is 1. If not specified, all view will be returned. If metric is not specified, this parameter must also not be specified. | [optional] 
 **last_hours** | **int**| Specifies the last hours of stats to sort. | [optional] 

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

# **get_workload_stats**
> WorkloadStatsSummary get_workload_stats(access_cluster_id=access_cluster_id, region_id=region_id)

Get Workload Stats Schema.

Get Workload Stats Schema. API will provide the high level information about different Workloads on Cohesity cluster along with their Entity Ids.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.workload_stats_summary import WorkloadStatsSummary
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Workload Stats Schema.
        api_response = api_instance.get_workload_stats(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of StatsApi->get_workload_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_workload_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**WorkloadStatsSummary**](WorkloadStatsSummary.md)

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
> McmGetPolicyLastRunStatsResponseBody mcm_get_policy_last_run_stats(region_id=region_id, region_ids=region_ids)

Compute stats of last Protection Run of Protection Policies.

Compute stats of last Protection Run of Protection Policies.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_get_policy_last_run_stats_response_body import McmGetPolicyLastRunStatsResponseBody
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)

    try:
        # Compute stats of last Protection Run of Protection Policies.
        api_response = api_instance.mcm_get_policy_last_run_stats(region_id=region_id, region_ids=region_ids)
        print("The response of StatsApi->mcm_get_policy_last_run_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->mcm_get_policy_last_run_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 

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
> McmGetProtectionLastRunStatsResponseBody mcm_get_protection_run_last_run_stats(region_id=region_id, region_ids=region_ids)

Compute stats of last Protection Run across all objects.

Compute stats of last Protection Run across all objects.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_get_protection_last_run_stats_response_body import McmGetProtectionLastRunStatsResponseBody
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.StatsApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)

    try:
        # Compute stats of last Protection Run across all objects.
        api_response = api_instance.mcm_get_protection_run_last_run_stats(region_id=region_id, region_ids=region_ids)
        print("The response of StatsApi->mcm_get_protection_run_last_run_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->mcm_get_protection_run_last_run_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 

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

