# cohesity_sdk.TestDataManagementApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tdm_task**](TestDataManagementApi.md#create_tdm_task) | **POST** /tdm/tasks | Create a TDM task
[**delete_tdm_snapshot_by_id**](TestDataManagementApi.md#delete_tdm_snapshot_by_id) | **DELETE** /tdm/snapshots/{id} | Delete a snapshot by ID
[**get_tdm_object_by_id**](TestDataManagementApi.md#get_tdm_object_by_id) | **GET** /tdm/objects/{id} | Get TDM object by ID
[**get_tdm_objects**](TestDataManagementApi.md#get_tdm_objects) | **GET** /tdm/objects | Get all TDM objects
[**get_tdm_task_by_id**](TestDataManagementApi.md#get_tdm_task_by_id) | **GET** /tdm/tasks/{id} | Get a TDM task by ID
[**get_tdm_tasks**](TestDataManagementApi.md#get_tdm_tasks) | **GET** /tdm/tasks | Get all TDM tasks
[**get_tdm_timeline_events_by_object_id**](TestDataManagementApi.md#get_tdm_timeline_events_by_object_id) | **GET** /tdm/objects/{id}/timeline-events | Get timeline events of object
[**perform_action_on_clones**](TestDataManagementApi.md#perform_action_on_clones) | **POST** /tdm/clones/actions | Perform actions on clones
[**update_tdm_snapshot_by_id**](TestDataManagementApi.md#update_tdm_snapshot_by_id) | **PUT** /tdm/snapshots/{id} | Update a snapshot by ID


# **create_tdm_task**
> TdmTask create_tdm_task(body)

Create a TDM task

Create a task for the Test Data Management (TDM) workflow.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.tdm_task import TdmTask
from cohesity_sdk.cluster.model.create_tdm_task_request import CreateTdmTaskRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = CreateTdmTaskRequest() # CreateTdmTaskRequest | Specifies the parameters to create a TDM task.

# example passing only required values which don't have defaults set
try:
	# Create a TDM task
	api_response = client.test_data_management.create_tdm_task(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->create_tdm_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTdmTaskRequest**](CreateTdmTaskRequest.md)| Specifies the parameters to create a TDM task. |

### Return type

[**TdmTask**](TdmTask.md)

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

# **delete_tdm_snapshot_by_id**
> delete_tdm_snapshot_by_id(id)

Delete a snapshot by ID

Delete a snapshot by specifying its ID.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = "id_example" # str | Specifies the ID of the snapshot.

# example passing only required values which don't have defaults set
try:
	# Delete a snapshot by ID
	client.test_data_management.delete_tdm_snapshot_by_id(id)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->delete_tdm_snapshot_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the snapshot. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tdm_object_by_id**
> TdmObject get_tdm_object_by_id(id)

Get TDM object by ID

Get a TDM object by specifying its ID.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tdm_object import TdmObject
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = "id_example" # str | Specifies the ID of the TDM object.

# example passing only required values which don't have defaults set
try:
	# Get TDM object by ID
	api_response = client.test_data_management.get_tdm_object_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->get_tdm_object_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the TDM object. |

### Return type

[**TdmObject**](TdmObject.md)

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

# **get_tdm_objects**
> TdmObjects get_tdm_objects()

Get all TDM objects

Get all TDM objects matching specified optional filter criteria.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tdm_objects import TdmObjects
from cohesity_sdk.cluster.model.error import Error
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
    ] # [str] | Get the objects matching specifies IDs. (optional)
environments = [
        "kSQL",
    ] # [str] | Get the objects matching specified environments. (optional)
name = "name_example" # str | Get the objects matching specified name. (optional)
task_ids = [
        "taskIds_example",
    ] # [str] | Get the objects belonging to the specified TDM task IDs. (optional)
statuses = [
        "scheduled",
    ] # [str] | Get the objects matching specified statuses. (optional)
pagination_cookie = "paginationCookie_example" # str | Get the next set of objects by specifying the cookie string, as received from the server in the last call. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get all TDM objects
	api_response = client.test_data_management.get_tdm_objects(ids=ids, environments=environments, name=name, task_ids=task_ids, statuses=statuses, pagination_cookie=pagination_cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->get_tdm_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Get the objects matching specifies IDs. | [optional]
 **environments** | **[str]**| Get the objects matching specified environments. | [optional]
 **name** | **str**| Get the objects matching specified name. | [optional]
 **task_ids** | **[str]**| Get the objects belonging to the specified TDM task IDs. | [optional]
 **statuses** | **[str]**| Get the objects matching specified statuses. | [optional]
 **pagination_cookie** | **str**| Get the next set of objects by specifying the cookie string, as received from the server in the last call. | [optional]

### Return type

[**TdmObjects**](TdmObjects.md)

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

# **get_tdm_task_by_id**
> TdmTask get_tdm_task_by_id(id)

Get a TDM task by ID

Get a TDM task by ID.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.tdm_task import TdmTask
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = "id_example" # str | Specifies the ID of the TDM task.

# example passing only required values which don't have defaults set
try:
	# Get a TDM task by ID
	api_response = client.test_data_management.get_tdm_task_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->get_tdm_task_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the TDM task. |

### Return type

[**TdmTask**](TdmTask.md)

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

# **get_tdm_tasks**
> TdmTasks get_tdm_tasks()

Get all TDM tasks

Get all the TDM tasks matching specified optional filter criteria.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.tdm_tasks import TdmTasks
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
    ] # [str] | Get the tasks matching specified IDs. (optional)
actions = [
        "clone",
    ] # [str] | Get the tasks matching specified actions. (optional)
environments = [
        "kSQL",
    ] # [str] | Get the tasks matching specified environments. (optional)
created_after_usecs = 1 # int | Get the tasks created after the specified time (in usecs from epoch). (optional)
created_before_usecs = 1 # int | Get the tasks created before the specified time (in usecs from epoch). (optional)
statuses = [
        "scheduled",
    ] # [str] | Get the tasks matching specified statuses. (optional)
object_ids = [
        "objectIds_example",
    ] # [str] | Get the tasks for the specified TDM object IDs. (optional)
pagination_cookie = "paginationCookie_example" # str | Get the next set of tasks by specifying the cookie string, as received from the server in the last call. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get all TDM tasks
	api_response = client.test_data_management.get_tdm_tasks(ids=ids, actions=actions, environments=environments, created_after_usecs=created_after_usecs, created_before_usecs=created_before_usecs, statuses=statuses, object_ids=object_ids, pagination_cookie=pagination_cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->get_tdm_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Get the tasks matching specified IDs. | [optional]
 **actions** | **[str]**| Get the tasks matching specified actions. | [optional]
 **environments** | **[str]**| Get the tasks matching specified environments. | [optional]
 **created_after_usecs** | **int**| Get the tasks created after the specified time (in usecs from epoch). | [optional]
 **created_before_usecs** | **int**| Get the tasks created before the specified time (in usecs from epoch). | [optional]
 **statuses** | **[str]**| Get the tasks matching specified statuses. | [optional]
 **object_ids** | **[str]**| Get the tasks for the specified TDM object IDs. | [optional]
 **pagination_cookie** | **str**| Get the next set of tasks by specifying the cookie string, as received from the server in the last call. | [optional]

### Return type

[**TdmTasks**](TdmTasks.md)

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

# **get_tdm_timeline_events_by_object_id**
> TdmObjectTimelineEvents get_tdm_timeline_events_by_object_id(id)

Get timeline events of object

Get the collection of timeline events of a TDM object by specifying its ID.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tdm_object_timeline_events import TdmObjectTimelineEvents
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = "id_example" # str | Specifies the ID of the TDM object.
created_after = 1 # int | Get the events created after the specified time (in usecs from epoch). (optional)
created_before = 1 # int | Get the events created before the specified time (in usecs from epoch). (optional)

# example passing only required values which don't have defaults set
try:
	# Get timeline events of object
	api_response = client.test_data_management.get_tdm_timeline_events_by_object_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->get_tdm_timeline_events_by_object_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get timeline events of object
	api_response = client.test_data_management.get_tdm_timeline_events_by_object_id(id, created_after=created_after, created_before=created_before)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->get_tdm_timeline_events_by_object_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the TDM object. |
 **created_after** | **int**| Get the events created after the specified time (in usecs from epoch). | [optional]
 **created_before** | **int**| Get the events created before the specified time (in usecs from epoch). | [optional]

### Return type

[**TdmObjectTimelineEvents**](TdmObjectTimelineEvents.md)

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

# **perform_action_on_clones**
> perform_action_on_clones(body)

Perform actions on clones

Performs various actions on clones. Supports actions on multiple clones.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.perform_action_on_clones_request import PerformActionOnClonesRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = PerformActionOnClonesRequest(
        action="Cleanup",
        cleanup_params=CloneActionCleanupParams(
            cleanup_type="PowerOffVM",
            cloud_resources_cleanup_params=CloneActionCleanupCloudResourcesCleanupParams(
                restore_tasks=[
                    CloudResourcesCleanupRestoreTaskDetails(
                        ami_instance_ids=[
                            CloudResourcesCleanupAmiInstanceId(
                                ami_id="ami_id_example",
                                instance_id="instance_id_example",
                            ),
                        ],
                        task_id=3.14,
                    ),
                ],
            ),
            power_off_vm_params=CloneActionCleanupPowerOffVmParams(
                vm_ids=[
                    3.14,
                ],
            ),
        ),
    ) # PerformActionOnClonesRequest | Specifies the parameters to perform an action on multiple clones.

# example passing only required values which don't have defaults set
try:
	# Perform actions on clones
	client.test_data_management.perform_action_on_clones(body)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->perform_action_on_clones: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformActionOnClonesRequest**](PerformActionOnClonesRequest.md)| Specifies the parameters to perform an action on multiple clones. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tdm_snapshot_by_id**
> TdmSnapshot update_tdm_snapshot_by_id(id, body)

Update a snapshot by ID

Update the details of a snapshot by specifying its ID.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_tdm_snapshot_request import UpdateTdmSnapshotRequest
from cohesity_sdk.cluster.model.tdm_snapshot import TdmSnapshot
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = "id_example" # str | Specifies the ID of the snapshot.
body = UpdateTdmSnapshotRequest() # UpdateTdmSnapshotRequest | Specifies the parameters to update the snapshot.

# example passing only required values which don't have defaults set
try:
	# Update a snapshot by ID
	api_response = client.test_data_management.update_tdm_snapshot_by_id(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TestDataManagementApi->update_tdm_snapshot_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the snapshot. |
 **body** | [**UpdateTdmSnapshotRequest**](UpdateTdmSnapshotRequest.md)| Specifies the parameters to update the snapshot. |

### Return type

[**TdmSnapshot**](TdmSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

