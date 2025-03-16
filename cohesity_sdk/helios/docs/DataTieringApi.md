# cohesity_sdk.helios.DataTieringApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_data_tiering_analysis_group_run**](DataTieringApi.md#cancel_data_tiering_analysis_group_run) | **POST** /data-tiering/analysis-groups/{id}/runs/{runId}/cancel | Cancel data tiering analysis run.
[**cancel_data_tiering_task_run**](DataTieringApi.md#cancel_data_tiering_task_run) | **POST** /data-tiering/tasks/{id}/runs/{runId}/cancel | Cancel data tiering task.
[**create_data_tiering_analysis_group**](DataTieringApi.md#create_data_tiering_analysis_group) | **POST** /data-tiering/analysis-groups | Create a data tiering analysis group.
[**create_data_tiering_analysis_group_run**](DataTieringApi.md#create_data_tiering_analysis_group_run) | **POST** /data-tiering/analysis-groups/{id}/runs | Create a data tiering analysis group run.
[**create_data_tiering_task**](DataTieringApi.md#create_data_tiering_task) | **POST** /data-tiering/tasks | Create a data tiering task.
[**create_data_tiering_task_run**](DataTieringApi.md#create_data_tiering_task_run) | **POST** /data-tiering/tasks/{id}/runs | Create a data tiering tasks run.
[**delete_data_tiering_analysis_group**](DataTieringApi.md#delete_data_tiering_analysis_group) | **DELETE** /data-tiering/analysis-groups/{id} | Delete data tiering analysis group.
[**delete_data_tiering_task**](DataTieringApi.md#delete_data_tiering_task) | **DELETE** /data-tiering/tasks/{id} | delete the data tiering task.
[**get_capacity_trend_analysis**](DataTieringApi.md#get_capacity_trend_analysis) | **GET** /data-tiering/capacity-trend | Get capacity trend analysis for all sources or a specific source.
[**get_data_tiering_analysis_group_by_id**](DataTieringApi.md#get_data_tiering_analysis_group_by_id) | **GET** /data-tiering/analysis-groups/{id} | Get data tiering analysis group by id.
[**get_data_tiering_analysis_group_runs**](DataTieringApi.md#get_data_tiering_analysis_group_runs) | **GET** /data-tiering/analysis-groups/{id}/runs | Get data tiering analysis group runs.
[**get_data_tiering_analysis_groups**](DataTieringApi.md#get_data_tiering_analysis_groups) | **GET** /data-tiering/analysis-groups | Get the list of data tiering analysis groups.
[**get_data_tiering_analysis_groups_default_config**](DataTieringApi.md#get_data_tiering_analysis_groups_default_config) | **GET** /data-tiering/analysis-groups/config | Get the default config of data tiering analysis groups.
[**get_data_tiering_task_by_id**](DataTieringApi.md#get_data_tiering_task_by_id) | **GET** /data-tiering/tasks/{id} | Get data tiering task by id.
[**get_data_tiering_tasks**](DataTieringApi.md#get_data_tiering_tasks) | **GET** /data-tiering/tasks | Get the list of data tiering tasks.
[**update_data_tiering_analysis_group**](DataTieringApi.md#update_data_tiering_analysis_group) | **PUT** /data-tiering/analysis-groups/{id} | Update a data tiering analysis group. Currently, it supports updating sources and schedule only.
[**update_data_tiering_analysis_group_tags_config**](DataTieringApi.md#update_data_tiering_analysis_group_tags_config) | **PUT** /data-tiering/analysis-groups/{id}/config | Update data tiering analysis group config.
[**update_data_tiering_analysis_groups_state**](DataTieringApi.md#update_data_tiering_analysis_groups_state) | **POST** /data-tiering/analysis-groups/states | Update data tiering analysis groups state.
[**update_data_tiering_task**](DataTieringApi.md#update_data_tiering_task) | **PUT** /data-tiering/tasks/{id} | Update a data tiering task.
[**update_data_tiering_tasks_state**](DataTieringApi.md#update_data_tiering_tasks_state) | **POST** /data-tiering/tasks/states | Update data tiering source analysis tasks state.


# **cancel_data_tiering_analysis_group_run**
> cancel_data_tiering_analysis_group_run(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id)

Cancel data tiering analysis run.

Cancel data tiering analysis run for given analysis group ID and run ID

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies a unique id of data tiering group.
    run_id = 'run_id_example' # str | Specifies a unique run id of data tiering group run.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Cancel data tiering analysis run.
        api_instance.cancel_data_tiering_analysis_group_run(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling DataTieringApi->cancel_data_tiering_analysis_group_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of data tiering group. | 
 **run_id** | **str**| Specifies a unique run id of data tiering group run. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_data_tiering_task_run**
> cancel_data_tiering_task_run(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id)

Cancel data tiering task.

Cancel data tiering task run for given data tiering task id and run id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies a unique id of data tiering task.
    run_id = 'run_id_example' # str | Specifies a unique run id of data tiering task.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Cancel data tiering task.
        api_instance.cancel_data_tiering_task_run(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling DataTieringApi->cancel_data_tiering_task_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of data tiering task. | 
 **run_id** | **str**| Specifies a unique run id of data tiering task. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_tiering_analysis_group**
> DataTieringAnalysisGroup create_data_tiering_analysis_group(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create a data tiering analysis group.

Create a data tiering analysis group.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.common_data_tiering_analysis_group_params import CommonDataTieringAnalysisGroupParams
from cohesity_sdk.helios.models.data_tiering_analysis_group import DataTieringAnalysisGroup
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    body = cohesity_sdk.helios.CommonDataTieringAnalysisGroupParams() # CommonDataTieringAnalysisGroupParams | Specifies the data tiering analysis group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create a data tiering analysis group.
        api_response = api_instance.create_data_tiering_analysis_group(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->create_data_tiering_analysis_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->create_data_tiering_analysis_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonDataTieringAnalysisGroupParams**](CommonDataTieringAnalysisGroupParams.md)| Specifies the data tiering analysis group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringAnalysisGroup**](DataTieringAnalysisGroup.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_tiering_analysis_group_run**
> create_data_tiering_analysis_group_run(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)

Create a data tiering analysis group run.

Create a data tiering analysis group run.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_analysis_run_request import DataTieringAnalysisRunRequest
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies the id of the data tiering analysis group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    body = cohesity_sdk.helios.DataTieringAnalysisRunRequest() # DataTieringAnalysisRunRequest | Specifies the request to run analysis group once. (optional)

    try:
        # Create a data tiering analysis group run.
        api_instance.create_data_tiering_analysis_group_run(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)
    except Exception as e:
        print("Exception when calling DataTieringApi->create_data_tiering_analysis_group_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering analysis group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **body** | [**DataTieringAnalysisRunRequest**](DataTieringAnalysisRunRequest.md)| Specifies the request to run analysis group once. | [optional] 

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
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_tiering_task**
> DataTieringTask create_data_tiering_task(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create a data tiering task.

Create a data tiering task.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_or_update_data_tiering_task_request import CreateOrUpdateDataTieringTaskRequest
from cohesity_sdk.helios.models.data_tiering_task import DataTieringTask
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    body = cohesity_sdk.helios.CreateOrUpdateDataTieringTaskRequest() # CreateOrUpdateDataTieringTaskRequest | Specifies the parameters to create a data tiering task.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create a data tiering task.
        api_response = api_instance.create_data_tiering_task(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->create_data_tiering_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->create_data_tiering_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateDataTieringTaskRequest**](CreateOrUpdateDataTieringTaskRequest.md)| Specifies the parameters to create a data tiering task. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringTask**](DataTieringTask.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_tiering_task_run**
> create_data_tiering_task_run(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)

Create a data tiering tasks run.

Create a data tiering tasks run.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_task_run_request import DataTieringTaskRunRequest
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies the id of the data tiering tasks.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    body = cohesity_sdk.helios.DataTieringTaskRunRequest() # DataTieringTaskRunRequest | Specifies the request to run tiering task once. (optional)

    try:
        # Create a data tiering tasks run.
        api_instance.create_data_tiering_task_run(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)
    except Exception as e:
        print("Exception when calling DataTieringApi->create_data_tiering_task_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering tasks. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **body** | [**DataTieringTaskRunRequest**](DataTieringTaskRunRequest.md)| Specifies the request to run tiering task once. | [optional] 

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
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_tiering_analysis_group**
> delete_data_tiering_analysis_group(id, access_cluster_id=access_cluster_id, region_id=region_id)

Delete data tiering analysis group.

Returns NoContentResponse if the data tiering analysis group is deleted.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the data tiering analysis group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete data tiering analysis group.
        api_instance.delete_data_tiering_analysis_group(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling DataTieringApi->delete_data_tiering_analysis_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_tiering_task**
> delete_data_tiering_task(id, access_cluster_id=access_cluster_id, region_id=region_id)

delete the data tiering task.

Returns Success if the data tiering task is deleted.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies the id of the data tiering task.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # delete the data tiering task.
        api_instance.delete_data_tiering_task(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling DataTieringApi->delete_data_tiering_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering task. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capacity_trend_analysis**
> CapacityTrendAnalysis get_capacity_trend_analysis(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, source_id=source_id)

Get capacity trend analysis for all sources or a specific source.

Get capacity trend analysis for the given time range, and for the given source or set of sources.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.capacity_trend_analysis import CapacityTrendAnalysis
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    start_time_usecs = 56 # int | Filter by a start time. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
    end_time_usecs = 56 # int | Filter by a end time. Specify the end time as a Unix epoch Timestamp (in microseconds). (optional)
    source_id = 56 # int | Filter by source id. If specified, this will only return the capacity trend analysis of the specific source. (optional)

    try:
        # Get capacity trend analysis for all sources or a specific source.
        api_response = api_instance.get_capacity_trend_analysis(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, source_id=source_id)
        print("The response of DataTieringApi->get_capacity_trend_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->get_capacity_trend_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **start_time_usecs** | **int**| Filter by a start time. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional] 
 **end_time_usecs** | **int**| Filter by a end time. Specify the end time as a Unix epoch Timestamp (in microseconds). | [optional] 
 **source_id** | **int**| Filter by source id. If specified, this will only return the capacity trend analysis of the specific source. | [optional] 

### Return type

[**CapacityTrendAnalysis**](CapacityTrendAnalysis.md)

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

# **get_data_tiering_analysis_group_by_id**
> DataTieringAnalysisGroup get_data_tiering_analysis_group_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)

Get data tiering analysis group by id.

Get data tiering analysis group by id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_analysis_group import DataTieringAnalysisGroup
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the data tiering analysis group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get data tiering analysis group by id.
        api_response = api_instance.get_data_tiering_analysis_group_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->get_data_tiering_analysis_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->get_data_tiering_analysis_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringAnalysisGroup**](DataTieringAnalysisGroup.md)

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

# **get_data_tiering_analysis_group_runs**
> List[DataTieringAnalysisGroupRun] get_data_tiering_analysis_group_runs(id, access_cluster_id=access_cluster_id, region_id=region_id, run_ids=run_ids)

Get data tiering analysis group runs.

Get data tiering analysis group runs for an analysis group.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_analysis_group_run import DataTieringAnalysisGroupRun
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the data tiering analysis group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    run_ids = ['run_ids_example'] # List[str] | Filter by a list of analysis group run ids. (optional)

    try:
        # Get data tiering analysis group runs.
        api_response = api_instance.get_data_tiering_analysis_group_runs(id, access_cluster_id=access_cluster_id, region_id=region_id, run_ids=run_ids)
        print("The response of DataTieringApi->get_data_tiering_analysis_group_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->get_data_tiering_analysis_group_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **run_ids** | [**List[str]**](str.md)| Filter by a list of analysis group run ids. | [optional] 

### Return type

[**List[DataTieringAnalysisGroupRun]**](DataTieringAnalysisGroupRun.md)

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

# **get_data_tiering_analysis_groups**
> List[DataTieringAnalysisGroup] get_data_tiering_analysis_groups(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, include_last_run_stats=include_last_run_stats)

Get the list of data tiering analysis groups.

Get list of all data tiering analysis groups.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_analysis_group import DataTieringAnalysisGroup
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = ['ids_example'] # List[str] | Filter by a list of Analysis Group IDs. (optional)
    include_last_run_stats = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)

    try:
        # Get the list of data tiering analysis groups.
        api_response = api_instance.get_data_tiering_analysis_groups(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, include_last_run_stats=include_last_run_stats)
        print("The response of DataTieringApi->get_data_tiering_analysis_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->get_data_tiering_analysis_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[str]**](str.md)| Filter by a list of Analysis Group IDs. | [optional] 
 **include_last_run_stats** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional] 

### Return type

[**List[DataTieringAnalysisGroup]**](DataTieringAnalysisGroup.md)

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

# **get_data_tiering_analysis_groups_default_config**
> DataTieringTagConfig get_data_tiering_analysis_groups_default_config(access_cluster_id=access_cluster_id, region_id=region_id)

Get the default config of data tiering analysis groups.

Get default grouping configuration for data tiering analysis groups.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_tag_config import DataTieringTagConfig
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get the default config of data tiering analysis groups.
        api_response = api_instance.get_data_tiering_analysis_groups_default_config(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->get_data_tiering_analysis_groups_default_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->get_data_tiering_analysis_groups_default_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringTagConfig**](DataTieringTagConfig.md)

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

# **get_data_tiering_task_by_id**
> DataTieringTask get_data_tiering_task_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)

Get data tiering task by id.

Get data tiering task by id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_task import DataTieringTask
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies the id of the data tiering task.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get data tiering task by id.
        api_response = api_instance.get_data_tiering_task_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->get_data_tiering_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->get_data_tiering_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering task. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringTask**](DataTieringTask.md)

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

# **get_data_tiering_tasks**
> List[DataTieringTask] get_data_tiering_tasks(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, include_downtiered_data_location=include_downtiered_data_location)

Get the list of data tiering tasks.

Get the list of data tiering tasks.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_task import DataTieringTask
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = ['ids_example'] # List[str] | Filter by a list of data tiering task ids. (optional)
    include_downtiered_data_location = True # bool | If true, it will also return a list of downtiered data locations for downtiered tasks. (optional)

    try:
        # Get the list of data tiering tasks.
        api_response = api_instance.get_data_tiering_tasks(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, include_downtiered_data_location=include_downtiered_data_location)
        print("The response of DataTieringApi->get_data_tiering_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->get_data_tiering_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[str]**](str.md)| Filter by a list of data tiering task ids. | [optional] 
 **include_downtiered_data_location** | **bool**| If true, it will also return a list of downtiered data locations for downtiered tasks. | [optional] 

### Return type

[**List[DataTieringTask]**](DataTieringTask.md)

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

# **update_data_tiering_analysis_group**
> DataTieringAnalysisGroup update_data_tiering_analysis_group(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update a data tiering analysis group. Currently, it supports updating sources and schedule only.

Update a data tiering analysis group.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.common_data_tiering_analysis_group_params import CommonDataTieringAnalysisGroupParams
from cohesity_sdk.helios.models.data_tiering_analysis_group import DataTieringAnalysisGroup
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the data tiering analysis group.
    body = cohesity_sdk.helios.CommonDataTieringAnalysisGroupParams() # CommonDataTieringAnalysisGroupParams | Specifies the data tiering analysis group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update a data tiering analysis group. Currently, it supports updating sources and schedule only.
        api_response = api_instance.update_data_tiering_analysis_group(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->update_data_tiering_analysis_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->update_data_tiering_analysis_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. | 
 **body** | [**CommonDataTieringAnalysisGroupParams**](CommonDataTieringAnalysisGroupParams.md)| Specifies the data tiering analysis group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringAnalysisGroup**](DataTieringAnalysisGroup.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_tiering_analysis_group_tags_config**
> DataTieringTagConfig update_data_tiering_analysis_group_tags_config(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update data tiering analysis group config.

Update data tiering analysis group config.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.data_tiering_tag_config import DataTieringTagConfig
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the data tiering analysis group.
    body = cohesity_sdk.helios.DataTieringTagConfig() # DataTieringTagConfig | Specifies the data tiering analysis Tags Config.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update data tiering analysis group config.
        api_response = api_instance.update_data_tiering_analysis_group_tags_config(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->update_data_tiering_analysis_group_tags_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->update_data_tiering_analysis_group_tags_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. | 
 **body** | [**DataTieringTagConfig**](DataTieringTagConfig.md)| Specifies the data tiering analysis Tags Config. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringTagConfig**](DataTieringTagConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_tiering_analysis_groups_state**
> UpdateDataTieringState update_data_tiering_analysis_groups_state(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update data tiering analysis groups state.

Perform actions like pause or resume on the data tiering analysis groups for the specified sources.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.update_data_tiering_state import UpdateDataTieringState
from cohesity_sdk.helios.models.update_data_tiering_state_request import UpdateDataTieringStateRequest
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    body = cohesity_sdk.helios.UpdateDataTieringStateRequest() # UpdateDataTieringStateRequest | Specifies the parameters to perform an action of list of data tiering analysis groups.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update data tiering analysis groups state.
        api_response = api_instance.update_data_tiering_analysis_groups_state(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->update_data_tiering_analysis_groups_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->update_data_tiering_analysis_groups_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDataTieringStateRequest**](UpdateDataTieringStateRequest.md)| Specifies the parameters to perform an action of list of data tiering analysis groups. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**UpdateDataTieringState**](UpdateDataTieringState.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_tiering_task**
> DataTieringTask update_data_tiering_task(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update a data tiering task.

Update a data tiering task.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_or_update_data_tiering_task_request import CreateOrUpdateDataTieringTaskRequest
from cohesity_sdk.helios.models.data_tiering_task import DataTieringTask
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    id = 'id_example' # str | Specifies the id of the data tiering task.
    body = cohesity_sdk.helios.CreateOrUpdateDataTieringTaskRequest() # CreateOrUpdateDataTieringTaskRequest | Specifies the parameters to update a data tiering task.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update a data tiering task.
        api_response = api_instance.update_data_tiering_task(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->update_data_tiering_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->update_data_tiering_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering task. | 
 **body** | [**CreateOrUpdateDataTieringTaskRequest**](CreateOrUpdateDataTieringTaskRequest.md)| Specifies the parameters to update a data tiering task. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DataTieringTask**](DataTieringTask.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_tiering_tasks_state**
> UpdateDataTieringState update_data_tiering_tasks_state(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update data tiering source analysis tasks state.

Perform actions like pause or resume on the data tiering tasks.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.update_data_tiering_state import UpdateDataTieringState
from cohesity_sdk.helios.models.update_data_tiering_state_request import UpdateDataTieringStateRequest
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
    api_instance = cohesity_sdk.helios.DataTieringApi(api_client)
    body = cohesity_sdk.helios.UpdateDataTieringStateRequest() # UpdateDataTieringStateRequest | Specifies the parameters to perform an action of list of data tiering tasks.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update data tiering source analysis tasks state.
        api_response = api_instance.update_data_tiering_tasks_state(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of DataTieringApi->update_data_tiering_tasks_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTieringApi->update_data_tiering_tasks_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDataTieringStateRequest**](UpdateDataTieringStateRequest.md)| Specifies the parameters to perform an action of list of data tiering tasks. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**UpdateDataTieringState**](UpdateDataTieringState.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

