# cohesity_sdk.cluster.CloudRetrieveTaskApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_retrieve_task**](CloudRetrieveTaskApi.md#create_cloud_retrieve_task) | **POST** /data-protect/retrieve | Create a cloud retrieve task.
[**get_cloud_retrieve_task_by_job_id**](CloudRetrieveTaskApi.md#get_cloud_retrieve_task_by_job_id) | **GET** /data-protect/retrieve/{jobId} | List details about the cloud retrieve task with the specific job id.
[**get_cloud_retrieve_tasks**](CloudRetrieveTaskApi.md#get_cloud_retrieve_tasks) | **GET** /data-protect/retrieve | Get the list of cloud retrieve tasks.


# **create_cloud_retrieve_task**
> CreateCloudRetrieveTaskRespBody create_cloud_retrieve_task(body)

Create a cloud retrieve task.

Create a cloud retrieve task.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_cloud_retrieve_task_request import CreateCloudRetrieveTaskRequest
from cohesity_sdk.cluster.models.create_cloud_retrieve_task_resp_body import CreateCloudRetrieveTaskRespBody
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.CloudRetrieveTaskApi(api_client)
    body = cohesity_sdk.cluster.CreateCloudRetrieveTaskRequest() # CreateCloudRetrieveTaskRequest | Specifies the parameters to create a cloud retrieve.

    try:
        # Create a cloud retrieve task.
        api_response = api_instance.create_cloud_retrieve_task(body)
        print("The response of CloudRetrieveTaskApi->create_cloud_retrieve_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRetrieveTaskApi->create_cloud_retrieve_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCloudRetrieveTaskRequest**](CreateCloudRetrieveTaskRequest.md)| Specifies the parameters to create a cloud retrieve. | 

### Return type

[**CreateCloudRetrieveTaskRespBody**](CreateCloudRetrieveTaskRespBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_retrieve_task_by_job_id**
> CloudRetrieveTask get_cloud_retrieve_task_by_job_id(job_id)

List details about the cloud retrieve task with the specific job id.

Returns the cloud retrieve task corresponding to the job id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cloud_retrieve_task import CloudRetrieveTask
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.CloudRetrieveTaskApi(api_client)
    job_id = 56 # int | Specifies a job id of the cloud retrieve task.

    try:
        # List details about the cloud retrieve task with the specific job id.
        api_response = api_instance.get_cloud_retrieve_task_by_job_id(job_id)
        print("The response of CloudRetrieveTaskApi->get_cloud_retrieve_task_by_job_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRetrieveTaskApi->get_cloud_retrieve_task_by_job_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Specifies a job id of the cloud retrieve task. | 

### Return type

[**CloudRetrieveTask**](CloudRetrieveTask.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_retrieve_tasks**
> CloudRetrieveTasks get_cloud_retrieve_tasks()

Get the list of cloud retrieve tasks.

Get the list of cloud retrieve tasks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cloud_retrieve_tasks import CloudRetrieveTasks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.CloudRetrieveTaskApi(api_client)

    try:
        # Get the list of cloud retrieve tasks.
        api_response = api_instance.get_cloud_retrieve_tasks()
        print("The response of CloudRetrieveTaskApi->get_cloud_retrieve_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudRetrieveTaskApi->get_cloud_retrieve_tasks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CloudRetrieveTasks**](CloudRetrieveTasks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

