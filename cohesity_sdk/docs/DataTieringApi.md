# cohesity_sdk.DataTieringApi


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
> cancel_data_tiering_analysis_group_run(id, run_id)

Cancel data tiering analysis run.

Cancel data tiering analysis run for given analysis group ID and run ID

### Example

* Api Key Authentication (APIKeyHeader):
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


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of data tiering group.
run_id = "4:072888001528021798096225500850762068629" # str | Specifies a unique run id of data tiering group run.

# example passing only required values which don't have defaults set
try:
	# Cancel data tiering analysis run.
	client.data_tiering.cancel_data_tiering_analysis_group_run(id, run_id)
except ApiException as e:
	print("Exception when calling DataTieringApi->cancel_data_tiering_analysis_group_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of data tiering group. |
 **run_id** | **str**| Specifies a unique run id of data tiering group run. |

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
> cancel_data_tiering_task_run(id, run_id)

Cancel data tiering task.

Cancel data tiering task run for given data tiering task id and run id.

### Example

* Api Key Authentication (APIKeyHeader):
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


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of data tiering task.
run_id = "4:072888001528021798096225500850762068629" # str | Specifies a unique run id of data tiering task.

# example passing only required values which don't have defaults set
try:
	# Cancel data tiering task.
	client.data_tiering.cancel_data_tiering_task_run(id, run_id)
except ApiException as e:
	print("Exception when calling DataTieringApi->cancel_data_tiering_task_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of data tiering task. |
 **run_id** | **str**| Specifies a unique run id of data tiering task. |

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
> DataTieringAnalysisGroup create_data_tiering_analysis_group(body)

Create a data tiering analysis group.

Create a data tiering analysis group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_data_tiering_analysis_group_params import CommonDataTieringAnalysisGroupParams
from cohesity_sdk.cluster.model.data_tiering_analysis_group import DataTieringAnalysisGroup
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CommonDataTieringAnalysisGroupParams(
        name="name_example",
        source=DataTieringSource(
            environment="kGenericNas",
            generic_nas_params=GenericNasDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            isilon_params=IsilonDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            netapp_params=NetappDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
        ),
        schedule=DataTieringSchedule(
            unit="Days",
            day_schedule=DaySchedule(),
            week_schedule=WeekSchedule(
                day_of_week=[
                    "Sunday",
                ],
            ),
            month_schedule=MonthSchedule(
                day_of_week=[
                    "Sunday",
                ],
                week_of_month="First",
                day_of_month=1,
            ),
            start_time=TimeOfDay(
                hour=0,
                minute=0,
                time_zone="America/Los_Angeles",
            ),
        ),
    ) # CommonDataTieringAnalysisGroupParams | Specifies the data tiering analysis group.

# example passing only required values which don't have defaults set
try:
	# Create a data tiering analysis group.
	api_response = client.data_tiering.create_data_tiering_analysis_group(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->create_data_tiering_analysis_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonDataTieringAnalysisGroupParams**](CommonDataTieringAnalysisGroupParams.md)| Specifies the data tiering analysis group. |

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
> create_data_tiering_analysis_group_run(id)

Create a data tiering analysis group run.

Create a data tiering analysis group run.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.data_tiering_analysis_run_request import DataTieringAnalysisRunRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of the data tiering analysis group.
body = DataTieringAnalysisRunRequest(
        shares=[
            DataTieringAnalysisShareInfo(
                share_id=1,
            ),
        ],
    ) # DataTieringAnalysisRunRequest | Specifies the request to run analysis group once. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a data tiering analysis group run.
	client.data_tiering.create_data_tiering_analysis_group_run(id)
except ApiException as e:
	print("Exception when calling DataTieringApi->create_data_tiering_analysis_group_run: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a data tiering analysis group run.
	client.data_tiering.create_data_tiering_analysis_group_run(id, body=body)
except ApiException as e:
	print("Exception when calling DataTieringApi->create_data_tiering_analysis_group_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering analysis group. |
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
> CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9 create_data_tiering_task(body)

Create a data tiering task.

Create a data tiering task.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_data_tiering_task_response29ec89c4_f06e4868_a4710fdd67809bd9 import CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9
from cohesity_sdk.cluster.model.common_data_tiering_task_params0e0b87411857430e_ab5330b6e7bc4e9e import CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e(
        name="name_example",
        description="description_example",
        alert_policy=ProtectionGroupAlertingPolicy(
            backup_run_status=[
                "kSuccess",
            ],
            alert_targets=[
                AlertTarget(
                    email_address="email_address_example",
                    language="en-us",
                    recipient_type="kTo",
                ),
            ],
        ),
        source=DataTieringSource(
            environment="kGenericNas",
            generic_nas_params=GenericNasDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            isilon_params=IsilonDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            netapp_params=NetappDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
        ),
        target=DataTieringTarget(
            view_name="view_name_example",
            mount_path="mount_path_example",
            storage_domain_id=1,
        ),
        schedule=DataTieringSchedule(
            unit="Days",
            day_schedule=DaySchedule(),
            week_schedule=WeekSchedule(
                day_of_week=[
                    "Sunday",
                ],
            ),
            month_schedule=MonthSchedule(
                day_of_week=[
                    "Sunday",
                ],
                week_of_month="First",
                day_of_month=1,
            ),
            start_time=TimeOfDay(
                hour=0,
                minute=0,
                time_zone="America/Los_Angeles",
            ),
        ),
        type="Downtier",
    ) # CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e | Specifies the parameters to create a data tiering task.

# example passing only required values which don't have defaults set
try:
	# Create a data tiering task.
	api_response = client.data_tiering.create_data_tiering_task(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->create_data_tiering_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e**](CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e.md)| Specifies the parameters to create a data tiering task. |

### Return type

[**CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9**](CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9.md)

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
> create_data_tiering_task_run(id)

Create a data tiering tasks run.

Create a data tiering tasks run.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.data_tiering_task_run_request import DataTieringTaskRunRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id of the data tiering tasks.
body = DataTieringTaskRunRequest(
        uptier_path="uptier_path_example",
        shares=[
            DataTieringShareInfo(
                share_id=1,
                uptier_path="uptier_path_example",
            ),
        ],
    ) # DataTieringTaskRunRequest | Specifies the request to run tiering task once. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a data tiering tasks run.
	client.data_tiering.create_data_tiering_task_run(id)
except ApiException as e:
	print("Exception when calling DataTieringApi->create_data_tiering_task_run: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a data tiering tasks run.
	client.data_tiering.create_data_tiering_task_run(id, body=body)
except ApiException as e:
	print("Exception when calling DataTieringApi->create_data_tiering_task_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering tasks. |
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
> delete_data_tiering_analysis_group(id)

Delete data tiering analysis group.

Returns NoContentResponse if the data tiering analysis group is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
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


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of the data tiering analysis group.

# example passing only required values which don't have defaults set
try:
	# Delete data tiering analysis group.
	client.data_tiering.delete_data_tiering_analysis_group(id)
except ApiException as e:
	print("Exception when calling DataTieringApi->delete_data_tiering_analysis_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. |

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
> delete_data_tiering_task(id)

delete the data tiering task.

Returns Success if the data tiering task is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
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


id = "id_example" # str | Specifies the id of the data tiering task.

# example passing only required values which don't have defaults set
try:
	# delete the data tiering task.
	client.data_tiering.delete_data_tiering_task(id)
except ApiException as e:
	print("Exception when calling DataTieringApi->delete_data_tiering_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering task. |

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
> CapacityTrendAnalysis get_capacity_trend_analysis()

Get capacity trend analysis for all sources or a specific source.

Get capacity trend analysis for the given time range, and for the given source or set of sources.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.capacity_trend_analysis import CapacityTrendAnalysis
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_usecs = 1 # int | Filter by a start time. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 1 # int | Filter by a end time. Specify the end time as a Unix epoch Timestamp (in microseconds). (optional)
source_id = 1 # int | Filter by source id. If specified, this will only return the capacity trend analysis of the specific source. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get capacity trend analysis for all sources or a specific source.
	api_response = client.data_tiering.get_capacity_trend_analysis(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, source_id=source_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->get_capacity_trend_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> DataTieringAnalysisGroup get_data_tiering_analysis_group_by_id(id)

Get data tiering analysis group by id.

Get data tiering analysis group by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.data_tiering_analysis_group import DataTieringAnalysisGroup
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of the data tiering analysis group.

# example passing only required values which don't have defaults set
try:
	# Get data tiering analysis group by id.
	api_response = client.data_tiering.get_data_tiering_analysis_group_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->get_data_tiering_analysis_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. |

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

# **get_data_tiering_analysis_groups**
> DataTieringAnalysisGroups get_data_tiering_analysis_groups()

Get the list of data tiering analysis groups.

Get list of all data tiering analysis groups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.data_tiering_analysis_groups import DataTieringAnalysisGroups
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
    ] # [str] | Filter by a list of Analysis Group IDs. (optional)
include_last_run_stats = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of data tiering analysis groups.
	api_response = client.data_tiering.get_data_tiering_analysis_groups(ids=ids, include_last_run_stats=include_last_run_stats)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->get_data_tiering_analysis_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Filter by a list of Analysis Group IDs. | [optional]
 **include_last_run_stats** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional]

### Return type

[**DataTieringAnalysisGroups**](DataTieringAnalysisGroups.md)

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
> DataTieringTagConfig get_data_tiering_analysis_groups_default_config()

Get the default config of data tiering analysis groups.

Get default grouping configuration for data tiering analysis groups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.data_tiering_tag_config import DataTieringTagConfig
from cohesity_sdk.cluster.model.error import Error
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
	# Get the default config of data tiering analysis groups.
	api_response = client.data_tiering.get_data_tiering_analysis_groups_default_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->get_data_tiering_analysis_groups_default_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
> CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9 get_data_tiering_task_by_id(id)

Get data tiering task by id.

Get data tiering task by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_data_tiering_task_response29ec89c4_f06e4868_a4710fdd67809bd9 import CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies the id of the data tiering task.

# example passing only required values which don't have defaults set
try:
	# Get data tiering task by id.
	api_response = client.data_tiering.get_data_tiering_task_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->get_data_tiering_task_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering task. |

### Return type

[**CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9**](CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9.md)

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
> DataTieringTasks get_data_tiering_tasks()

Get the list of data tiering tasks.

Get the list of data tiering tasks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.data_tiering_tasks import DataTieringTasks
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
    ] # [str] | Filter by a list of data tiering task ids. (optional)
include_downtiered_data_location = True # bool | If true, it will also return a list of downtiered data locations for downtiered tasks. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of data tiering tasks.
	api_response = client.data_tiering.get_data_tiering_tasks(ids=ids, include_downtiered_data_location=include_downtiered_data_location)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->get_data_tiering_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Filter by a list of data tiering task ids. | [optional]
 **include_downtiered_data_location** | **bool**| If true, it will also return a list of downtiered data locations for downtiered tasks. | [optional]

### Return type

[**DataTieringTasks**](DataTieringTasks.md)

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
> DataTieringAnalysisGroup update_data_tiering_analysis_group(id, body)

Update a data tiering analysis group. Currently, it supports updating sources and schedule only.

Update a data tiering analysis group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_data_tiering_analysis_group_params import CommonDataTieringAnalysisGroupParams
from cohesity_sdk.cluster.model.data_tiering_analysis_group import DataTieringAnalysisGroup
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of the data tiering analysis group.
body = CommonDataTieringAnalysisGroupParams(
        name="name_example",
        source=DataTieringSource(
            environment="kGenericNas",
            generic_nas_params=GenericNasDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            isilon_params=IsilonDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            netapp_params=NetappDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
        ),
        schedule=DataTieringSchedule(
            unit="Days",
            day_schedule=DaySchedule(),
            week_schedule=WeekSchedule(
                day_of_week=[
                    "Sunday",
                ],
            ),
            month_schedule=MonthSchedule(
                day_of_week=[
                    "Sunday",
                ],
                week_of_month="First",
                day_of_month=1,
            ),
            start_time=TimeOfDay(
                hour=0,
                minute=0,
                time_zone="America/Los_Angeles",
            ),
        ),
    ) # CommonDataTieringAnalysisGroupParams | Specifies the data tiering analysis group.

# example passing only required values which don't have defaults set
try:
	# Update a data tiering analysis group. Currently, it supports updating sources and schedule only.
	api_response = client.data_tiering.update_data_tiering_analysis_group(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->update_data_tiering_analysis_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. |
 **body** | [**CommonDataTieringAnalysisGroupParams**](CommonDataTieringAnalysisGroupParams.md)| Specifies the data tiering analysis group. |

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
> DataTieringTagConfig update_data_tiering_analysis_group_tags_config(id, body)

Update data tiering analysis group config.

Update data tiering analysis group config.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.data_tiering_tag_config import DataTieringTagConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of the data tiering analysis group.
body = DataTieringTagConfig(
        tags_info=[
            DataTieringTagObject(
                type="fileTypeTag",
                tags=[
                    DataTieringTag(
                        label="label_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
    ) # DataTieringTagConfig | Specifies the data tiering analysis Tags Config.

# example passing only required values which don't have defaults set
try:
	# Update data tiering analysis group config.
	api_response = client.data_tiering.update_data_tiering_analysis_group_tags_config(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->update_data_tiering_analysis_group_tags_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the data tiering analysis group. |
 **body** | [**DataTieringTagConfig**](DataTieringTagConfig.md)| Specifies the data tiering analysis Tags Config. |

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
> UpdateDataTieringState update_data_tiering_analysis_groups_state(body)

Update data tiering analysis groups state.

Perform actions like pause or resume on the data tiering analysis groups for the specified sources.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_data_tiering_state import UpdateDataTieringState
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_data_tiering_state_request import UpdateDataTieringStateRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateDataTieringStateRequest(
        action="Pause",
        ids=[
            "ids_example",
        ],
    ) # UpdateDataTieringStateRequest | Specifies the parameters to perform an action of list of data tiering analysis groups.

# example passing only required values which don't have defaults set
try:
	# Update data tiering analysis groups state.
	api_response = client.data_tiering.update_data_tiering_analysis_groups_state(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->update_data_tiering_analysis_groups_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDataTieringStateRequest**](UpdateDataTieringStateRequest.md)| Specifies the parameters to perform an action of list of data tiering analysis groups. |

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
> CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9 update_data_tiering_task(id, body)

Update a data tiering task.

Update a data tiering task.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_data_tiering_task_response29ec89c4_f06e4868_a4710fdd67809bd9 import CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9
from cohesity_sdk.cluster.model.common_data_tiering_task_params0e0b87411857430e_ab5330b6e7bc4e9e import CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies the id of the data tiering task.
body = CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e(
        name="name_example",
        description="description_example",
        alert_policy=ProtectionGroupAlertingPolicy(
            backup_run_status=[
                "kSuccess",
            ],
            alert_targets=[
                AlertTarget(
                    email_address="email_address_example",
                    language="en-us",
                    recipient_type="kTo",
                ),
            ],
        ),
        source=DataTieringSource(
            environment="kGenericNas",
            generic_nas_params=GenericNasDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            isilon_params=IsilonDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
            netapp_params=NetappDataTieringParams(
                objects=[
                    ProtectionObjectInput(
                        id=1,
                    ),
                ],
                source_id=1,
            ),
        ),
        target=DataTieringTarget(
            view_name="view_name_example",
            mount_path="mount_path_example",
            storage_domain_id=1,
        ),
        schedule=DataTieringSchedule(
            unit="Days",
            day_schedule=DaySchedule(),
            week_schedule=WeekSchedule(
                day_of_week=[
                    "Sunday",
                ],
            ),
            month_schedule=MonthSchedule(
                day_of_week=[
                    "Sunday",
                ],
                week_of_month="First",
                day_of_month=1,
            ),
            start_time=TimeOfDay(
                hour=0,
                minute=0,
                time_zone="America/Los_Angeles",
            ),
        ),
        type="Downtier",
    ) # CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e | Specifies the parameters to update a data tiering task.

# example passing only required values which don't have defaults set
try:
	# Update a data tiering task.
	api_response = client.data_tiering.update_data_tiering_task(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->update_data_tiering_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the data tiering task. |
 **body** | [**CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e**](CommonDataTieringTaskParams0e0b87411857430eAb5330b6e7bc4e9e.md)| Specifies the parameters to update a data tiering task. |

### Return type

[**CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9**](CommonDataTieringTaskResponse29ec89c4F06e4868A4710fdd67809bd9.md)

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
> UpdateDataTieringState update_data_tiering_tasks_state(body)

Update data tiering source analysis tasks state.

Perform actions like pause or resume on the data tiering tasks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_data_tiering_state import UpdateDataTieringState
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_data_tiering_state_request import UpdateDataTieringStateRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateDataTieringStateRequest(
        action="Pause",
        ids=[
            "ids_example",
        ],
    ) # UpdateDataTieringStateRequest | Specifies the parameters to perform an action of list of data tiering tasks.

# example passing only required values which don't have defaults set
try:
	# Update data tiering source analysis tasks state.
	api_response = client.data_tiering.update_data_tiering_tasks_state(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataTieringApi->update_data_tiering_tasks_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDataTieringStateRequest**](UpdateDataTieringStateRequest.md)| Specifies the parameters to perform an action of list of data tiering tasks. |

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

