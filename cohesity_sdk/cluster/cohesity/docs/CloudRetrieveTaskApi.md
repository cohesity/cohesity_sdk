# cohesity_sdk.cluster.CloudRetrieveTaskApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_retrieve_task**](CloudRetrieveTaskApi.md#create_cloud_retrieve_task) | **POST** /data-protect/retrieve | Create a cloud retrieve task.
[**get_cloud_retrieve_task_by_job_id**](CloudRetrieveTaskApi.md#get_cloud_retrieve_task_by_job_id) | **GET** /data-protect/retrieve/{jobId} | List details about the cloud retrieve task with the specific job id.
[**get_cloud_retrieve_tasks**](CloudRetrieveTaskApi.md#get_cloud_retrieve_tasks) | **GET** /data-protect/retrieve | Get the list of cloud retrieve tasks.


# **create_cloud_retrieve_task**
> CreateCloudRetrieveTaskRespBody create_cloud_retrieve_task(body)

Create a cloud retrieve task.

```Unknown Privileges``` <br><br>Create a cloud retrieve task.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import cloud_retrieve_task
from cohesity_sdk.cluster.cohesity.model.create_cloud_retrieve_task_resp_body import CreateCloudRetrieveTaskRespBody
from cohesity_sdk.cluster.cohesity.model.create_cloud_retrieve_task_request import CreateCloudRetrieveTaskRequest
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_retrieve_task.CloudRetrieveTaskApi(api_client)
    body = CreateCloudRetrieveTaskRequest(
        cluster_id=1,
        end_time_usecs=1,
        job_ids=[
            "job_ids_example",
        ],
        retrieve_all_jobs=True,
        start_time_usecs=1,
        vault_ids=[
            1,
        ],
    ) # CreateCloudRetrieveTaskRequest | Specifies the parameters to create a cloud retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Create a cloud retrieve task.
        api_response = api_instance.create_cloud_retrieve_task(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CloudRetrieveTaskApi->create_cloud_retrieve_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCloudRetrieveTaskRequest**](CreateCloudRetrieveTaskRequest.md)| Specifies the parameters to create a cloud retrieve. |

### Return type

[**CreateCloudRetrieveTaskRespBody**](CreateCloudRetrieveTaskRespBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

```Unknown Privileges``` <br><br>Returns the cloud retrieve task corresponding to the job id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import cloud_retrieve_task
from cohesity_sdk.cluster.cohesity.model.cloud_retrieve_task import CloudRetrieveTask
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_retrieve_task.CloudRetrieveTaskApi(api_client)
    job_id = 1 # int | Specifies a job id of the cloud retrieve task.

    # example passing only required values which don't have defaults set
    try:
        # List details about the cloud retrieve task with the specific job id.
        api_response = api_instance.get_cloud_retrieve_task_by_job_id(job_id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CloudRetrieveTaskApi->get_cloud_retrieve_task_by_job_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Specifies a job id of the cloud retrieve task. |

### Return type

[**CloudRetrieveTask**](CloudRetrieveTask.md)

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

# **get_cloud_retrieve_tasks**
> CloudRetrieveTasks get_cloud_retrieve_tasks()

Get the list of cloud retrieve tasks.

```Unknown Privileges``` <br><br>Get the list of cloud retrieve tasks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import cloud_retrieve_task
from cohesity_sdk.cluster.cohesity.model.cloud_retrieve_tasks import CloudRetrieveTasks
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_retrieve_task.CloudRetrieveTaskApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the list of cloud retrieve tasks.
        api_response = api_instance.get_cloud_retrieve_tasks()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CloudRetrieveTaskApi->get_cloud_retrieve_tasks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudRetrieveTasks**](CloudRetrieveTasks.md)

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

