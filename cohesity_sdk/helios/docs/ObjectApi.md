# cohesity_sdk.ObjectApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_object_contents**](ObjectApi.md#browse_object_contents) | **POST** /data-protect/objects/{id}/browse | Fetch the contents (files &amp; folders) for the specified object.
[**cancel_object_runs**](ObjectApi.md#cancel_object_runs) | **POST** /data-protect/objects/runs/cancel | Cancel object runs.
[**construct_meta_info**](ObjectApi.md#construct_meta_info) | **POST** /data-protect/snapshots/{snapshotId}/meta-info | Construct meta info for any workflow from object snapshot and some other information.
[**filter_objects**](ObjectApi.md#filter_objects) | **POST** /data-protect/filter/objects | List all the filtered objects.
[**get_all_indexed_object_snapshots**](ObjectApi.md#get_all_indexed_object_snapshots) | **GET** /data-protect/objects/{objectId}/indexed-objects/snapshots | Get snapshots of indexed object.
[**get_deleted_protected_objects**](ObjectApi.md#get_deleted_protected_objects) | **GET** /data-protect/sources/{sourceId}/deleted-protected-objects | List deleted protected objects.
[**get_indexed_object_snapshots**](ObjectApi.md#get_indexed_object_snapshots) | **GET** /data-protect/objects/{objectId}/protection-groups/{protectionGroupId}/indexed-objects/snapshots | Get snapshots of indexed object.
[**get_mcm_object_snapshots**](ObjectApi.md#get_mcm_object_snapshots) | **GET** /mcm/data-protect/objects/snapshots | List the snapshots for a given object.
[**get_mcm_object_stats**](ObjectApi.md#get_mcm_object_stats) | **GET** /mcm/data-protect/objects/stats | Get stats for a given object.
[**get_mcm_object_summary**](ObjectApi.md#get_mcm_object_summary) | **GET** /mcm/objects/summary | Get the summary for a given object.
[**get_mcm_objects_activity**](ObjectApi.md#get_mcm_objects_activity) | **POST** /mcm/data-protect/objects/activity | Get Object activity on Helios.
[**get_mcm_objects_activity_by_id**](ObjectApi.md#get_mcm_objects_activity_by_id) | **GET** /mcm/data-protect/objects/activity/{id} | Get Object activity on Helios.
[**get_mcm_objects_last_run_activity**](ObjectApi.md#get_mcm_objects_last_run_activity) | **POST** /mcm/data-protect/objects/last-run-activity | Get last protection run of objects.
[**get_object_archival_run_stats**](ObjectApi.md#get_object_archival_run_stats) | **GET** /mcm/data-protect/objects/stats/archival-runs | Get the object archival run stats.
[**get_object_identifiers**](ObjectApi.md#get_object_identifiers) | **GET** /data-protect/objects/object-identifiers | Get Object Identifiers
[**get_object_run_by_run_id**](ObjectApi.md#get_object_run_by_run_id) | **GET** /data-protect/objects/{id}/runs/{runId} | Get a run for an object.
[**get_object_runs**](ObjectApi.md#get_object_runs) | **GET** /data-protect/objects/{id}/runs | Get the list of runs for an object.
[**get_object_snapshot_id**](ObjectApi.md#get_object_snapshot_id) | **POST** /data-protect/objects/{objectId}/snapshotId | Get snapshot id for a given object.
[**get_object_snapshot_info**](ObjectApi.md#get_object_snapshot_info) | **GET** /data-protect/snapshots/{snapshotId} | Get details of object snapshot.
[**get_object_snapshot_volume_info**](ObjectApi.md#get_object_snapshot_volume_info) | **GET** /data-protect/snapshots/{snapshotId}/volume | Get volume info of object snapshot.
[**get_object_snapshots**](ObjectApi.md#get_object_snapshots) | **GET** /data-protect/objects/{id}/snapshots | List the snapshots for a given object.
[**get_object_stats**](ObjectApi.md#get_object_stats) | **GET** /data-protect/objects/{id}/stats | Get stats for a given object.
[**get_object_tree**](ObjectApi.md#get_object_tree) | **GET** /data-protect/objects/{id}/tree | Get the objects tree hierarchy for for an Object.
[**get_objects_last_run**](ObjectApi.md#get_objects_last_run) | **GET** /data-protect/objects/last-run | Get last protection run of objects.
[**get_pit_ranges_for_protected_object**](ObjectApi.md#get_pit_ranges_for_protected_object) | **GET** /data-protect/objects/{id}/pit-ranges | Get PIT ranges for an object
[**get_protected_object_of_any_type_by_id**](ObjectApi.md#get_protected_object_of_any_type_by_id) | **GET** /data-protect/objects/{id} | Get an Object.
[**get_protected_objects_of_any_type**](ObjectApi.md#get_protected_objects_of_any_type) | **GET** /data-protect/objects | Get Objects.
[**get_snapshot_diff**](ObjectApi.md#get_snapshot_diff) | **POST** /data-protect/objects/{id}/snapshot-diff | Get diff between two snapshots of a given object.
[**get_source_hierarchy_objects**](ObjectApi.md#get_source_hierarchy_objects) | **GET** /data-protect/sources/{sourceId}/objects | List objects on a source which can be used for data protection.
[**internal_api_construct_meta_info**](ObjectApi.md#internal_api_construct_meta_info) | **POST** /data-protect/snapshots/{snapshotId}/metaInfo | Construct meta info for any workflow from object snapshot and some other information.
[**internal_api_get_snapshot_diff**](ObjectApi.md#internal_api_get_snapshot_diff) | **POST** /data-protect/objects/{id}/snapshotDiff | Get diff between two snapshots of a given object.
[**mcm_get_tenant_object_ids**](ObjectApi.md#mcm_get_tenant_object_ids) | **POST** /mcm/tenants/object-ids | GetTenantObjectIds
[**mcm_get_tenant_object_protections**](ObjectApi.md#mcm_get_tenant_object_protections) | **POST** /mcm/tenants/protected-objects | GetTenantObjectProtections
[**objects_actions**](ObjectApi.md#objects_actions) | **POST** /data-protect/objects/actions | Actions on Objects
[**perform_action_on_object**](ObjectApi.md#perform_action_on_object) | **POST** /data-protect/objects/{id}/actions | Perform an action on an object.
[**update_object_snapshot**](ObjectApi.md#update_object_snapshot) | **PUT** /data-protect/objects/{id}/snapshots/{snapshotId} | Update an object snapshot.


# **browse_object_contents**
> FileFolderInfo browse_object_contents(id, body)

Fetch the contents (files & folders) for the specified object.

Fetch the contents (files & folders) of the specified path inside the specified object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.file_folder_info import FileFolderInfo
from cohesity_sdk.helios.model.object_browse_request import ObjectBrowseRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Object.
body = ObjectBrowseRequest() # ObjectBrowseRequest | Specifies the parameters to fetch contents of an object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Fetch the contents (files & folders) for the specified object.
	api_response = client.object.browse_object_contents(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->browse_object_contents: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Fetch the contents (files & folders) for the specified object.
	api_response = client.object.browse_object_contents(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->browse_object_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **body** | [**ObjectBrowseRequest**](ObjectBrowseRequest.md)| Specifies the parameters to fetch contents of an object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**FileFolderInfo**](FileFolderInfo.md)

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

# **cancel_object_runs**
> CancelObjectRunsResults cancel_object_runs(body)

Cancel object runs.

Cancel object runs for object based protection. This does not apply to Group based protection.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.cancel_object_runs_results import CancelObjectRunsResults
from cohesity_sdk.helios.model.cancel_object_runs_request import CancelObjectRunsRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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
                snapshot_backend_types=[
                    "kAWSNative",
                ],
            ),
        ],
    ) # CancelObjectRunsRequest | Specifies the parameters to cancel object runs.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Cancel object runs.
	api_response = client.object.cancel_object_runs(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->cancel_object_runs: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Cancel object runs.
	api_response = client.object.cancel_object_runs(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->cancel_object_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelObjectRunsRequest**](CancelObjectRunsRequest.md)| Specifies the parameters to cancel object runs. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.construct_meta_info_result import ConstructMetaInfoResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.construct_meta_info_params import ConstructMetaInfoParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


snapshot_id = "snapshotId_example" # str | Specifies the snapshot id.
body = ConstructMetaInfoParams(
        environment="environment_example",
        oracle_params={},
        sfdc_params={},
    ) # ConstructMetaInfoParams | Specifies the parameters to construct meta info for desired workflow.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Construct meta info for any workflow from object snapshot and some other information.
	api_response = client.object.construct_meta_info(snapshot_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->construct_meta_info: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Construct meta info for any workflow from object snapshot and some other information.
	api_response = client.object.construct_meta_info(snapshot_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->construct_meta_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. |
 **body** | [**ConstructMetaInfoParams**](ConstructMetaInfoParams.md)| Specifies the parameters to construct meta info for desired workflow. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

# **filter_objects**
> FilteredObjectsResponseBody filter_objects(body)

List all the filtered objects.

List all the filtered objects using given regular expressions and wildcard supported search strings. We are currenly supporting this for only SQL adapter.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.filter_objects_request import FilterObjectsRequest
from cohesity_sdk.helios.model.filtered_objects_response_body import FilteredObjectsResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = FilterObjectsRequest(
        filter_type="exclude",
        filters=[
            Filter(
                filter_string="filter_string_example",
                is_regular_expression=False,
            ),
        ],
        object_ids=[
            1,
        ],
        application_environment="kSQL",
        tenant_ids=[
            "tenant_ids_example",
        ],
        include_tenants=False,
    ) # FilterObjectsRequest | Specifies the parameters to filter objects.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# List all the filtered objects.
	api_response = client.object.filter_objects(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->filter_objects: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List all the filtered objects.
	api_response = client.object.filter_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->filter_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilterObjectsRequest**](FilterObjectsRequest.md)| Specifies the parameters to filter objects. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**FilteredObjectsResponseBody**](FilteredObjectsResponseBody.md)

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_indexed_object_snapshots_response_body import GetIndexedObjectSnapshotsResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


object_id = 1 # int | Specifies the object id.
indexed_object_name = "indexedObjectName_example" # str | Specifies the indexed object name.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.object.get_all_indexed_object_snapshots(object_id, indexed_object_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_all_indexed_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get snapshots of indexed object.
	api_response = client.object.get_all_indexed_object_snapshots(object_id, indexed_object_name, access_cluster_id=access_cluster_id, region_id=region_id, protection_group_id=protection_group_id, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_all_indexed_object_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **int**| Specifies the object id. |
 **indexed_object_name** | **str**| Specifies the indexed object name. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_deleted_protected_objects**
> DeletedProtectedObjectsResponseBody get_deleted_protected_objects(source_id)

List deleted protected objects.

List of objects which are deleted but protected by object protection.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.deleted_protected_objects_response_body import DeletedProtectedObjectsResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


source_id = 1 # int | Specifies the source ID for which objects should be returned.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. (optional)
max_count = 1 # int | Specifies the max number of objects to return. (optional)
cookie = "cookie_example" # str | Specifies the pagination cookie. (optional)

# example passing only required values which don't have defaults set
try:
	# List deleted protected objects.
	api_response = client.object.get_deleted_protected_objects(source_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_deleted_protected_objects: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List deleted protected objects.
	api_response = client.object.get_deleted_protected_objects(source_id, access_cluster_id=access_cluster_id, region_id=region_id, tenant_ids=tenant_ids, include_tenants=include_tenants, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_deleted_protected_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| Specifies the source ID for which objects should be returned. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. | [optional]
 **max_count** | **int**| Specifies the max number of objects to return. | [optional]
 **cookie** | **str**| Specifies the pagination cookie. | [optional]

### Return type

[**DeletedProtectedObjectsResponseBody**](DeletedProtectedObjectsResponseBody.md)

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_indexed_object_snapshots_response_body import GetIndexedObjectSnapshotsResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


protection_group_id = "protectionGroupId_example" # str | Specifies the protection group id.
object_id = 1 # int | Specifies the object id.
indexed_object_name = "indexedObjectName_example" # str | Specifies the indexed object name.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
include_indexed_snapshots_only = False # bool | Specifies whether to only return snapshots which are indexed. In an indexed snapshots file are guaranteened to exist, while in a non-indexed snapshots file may not exist. (optional) if omitted the server will use the default value of False
from_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken after this value. (optional)
to_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken before this value. (optional)
run_types = [
        "kRegular",
    ] # [str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)

# example passing only required values which don't have defaults set
try:
	# Get snapshots of indexed object.
	api_response = client.object.get_indexed_object_snapshots(protection_group_id, object_id, indexed_object_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_indexed_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get snapshots of indexed object.
	api_response = client.object.get_indexed_object_snapshots(protection_group_id, object_id, indexed_object_name, access_cluster_id=access_cluster_id, region_id=region_id, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_indexed_object_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protection_group_id** | **str**| Specifies the protection group id. |
 **object_id** | **int**| Specifies the object id. |
 **indexed_object_name** | **str**| Specifies the indexed object name. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_mcm_object_snapshots**
> GetObjectSnapshotsResponseBody get_mcm_object_snapshots(global_id)

List the snapshots for a given object.

List the snapshots for a given object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_object_snapshots_response_body import GetObjectSnapshotsResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


global_id = "globalId_example" # str | Specifies the global id of the Object.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
uuid = "uuid_example" # str | Specifies the uuid of the Object. This field is deprecated. (optional)
from_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which are taken after this value. (optional)
to_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which are taken before this value. (optional)

# example passing only required values which don't have defaults set
try:
	# List the snapshots for a given object.
	api_response = client.object.get_mcm_object_snapshots(global_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the snapshots for a given object.
	api_response = client.object.get_mcm_object_snapshots(global_id, region_id=region_id, uuid=uuid, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_object_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_id** | **str**| Specifies the global id of the Object. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **uuid** | **str**| Specifies the uuid of the Object. This field is deprecated. | [optional]
 **from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which are taken after this value. | [optional]
 **to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which are taken before this value. | [optional]

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

# **get_mcm_object_stats**
> ObjectStats get_mcm_object_stats(global_id)

Get stats for a given object.

Get stats for a given object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.object_stats import ObjectStats
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


global_id = "globalId_example" # str | Specifies the global id of the Object. This field is required because we only fetches snapshots stats for one object.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
entity_hash = "entityHash_example" # str | Specifies the entity hash global id of the Object. This field is deprecated. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Specifies a list of region ids. Only records from clusters having these region ids will be returned. (optional)
cluster_identifiers = [
        "clusterIdentifiers_example",
    ] # [str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# Get stats for a given object.
	api_response = client.object.get_mcm_object_stats(global_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_object_stats: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get stats for a given object.
	api_response = client.object.get_mcm_object_stats(global_id, region_id=region_id, entity_hash=entity_hash, region_ids=region_ids, cluster_identifiers=cluster_identifiers)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_object_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_id** | **str**| Specifies the global id of the Object. This field is required because we only fetches snapshots stats for one object. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **entity_hash** | **str**| Specifies the entity hash global id of the Object. This field is deprecated. | [optional]
 **region_ids** | **[str]**| Specifies a list of region ids. Only records from clusters having these region ids will be returned. | [optional]
 **cluster_identifiers** | **[str]**| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. | [optional]

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

# **get_mcm_object_summary**
> McmObjectSummaryResult get_mcm_object_summary()

Get the summary for a given object.

Get the objects summary across clusters.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_object_summary_result import McmObjectSummaryResult
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
cluster_identifiers = [
        "clusterIdentifiers_example",
    ] # [str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. (optional)
environments = [
        "kVMware",
    ] # [str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protected objects protecting the specified environment types are returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the summary for a given object.
	api_response = client.object.get_mcm_object_summary(region_id=region_id, cluster_identifiers=cluster_identifiers, environments=environments)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_object_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **cluster_identifiers** | **[str]**| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. | [optional]
 **environments** | **[str]**| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protected objects protecting the specified environment types are returned. | [optional]

### Return type

[**McmObjectSummaryResult**](McmObjectSummaryResult.md)

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

# **get_mcm_objects_activity**
> McmObjectsActivity get_mcm_objects_activity()

Get Object activity on Helios.

Get object activity on Helios. Activity includes Protection Group Runs and Recoveries.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.get_mcm_objects_activity_req_params import GetMcmObjectsActivityReqParams
from cohesity_sdk.helios.model.mcm_objects_activity import McmObjectsActivity
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)
body = GetMcmObjectsActivityReqParams(
        object_identifiers=[
            McmObjectIdentifier(
                cluster_id=1,
                cluster_incarnation_id=1,
                region_id="region_id_example",
                object_id=1,
            ),
        ],
        environments=[
            "kVMware",
        ],
        statuses=[
            "Accepted",
        ],
        message_codes=[
            "message_codes_example",
        ],
        from_time_usecs=1,
        to_time_usecs=1,
        activity_types=[
            "BackupRun",
        ],
        backup_run_params={},
        archival_run_params=ArchivalRunFilterParams(
            run_types=[
                "kRegular",
            ],
            protection_environment_types=[
                "kVMware",
            ],
            is_rpaas=True,
        ),
        restore_params={},
        is_sla_violated=True,
        exclude_data=True,
        exclude_stats=True,
        stats_params=ActivityStatsParams(
            attributes=[
                "Status",
            ],
        ),
    ) # GetMcmObjectsActivityReqParams | Request parameters to filter object activity. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Object activity on Helios.
	api_response = client.object.get_mcm_objects_activity(region_id=region_id, region_ids=region_ids, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_objects_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]
 **body** | [**GetMcmObjectsActivityReqParams**](GetMcmObjectsActivityReqParams.md)| Request parameters to filter object activity. | [optional]

### Return type

[**McmObjectsActivity**](McmObjectsActivity.md)

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

# **get_mcm_objects_activity_by_id**
> McmObjectActivity get_mcm_objects_activity_by_id(id)

Get Object activity on Helios.

Get object activity on Helios by ID. Activity includes Protection Group Runs and Recoveries.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_object_activity import McmObjectActivity
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the Activity.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get Object activity on Helios.
	api_response = client.object.get_mcm_objects_activity_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_objects_activity_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Object activity on Helios.
	api_response = client.object.get_mcm_objects_activity_by_id(id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_objects_activity_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Activity. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmObjectActivity**](McmObjectActivity.md)

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

# **get_mcm_objects_last_run_activity**
> McmObjectLastRunActivities get_mcm_objects_last_run_activity()

Get last protection run of objects.

Get last protection run activity of objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_object_last_run_activities import McmObjectLastRunActivities
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_mcm_objects_last_run_req_params import GetMcmObjectsLastRunReqParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Specifies a list of region ids. Only records from clusters having these region ids will be returned. (optional)
cluster_identifiers = [
        "clusterIdentifiers_example",
    ] # [str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. (optional)
body = GetMcmObjectsLastRunReqParams(
        object_identifiers=[
            McmObjectIdentifier(
                cluster_id=1,
                cluster_incarnation_id=1,
                region_id="region_id_example",
                object_id=1,
            ),
        ],
        environments=[
            "kVMware",
        ],
        statuses=[
            "Accepted",
        ],
        is_sla_violated=True,
        source_identifier=McmObjectIdentifier(
            cluster_id=1,
            cluster_incarnation_id=1,
            region_id="region_id_example",
            object_id=1,
        ),
        activity_types=[
            "BackupRun",
        ],
        backup_run_params={},
        archival_run_params=ArchivalRunFilterParams(
            run_types=[
                "kRegular",
            ],
            protection_environment_types=[
                "kVMware",
            ],
            is_rpaas=True,
        ),
        include_details=True,
        is_protected=True,
        exclude_data=True,
        exclude_stats=True,
        stats_params=ActivityStatsParams(
            attributes=[
                "Status",
            ],
        ),
    ) # GetMcmObjectsLastRunReqParams | Request parameters to filter object last runs. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get last protection run of objects.
	api_response = client.object.get_mcm_objects_last_run_activity(region_id=region_id, region_ids=region_ids, cluster_identifiers=cluster_identifiers, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_mcm_objects_last_run_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Specifies a list of region ids. Only records from clusters having these region ids will be returned. | [optional]
 **cluster_identifiers** | **[str]**| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. | [optional]
 **body** | [**GetMcmObjectsLastRunReqParams**](GetMcmObjectsLastRunReqParams.md)| Request parameters to filter object last runs. | [optional]

### Return type

[**McmObjectLastRunActivities**](McmObjectLastRunActivities.md)

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

# **get_object_archival_run_stats**
> ObjectArchivalRunStats get_object_archival_run_stats()

Get the object archival run stats.

Get the stats for objects in archival runs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.object_archival_run_stats import ObjectArchivalRunStats
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
from_time_usecs = 1 # int, none_type | Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started after this value. The default value is 7 days ago from now. (optional)
to_time_usecs = 1 # int, none_type | Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started before this value. The default value is the current time. (optional)
rpaas_only = True # bool, none_type | Specifies whether the archival runs are only for RPaaS. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the object archival run stats.
	api_response = client.object.get_object_archival_run_stats(region_id=region_id, region_ids=region_ids, rpaas_region_ids=rpaas_region_ids, cluster_identifiers=cluster_identifiers, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, rpaas_only=rpaas_only)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_archival_run_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]
 **rpaas_region_ids** | **[str]**| Filter by a list of region ids. This is used for Rpaas only. | [optional]
 **cluster_identifiers** | **[str]**| Filter by a list of cluster identifiers in format of clusterId:clusterIncarnationId. | [optional]
 **from_time_usecs** | **int, none_type**| Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started after this value. The default value is 7 days ago from now. | [optional]
 **to_time_usecs** | **int, none_type**| Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started before this value. The default value is the current time. | [optional]
 **rpaas_only** | **bool, none_type**| Specifies whether the archival runs are only for RPaaS. | [optional]

### Return type

[**ObjectArchivalRunStats**](ObjectArchivalRunStats.md)

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

# **get_object_identifiers**
> LocalGlobalObjectIdList get_object_identifiers()

Get Object Identifiers

Get Object Identifiers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.local_global_object_id_list import LocalGlobalObjectIdList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
global_ids = [
        "globalIds_example",
    ] # [str] | Get the object identifier matching specified global IDs. (optional)
local_ids = [
        1,
    ] # [int] | Get the object identifier matching specified local IDs. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Object Identifiers
	api_response = client.object.get_object_identifiers(access_cluster_id=access_cluster_id, region_id=region_id, global_ids=global_ids, local_ids=local_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_identifiers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **global_ids** | **[str]**| Get the object identifier matching specified global IDs. | [optional]
 **local_ids** | **[int]**| Get the object identifier matching specified local IDs. | [optional]

### Return type

[**LocalGlobalObjectIdList**](LocalGlobalObjectIdList.md)

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.object_protection_run_summary import ObjectProtectionRunSummary
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the object.
run_id = "runId_example" # str | Specifies the id of the run.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a run for an object.
	api_response = client.object.get_object_run_by_run_id(id, run_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_run_by_run_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a run for an object.
	api_response = client.object.get_object_run_by_run_id(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_run_by_run_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the object. |
 **run_id** | **str**| Specifies the id of the run. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.get_object_runs_response_body import GetObjectRunsResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.object.get_object_runs(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_runs: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of runs for an object.
	api_response = client.object.get_object_runs(id, access_cluster_id=access_cluster_id, region_id=region_id, run_id=run_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, run_types=run_types, local_backup_object_status=local_backup_object_status, replication_object_status=replication_object_status, archival_object_status=archival_object_status, cloud_spin_run_status=cloud_spin_run_status, num_runs=num_runs, pagination_cookie=pagination_cookie, exclude_non_restorable_runs=exclude_non_restorable_runs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_object_snapshot_id**
> ObjectSnapshotIdResult get_object_snapshot_id(object_id, body)

Get snapshot id for a given object.

Get snapshot id for object for given params.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.object_snapshot_id_result import ObjectSnapshotIdResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.object_snapshot_id_params import ObjectSnapshotIdParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


object_id = 1 # int | Specifies the object id.
body = ObjectSnapshotIdParams(
        protection_group_id="protection_group_id_example",
        snapshot_job_instance_id=1,
        run_start_time_usecs=1,
        source_group_id="source_group_id_example",
        vault_id=1,
    ) # ObjectSnapshotIdParams | Specifies the parameters to fetch snapshot id for object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get snapshot id for a given object.
	api_response = client.object.get_object_snapshot_id(object_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshot_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get snapshot id for a given object.
	api_response = client.object.get_object_snapshot_id(object_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshot_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **int**| Specifies the object id. |
 **body** | [**ObjectSnapshotIdParams**](ObjectSnapshotIdParams.md)| Specifies the parameters to fetch snapshot id for object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ObjectSnapshotIdResult**](ObjectSnapshotIdResult.md)

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

# **get_object_snapshot_info**
> ObjectSnapshot get_object_snapshot_info(snapshot_id)

Get details of object snapshot.

Get details of object snapshot.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.object_snapshot import ObjectSnapshot
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


snapshot_id = "snapshotId_example" # str | Specifies the snapshot id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get details of object snapshot.
	api_response = client.object.get_object_snapshot_info(snapshot_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshot_info: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get details of object snapshot.
	api_response = client.object.get_object_snapshot_info(snapshot_id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshot_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.object_snapshot_volume_info import ObjectSnapshotVolumeInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


snapshot_id = "snapshotId_example" # str | Specifies the snapshot id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
include_supported_only = True # bool | Specifies whether to only return supported volumes. (optional)
point_in_time_usecs = 3.14 # float | Specifies the point-in-time timestamp (in usecs from epoch) between snapshots for which the volume info is to be returned. (optional)

# example passing only required values which don't have defaults set
try:
	# Get volume info of object snapshot.
	api_response = client.object.get_object_snapshot_volume_info(snapshot_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshot_volume_info: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get volume info of object snapshot.
	api_response = client.object.get_object_snapshot_volume_info(snapshot_id, access_cluster_id=access_cluster_id, region_id=region_id, include_supported_only=include_supported_only, point_in_time_usecs=point_in_time_usecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshot_volume_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_object_snapshots_response_body import GetObjectSnapshotsResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
from_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were taken after this value. (optional)
to_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were taken before this value. (optional)
run_start_from_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were run after this value. (optional)
run_start_to_time_usecs = 1 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were run before this value. (optional)
snapshot_actions = [
        "RecoverVMs",
    ] # [str] | Specifies a list of recovery actions. Only snapshots that applies to these actions will be returned. (optional)
run_types = [
        "kRegular",
    ] # [str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)
protection_group_ids = [
        "protectionGroupIds_example",
    ] # [str] | If specified, this returns only the snapshots of the specified object ID, which belong to the provided protection group IDs. (optional)
run_instance_ids = [
        1,
    ] # [int] | Filter by a list run instance ids. If specified, only snapshots created by these protection runs will be returned. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)
object_action_keys = [
        "kVMware",
    ] # [str] | Filter by ObjectActionKey, which uniquely represents protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey. When specified, only snapshots matching given action keys are returned for corresponding object. (optional)

# example passing only required values which don't have defaults set
try:
	# List the snapshots for a given object.
	api_response = client.object.get_object_snapshots(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the snapshots for a given object.
	api_response = client.object.get_object_snapshots(id, access_cluster_id=access_cluster_id, region_id=region_id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_start_from_time_usecs=run_start_from_time_usecs, run_start_to_time_usecs=run_start_to_time_usecs, snapshot_actions=snapshot_actions, run_types=run_types, protection_group_ids=protection_group_ids, run_instance_ids=run_instance_ids, region_ids=region_ids, object_action_keys=object_action_keys)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_snapshots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which were taken after this value. | [optional]
 **to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which were taken before this value. | [optional]
 **run_start_from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which were run after this value. | [optional]
 **run_start_to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter Object&#39;s snapshots which were run before this value. | [optional]
 **snapshot_actions** | **[str]**| Specifies a list of recovery actions. Only snapshots that applies to these actions will be returned. | [optional]
 **run_types** | **[str]**| Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. | [optional]
 **protection_group_ids** | **[str]**| If specified, this returns only the snapshots of the specified object ID, which belong to the provided protection group IDs. | [optional]
 **run_instance_ids** | **[int]**| Filter by a list run instance ids. If specified, only snapshots created by these protection runs will be returned. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]
 **object_action_keys** | **[str]**| Filter by ObjectActionKey, which uniquely represents protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey. When specified, only snapshots matching given action keys are returned for corresponding object. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.object_stats import ObjectStats
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)

# example passing only required values which don't have defaults set
try:
	# Get stats for a given object.
	api_response = client.object.get_object_stats(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_stats: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get stats for a given object.
	api_response = client.object.get_object_stats(id, access_cluster_id=access_cluster_id, region_id=region_id, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.object_with_children import ObjectWithChildren
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the objects tree hierarchy for for an Object.
	api_response = client.object.get_object_tree(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_tree: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the objects tree hierarchy for for an Object.
	api_response = client.object.get_object_tree(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_object_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.objects_last_run import ObjectsLastRun
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.object.get_objects_last_run(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, pagination_cookie=pagination_cookie, count=count)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_objects_last_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

Returns the ranges in various types like time, SCN etc. within which the specified protected object can be restored to any Point in time.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_pit_ranges_protected_object_response_body import GetPITRangesProtectedObjectResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the ID of the protected object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
from_time_usecs = 1 # int | If specified, return the restore ranges that lie after this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. (optional)
to_time_usecs = 1 # int | If specified, return the restore ranges that lie before this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. (optional)
protection_group_ids = [
        "protectionGroupIds_example",
    ] # [str] | If specified, return only the points in time corresponding to these protection group IDs. (optional)

# example passing only required values which don't have defaults set
try:
	# Get PIT ranges for an object
	api_response = client.object.get_pit_ranges_for_protected_object(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_pit_ranges_for_protected_object: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get PIT ranges for an object
	api_response = client.object.get_pit_ranges_for_protected_object(id, access_cluster_id=access_cluster_id, region_id=region_id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, protection_group_ids=protection_group_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_pit_ranges_for_protected_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the protected object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **from_time_usecs** | **int**| If specified, return the restore ranges that lie after this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. | [optional]
 **to_time_usecs** | **int**| If specified, return the restore ranges that lie before this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.protected_object_info import ProtectedObjectInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
object_action_key = [
        "kVMware",
    ] # [str] | Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id and this vec's size needs to be same as 'id'. (optional)
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
	api_response = client.object.get_protected_object_of_any_type_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_protected_object_of_any_type_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get an Object.
	api_response = client.object.get_protected_object_of_any_type_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, object_action_key=object_action_key, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_protected_object_of_any_type_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **object_action_key** | **[str]**| Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id and this vec&#39;s size needs to be same as &#39;id&#39;. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.get_protected_objects_response import GetProtectedObjectsResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
ids = [
        1,
    ] # [int] | Filter by a list of Object ids. (optional)
object_action_keys = [
        "kVMware",
    ] # [str] | Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id. The vec's size needs to be of either length one or same as the length of 'ids'. If the length of objectActionKey is one, it will be repeated as many number of times equal to the length of objectIds, as mandated by backend validation. If the length of objectActionKey and object ids are same then it will be passed as it is. (optional)
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
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)
max_count = 1 # int | Specifies the max number of objects to return. (optional)
cookie = "cookie_example" # str | Specifies the pagination cookie. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Objects.
	api_response = client.object.get_protected_objects_of_any_type(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, ids=ids, object_action_keys=object_action_keys, policy_ids=policy_ids, parent_id=parent_id, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects, region_ids=region_ids, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_protected_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **ids** | **[int]**| Filter by a list of Object ids. | [optional]
 **object_action_keys** | **[str]**| Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id. The vec&#39;s size needs to be of either length one or same as the length of &#39;ids&#39;. If the length of objectActionKey is one, it will be repeated as many number of times equal to the length of objectIds, as mandated by backend validation. If the length of objectActionKey and object ids are same then it will be passed as it is. | [optional]
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
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]
 **max_count** | **int**| Specifies the max number of objects to return. | [optional]
 **cookie** | **str**| Specifies the pagination cookie. | [optional]

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

# **get_snapshot_diff**
> SnapshotDiffResult get_snapshot_diff(id, body)

Get diff between two snapshots of a given object.

Get diff (files added/deleted) between two snapshots of a given object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.snapshot_diff_params import SnapshotDiffParams
from cohesity_sdk.helios.model.snapshot_diff_result import SnapshotDiffResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | 
body = SnapshotDiffParams(
        cluster_id=1,
        incarnation_id=1,
        partition_id=1,
        job_id=1,
        entity_type="kVMware",
        base_snapshot_job_instance_id=1,
        base_snapshot_time_usecs=1,
        snapshot_job_instance_id=1,
        snapshot_time_usecs=1,
        page_number=1,
        page_size=1,
    ) # SnapshotDiffParams | 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get diff between two snapshots of a given object.
	api_response = client.object.get_snapshot_diff(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_snapshot_diff: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get diff between two snapshots of a given object.
	api_response = client.object.get_snapshot_diff(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_snapshot_diff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **body** | [**SnapshotDiffParams**](SnapshotDiffParams.md)|  |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SnapshotDiffResult**](SnapshotDiffResult.md)

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

# **get_source_hierarchy_objects**
> SourceHierarchyObjectSummaries get_source_hierarchy_objects(source_id)

List objects on a source which can be used for data protection.

List objects which can be used for data protection.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.source_hierarchy_object_summaries import SourceHierarchyObjectSummaries
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


source_id = 1 # int | Specifies the source ID for which objects should be returned.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.object.get_source_hierarchy_objects(source_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_source_hierarchy_objects: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List objects on a source which can be used for data protection.
	api_response = client.object.get_source_hierarchy_objects(source_id, access_cluster_id=access_cluster_id, region_id=region_id, parent_id=parent_id, tenant_ids=tenant_ids, include_tenants=include_tenants, vmware_object_types=vmware_object_types, netapp_object_types=netapp_object_types, o365_object_types=o365_object_types, cassandra_object_types=cassandra_object_types, mongodb_object_types=mongodb_object_types, couchbase_object_types=couchbase_object_types, hdfs_object_types=hdfs_object_types, hbase_object_types=hbase_object_types, hive_object_types=hive_object_types, hyperv_object_types=hyperv_object_types, azure_object_types=azure_object_types, kvm_object_types=kvm_object_types, aws_object_types=aws_object_types, gcp_object_types=gcp_object_types, acropolis_object_types=acropolis_object_types, generic_nas_object_types=generic_nas_object_types, isilon_object_types=isilon_object_types, flashblade_object_types=flashblade_object_types, elastifile_object_types=elastifile_object_types, gpfs_object_types=gpfs_object_types, pure_object_types=pure_object_types, nimble_object_types=nimble_object_types, physical_object_types=physical_object_types, kubernetes_object_types=kubernetes_object_types, exchange_object_types=exchange_object_types, ad_object_types=ad_object_types, mssql_object_types=mssql_object_types, oracle_object_types=oracle_object_types)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->get_source_hierarchy_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| Specifies the source ID for which objects should be returned. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **internal_api_construct_meta_info**
> ConstructMetaInfoResult internal_api_construct_meta_info(snapshot_id, body)

Construct meta info for any workflow from object snapshot and some other information.

Construct meta info from object snapshot and some additional params.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.construct_meta_info_result import ConstructMetaInfoResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.construct_meta_info_params import ConstructMetaInfoParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


snapshot_id = "snapshotId_example" # str | Specifies the snapshot id.
body = ConstructMetaInfoParams(
        environment="environment_example",
        oracle_params={},
        sfdc_params={},
    ) # ConstructMetaInfoParams | Specifies the parameters to construct meta info for desired workflow.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Construct meta info for any workflow from object snapshot and some other information.
	api_response = client.object.internal_api_construct_meta_info(snapshot_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->internal_api_construct_meta_info: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Construct meta info for any workflow from object snapshot and some other information.
	api_response = client.object.internal_api_construct_meta_info(snapshot_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->internal_api_construct_meta_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. |
 **body** | [**ConstructMetaInfoParams**](ConstructMetaInfoParams.md)| Specifies the parameters to construct meta info for desired workflow. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

# **internal_api_get_snapshot_diff**
> SnapshotDiffResult internal_api_get_snapshot_diff(id, body)

Get diff between two snapshots of a given object.

Get diff (files added/deleted) between two snapshots of a given object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.snapshot_diff_params import SnapshotDiffParams
from cohesity_sdk.helios.model.snapshot_diff_result import SnapshotDiffResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | 
body = SnapshotDiffParams(
        cluster_id=1,
        incarnation_id=1,
        partition_id=1,
        job_id=1,
        entity_type="kVMware",
        base_snapshot_job_instance_id=1,
        base_snapshot_time_usecs=1,
        snapshot_job_instance_id=1,
        snapshot_time_usecs=1,
        page_number=1,
        page_size=1,
    ) # SnapshotDiffParams | 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get diff between two snapshots of a given object.
	api_response = client.object.internal_api_get_snapshot_diff(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->internal_api_get_snapshot_diff: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get diff between two snapshots of a given object.
	api_response = client.object.internal_api_get_snapshot_diff(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->internal_api_get_snapshot_diff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **body** | [**SnapshotDiffParams**](SnapshotDiffParams.md)|  |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SnapshotDiffResult**](SnapshotDiffResult.md)

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

# **mcm_get_tenant_object_ids**
> McmTenantObjectIds mcm_get_tenant_object_ids(body)

GetTenantObjectIds

Get the object IDs for a given DMaaS tenant given a list of object hashes.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_tenant_object_ids import McmTenantObjectIds
from cohesity_sdk.helios.model.mcm_tenant_object_ids_params import McmTenantObjectIdsParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = McmTenantObjectIdsParams(
        tenant_id="tenant_id_example",
        object_hashes=[
            "object_hashes_example",
        ],
    ) # McmTenantObjectIdsParams | Specifies the parameters to fetch object IDs.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# GetTenantObjectIds
	api_response = client.object.mcm_get_tenant_object_ids(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->mcm_get_tenant_object_ids: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# GetTenantObjectIds
	api_response = client.object.mcm_get_tenant_object_ids(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->mcm_get_tenant_object_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**McmTenantObjectIdsParams**](McmTenantObjectIdsParams.md)| Specifies the parameters to fetch object IDs. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmTenantObjectIds**](McmTenantObjectIds.md)

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

# **mcm_get_tenant_object_protections**
> McmTenantObjectProtections mcm_get_tenant_object_protections(body)

GetTenantObjectProtections

Get the protected objects for a given DMaaS tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_tenant_protected_objects_params import McmTenantProtectedObjectsParams
from cohesity_sdk.helios.model.mcm_tenant_object_protections import McmTenantObjectProtections
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = McmTenantProtectedObjectsParams(
        tenant_id="tenant_id_example",
        start_index=1,
        num_results=1,
    ) # McmTenantProtectedObjectsParams | Specifies the parameters to fetch protected objects.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# GetTenantObjectProtections
	api_response = client.object.mcm_get_tenant_object_protections(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->mcm_get_tenant_object_protections: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# GetTenantObjectProtections
	api_response = client.object.mcm_get_tenant_object_protections(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->mcm_get_tenant_object_protections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**McmTenantProtectedObjectsParams**](McmTenantProtectedObjectsParams.md)| Specifies the parameters to fetch protected objects. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmTenantObjectProtections**](McmTenantObjectProtections.md)

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

# **objects_actions**
> objects_actions(body)

Actions on Objects

Specifies the request to perform various actions on multiple objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.objects_action_request import ObjectsActionRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ObjectsActionRequest(
        action="Link",
        link_params=ObjectLinkingParams(),
        un_link_params=ObjectUnLinkingParams(),
    ) # ObjectsActionRequest | Specifies the paramteres to execute actions on given list of objects.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Actions on Objects
	client.object.objects_actions(body)
except ApiException as e:
	print("Exception when calling ObjectApi->objects_actions: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Actions on Objects
	client.object.objects_actions(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ObjectApi->objects_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectsActionRequest**](ObjectsActionRequest.md)| Specifies the paramteres to execute actions on given list of objects. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.object_action_request import ObjectActionRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Object.
body = ObjectActionRequest() # ObjectActionRequest | Specifies the parameters to perform an action on an object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform an action on an object.
	client.object.perform_action_on_object(id, body)
except ApiException as e:
	print("Exception when calling ObjectApi->perform_action_on_object: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform an action on an object.
	client.object.perform_action_on_object(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ObjectApi->perform_action_on_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **body** | [**ObjectActionRequest**](ObjectActionRequest.md)| Specifies the parameters to perform an action on an object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.update_object_snapshot_request import UpdateObjectSnapshotRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.object_snapshot import ObjectSnapshot
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Object.
snapshot_id = "snapshotId_example" # str | Specifies the id of the snapshot.<br> Note: 1. If the snapshotid of one of the apps is specified, it applies for all the databases in the Protection Run.<br> 2. In case of volume based jobs, please specify the snapshotid of the source not the database. if source snapshot is specified, applied to source snapshot. if database snapshotid is specified in case of volume based jobs, then it is applicable for host's snapshot.
body = UpdateObjectSnapshotRequest(
        set_legal_hold=True,
        data_lock_type="Compliance",
        expiry_time_secs=1,
    ) # UpdateObjectSnapshotRequest | Specifies the parameters update an object snapshot.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update an object snapshot.
	api_response = client.object.update_object_snapshot(id, snapshot_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->update_object_snapshot: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update an object snapshot.
	api_response = client.object.update_object_snapshot(id, snapshot_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ObjectApi->update_object_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. |
 **snapshot_id** | **str**| Specifies the id of the snapshot.&lt;br&gt; Note: 1. If the snapshotid of one of the apps is specified, it applies for all the databases in the Protection Run.&lt;br&gt; 2. In case of volume based jobs, please specify the snapshotid of the source not the database. if source snapshot is specified, applied to source snapshot. if database snapshotid is specified in case of volume based jobs, then it is applicable for host&#39;s snapshot. |
 **body** | [**UpdateObjectSnapshotRequest**](UpdateObjectSnapshotRequest.md)| Specifies the parameters update an object snapshot. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

