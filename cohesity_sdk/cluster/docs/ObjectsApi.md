# cohesity_sdk.ObjectsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_object_runs**](ObjectsApi.md#cancel_object_runs) | **POST** /data-protect/objects/runs/cancel | Cancel object runs.
[**construct_meta_info**](ObjectsApi.md#construct_meta_info) | **POST** /data-protect/snapshots/{snapshotId}/metaInfo | Construct meta info for any workflow from object snapshot and some other information.
[**get_all_indexed_object_snapshots**](ObjectsApi.md#get_all_indexed_object_snapshots) | **GET** /data-protect/objects/{objectId}/indexed-objects/snapshots | Get snapshots of indexed object.
[**get_indexed_object_snapshots**](ObjectsApi.md#get_indexed_object_snapshots) | **GET** /data-protect/objects/{objectId}/protection-groups/{protectionGroupId}/indexed-objects/snapshots | Get snapshots of indexed object.
[**get_object_run_by_run_id**](ObjectsApi.md#get_object_run_by_run_id) | **GET** /data-protect/objects/{id}/runs/{runId} | Get a run for an object.
[**get_object_runs**](ObjectsApi.md#get_object_runs) | **GET** /data-protect/objects/{id}/runs | Get the list of runs for an object.
[**get_object_snapshot_info**](ObjectsApi.md#get_object_snapshot_info) | **GET** /data-protect/snapshots/{snapshotId} | Get details of object snapshot.
[**get_object_snapshot_volume_info**](ObjectsApi.md#get_object_snapshot_volume_info) | **GET** /data-protect/snapshots/{snapshotId}/volume | Get volume info of object snapshot.
[**get_object_snapshots**](ObjectsApi.md#get_object_snapshots) | **GET** /data-protect/objects/{id}/snapshots | List the snapshots for a given object.
[**get_object_stats**](ObjectsApi.md#get_object_stats) | **GET** /data-protect/objects/{id}/stats | Get stats for a given object.
[**get_object_tree**](ObjectsApi.md#get_object_tree) | **GET** /data-protect/objects/{id}/tree | Get the objects tree hierarchy for for an Object.
[**get_objects_last_run**](ObjectsApi.md#get_objects_last_run) | **GET** /data-protect/objects/last-run | Get last protection run of objects.
[**get_pit_ranges_for_protected_object**](ObjectsApi.md#get_pit_ranges_for_protected_object) | **GET** /data-protect/objects/{id}/pit-ranges | Get PIT ranges for an object
[**get_protected_object_of_any_type_by_id**](ObjectsApi.md#get_protected_object_of_any_type_by_id) | **GET** /data-protect/objects/{id} | Get an Object.
[**get_protected_objects_of_any_type**](ObjectsApi.md#get_protected_objects_of_any_type) | **GET** /data-protect/objects | Get Objects.
[**get_source_hierarchy_objects**](ObjectsApi.md#get_source_hierarchy_objects) | **GET** /data-protect/sources/{sourceId}/objects | List objects on a source which can be used for data protection.
[**objects_actions**](ObjectsApi.md#objects_actions) | **POST** /data-protect/objects/actions | Actions on Objects
[**perform_action_on_object**](ObjectsApi.md#perform_action_on_object) | **POST** /data-protect/objects/{id}/actions | Perform an action on an object.
[**update_object_snapshot**](ObjectsApi.md#update_object_snapshot) | **PUT** /data-protect/objects/{id}/snapshots/{snapshotId} | Update an object snapshot.


# **cancel_object_runs**
> CancelObjectRunsResults cancel_object_runs(body)

Cancel object runs.

Cancel object runs for object based protection. This does not apply to Group based protection.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.cancel_object_runs_results import CancelObjectRunsResults
from cohesity_sdk.cluster.model.cancel_object_runs_request import CancelObjectRunsRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CancelObjectRunsRequest(
        object_runs=[
            CancelObjectRunsParams(
                object_id=1,
                runs_config=[
                    CancelObjectRunParams(
                        run_id="run_id_example",
                        cancel_local_run=True,
                        archival_target_ids=[
                            1,
                        ],
                        replication_targets=[
                            ClusterIdentifier(
                                cluster_id=1,
                                cluster_incarnation_id=1,
                            ),
                        ],
                        cloud_spin_target_ids=[
                            1,
                        ],
                    ),
                ],
            ),
        ],
    ) # CancelObjectRunsRequest | Specifies the parameters to cancel object runs.

# example passing only required values which don't have defaults set
try:
	# Cancel object runs.
	api_response = client.objects.cancel_object_runs(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->cancel_object_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelObjectRunsRequest**](CancelObjectRunsRequest.md)| Specifies the parameters to cancel object runs. |

### Return type

[**CancelObjectRunsResults**](CancelObjectRunsResults.md)

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

# **construct_meta_info**
> ConstructMetaInfoResult construct_meta_info(snapshot_id, body)

Construct meta info for any workflow from object snapshot and some other information.

Construct meta info from object snapshot and some additional params.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.construct_meta_info_params import ConstructMetaInfoParams
from cohesity_sdk.cluster.model.construct_meta_info_result import ConstructMetaInfoResult
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


snapshot_id = "snapshotId_example" # str | Specifies the snapshot id.
body = ConstructMetaInfoParams(
        environment="kOracle",
        oracle_params={},
    ) # ConstructMetaInfoParams | Specifies the parameters to construct meta info for desired workflow.

# example passing only required values which don't have defaults set
try:
	# Construct meta info for any workflow from object snapshot and some other information.
	api_response = client.objects.construct_meta_info(snapshot_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->construct_meta_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. |
 **body** | [**ConstructMetaInfoParams**](ConstructMetaInfoParams.md)| Specifies the parameters to construct meta info for desired workflow. |

### Return type

[**ConstructMetaInfoResult**](ConstructMetaInfoResult.md)

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

# **get_all_indexed_object_snapshots**
> GetIndexedObjectSnapshotsResponseBody get_all_indexed_object_snapshots(object_id, indexed_object_name)

Get snapshots of indexed object.

Get snapshots of indexed object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_indexed_object_snapshots_response_body import GetIndexedObjectSnapshotsResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


object_id = 1 # int | Specifies the object id.
indexed_object_name = "indexedObjectName_example" # str | Specifies the indexed object name.
protection_group_id = "protectionGroupId_example" # str | Specifies the protection group id. (optional)
include_indexed_snapshots_only = False # bool | Specifies whether to only return snapshots which are indexed. In an indexed snapshot files are guaranteed to exist, while in a non-indexed snapshot files may not exist. (optional) if omitted the server will use the default value of False
from_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken after this value. (optional)
to_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken before this value. (optional)
run_types = [
        "kRegular",
    ] # [str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)

# example passing only required values which don't have defaults set
try:
	# Get snapshots of indexed object.
	api_response = client.objects.get_all_indexed_object_snapshots(object_id, indexed_object_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_all_indexed_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get snapshots of indexed object.
	api_response = client.objects.get_all_indexed_object_snapshots(object_id, indexed_object_name, protection_group_id=protection_group_id, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_all_indexed_object_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **int**| Specifies the object id. |
 **indexed_object_name** | **str**| Specifies the indexed object name. |
 **protection_group_id** | **str**| Specifies the protection group id. | [optional]
 **include_indexed_snapshots_only** | **bool**| Specifies whether to only return snapshots which are indexed. In an indexed snapshot files are guaranteed to exist, while in a non-indexed snapshot files may not exist. | [optional] if omitted the server will use the default value of False
 **from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken after this value. | [optional]
 **to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken before this value. | [optional]
 **run_types** | **[str]**| Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. | [optional]

### Return type

[**GetIndexedObjectSnapshotsResponseBody**](GetIndexedObjectSnapshotsResponseBody.md)

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

# **get_indexed_object_snapshots**
> GetIndexedObjectSnapshotsResponseBody get_indexed_object_snapshots(protection_group_id, object_id, indexed_object_name)

Get snapshots of indexed object.

Get snapshots of indexed object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_indexed_object_snapshots_response_body import GetIndexedObjectSnapshotsResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


protection_group_id = "protectionGroupId_example" # str | Specifies the protection group id.
object_id = 1 # int | Specifies the object id.
indexed_object_name = "indexedObjectName_example" # str | Specifies the indexed object name.
include_indexed_snapshots_only = False # bool | Specifies whether to only return snapshots which are indexed. In an indexed snapshots file are guaranteened to exist, while in a non-indexed snapshots file may not exist. (optional) if omitted the server will use the default value of False
from_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken after this value. (optional)
to_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken before this value. (optional)
run_types = [
        "kRegular",
    ] # [str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)

# example passing only required values which don't have defaults set
try:
	# Get snapshots of indexed object.
	api_response = client.objects.get_indexed_object_snapshots(protection_group_id, object_id, indexed_object_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_indexed_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get snapshots of indexed object.
	api_response = client.objects.get_indexed_object_snapshots(protection_group_id, object_id, indexed_object_name, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_indexed_object_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protection_group_id** | **str**| Specifies the protection group id. |
 **object_id** | **int**| Specifies the object id. |
 **indexed_object_name** | **str**| Specifies the indexed object name. |
 **include_indexed_snapshots_only** | **bool**| Specifies whether to only return snapshots which are indexed. In an indexed snapshots file are guaranteened to exist, while in a non-indexed snapshots file may not exist. | [optional] if omitted the server will use the default value of False
 **from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken after this value. | [optional]
 **to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken before this value. | [optional]
 **run_types** | **[str]**| Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. | [optional]

### Return type

[**GetIndexedObjectSnapshotsResponseBody**](GetIndexedObjectSnapshotsResponseBody.md)

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

# **get_object_run_by_run_id**
> ObjectProtectionRunSummary get_object_run_by_run_id(id, run_id)

Get a run for an object.

Get a run for an object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.object_protection_run_summary import ObjectProtectionRunSummary
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the object.
run_id = "runId_example" # str | Specifies the id of the run.

# example passing only required values which don't have defaults set
try:
	# Get a run for an object.
	api_response = client.objects.get_object_run_by_run_id(id, run_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_run_by_run_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the object. |
 **run_id** | **str**| Specifies the id of the run. |

### Return type

[**ObjectProtectionRunSummary**](ObjectProtectionRunSummary.md)

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

# **get_object_runs**
> GetObjectRunsResponseBody get_object_runs(id)

Get the list of runs for an object.

Get the runs for a particular object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.get_object_runs_response_body import GetObjectRunsResponseBody
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the object.
run_id = "runId_example" # str | Specifies a unique id of the run. (optional)
start_time_usecs = 1 # int | Filter by a start time when the run starts. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 1 # int | Filter by a end time when the run starts. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. (optional)
run_types = [
        "kAll",
    ] # [str] | Filter by run type. Only protection run matching the specified types will be returned. (optional)
local_backup_object_status = [
        "kInProgress",
    ] # [str] | Specifies a list of status for the object in the backup run. (optional)
replication_object_status = [
        "kInProgress",
    ] # [str] | Specifies a list of status for the object in the replication run. (optional)
archival_object_status = [
        "kInProgress",
    ] # [str] | Specifies a list of status for the object in the archival run. (optional)
cloud_spin_run_status = [
        "kInProgress",
    ] # [str] | Specifies a list of status for the object in the cloud spin run. (optional)
num_runs = 1 # int | Specifies the max number of runs. If not specified, at most 100 runs will be returned. (optional)
pagination_cookie = "paginationCookie_example" # str | Specifies the pagination cookie with which subsequent parts of the response can be fetched. Users can use this to get next runs (optional)
exclude_non_restorable_runs = False # bool | Specifies whether to exclude non restorable runs. Run is treated restorable only if there is atleast one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
try:
	# Get the list of runs for an object.
	api_response = client.objects.get_object_runs(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_runs: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of runs for an object.
	api_response = client.objects.get_object_runs(id, run_id=run_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, run_types=run_types, local_backup_object_status=local_backup_object_status, replication_object_status=replication_object_status, archival_object_status=archival_object_status, cloud_spin_run_status=cloud_spin_run_status, num_runs=num_runs, pagination_cookie=pagination_cookie, exclude_non_restorable_runs=exclude_non_restorable_runs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the object. |
 **run_id** | **str**| Specifies a unique id of the run. | [optional]
 **start_time_usecs** | **int**| Filter by a start time when the run starts. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional]
 **end_time_usecs** | **int**| Filter by a end time when the run starts. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. | [optional]
 **run_types** | **[str]**| Filter by run type. Only protection run matching the specified types will be returned. | [optional]
 **local_backup_object_status** | **[str]**| Specifies a list of status for the object in the backup run. | [optional]
 **replication_object_status** | **[str]**| Specifies a list of status for the object in the replication run. | [optional]
 **archival_object_status** | **[str]**| Specifies a list of status for the object in the archival run. | [optional]
 **cloud_spin_run_status** | **[str]**| Specifies a list of status for the object in the cloud spin run. | [optional]
 **num_runs** | **int**| Specifies the max number of runs. If not specified, at most 100 runs will be returned. | [optional]
 **pagination_cookie** | **str**| Specifies the pagination cookie with which subsequent parts of the response can be fetched. Users can use this to get next runs | [optional]
 **exclude_non_restorable_runs** | **bool**| Specifies whether to exclude non restorable runs. Run is treated restorable only if there is atleast one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. | [optional] if omitted the server will use the default value of False

### Return type

[**GetObjectRunsResponseBody**](GetObjectRunsResponseBody.md)

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

# **get_object_snapshot_info**
> ObjectSnapshot get_object_snapshot_info(snapshot_id)

Get details of object snapshot.

Get details of object snapshot.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.object_snapshot import ObjectSnapshot
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


snapshot_id = "snapshotId_example" # str | Specifies the snapshot id.

# example passing only required values which don't have defaults set
try:
	# Get details of object snapshot.
	api_response = client.objects.get_object_snapshot_info(snapshot_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_snapshot_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. |

### Return type

[**ObjectSnapshot**](ObjectSnapshot.md)

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

# **get_object_snapshot_volume_info**
> ObjectSnapshotVolumeInfo get_object_snapshot_volume_info(snapshot_id)

Get volume info of object snapshot.

Get volume info of object snapshot.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.object_snapshot_volume_info import ObjectSnapshotVolumeInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


snapshot_id = "snapshotId_example" # str | Specifies the snapshot id.
include_supported_only = True # bool | Specifies whether to only return supported volumes. (optional)
point_in_time_usecs = 3.14 # float | Specifies the point-in-time timestamp (in usecs from epoch) between snapshots for which the volume info is to be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# Get volume info of object snapshot.
	api_response = client.objects.get_object_snapshot_volume_info(snapshot_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_snapshot_volume_info: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get volume info of object snapshot.
	api_response = client.objects.get_object_snapshot_volume_info(snapshot_id, include_supported_only=include_supported_only, point_in_time_usecs=point_in_time_usecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_snapshot_volume_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. |
 **include_supported_only** | **bool**| Specifies whether to only return supported volumes. | [optional]
 **point_in_time_usecs** | **float**| Specifies the point-in-time timestamp (in usecs from epoch) between snapshots for which the volume info is to be returned. | [optional]

### Return type

[**ObjectSnapshotVolumeInfo**](ObjectSnapshotVolumeInfo.md)

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

# **get_object_snapshots**
> GetObjectSnapshotsResponseBody get_object_snapshots(id)

List the snapshots for a given object.

List the snapshots for a given object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_object_snapshots_response_body import GetObjectSnapshotsResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Object.
from_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which are taken after this value. (optional)
to_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which are taken before this value. (optional)
run_types = [
        "kRegular",
    ] # [str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)
protection_group_ids = [
        "protectionGroupIds_example",
    ] # [str] | If specified, this returns only the snapshots of the specified object ID, which belong to the provided protection group IDs. (optional)
run_instance_ids = [
        1,
    ] # [int] | Filter by a list run instance ids. If specified, only snapshots created by these protection runs will be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# List the snapshots for a given object.
	api_response = client.objects.get_object_snapshots(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the snapshots for a given object.
	api_response = client.objects.get_object_snapshots(id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types, protection_group_ids=protection_group_ids, run_instance_ids=run_instance_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which are taken after this value. | [optional]
 **to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which are taken before this value. | [optional]
 **run_types** | **[str]**| Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. | [optional]
 **protection_group_ids** | **[str]**| If specified, this returns only the snapshots of the specified object ID, which belong to the provided protection group IDs. | [optional]
 **run_instance_ids** | **[int]**| Filter by a list run instance ids. If specified, only snapshots created by these protection runs will be returned. | [optional]

### Return type

[**GetObjectSnapshotsResponseBody**](GetObjectSnapshotsResponseBody.md)

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

# **get_object_stats**
> ObjectStats get_object_stats(id)

Get stats for a given object.

Get stats for a given object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.object_stats import ObjectStats
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Object.

# example passing only required values which don't have defaults set
try:
	# Get stats for a given object.
	api_response = client.objects.get_object_stats(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |

### Return type

[**ObjectStats**](ObjectStats.md)

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

# **get_object_tree**
> ObjectWithChildren get_object_tree(id)

Get the objects tree hierarchy for for an Object.

Get the objects tree hierarchy for for an Object. If the object does not have a hierarchy then a single object will be returned.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.object_with_children import ObjectWithChildren
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Object.

# example passing only required values which don't have defaults set
try:
	# Get the objects tree hierarchy for for an Object.
	api_response = client.objects.get_object_tree(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_object_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |

### Return type

[**ObjectWithChildren**](ObjectWithChildren.md)

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

# **get_objects_last_run**
> ObjectsLastRun get_objects_last_run()

Get last protection run of objects.

Get last protection run of objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.objects_last_run import ObjectsLastRun
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int] | Specifies a list of object ids, only last runs for these objects will be returned. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Objects which belongs to all tenants which the current user has permission to see. (optional)
pagination_cookie = "paginationCookie_example" # str | Specifies the pagination cookie with which subsequent parts of the response can be fetched. (optional)
count = 1 # int | Specifies the number of objects to be fetched for the specified pagination cookie. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get last protection run of objects.
	api_response = client.objects.get_objects_last_run(ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, pagination_cookie=pagination_cookie, count=count)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_objects_last_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Specifies a list of object ids, only last runs for these objects will be returned. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Objects which belongs to all tenants which the current user has permission to see. | [optional]
 **pagination_cookie** | **str**| Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional]
 **count** | **int**| Specifies the number of objects to be fetched for the specified pagination cookie. | [optional]

### Return type

[**ObjectsLastRun**](ObjectsLastRun.md)

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

# **get_pit_ranges_for_protected_object**
> GetPITRangesProtectedObjectResponseBody get_pit_ranges_for_protected_object(id)

Get PIT ranges for an object

Returns the time ranges within which the specified protected object can be restored to any Point in time.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_pit_ranges_protected_object_response_body import GetPITRangesProtectedObjectResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the ID of the protected object.
from_time_usecs = 1 # int | If specified, return the time ranges that lie after this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. (optional)
to_time_usecs = 1 # int | If specified, return the time ranges that lie before this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. (optional)
protection_group_ids = [
        "protectionGroupIds_example",
    ] # [str] | If specified, return only the points in time corresponding to these protection group IDs. (optional)

# example passing only required values which don't have defaults set
try:
	# Get PIT ranges for an object
	api_response = client.objects.get_pit_ranges_for_protected_object(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_pit_ranges_for_protected_object: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get PIT ranges for an object
	api_response = client.objects.get_pit_ranges_for_protected_object(id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, protection_group_ids=protection_group_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_pit_ranges_for_protected_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the protected object. |
 **from_time_usecs** | **int**| If specified, return the time ranges that lie after this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. | [optional]
 **to_time_usecs** | **int**| If specified, return the time ranges that lie before this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. | [optional]
 **protection_group_ids** | **[str]**| If specified, return only the points in time corresponding to these protection group IDs. | [optional]

### Return type

[**GetPITRangesProtectedObjectResponseBody**](GetPITRangesProtectedObjectResponseBody.md)

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

# **get_protected_object_of_any_type_by_id**
> ProtectedObjectInfo get_protected_object_of_any_type_by_id(id)

Get an Object.

Get Object configrations for given object id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.protected_object_info import ProtectedObjectInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Object.
only_protected_objects = True # bool | If true, the response will include only objects which have been protected. (optional)
storage_domain_id = 1 # int | Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. (optional)
environments = [
        "kVMware",
    ] # [str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protected objects protecting the specified environment types are returned. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. (optional)
include_last_run_info = True # bool | If true, the response will include information about the last protection run on this object. (optional)
only_auto_protected_objects = True # bool | If true, the response will include only the auto protected objects. (optional)
only_leaf_objects = True # bool | If true, the response will include only the leaf level objects. (optional)

# example passing only required values which don't have defaults set
try:
	# Get an Object.
	api_response = client.objects.get_protected_object_of_any_type_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_protected_object_of_any_type_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get an Object.
	api_response = client.objects.get_protected_object_of_any_type_by_id(id, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_protected_object_of_any_type_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **only_protected_objects** | **bool**| If true, the response will include only objects which have been protected. | [optional]
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. | [optional]
 **environments** | **[str]**| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protected objects protecting the specified environment types are returned. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. | [optional]
 **include_last_run_info** | **bool**| If true, the response will include information about the last protection run on this object. | [optional]
 **only_auto_protected_objects** | **bool**| If true, the response will include only the auto protected objects. | [optional]
 **only_leaf_objects** | **bool**| If true, the response will include only the leaf level objects. | [optional]

### Return type

[**ProtectedObjectInfo**](ProtectedObjectInfo.md)

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

# **get_protected_objects_of_any_type**
> GetProtectedObjectsResponse get_protected_objects_of_any_type()

Get Objects.

Get Objects Configurations.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_protected_objects_response import GetProtectedObjectsResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int] | Filter by a list of Object ids. (optional)
policy_ids = [
        "policyIds_example",
    ] # [str] | Filter by Policy ids that are associated with Protected Objects. (optional)
parent_id = 1 # int | Filter by Parent Id. Parent id is a unique object Id which may contain protected objects underneath in the source tree. (optional)
only_protected_objects = True # bool | If true, the response will include only objects which have been protected. (optional)
storage_domain_id = 1 # int | Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. (optional)
environments = [
        "kVMware",
    ] # [str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protected objects protecting the specified environment types are returned. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. (optional)
include_last_run_info = True # bool | If true, the response will include information about the last protection run on this object. (optional)
only_auto_protected_objects = True # bool | If true, the response will include only the auto protected objects. (optional)
only_leaf_objects = True # bool | If true, the response will include only the leaf level objects. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Objects.
	api_response = client.objects.get_protected_objects_of_any_type(ids=ids, policy_ids=policy_ids, parent_id=parent_id, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_protected_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Filter by a list of Object ids. | [optional]
 **policy_ids** | **[str]**| Filter by Policy ids that are associated with Protected Objects. | [optional]
 **parent_id** | **int**| Filter by Parent Id. Parent id is a unique object Id which may contain protected objects underneath in the source tree. | [optional]
 **only_protected_objects** | **bool**| If true, the response will include only objects which have been protected. | [optional]
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. | [optional]
 **environments** | **[str]**| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protected objects protecting the specified environment types are returned. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. | [optional]
 **include_last_run_info** | **bool**| If true, the response will include information about the last protection run on this object. | [optional]
 **only_auto_protected_objects** | **bool**| If true, the response will include only the auto protected objects. | [optional]
 **only_leaf_objects** | **bool**| If true, the response will include only the leaf level objects. | [optional]

### Return type

[**GetProtectedObjectsResponse**](GetProtectedObjectsResponse.md)

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

# **get_source_hierarchy_objects**
> SourceHierarchyObjectSummaries get_source_hierarchy_objects(source_id)

List objects on a source which can be used for data protection.

List objects which can be used for data protection.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.source_hierarchy_object_summaries import SourceHierarchyObjectSummaries
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


source_id = 1 # int | Specifies the source ID for which objects should be returned.
parent_id = 1 # int, none_type | Specifies the parent ID under which objects should be returned. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Objects which belongs to all tenants which the current user has permission to see. (optional)
vmware_object_types = [
        "kVCenter",
    ] # [str] | Specifies the VMware object types to filter objects. (optional)
netapp_object_types = [
        "kCluster",
    ] # [str] | Specifies the Netapp object types to filter objects. (optional)
o365_object_types = [
        "kDomain",
    ] # [str] | Specifies the Office 365 object types to filter objects. (optional)
cassandra_object_types = [
        "kCluster",
    ] # [str] | Specifies the Cassandra object types to filter objects. (optional)
mongodb_object_types = [
        "kCluster",
    ] # [str] | Specifies the Mongo DB object types to filter objects. (optional)
couchbase_object_types = [
        "kCluster",
    ] # [str] | Specifies the Couchbase object types to filter objects. (optional)
hdfs_object_types = [
        "kCluster",
    ] # [str] | Specifies the HDFS object types to filter objects. (optional)
hbase_object_types = [
        "kCluster",
    ] # [str] | Specifies the Hbase object types to filter objects. (optional)
hive_object_types = [
        "kCluster",
    ] # [str] | Specifies the Hive object types to filter objects. (optional)
hyperv_object_types = [
        "kSCVMMServer",
    ] # [str] | Specifies the HyperV object types to filter objects. (optional)
azure_object_types = [
        "kSubscription",
    ] # [str] | Specifies the Azure object types to filter objects. (optional)
kvm_object_types = [
        "kOVirtManager",
    ] # [str] | Specifies the KVM object types to filter objects. (optional)
aws_object_types = [
        "kIAMUser",
    ] # [str] | Specifies the AWS object types to filter objects. (optional)
gcp_object_types = [
        "kIAMUser",
    ] # [str] | Specifies the GCP object types to filter objects. (optional)
acropolis_object_types = [
        "kPrismCentral",
    ] # [str] | Specifies the Acropolis object types to filter objects. (optional)
generic_nas_object_types = [
        "kGroup",
    ] # [str] | Specifies the generic NAS object types to filter objects. (optional)
isilon_object_types = [
        "kCluster",
    ] # [str] | Specifies the Isilon object types to filter objects. (optional)
flashblade_object_types = [
        "kStorageArray",
    ] # [str] | Specifies the Flashblade object types to filter objects. (optional)
elastifile_object_types = [
        "kCluster",
    ] # [str] | Specifies the Elastifile object types to filter objects. (optional)
gpfs_object_types = [
        "kCluster",
    ] # [str] | Specifies the GPFS object types to filter objects. (optional)
pure_object_types = [
        "kStorageArray",
    ] # [str] | Specifies the Pure object types to filter objects. (optional)
nimble_object_types = [
        "kStorageArray",
    ] # [str] | Specifies the Nimble object types to filter objects. (optional)
physical_object_types = [
        "kGroup",
    ] # [str] | Specifies the Physical object types to filter objects. (optional)
kubernetes_object_types = [
        "kCluster",
    ] # [str] | Specifies the Kubernetes object types to filter objects. (optional)
exchange_object_types = [
        "kRootContainer",
    ] # [str] | Specifies the Exchange object types to filter objects. (optional)
ad_object_types = [
        "kRootContainer",
    ] # [str] | Specifies the AD object types to filter objects. (optional)
mssql_object_types = [
        "kInstance",
    ] # [str] | Specifies the MSSQL object types to filter objects. (optional)
oracle_object_types = [
        "kRACRootContainer",
    ] # [str] | Specifies the Oracle object types to filter objects. (optional)

# example passing only required values which don't have defaults set
try:
	# List objects on a source which can be used for data protection.
	api_response = client.objects.get_source_hierarchy_objects(source_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_source_hierarchy_objects: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List objects on a source which can be used for data protection.
	api_response = client.objects.get_source_hierarchy_objects(source_id, parent_id=parent_id, tenant_ids=tenant_ids, include_tenants=include_tenants, vmware_object_types=vmware_object_types, netapp_object_types=netapp_object_types, o365_object_types=o365_object_types, cassandra_object_types=cassandra_object_types, mongodb_object_types=mongodb_object_types, couchbase_object_types=couchbase_object_types, hdfs_object_types=hdfs_object_types, hbase_object_types=hbase_object_types, hive_object_types=hive_object_types, hyperv_object_types=hyperv_object_types, azure_object_types=azure_object_types, kvm_object_types=kvm_object_types, aws_object_types=aws_object_types, gcp_object_types=gcp_object_types, acropolis_object_types=acropolis_object_types, generic_nas_object_types=generic_nas_object_types, isilon_object_types=isilon_object_types, flashblade_object_types=flashblade_object_types, elastifile_object_types=elastifile_object_types, gpfs_object_types=gpfs_object_types, pure_object_types=pure_object_types, nimble_object_types=nimble_object_types, physical_object_types=physical_object_types, kubernetes_object_types=kubernetes_object_types, exchange_object_types=exchange_object_types, ad_object_types=ad_object_types, mssql_object_types=mssql_object_types, oracle_object_types=oracle_object_types)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->get_source_hierarchy_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| Specifies the source ID for which objects should be returned. |
 **parent_id** | **int, none_type**| Specifies the parent ID under which objects should be returned. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Objects which belongs to all tenants which the current user has permission to see. | [optional]
 **vmware_object_types** | **[str]**| Specifies the VMware object types to filter objects. | [optional]
 **netapp_object_types** | **[str]**| Specifies the Netapp object types to filter objects. | [optional]
 **o365_object_types** | **[str]**| Specifies the Office 365 object types to filter objects. | [optional]
 **cassandra_object_types** | **[str]**| Specifies the Cassandra object types to filter objects. | [optional]
 **mongodb_object_types** | **[str]**| Specifies the Mongo DB object types to filter objects. | [optional]
 **couchbase_object_types** | **[str]**| Specifies the Couchbase object types to filter objects. | [optional]
 **hdfs_object_types** | **[str]**| Specifies the HDFS object types to filter objects. | [optional]
 **hbase_object_types** | **[str]**| Specifies the Hbase object types to filter objects. | [optional]
 **hive_object_types** | **[str]**| Specifies the Hive object types to filter objects. | [optional]
 **hyperv_object_types** | **[str]**| Specifies the HyperV object types to filter objects. | [optional]
 **azure_object_types** | **[str]**| Specifies the Azure object types to filter objects. | [optional]
 **kvm_object_types** | **[str]**| Specifies the KVM object types to filter objects. | [optional]
 **aws_object_types** | **[str]**| Specifies the AWS object types to filter objects. | [optional]
 **gcp_object_types** | **[str]**| Specifies the GCP object types to filter objects. | [optional]
 **acropolis_object_types** | **[str]**| Specifies the Acropolis object types to filter objects. | [optional]
 **generic_nas_object_types** | **[str]**| Specifies the generic NAS object types to filter objects. | [optional]
 **isilon_object_types** | **[str]**| Specifies the Isilon object types to filter objects. | [optional]
 **flashblade_object_types** | **[str]**| Specifies the Flashblade object types to filter objects. | [optional]
 **elastifile_object_types** | **[str]**| Specifies the Elastifile object types to filter objects. | [optional]
 **gpfs_object_types** | **[str]**| Specifies the GPFS object types to filter objects. | [optional]
 **pure_object_types** | **[str]**| Specifies the Pure object types to filter objects. | [optional]
 **nimble_object_types** | **[str]**| Specifies the Nimble object types to filter objects. | [optional]
 **physical_object_types** | **[str]**| Specifies the Physical object types to filter objects. | [optional]
 **kubernetes_object_types** | **[str]**| Specifies the Kubernetes object types to filter objects. | [optional]
 **exchange_object_types** | **[str]**| Specifies the Exchange object types to filter objects. | [optional]
 **ad_object_types** | **[str]**| Specifies the AD object types to filter objects. | [optional]
 **mssql_object_types** | **[str]**| Specifies the MSSQL object types to filter objects. | [optional]
 **oracle_object_types** | **[str]**| Specifies the Oracle object types to filter objects. | [optional]

### Return type

[**SourceHierarchyObjectSummaries**](SourceHierarchyObjectSummaries.md)

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

# **objects_actions**
> objects_actions(body)

Actions on Objects

Specifies the request to perform various actions on multiple objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.objects_action_request import ObjectsActionRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ObjectsActionRequest(
        action="Link",
        link_params=ObjectLinkingParams(),
        un_link_params=ObjectUnLinkingParams(),
    ) # ObjectsActionRequest | Specifies the paramteres to execute actions on given list of objects.

# example passing only required values which don't have defaults set
try:
	# Actions on Objects
	client.objects.objects_actions(body)
except ApiException as e:
	print("Exception when calling ObjectsApi->objects_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectsActionRequest**](ObjectsActionRequest.md)| Specifies the paramteres to execute actions on given list of objects. |

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_action_on_object**
> perform_action_on_object(id, body)

Perform an action on an object.

Perform an action on an object. Depending on the object environment type, different actions are available.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_object_action_requeste34c1ef0_ccb3462a_a3b358a8e5c7a1e7 import CommonObjectActionRequeste34c1ef0Ccb3462aA3b358a8e5c7a1e7
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Object.
body = CommonObjectActionRequeste34c1ef0Ccb3462aA3b358a8e5c7a1e7(
        environment="kVMware",
    ) # CommonObjectActionRequeste34c1ef0Ccb3462aA3b358a8e5c7a1e7 | Specifies the parameters to perform an action on an object.

# example passing only required values which don't have defaults set
try:
	# Perform an action on an object.
	client.objects.perform_action_on_object(id, body)
except ApiException as e:
	print("Exception when calling ObjectsApi->perform_action_on_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **body** | [**CommonObjectActionRequeste34c1ef0Ccb3462aA3b358a8e5c7a1e7**](CommonObjectActionRequeste34c1ef0Ccb3462aA3b358a8e5c7a1e7.md)| Specifies the parameters to perform an action on an object. |

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_snapshot**
> ObjectSnapshot update_object_snapshot(id, snapshot_id, body)

Update an object snapshot.

Update an object snapshot.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_object_snapshot_request import UpdateObjectSnapshotRequest
from cohesity_sdk.cluster.model.object_snapshot import ObjectSnapshot
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Object.
snapshot_id = "snapshotId_example" # str | Specifies the id of the snapshot.<br> Note: 1. If the snapshotid of one of the apps is specified, it applies for all the databases in the Protection Run.<br> 2. In case of volume based jobs, please specify the snapshotid of the source not the database. if source snapshot is specified, applied to source snapshot. if database snapshotid is specified in case of volume based jobs, then it is applicable for host's snapshot.
body = UpdateObjectSnapshotRequest(
        set_legal_hold=True,
        data_lock_type="Compliance",
        expiry_time_secs=1,
    ) # UpdateObjectSnapshotRequest | Specifies the parameters update an object snapshot.

# example passing only required values which don't have defaults set
try:
	# Update an object snapshot.
	api_response = client.objects.update_object_snapshot(id, snapshot_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectsApi->update_object_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **snapshot_id** | **str**| Specifies the id of the snapshot.&lt;br&gt; Note: 1. If the snapshotid of one of the apps is specified, it applies for all the databases in the Protection Run.&lt;br&gt; 2. In case of volume based jobs, please specify the snapshotid of the source not the database. if source snapshot is specified, applied to source snapshot. if database snapshotid is specified in case of volume based jobs, then it is applicable for host&#39;s snapshot. |
 **body** | [**UpdateObjectSnapshotRequest**](UpdateObjectSnapshotRequest.md)| Specifies the parameters update an object snapshot. |

### Return type

[**ObjectSnapshot**](ObjectSnapshot.md)

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
