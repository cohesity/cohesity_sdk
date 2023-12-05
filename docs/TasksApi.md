# cohesity_sdk.TasksApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_progress_tasks**](TasksApi.md#get_progress_tasks) | **GET** /tasks | Get tasks details.


# **get_progress_tasks**
> ProgressTasks get_progress_tasks()

Get tasks details.

Get details about tasks by providing task ids.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.progress_tasks import ProgressTasks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

ids = [
        "ids_example",
    ] # [str] | Specifies a unique task id to get the deatils of a task. To fetch the status of multiple tasks, pass comma seperated list of taskIds. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get tasks details.
	api_response = client.tasks.get_progress_tasks(ids=ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TasksApi->get_progress_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Specifies a unique task id to get the deatils of a task. To fetch the status of multiple tasks, pass comma seperated list of taskIds. | [optional]

### Return type

[**ProgressTasks**](ProgressTasks.md)

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

