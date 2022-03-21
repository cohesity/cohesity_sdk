# cohesity_sdk.ProtectionGroupApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcm_protection_group**](ProtectionGroupApi.md#create_mcm_protection_group) | **POST** /mcm/data-protect/protection-groups | Create a Protection Group.
[**create_protection_group**](ProtectionGroupApi.md#create_protection_group) | **POST** /data-protect/protection-groups | Create a Protection Group.
[**create_protection_group_run**](ProtectionGroupApi.md#create_protection_group_run) | **POST** /data-protect/protection-groups/{id}/runs | Create a new protection run.
[**delete_mcm_protection_group**](ProtectionGroupApi.md#delete_mcm_protection_group) | **DELETE** /mcm/data-protect/protection-groups/{id} | Delete a Protection Group.
[**delete_protection_group**](ProtectionGroupApi.md#delete_protection_group) | **DELETE** /data-protect/protection-groups/{id} | Delete a Protection Group.
[**get_mcm_protection_group_by_id**](ProtectionGroupApi.md#get_mcm_protection_group_by_id) | **GET** /mcm/data-protect/protection-groups/{id} | List details about single Protection Group.
[**get_mcm_protection_groups**](ProtectionGroupApi.md#get_mcm_protection_groups) | **GET** /mcm/data-protect/protection-groups | Get the list of Protection Groups.
[**get_mcm_protection_groups_activity**](ProtectionGroupApi.md#get_mcm_protection_groups_activity) | **POST** /mcm/data-protect/protection-group/activity | Get Protection Group activity on Helios.
[**get_protection_group_by_id**](ProtectionGroupApi.md#get_protection_group_by_id) | **GET** /data-protect/protection-groups/{id} | List details about single Protection Group.
[**get_protection_group_run**](ProtectionGroupApi.md#get_protection_group_run) | **GET** /data-protect/protection-groups/{id}/runs/{runId} | Get a run for a Protection Group.
[**get_protection_group_runs**](ProtectionGroupApi.md#get_protection_group_runs) | **GET** /data-protect/protection-groups/{id}/runs | Get the list of runs for a Protection Group.
[**get_protection_groups**](ProtectionGroupApi.md#get_protection_groups) | **GET** /data-protect/protection-groups | Get the list of Protection Groups.
[**get_protection_run_progress**](ProtectionGroupApi.md#get_protection_run_progress) | **GET** /data-protect/runs/{runId}/progress | Get the progress of a run.
[**get_protection_runs**](ProtectionGroupApi.md#get_protection_runs) | **GET** /data-protect/runs/summary | Get the list of runs.
[**get_run_debug_logs**](ProtectionGroupApi.md#get_run_debug_logs) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/debug-logs | Get the debug logs for a run from a Protection Group.
[**get_run_debug_logs_for_object**](ProtectionGroupApi.md#get_run_debug_logs_for_object) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/objects/{objectId}/debug-logs | Get the debug logs for a particular object in a run from a Protection Group.
[**get_run_errors_report**](ProtectionGroupApi.md#get_run_errors_report) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/objects/{objectId}/download-messages | Get the CSV of errors/warnings for a given run and an object.
[**get_runs_report**](ProtectionGroupApi.md#get_runs_report) | **GET** /data-protect/protection-groups/{id}/runs/{runId}/objects/{objectId}/downloadFiles | Get the CSV of errors/warnings for a given run and an object.
[**perform_action_on_protection_group_run**](ProtectionGroupApi.md#perform_action_on_protection_group_run) | **POST** /data-protect/protection-groups/{id}/runs/actions | Actions on protection group run.
[**update_mcm_protection_group**](ProtectionGroupApi.md#update_mcm_protection_group) | **PUT** /mcm/data-protect/protection-groups/{id} | Update a Protection Group.
[**update_protection_group**](ProtectionGroupApi.md#update_protection_group) | **PUT** /data-protect/protection-groups/{id} | Update a Protection Group.
[**update_protection_group_run**](ProtectionGroupApi.md#update_protection_group_run) | **PUT** /data-protect/protection-groups/{id}/runs | Update runs for a particular Protection Group.
[**update_protection_groups_state**](ProtectionGroupApi.md#update_protection_groups_state) | **POST** /data-protect/protection-groups/states | Perform an action like pause, resume, active, deactivate on all specified Protection Groups.


# **create_mcm_protection_group**
> ProtectionGroup create_mcm_protection_group(body)

Create a Protection Group.

Create a Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to create a Protection Group.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Protection Group.
	api_response = client.protection_group.create_mcm_protection_group(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->create_mcm_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Protection Group.
	api_response = client.protection_group.create_mcm_protection_group(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->create_mcm_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to create a Protection Group. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **create_protection_group**
> ProtectionGroup create_protection_group(body)

Create a Protection Group.

Create a Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to create a Protection Group.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Protection Group.
	api_response = client.protection_group.create_protection_group(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->create_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Protection Group.
	api_response = client.protection_group.create_protection_group(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->create_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to create a Protection Group. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **create_protection_group_run**
> CreateProtectionGroupRunResponseBody create_protection_group_run(id, body)

Create a new protection run.

Create a new protection run. This can be used to start a run for a Protection Group on demand, ignoring the schedule and retention specified in the protection policy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_protection_group_run_response_body import CreateProtectionGroupRunResponseBody
from cohesity_sdk.helios.model.create_protection_group_run_request import CreateProtectionGroupRunRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
body = CreateProtectionGroupRunRequest(
        run_type="kRegular",
        objects=[
            RunObject(
                id=1,
                app_ids=[
                    1,
                ],
                physical_params=RunObjectPhysicalParams(
                    metadata_file_path="metadata_file_path_example",
                ),
            ),
        ],
        targets_config=RunTargetsConfiguration(
            use_policy_defaults=False,
            replications=[
                RunReplicationConfig(
                    id=1,
                    retention=Retention(
                        unit="Days",
                        duration=1,
                        data_lock_config=DataLockConfig(
                            mode="Compliance",
                            unit="Days",
                            duration=1,
                            enable_worm_on_external_target=True,
                        ),
                    ),
                ),
            ],
            archivals=[
                RunArchivalConfig(
                    id=1,
                    archival_target_type="Tape",
                    retention=Retention(
                        unit="Days",
                        duration=1,
                        data_lock_config=DataLockConfig(
                            mode="Compliance",
                            unit="Days",
                            duration=1,
                            enable_worm_on_external_target=True,
                        ),
                    ),
                    copy_only_fully_successful=True,
                ),
            ],
            cloud_replications=[
                RunCloudReplicationConfig(
                    target_type="AWS",
                    aws_target=AWSTargetConfig(
                        source_id=1,
                        region=1,
                    ),
                    azure_target=AzureTargetConfig(
                        source_id=1,
                        resource_group=1,
                    ),
                    retention=Retention(
                        unit="Days",
                        duration=1,
                        data_lock_config=DataLockConfig(
                            mode="Compliance",
                            unit="Days",
                            duration=1,
                            enable_worm_on_external_target=True,
                        ),
                    ),
                ),
            ],
        ),
    ) # CreateProtectionGroupRunRequest | Specifies the parameters to start a protection run.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a new protection run.
	api_response = client.protection_group.create_protection_group_run(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->create_protection_group_run: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a new protection run.
	api_response = client.protection_group.create_protection_group_run(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->create_protection_group_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **body** | [**CreateProtectionGroupRunRequest**](CreateProtectionGroupRunRequest.md)| Specifies the parameters to start a protection run. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**CreateProtectionGroupRunResponseBody**](CreateProtectionGroupRunResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mcm_protection_group**
> delete_mcm_protection_group(id)

Delete a Protection Group.

Returns Success if the Protection Group is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
delete_snapshots = True # bool | Specifies if Snapshots generated by the Protection Group should also be deleted when the Protection Group is deleted. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a Protection Group.
	client.protection_group.delete_mcm_protection_group(id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->delete_mcm_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Protection Group.
	client.protection_group.delete_mcm_protection_group(id, region_id=region_id, delete_snapshots=delete_snapshots)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->delete_mcm_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **delete_snapshots** | **bool**| Specifies if Snapshots generated by the Protection Group should also be deleted when the Protection Group is deleted. | [optional]

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

# **delete_protection_group**
> delete_protection_group(id)

Delete a Protection Group.

Returns Success if the Protection Group is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
delete_snapshots = True # bool | Specifies if Snapshots generated by the Protection Group should also be deleted when the Protection Group is deleted. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a Protection Group.
	client.protection_group.delete_protection_group(id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->delete_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Protection Group.
	client.protection_group.delete_protection_group(id, access_cluster_id=access_cluster_id, region_id=region_id, delete_snapshots=delete_snapshots)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->delete_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **delete_snapshots** | **bool**| Specifies if Snapshots generated by the Protection Group should also be deleted when the Protection Group is deleted. | [optional]

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

# **get_mcm_protection_group_by_id**
> ProtectionGroup get_mcm_protection_group_by_id(id)

List details about single Protection Group.

Returns the Protection Group corresponding to the specified Group id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
include_last_run_info = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# List details about single Protection Group.
	api_response = client.protection_group.get_mcm_protection_group_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_mcm_protection_group_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about single Protection Group.
	api_response = client.protection_group.get_mcm_protection_group_by_id(id, region_id=region_id, request_initiator_type=request_initiator_type, include_last_run_info=include_last_run_info)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_mcm_protection_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **include_last_run_info** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **get_mcm_protection_groups**
> ProtectionGroups get_mcm_protection_groups()

Get the list of Protection Groups.

Get the list of Protection Groups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.protection_groups import ProtectionGroups
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
ids = [
        "ids_example",
    ] # [str] | Filter by a list of Protection Group ids. (optional)
names = [
        "names_example",
    ] # [str] | Filter by a list of Protection Group names. (optional)
policy_ids = [
        "policyIds_example",
    ] # [str] | Filter by Policy ids that are associated with Protection Groups. Only Protection Groups associated with the specified Policy ids, are returned. (optional)
environments = [
        "kVMware",
    ] # [str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protection Groups protecting the specified environment types are returned. (optional)
is_active = True # bool | Filter by Inactive or Active Protection Groups. If not set, all Inactive and Active Protection Groups are returned. If true, only Active Protection Groups are returned. If false, only Inactive Protection Groups are returned. When you create a Protection Group on a Primary Cluster with a replication schedule, the Cluster creates an Inactive copy of the Protection Group on the Remote Cluster. In addition, when an Active and running Protection Group is deactivated, the Protection Group becomes Inactive. (optional)
is_deleted = True # bool | If true, return only Protection Groups that have been deleted but still have Snapshots associated with them. If false, return all Protection Groups except those Protection Groups that have been deleted and still have Snapshots associated with them. A Protection Group that is deleted with all its Snapshots is not returned for either of these cases. (optional)
is_paused = True # bool | Filter by paused or non paused Protection Groups, If not set, all paused and non paused Protection Groups are returned. If true, only paused Protection Groups are returned. If false, only non paused Protection Groups are returned. (optional)
last_run_any_status = [
        "Accepted",
    ] # [str] | Filter by last any run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)
is_last_run_sla_violated = True # bool | If true, return Protection Groups for which last run SLA was violated. (optional)
include_last_run_info = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of Protection Groups.
	api_response = client.protection_group.get_mcm_protection_groups(region_id=region_id, ids=ids, names=names, policy_ids=policy_ids, environments=environments, is_active=is_active, is_deleted=is_deleted, is_paused=is_paused, last_run_any_status=last_run_any_status, is_last_run_sla_violated=is_last_run_sla_violated, include_last_run_info=include_last_run_info)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_mcm_protection_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **ids** | **[str]**| Filter by a list of Protection Group ids. | [optional]
 **names** | **[str]**| Filter by a list of Protection Group names. | [optional]
 **policy_ids** | **[str]**| Filter by Policy ids that are associated with Protection Groups. Only Protection Groups associated with the specified Policy ids, are returned. | [optional]
 **environments** | **[str]**| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protection Groups protecting the specified environment types are returned. | [optional]
 **is_active** | **bool**| Filter by Inactive or Active Protection Groups. If not set, all Inactive and Active Protection Groups are returned. If true, only Active Protection Groups are returned. If false, only Inactive Protection Groups are returned. When you create a Protection Group on a Primary Cluster with a replication schedule, the Cluster creates an Inactive copy of the Protection Group on the Remote Cluster. In addition, when an Active and running Protection Group is deactivated, the Protection Group becomes Inactive. | [optional]
 **is_deleted** | **bool**| If true, return only Protection Groups that have been deleted but still have Snapshots associated with them. If false, return all Protection Groups except those Protection Groups that have been deleted and still have Snapshots associated with them. A Protection Group that is deleted with all its Snapshots is not returned for either of these cases. | [optional]
 **is_paused** | **bool**| Filter by paused or non paused Protection Groups, If not set, all paused and non paused Protection Groups are returned. If true, only paused Protection Groups are returned. If false, only non paused Protection Groups are returned. | [optional]
 **last_run_any_status** | **[str]**| Filter by last any run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional]
 **is_last_run_sla_violated** | **bool**| If true, return Protection Groups for which last run SLA was violated. | [optional]
 **include_last_run_info** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional]

### Return type

[**ProtectionGroups**](ProtectionGroups.md)

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

# **get_mcm_protection_groups_activity**
> McmProtectionGroupsActivity get_mcm_protection_groups_activity()

Get Protection Group activity on Helios.

Get Protection Group activity on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_protection_groups_activity import McmProtectionGroupsActivity
from cohesity_sdk.helios.model.get_mcm_protection_groups_activity_req_params import GetMcmProtectionGroupsActivityReqParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)
rpaas_region_ids = [
        "rpaasRegionIds_example",
    ] # [str] | Filter by a list of region ids. This is used for Rpaas only. (optional)
cluster_identifiers = [
        "clusterIdentifiers_example",
    ] # [str] | Filter by a list of cluster identifiers in format of clusterId:clusterIncarnationId. (optional)
body = GetMcmProtectionGroupsActivityReqParams(
        protection_group_identifiers=[
            "protection_group_identifiers_example",
        ],
        environments=[
            "kVMware",
        ],
        statuses=[
            "Accepted",
        ],
        run_start_time_usecs=1,
        from_time_usecs=1,
        to_time_usecs=1,
        activity_types=[
            "BackupRun",
        ],
        include_object_details=True,
        backup_run_params={},
        archival_run_params=ProtectionGroupArchivalRunFilterParams(
            is_full_archive=True,
            protection_environment_types=[
                "kVMware",
            ],
            is_rpaas=True,
        ),
    ) # GetMcmProtectionGroupsActivityReqParams | Request parameters to filter Protection Group activity. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Protection Group activity on Helios.
	api_response = client.protection_group.get_mcm_protection_groups_activity(region_id=region_id, region_ids=region_ids, rpaas_region_ids=rpaas_region_ids, cluster_identifiers=cluster_identifiers, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_mcm_protection_groups_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]
 **rpaas_region_ids** | **[str]**| Filter by a list of region ids. This is used for Rpaas only. | [optional]
 **cluster_identifiers** | **[str]**| Filter by a list of cluster identifiers in format of clusterId:clusterIncarnationId. | [optional]
 **body** | [**GetMcmProtectionGroupsActivityReqParams**](GetMcmProtectionGroupsActivityReqParams.md)| Request parameters to filter Protection Group activity. | [optional]

### Return type

[**McmProtectionGroupsActivity**](McmProtectionGroupsActivity.md)

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

# **get_protection_group_by_id**
> ProtectionGroup get_protection_group_by_id(id)

List details about single Protection Group.

Returns the Protection Group corresponding to the specified Group id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
include_last_run_info = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)
prune_excluded_source_ids = True # bool | If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. (optional)
prune_source_ids = True # bool, none_type | If true, the response will exclude the list of source IDs within the group specified. (optional)

# example passing only required values which don't have defaults set
try:
	# List details about single Protection Group.
	api_response = client.protection_group.get_protection_group_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_group_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about single Protection Group.
	api_response = client.protection_group.get_protection_group_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, include_last_run_info=include_last_run_info, prune_excluded_source_ids=prune_excluded_source_ids, prune_source_ids=prune_source_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **include_last_run_info** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional]
 **prune_excluded_source_ids** | **bool**| If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. | [optional]
 **prune_source_ids** | **bool, none_type**| If true, the response will exclude the list of source IDs within the group specified. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **get_protection_group_run**
> ProtectionGroupRun get_protection_group_run(id, run_id)

Get a run for a Protection Group.

Get a run for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.protection_group_run import ProtectionGroupRun
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
run_id = "4:072888001528021798096225500850762068629" # str | Specifies a unique run id of the Protection Group run.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which the run is to be returned. (optional)
include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it's not specified, it is true by default. (optional)
include_object_details = True # bool | Specifies if the result includes the object details for a protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a run for a Protection Group.
	api_response = client.protection_group.get_protection_group_run(id, run_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_group_run: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a run for a Protection Group.
	api_response = client.protection_group.get_protection_group_run(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, tenant_ids=tenant_ids, include_tenants=include_tenants, include_object_details=include_object_details)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_group_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which the run is to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it&#39;s not specified, it is true by default. | [optional]
 **include_object_details** | **bool**| Specifies if the result includes the object details for a protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. | [optional]

### Return type

[**ProtectionGroupRun**](ProtectionGroupRun.md)

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

# **get_protection_group_runs**
> ProtectionGroupRuns get_protection_group_runs(id)

Get the list of runs for a Protection Group.

Get the runs for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group_runs import ProtectionGroupRuns
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
run_id = "4:072888001528021798096225500850762068629" # str | Specifies the protection run id. (optional)
start_time_usecs = 1 # int | Filter by a start time. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 1 # int | Filter by a end time. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. (optional)
run_types = [
        "kAll",
    ] # [str] | Filter by run type. Only protection run matching the specified types will be returned. (optional)
include_object_details = True # bool | Specifies if the result includes the object details for each protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. (optional)
local_backup_run_status = [
        "Accepted",
    ] # [str] | Specifies a list of local backup status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
replication_run_status = [
        "Accepted",
    ] # [str] | Specifies a list of replication status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
archival_run_status = [
        "Accepted",
    ] # [str] | Specifies a list of archival status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
cloud_spin_run_status = [
        "Accepted",
    ] # [str] | Specifies a list of cloud spin status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
num_runs = 1 # int | Specifies the max number of runs. If not specified, at most 100 runs will be returned. (optional)
exclude_non_restorable_runs = False # bool | Specifies whether to exclude non restorable runs. Run is treated restorable only if there is atleast one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. (optional) if omitted the server will use the default value of False
run_tags = [
        "runTags_example",
    ] # [str] | Specifies a list of tags for protection runs. If this is specified, only the runs which match these tags will be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the list of runs for a Protection Group.
	api_response = client.protection_group.get_protection_group_runs(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_group_runs: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of runs for a Protection Group.
	api_response = client.protection_group.get_protection_group_runs(id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, run_id=run_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, run_types=run_types, include_object_details=include_object_details, local_backup_run_status=local_backup_run_status, replication_run_status=replication_run_status, archival_run_status=archival_run_status, cloud_spin_run_status=cloud_spin_run_status, num_runs=num_runs, exclude_non_restorable_runs=exclude_non_restorable_runs, run_tags=run_tags)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_group_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **run_id** | **str**| Specifies the protection run id. | [optional]
 **start_time_usecs** | **int**| Filter by a start time. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional]
 **end_time_usecs** | **int**| Filter by a end time. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. | [optional]
 **run_types** | **[str]**| Filter by run type. Only protection run matching the specified types will be returned. | [optional]
 **include_object_details** | **bool**| Specifies if the result includes the object details for each protection run. If set to true, details of the protected object will be returned. If set to false or not specified, details will not be returned. | [optional]
 **local_backup_run_status** | **[str]**| Specifies a list of local backup status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **replication_run_status** | **[str]**| Specifies a list of replication status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **archival_run_status** | **[str]**| Specifies a list of archival status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **cloud_spin_run_status** | **[str]**| Specifies a list of cloud spin status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **num_runs** | **int**| Specifies the max number of runs. If not specified, at most 100 runs will be returned. | [optional]
 **exclude_non_restorable_runs** | **bool**| Specifies whether to exclude non restorable runs. Run is treated restorable only if there is atleast one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. | [optional] if omitted the server will use the default value of False
 **run_tags** | **[str]**| Specifies a list of tags for protection runs. If this is specified, only the runs which match these tags will be returned. | [optional]

### Return type

[**ProtectionGroupRuns**](ProtectionGroupRuns.md)

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

# **get_protection_groups**
> ProtectionGroups get_protection_groups()

Get the list of Protection Groups.

Get the list of Protection Groups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.protection_groups import ProtectionGroups
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
ids = [
        "ids_example",
    ] # [str] | Filter by a list of Protection Group ids. (optional)
names = [
        "names_example",
    ] # [str] | Filter by a list of Protection Group names. (optional)
policy_ids = [
        "policyIds_example",
    ] # [str] | Filter by Policy ids that are associated with Protection Groups. Only Protection Groups associated with the specified Policy ids, are returned. (optional)
storage_domain_id = 1 # int | Filter by Storage Domain id. Only Protection Groups writing data to this Storage Domain will be returned. (optional)
include_groups_with_datalock_only = True # bool | Whether to only return Protection Groups with a datalock. (optional)
environments = [
        "kVMware",
    ] # [str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protection Groups protecting the specified environment types are returned. (optional)
office365_workloads = [
        "kMailbox",
    ] # [str] |  (optional)
is_active = True # bool | Filter by Inactive or Active Protection Groups. If not set, all Inactive and Active Protection Groups are returned. If true, only Active Protection Groups are returned. If false, only Inactive Protection Groups are returned. When you create a Protection Group on a Primary Cluster with a replication schedule, the Cluster creates an Inactive copy of the Protection Group on the Remote Cluster. In addition, when an Active and running Protection Group is deactivated, the Protection Group becomes Inactive. (optional)
is_deleted = True # bool | If true, return only Protection Groups that have been deleted but still have Snapshots associated with them. If false, return all Protection Groups except those Protection Groups that have been deleted and still have Snapshots associated with them. A Protection Group that is deleted with all its Snapshots is not returned for either of these cases. (optional)
is_paused = True # bool | Filter by paused or non paused Protection Groups, If not set, all paused and non paused Protection Groups are returned. If true, only paused Protection Groups are returned. If false, only non paused Protection Groups are returned. (optional)
last_run_local_backup_status = [
        "Accepted",
    ] # [str] | Filter by last local backup run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
last_run_replication_status = [
        "Accepted",
    ] # [str] | Filter by last remote replication run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
last_run_archival_status = [
        "Accepted",
    ] # [str] | Filter by last cloud archival run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
last_run_cloud_spin_status = [
        "Accepted",
    ] # [str] | Filter by last cloud spin run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
last_run_any_status = [
        "Accepted",
    ] # [str] | Filter by last any run status.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused. (optional)
is_last_run_sla_violated = True # bool | If true, return Protection Groups for which last run SLA was violated. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)
include_last_run_info = True # bool | If true, the response will include last run info. If it is false or not specified, the last run info won't be returned. (optional)
prune_excluded_source_ids = True # bool | If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. (optional)
prune_source_ids = True # bool, none_type | If true, the response will exclude the list of source IDs within the group specified. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of Protection Groups.
	api_response = client.protection_group.get_protection_groups(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, ids=ids, names=names, policy_ids=policy_ids, storage_domain_id=storage_domain_id, include_groups_with_datalock_only=include_groups_with_datalock_only, environments=environments, office365_workloads=office365_workloads, is_active=is_active, is_deleted=is_deleted, is_paused=is_paused, last_run_local_backup_status=last_run_local_backup_status, last_run_replication_status=last_run_replication_status, last_run_archival_status=last_run_archival_status, last_run_cloud_spin_status=last_run_cloud_spin_status, last_run_any_status=last_run_any_status, is_last_run_sla_violated=is_last_run_sla_violated, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, prune_excluded_source_ids=prune_excluded_source_ids, prune_source_ids=prune_source_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **ids** | **[str]**| Filter by a list of Protection Group ids. | [optional]
 **names** | **[str]**| Filter by a list of Protection Group names. | [optional]
 **policy_ids** | **[str]**| Filter by Policy ids that are associated with Protection Groups. Only Protection Groups associated with the specified Policy ids, are returned. | [optional]
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only Protection Groups writing data to this Storage Domain will be returned. | [optional]
 **include_groups_with_datalock_only** | **bool**| Whether to only return Protection Groups with a datalock. | [optional]
 **environments** | **[str]**| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protection Groups protecting the specified environment types are returned. | [optional]
 **office365_workloads** | **[str]**|  | [optional]
 **is_active** | **bool**| Filter by Inactive or Active Protection Groups. If not set, all Inactive and Active Protection Groups are returned. If true, only Active Protection Groups are returned. If false, only Inactive Protection Groups are returned. When you create a Protection Group on a Primary Cluster with a replication schedule, the Cluster creates an Inactive copy of the Protection Group on the Remote Cluster. In addition, when an Active and running Protection Group is deactivated, the Protection Group becomes Inactive. | [optional]
 **is_deleted** | **bool**| If true, return only Protection Groups that have been deleted but still have Snapshots associated with them. If false, return all Protection Groups except those Protection Groups that have been deleted and still have Snapshots associated with them. A Protection Group that is deleted with all its Snapshots is not returned for either of these cases. | [optional]
 **is_paused** | **bool**| Filter by paused or non paused Protection Groups, If not set, all paused and non paused Protection Groups are returned. If true, only paused Protection Groups are returned. If false, only non paused Protection Groups are returned. | [optional]
 **last_run_local_backup_status** | **[str]**| Filter by last local backup run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **last_run_replication_status** | **[str]**| Filter by last remote replication run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **last_run_archival_status** | **[str]**| Filter by last cloud archival run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **last_run_cloud_spin_status** | **[str]**| Filter by last cloud spin run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **last_run_any_status** | **[str]**| Filter by last any run status.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused. | [optional]
 **is_last_run_sla_violated** | **bool**| If true, return Protection Groups for which last run SLA was violated. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional]
 **include_last_run_info** | **bool**| If true, the response will include last run info. If it is false or not specified, the last run info won&#39;t be returned. | [optional]
 **prune_excluded_source_ids** | **bool**| If true, the response will not include the list of excluded source IDs in groups that contain this field. This can be set to true in order to improve performance if excluded source IDs are not needed by the user. | [optional]
 **prune_source_ids** | **bool, none_type**| If true, the response will exclude the list of source IDs within the group specified. | [optional]

### Return type

[**ProtectionGroups**](ProtectionGroups.md)

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

# **get_protection_run_progress**
> GetProtectionRunProgressBody get_protection_run_progress(run_id)

Get the progress of a run.

Get the progress of a run.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.get_protection_run_progress_body import GetProtectionRunProgressBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


run_id = "runId_example" # str | Specifies a unique run id of the Protection Run.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
objects = [
        1,
    ] # [int] | Specifies the objects whose progress will be returned. This only applies to protection group runs and will be ignored for object runs. If the objects are specified, the run progress will not be returned and only the progress of the specified objects will be returned. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which the run is to be returned. (optional)
include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it's not specified, it is true by default. (optional)
include_finished_tasks = True # bool | Specifies whether to return finished tasks. By default only active tasks are returned. (optional)
start_time_usecs = 1 # int | Specifies the time after which the progress task starts in Unix epoch Timestamp(in microseconds). (optional)
end_time_usecs = 1 # int | Specifies the time before which the progress task ends in Unix epoch Timestamp(in microseconds). (optional)
max_tasks_num = 1 # int | Specifies the maximum number of tasks to return. (optional)
exclude_object_details = True # bool | Specifies whether to return objects. By default all the task tree are returned. (optional)
include_event_logs = True # bool | Specifies whether to include event logs (optional)
max_log_level = 1 # int | Specifies the number of levels till which to fetch the event logs. This is applicable only when includeEventLogs is true. (optional)
run_task_path = "runTaskPath_example" # str | Specifies the task path of the run or object run. This is applicable only if progress of a protection group with one or more object is required.If provided this will be used to fetch progress details directly without looking actual task path of the object. Objects field is stil expected else it changes the response format. (optional)
object_task_paths = [
        "objectTaskPaths_example",
    ] # [str] | Specifies the object level task path. This relates to the objectID. If provided this will take precedence over the objects, and will be used to fetch progress details directly without looking actuall task path of the object. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the progress of a run.
	api_response = client.protection_group.get_protection_run_progress(run_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_run_progress: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the progress of a run.
	api_response = client.protection_group.get_protection_run_progress(run_id, access_cluster_id=access_cluster_id, region_id=region_id, objects=objects, tenant_ids=tenant_ids, include_tenants=include_tenants, include_finished_tasks=include_finished_tasks, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_tasks_num=max_tasks_num, exclude_object_details=exclude_object_details, include_event_logs=include_event_logs, max_log_level=max_log_level, run_task_path=run_task_path, object_task_paths=object_task_paths)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_run_progress: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Specifies a unique run id of the Protection Run. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **objects** | **[int]**| Specifies the objects whose progress will be returned. This only applies to protection group runs and will be ignored for object runs. If the objects are specified, the run progress will not be returned and only the progress of the specified objects will be returned. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which the run is to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. If it&#39;s not specified, it is true by default. | [optional]
 **include_finished_tasks** | **bool**| Specifies whether to return finished tasks. By default only active tasks are returned. | [optional]
 **start_time_usecs** | **int**| Specifies the time after which the progress task starts in Unix epoch Timestamp(in microseconds). | [optional]
 **end_time_usecs** | **int**| Specifies the time before which the progress task ends in Unix epoch Timestamp(in microseconds). | [optional]
 **max_tasks_num** | **int**| Specifies the maximum number of tasks to return. | [optional]
 **exclude_object_details** | **bool**| Specifies whether to return objects. By default all the task tree are returned. | [optional]
 **include_event_logs** | **bool**| Specifies whether to include event logs | [optional]
 **max_log_level** | **int**| Specifies the number of levels till which to fetch the event logs. This is applicable only when includeEventLogs is true. | [optional]
 **run_task_path** | **str**| Specifies the task path of the run or object run. This is applicable only if progress of a protection group with one or more object is required.If provided this will be used to fetch progress details directly without looking actual task path of the object. Objects field is stil expected else it changes the response format. | [optional]
 **object_task_paths** | **[str]**| Specifies the object level task path. This relates to the objectID. If provided this will take precedence over the objects, and will be used to fetch progress details directly without looking actuall task path of the object. | [optional]

### Return type

[**GetProtectionRunProgressBody**](GetProtectionRunProgressBody.md)

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

# **get_protection_runs**
> ProtectionRunsSummary get_protection_runs()

Get the list of runs.

Get a list of protection runs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_runs_summary import ProtectionRunsSummary
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
start_time_usecs = 1 # int | Filter by a start time. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be returned. By default it is endTimeUsecs minus an hour. (optional)
end_time_usecs = 1 # int | Filter by a end time. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be returned. By default it is current time. (optional)
run_status = [
        "Accepted",
    ] # [str] | Specifies a list of status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of runs.
	api_response = client.protection_group.get_protection_runs(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, run_status=run_status)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_protection_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **start_time_usecs** | **int**| Filter by a start time. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing after this time will be returned. By default it is endTimeUsecs minus an hour. | [optional]
 **end_time_usecs** | **int**| Filter by a end time. Specify the start time as a Unix epoch Timestamp (in microseconds), only runs executing before this time will be returned. By default it is current time. | [optional]
 **run_status** | **[str]**| Specifies a list of status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional]

### Return type

[**ProtectionRunsSummary**](ProtectionRunsSummary.md)

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

# **get_run_debug_logs**
> get_run_debug_logs(id, run_id)

Get the debug logs for a run from a Protection Group.

Get the debug logs for all objects of a run for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of the Protection Group.
run_id = "4:072888001528021798096225500850762068629" # str | Specifies a unique run id of the Protection Group run.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
object_id = "objectId_example" # str | Specifies the id of the object for which debug logs are to be returned.  (optional)

# example passing only required values which don't have defaults set
try:
	# Get the debug logs for a run from a Protection Group.
	client.protection_group.get_run_debug_logs(id, run_id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_run_debug_logs: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the debug logs for a run from a Protection Group.
	client.protection_group.get_run_debug_logs(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id, object_id=object_id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_run_debug_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **object_id** | **str**| Specifies the id of the object for which debug logs are to be returned.  | [optional]

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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_debug_logs_for_object**
> get_run_debug_logs_for_object(id, run_id, object_id)

Get the debug logs for a particular object in a run from a Protection Group.

Get the debug logs for a particular object of a run for a particular Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of the Protection Group.
run_id = "4:072888001528021798096225500850762068629" # str | Specifies a unique run id of the Protection Group run.
object_id = "objectId_example" # str | Specifies the id of the object for which debug logs are to be returned. 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the debug logs for a particular object in a run from a Protection Group.
	client.protection_group.get_run_debug_logs_for_object(id, run_id, object_id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_run_debug_logs_for_object: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the debug logs for a particular object in a run from a Protection Group.
	client.protection_group.get_run_debug_logs_for_object(id, run_id, object_id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_run_debug_logs_for_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. |
 **object_id** | **str**| Specifies the id of the object for which debug logs are to be returned.  |
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
**200** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_errors_report**
> get_run_errors_report(id, run_id, object_id)

Get the CSV of errors/warnings for a given run and an object.

Get an CSV error report for given objectId and run id. Each row in CSV report contains the File Path, error/warning code and error/warning message.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
run_id = "4:072888001528021798096225500850762068629" # str | Specifies a unique run id of the Protection Group run.
object_id = "objectId_example" # str | Specifies the id of the object for which errors/warnings are to be returned. 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the CSV of errors/warnings for a given run and an object.
	client.protection_group.get_run_errors_report(id, run_id, object_id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_run_errors_report: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the CSV of errors/warnings for a given run and an object.
	client.protection_group.get_run_errors_report(id, run_id, object_id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_run_errors_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. |
 **object_id** | **str**| Specifies the id of the object for which errors/warnings are to be returned.  |
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
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runs_report**
> get_runs_report(id, run_id, object_id)

Get the CSV of errors/warnings for a given run and an object.

Get an CSV report for given objectId and run id. Report will depend on the query parameter fileType, default will be: success_files_list where each row contains the name of file backedup successfully.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies a unique id of the Protection Group.
run_id = "4:072888001528021798096225500850762068629" # str | Specifies a unique run id of the Protection Group run.
object_id = "objectId_example" # str | Specifies the id of the object for which errors/warnings are to be returned. 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
file_type = "fileType_example" # str | Specifies the downloaded type, i.e: success_files_list, default: success_files_list (optional)

# example passing only required values which don't have defaults set
try:
	# Get the CSV of errors/warnings for a given run and an object.
	client.protection_group.get_runs_report(id, run_id, object_id)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_runs_report: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the CSV of errors/warnings for a given run and an object.
	client.protection_group.get_runs_report(id, run_id, object_id, access_cluster_id=access_cluster_id, region_id=region_id, file_type=file_type)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->get_runs_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **run_id** | **str**| Specifies a unique run id of the Protection Group run. |
 **object_id** | **str**| Specifies the id of the object for which errors/warnings are to be returned.  |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **file_type** | **str**| Specifies the downloaded type, i.e: success_files_list, default: success_files_list | [optional]

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
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_action_on_protection_group_run**
> PerformRunActionResponse perform_action_on_protection_group_run(id, body)

Actions on protection group run.

Perform various actions on a Protection Group run.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.perform_run_action_response import PerformRunActionResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.perform_action_on_protection_group_run_request import PerformActionOnProtectionGroupRunRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
body = PerformActionOnProtectionGroupRunRequest(
        action="Pause",
        pause_params=[
            PauseProtectionRunActionParams(
                run_id="4:072888001528021798096225500850762068629",
            ),
        ],
        resume_params=[
            ResumeProtectionRunActionParams(
                run_id="4:072888001528021798096225500850762068629",
            ),
        ],
        cancel_params=[
            CancelProtectionGroupRunRequest(
                run_id="4:072888001528021798096225500850762068629",
                local_task_id="4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026",
                object_ids=[
                    1,
                ],
                replication_task_id=[
                    "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026",
                ],
                archival_task_id=[
                    "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026",
                ],
                cloud_spin_task_id=[
                    "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026",
                ],
            ),
        ],
    ) # PerformActionOnProtectionGroupRunRequest | Specifies the parameters to perform an action on a protection run.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Actions on protection group run.
	api_response = client.protection_group.perform_action_on_protection_group_run(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->perform_action_on_protection_group_run: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Actions on protection group run.
	api_response = client.protection_group.perform_action_on_protection_group_run(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->perform_action_on_protection_group_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **body** | [**PerformActionOnProtectionGroupRunRequest**](PerformActionOnProtectionGroupRunRequest.md)| Specifies the parameters to perform an action on a protection run. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**PerformRunActionResponse**](PerformRunActionResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mcm_protection_group**
> ProtectionGroup update_mcm_protection_group(id, body)

Update a Protection Group.

Update the specified Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the Protection Group.
body = CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to update a Protection Group.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a Protection Group.
	api_response = client.protection_group.update_mcm_protection_group(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_mcm_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Protection Group.
	api_response = client.protection_group.update_mcm_protection_group(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_mcm_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Group. |
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to update a Protection Group. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **update_protection_group**
> ProtectionGroup update_protection_group(id, body)

Update a Protection Group.

Update the specified Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the Protection Group.
body = CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to update a Protection Group.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a Protection Group.
	api_response = client.protection_group.update_protection_group(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Protection Group.
	api_response = client.protection_group.update_protection_group(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Group. |
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to update a Protection Group. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **update_protection_group_run**
> UpdateProtectionGroupRunResponseBody update_protection_group_run(id, body)

Update runs for a particular Protection Group.

Update runs for a particular Protection Group. A user can perform the following actions: 1. Extend or reduce retention of a local, replication and archival snapshots. 2. Can perform resync operation on failed copy snapshots attempts in this Run. 3. Add new replication and archival snapshot targets to the Run. 4. Add or remove legal hold on the snapshots. Only a user with DSO role can perform this operation. 5. Delete the snapshots that were created as a part of this Run. 6. Apply datalock on existing snapshots where a user cannot manually delete snapshots before the expiry time. 

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_protection_group_run_response_body import UpdateProtectionGroupRunResponseBody
from cohesity_sdk.helios.model.update_protection_group_run_request_body import UpdateProtectionGroupRunRequestBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Group.
body = UpdateProtectionGroupRunRequestBody(
        update_protection_group_run_params=[
            UpdateProtectionGroupRunParams(
                run_id="4:072888001528021798096225500850762068629",
                local_snapshot_config=UpdateLocalSnapshotConfig(
                    enable_legal_hold=True,
                    delete_snapshot=True,
                    data_lock="Compliance",
                    days_to_keep=1,
                ),
                replication_snapshot_config=UpdateReplicationSnapshotConfig(
                    new_snapshot_config=[
                        RunReplicationConfig(
                            id=1,
                            retention=Retention(
                                unit="Days",
                                duration=1,
                                data_lock_config=DataLockConfig(
                                    mode="Compliance",
                                    unit="Days",
                                    duration=1,
                                    enable_worm_on_external_target=True,
                                ),
                            ),
                        ),
                    ],
                    update_existing_snapshot_config=[
                        UpdateExistingReplicationSnapshotConfig(
                            id=1,
                            enable_legal_hold=True,
                            delete_snapshot=True,
                            resync=True,
                            data_lock="Compliance",
                            days_to_keep=1,
                        ),
                    ],
                ),
                archival_snapshot_config=UpdateArchivalSnapshotConfig(
                    new_snapshot_config=[
                        RunArchivalConfig(
                            id=1,
                            archival_target_type="Tape",
                            retention=Retention(
                                unit="Days",
                                duration=1,
                                data_lock_config=DataLockConfig(
                                    mode="Compliance",
                                    unit="Days",
                                    duration=1,
                                    enable_worm_on_external_target=True,
                                ),
                            ),
                            copy_only_fully_successful=True,
                        ),
                    ],
                    update_existing_snapshot_config=[
                        UpdateExistingArchivalSnapshotConfig(
                            id=1,
                            archival_target_type="Tape",
                            enable_legal_hold=True,
                            delete_snapshot=True,
                            resync=True,
                            data_lock="Compliance",
                            days_to_keep=1,
                        ),
                    ],
                ),
            ),
        ],
    ) # UpdateProtectionGroupRunRequestBody | Specifies the parameters to update a Protection Group Run.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update runs for a particular Protection Group.
	api_response = client.protection_group.update_protection_group_run(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_protection_group_run: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update runs for a particular Protection Group.
	api_response = client.protection_group.update_protection_group_run(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_protection_group_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Group. |
 **body** | [**UpdateProtectionGroupRunRequestBody**](UpdateProtectionGroupRunRequestBody.md)| Specifies the parameters to update a Protection Group Run. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**UpdateProtectionGroupRunResponseBody**](UpdateProtectionGroupRunResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_protection_groups_state**
> UpdateProtectionGroupsState update_protection_groups_state(body)

Perform an action like pause, resume, active, deactivate on all specified Protection Groups.

Perform an action like pause, resume, active, deactivate on all specified Protection Groups. Note that the pause or resume actions will take effect from next Protection Run. Also, user can specify only one type of action on all the Protection Groups. Deactivate and activate actions are independent of pause and resume state. Deactivate and activate actions are useful in case of failover situations. Returns success if the state of all the Protection Groups state is changed successfully.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.update_protection_groups_state_request import UpdateProtectionGroupsStateRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_protection_groups_state import UpdateProtectionGroupsState
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UpdateProtectionGroupsStateRequest(
        action="kPause",
        ids=[
            "ids_example",
        ],
    ) # UpdateProtectionGroupsStateRequest | Specifies the parameters to perform an action of list of Protection Groups.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform an action like pause, resume, active, deactivate on all specified Protection Groups.
	api_response = client.protection_group.update_protection_groups_state(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_protection_groups_state: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform an action like pause, resume, active, deactivate on all specified Protection Groups.
	api_response = client.protection_group.update_protection_groups_state(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionGroupApi->update_protection_groups_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProtectionGroupsStateRequest**](UpdateProtectionGroupsStateRequest.md)| Specifies the parameters to perform an action of list of Protection Groups. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**UpdateProtectionGroupsState**](UpdateProtectionGroupsState.md)

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

