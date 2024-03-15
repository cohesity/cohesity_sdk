# cohesity_sdk.CloudRetrieveTaskApi


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

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_cloud_retrieve_task_request import CreateCloudRetrieveTaskRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_cloud_retrieve_task_resp_body import CreateCloudRetrieveTaskRespBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

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
	api_response = client.cloud_retrieve_task.create_cloud_retrieve_task(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CloudRetrieveTaskApi->create_cloud_retrieve_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCloudRetrieveTaskRequest**](CreateCloudRetrieveTaskRequest.md)| Specifies the parameters to create a cloud retrieve. |

### Return type

[**CreateCloudRetrieveTaskRespBody**](CreateCloudRetrieveTaskRespBody.md)

### Authorization

No authorization required

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

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cloud_retrieve_task import CloudRetrieveTask
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

job_id = 1 # int | Specifies a job id of the cloud retrieve task.

# example passing only required values which don't have defaults set
try:
	# List details about the cloud retrieve task with the specific job id.
	api_response = client.cloud_retrieve_task.get_cloud_retrieve_task_by_job_id(job_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CloudRetrieveTaskApi->get_cloud_retrieve_task_by_job_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Specifies a job id of the cloud retrieve task. |

### Return type

[**CloudRetrieveTask**](CloudRetrieveTask.md)

### Authorization

No authorization required

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

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cloud_retrieve_tasks import CloudRetrieveTasks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)


# example, this endpoint has no required or optional parameters
try:
	# Get the list of cloud retrieve tasks.
	api_response = client.cloud_retrieve_task.get_cloud_retrieve_tasks()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CloudRetrieveTaskApi->get_cloud_retrieve_tasks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudRetrieveTasks**](CloudRetrieveTasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

