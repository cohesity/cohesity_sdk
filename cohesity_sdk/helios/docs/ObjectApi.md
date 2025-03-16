# cohesity_sdk.helios.ObjectApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_entity_metadata**](ObjectApi.md#associate_entity_metadata) | **PUT** /data-protect/objects/metadata | Associate Metadata with Entity
[**browse_object_contents**](ObjectApi.md#browse_object_contents) | **POST** /data-protect/objects/{id}/browse | Fetch the contents (files &amp; folders) for the specified object.
[**cancel_object_runs**](ObjectApi.md#cancel_object_runs) | **POST** /data-protect/objects/runs/cancel | Cancel object runs.
[**construct_meta_info**](ObjectApi.md#construct_meta_info) | **POST** /data-protect/snapshots/{snapshotId}/meta-info | Construct meta info for any workflow from object snapshot and some other information.
[**filter_objects**](ObjectApi.md#filter_objects) | **POST** /data-protect/filter/objects | List all the filtered objects.
[**get_all_indexed_object_snapshots**](ObjectApi.md#get_all_indexed_object_snapshots) | **GET** /data-protect/objects/{objectId}/indexed-objects/snapshots | Get snapshots of indexed object.
[**get_entity_metadata**](ObjectApi.md#get_entity_metadata) | **GET** /data-protect/objects/{sourceId}/metadata | Get Metadata of Entities
[**get_indexed_object_snapshots**](ObjectApi.md#get_indexed_object_snapshots) | **GET** /data-protect/objects/{objectId}/protection-groups/{protectionGroupId}/indexed-objects/snapshots | Get snapshots of indexed object.
[**get_mcm_object_snapshots**](ObjectApi.md#get_mcm_object_snapshots) | **GET** /mcm/data-protect/objects/snapshots | List the snapshots for a given object.
[**get_mcm_object_stats**](ObjectApi.md#get_mcm_object_stats) | **GET** /mcm/data-protect/objects/stats | Get stats for a given object.
[**get_mcm_object_summary**](ObjectApi.md#get_mcm_object_summary) | **GET** /mcm/objects/summary | Get the summary for a given object.
[**get_mcm_objects_activity**](ObjectApi.md#get_mcm_objects_activity) | **POST** /mcm/data-protect/objects/activity | Get Object activity on Helios.
[**get_mcm_objects_activity_by_id**](ObjectApi.md#get_mcm_objects_activity_by_id) | **GET** /mcm/data-protect/objects/activity/{id} | Get Object activity on Helios.
[**get_mcm_objects_last_run_activity**](ObjectApi.md#get_mcm_objects_last_run_activity) | **POST** /mcm/data-protect/objects/last-run-activity | Get last protection run of objects.
[**get_object_archival_run_stats**](ObjectApi.md#get_object_archival_run_stats) | **GET** /mcm/data-protect/objects/stats/archival-runs | Get the object archival run stats.
[**get_object_run_by_run_id**](ObjectApi.md#get_object_run_by_run_id) | **GET** /data-protect/objects/{id}/runs/{runId} | Get a run for an object.
[**get_object_runs**](ObjectApi.md#get_object_runs) | **GET** /data-protect/objects/{id}/runs | Get the list of runs for an object.
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
[**mcm_get_tenant_object_ids**](ObjectApi.md#mcm_get_tenant_object_ids) | **POST** /mcm/tenants/object-ids | GetTenantObjectIds
[**objects_actions**](ObjectApi.md#objects_actions) | **POST** /data-protect/objects/actions | Actions on Objects
[**perform_action_on_object**](ObjectApi.md#perform_action_on_object) | **POST** /data-protect/objects/{id}/actions | Perform an action on an object.
[**update_object_snapshot**](ObjectApi.md#update_object_snapshot) | **PUT** /data-protect/objects/{id}/snapshots/{snapshotId} | Update an object snapshot.


# **associate_entity_metadata**
> AssociateEntityMetadataResult associate_entity_metadata(body, access_cluster_id=access_cluster_id, region_id=region_id)

Associate Metadata with Entity

Associates metadata with entities in the entity hierarchy. This metadata can be of various types (eg. Credentials). Returns a list of entity id and corresponding errors encountered (if any) while associating metadata with that entity. Note that a partial success response is possible where we succeed in associating metadata with some of the entities but fail for others. The API also expects the entities being updated belong to same source.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.associate_entity_metadata_request import AssociateEntityMetadataRequest
from cohesity_sdk.helios.models.associate_entity_metadata_result import AssociateEntityMetadataResult
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    body = cohesity_sdk.helios.AssociateEntityMetadataRequest() # AssociateEntityMetadataRequest | Specifies the parameters to associate metadata with entities in the entity hierarchy.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Associate Metadata with Entity
        api_response = api_instance.associate_entity_metadata(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->associate_entity_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->associate_entity_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssociateEntityMetadataRequest**](AssociateEntityMetadataRequest.md)| Specifies the parameters to associate metadata with entities in the entity hierarchy. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AssociateEntityMetadataResult**](AssociateEntityMetadataResult.md)

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

# **browse_object_contents**
> FileFolderInfo browse_object_contents(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Fetch the contents (files & folders) for the specified object.

Fetch the contents (files & folders) of the specified path inside the specified object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.file_folder_info import FileFolderInfo
from cohesity_sdk.helios.models.object_browse_request import ObjectBrowseRequest
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the id of the Object.
    body = cohesity_sdk.helios.ObjectBrowseRequest() # ObjectBrowseRequest | Specifies the parameters to fetch contents of an object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Fetch the contents (files & folders) for the specified object.
        api_response = api_instance.browse_object_contents(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->browse_object_contents:\n")
        pprint(api_response)
    except Exception as e:
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
> CancelObjectRunsResults cancel_object_runs(body, access_cluster_id=access_cluster_id, region_id=region_id)

Cancel object runs.

Cancel object runs for object based protection. This does not apply to Group based protection.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.cancel_object_runs_request import CancelObjectRunsRequest
from cohesity_sdk.helios.models.cancel_object_runs_results import CancelObjectRunsResults
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    body = cohesity_sdk.helios.CancelObjectRunsRequest() # CancelObjectRunsRequest | Specifies the parameters to cancel object runs.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Cancel object runs.
        api_response = api_instance.cancel_object_runs(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->cancel_object_runs:\n")
        pprint(api_response)
    except Exception as e:
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
> ConstructMetaInfoResult construct_meta_info(snapshot_id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Construct meta info for any workflow from object snapshot and some other information.

Construct meta info from object snapshot and some additional params.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.construct_meta_info_request import ConstructMetaInfoRequest
from cohesity_sdk.helios.models.construct_meta_info_result import ConstructMetaInfoResult
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | Specifies the snapshot id.
    body = cohesity_sdk.helios.ConstructMetaInfoRequest() # ConstructMetaInfoRequest | Specifies the parameters to construct meta info for desired workflow.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Construct meta info for any workflow from object snapshot and some other information.
        api_response = api_instance.construct_meta_info(snapshot_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->construct_meta_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->construct_meta_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Specifies the snapshot id. | 
 **body** | [**ConstructMetaInfoRequest**](ConstructMetaInfoRequest.md)| Specifies the parameters to construct meta info for desired workflow. | 
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
> FilteredObjectsResponseBody filter_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)

List all the filtered objects.

List all the filtered objects using given regular expressions and wildcard supported search strings. We are currenly supporting this for only SQL adapter.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.filter_objects_request import FilterObjectsRequest
from cohesity_sdk.helios.models.filtered_objects_response_body import FilteredObjectsResponseBody
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    body = cohesity_sdk.helios.FilterObjectsRequest() # FilterObjectsRequest | Specifies the parameters to filter objects.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # List all the filtered objects.
        api_response = api_instance.filter_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->filter_objects:\n")
        pprint(api_response)
    except Exception as e:
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
> GetIndexedObjectSnapshotsResponseBody get_all_indexed_object_snapshots(object_id, indexed_object_name, access_cluster_id=access_cluster_id, region_id=region_id, protection_group_id=protection_group_id, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types, use_cached_data=use_cached_data, object_action_key=object_action_key)

Get snapshots of indexed object.

Get snapshots of indexed object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_indexed_object_snapshots_response_body import GetIndexedObjectSnapshotsResponseBody
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    object_id = 56 # int | Specifies the object id.
    indexed_object_name = 'indexed_object_name_example' # str | Specifies the indexed object name.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    protection_group_id = 'protection_group_id_example' # str | Specifies the protection group id. (optional)
    include_indexed_snapshots_only = False # bool | Specifies whether to only return snapshots which are indexed. In an indexed snapshot files are guaranteed to exist, while in a non-indexed snapshot files may not exist. (optional) (default to False)
    from_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken after this value. (optional)
    to_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken before this value. (optional)
    run_types = ['run_types_example'] # List[str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)
    object_action_key = 'object_action_key_example' # str | Filter by ObjectActionKey, which uniquely represents backup type for a given version. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey and ObjectId. When specified, only versions of given ObjectActionKey are returned for corresponding object id. (optional)

    try:
        # Get snapshots of indexed object.
        api_response = api_instance.get_all_indexed_object_snapshots(object_id, indexed_object_name, access_cluster_id=access_cluster_id, region_id=region_id, protection_group_id=protection_group_id, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types, use_cached_data=use_cached_data, object_action_key=object_action_key)
        print("The response of ObjectApi->get_all_indexed_object_snapshots:\n")
        pprint(api_response)
    except Exception as e:
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
 **include_indexed_snapshots_only** | **bool**| Specifies whether to only return snapshots which are indexed. In an indexed snapshot files are guaranteed to exist, while in a non-indexed snapshot files may not exist. | [optional] [default to False]
 **from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken after this value. | [optional] 
 **to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken before this value. | [optional] 
 **run_types** | [**List[str]**](str.md)| Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
 **object_action_key** | **str**| Filter by ObjectActionKey, which uniquely represents backup type for a given version. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey and ObjectId. When specified, only versions of given ObjectActionKey are returned for corresponding object id. | [optional] 

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

# **get_entity_metadata**
> GetEntityMetadataResult get_entity_metadata(source_id, access_cluster_id=access_cluster_id, region_id=region_id, entity_ids=entity_ids)

Get Metadata of Entities

Gets entity metadata for entities. This can be used as a input for the PUT API. 

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_entity_metadata_result import GetEntityMetadataResult
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    source_id = 56 # int | Specifies the source ID for which objects should be returned.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    entity_ids = [56] # List[int] | EntityIds contains ids of the entities for which objects are to be returned. (optional)

    try:
        # Get Metadata of Entities
        api_response = api_instance.get_entity_metadata(source_id, access_cluster_id=access_cluster_id, region_id=region_id, entity_ids=entity_ids)
        print("The response of ObjectApi->get_entity_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_entity_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| Specifies the source ID for which objects should be returned. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **entity_ids** | [**List[int]**](int.md)| EntityIds contains ids of the entities for which objects are to be returned. | [optional] 

### Return type

[**GetEntityMetadataResult**](GetEntityMetadataResult.md)

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
> GetIndexedObjectSnapshotsResponseBody get_indexed_object_snapshots(protection_group_id, object_id, indexed_object_name, access_cluster_id=access_cluster_id, region_id=region_id, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types, use_cached_data=use_cached_data, object_action_key=object_action_key)

Get snapshots of indexed object.

Get snapshots of indexed object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_indexed_object_snapshots_response_body import GetIndexedObjectSnapshotsResponseBody
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    protection_group_id = 'protection_group_id_example' # str | Specifies the protection group id.
    object_id = 56 # int | Specifies the object id.
    indexed_object_name = 'indexed_object_name_example' # str | Specifies the indexed object name.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    include_indexed_snapshots_only = False # bool | Specifies whether to only return snapshots which are indexed. In an indexed snapshots file are guaranteed to exist, while in a non-indexed snapshots file may not exist. (optional) (default to False)
    from_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken after this value. (optional)
    to_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter indexed object's snapshots which are taken before this value. (optional)
    run_types = ['run_types_example'] # List[str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)
    object_action_key = 'object_action_key_example' # str | Filter by ObjectActionKey, which uniquely represents backup type for a given version. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey and ObjectId. When specified, only versions of given ObjectActionKey are returned for corresponding object id. (optional)

    try:
        # Get snapshots of indexed object.
        api_response = api_instance.get_indexed_object_snapshots(protection_group_id, object_id, indexed_object_name, access_cluster_id=access_cluster_id, region_id=region_id, include_indexed_snapshots_only=include_indexed_snapshots_only, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_types=run_types, use_cached_data=use_cached_data, object_action_key=object_action_key)
        print("The response of ObjectApi->get_indexed_object_snapshots:\n")
        pprint(api_response)
    except Exception as e:
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
 **include_indexed_snapshots_only** | **bool**| Specifies whether to only return snapshots which are indexed. In an indexed snapshots file are guaranteed to exist, while in a non-indexed snapshots file may not exist. | [optional] [default to False]
 **from_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken after this value. | [optional] 
 **to_time_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter indexed object&#39;s snapshots which are taken before this value. | [optional] 
 **run_types** | [**List[str]**](str.md)| Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
 **object_action_key** | **str**| Filter by ObjectActionKey, which uniquely represents backup type for a given version. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey and ObjectId. When specified, only versions of given ObjectActionKey are returned for corresponding object id. | [optional] 

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
> GetObjectSnapshotsResponseBody get_mcm_object_snapshots(global_id, region_id=region_id, uuid=uuid, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs)

List the snapshots for a given object.

List the snapshots for a given object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_object_snapshots_response_body import GetObjectSnapshotsResponseBody
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    global_id = 'global_id_example' # str | Specifies the global id of the Object.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    uuid = 'uuid_example' # str | Specifies the uuid of the Object. This field is deprecated. (optional)
    from_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which are taken after this value. (optional)
    to_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which are taken before this value. (optional)

    try:
        # List the snapshots for a given object.
        api_response = api_instance.get_mcm_object_snapshots(global_id, region_id=region_id, uuid=uuid, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs)
        print("The response of ObjectApi->get_mcm_object_snapshots:\n")
        pprint(api_response)
    except Exception as e:
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
> ObjectStats get_mcm_object_stats(global_id, region_id=region_id, entity_hash=entity_hash, region_ids=region_ids, cluster_identifiers=cluster_identifiers)

Get stats for a given object.

Get stats for a given object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_stats import ObjectStats
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    global_id = 'global_id_example' # str | Specifies the global id of the Object. This field is required because we only fetches snapshots stats for one object.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    entity_hash = 'entity_hash_example' # str | Specifies the entity hash global id of the Object. This field is deprecated. (optional)
    region_ids = ['region_ids_example'] # List[str] | Specifies a list of region ids. Only records from clusters having these region ids will be returned. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. (optional)

    try:
        # Get stats for a given object.
        api_response = api_instance.get_mcm_object_stats(global_id, region_id=region_id, entity_hash=entity_hash, region_ids=region_ids, cluster_identifiers=cluster_identifiers)
        print("The response of ObjectApi->get_mcm_object_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_mcm_object_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_id** | **str**| Specifies the global id of the Object. This field is required because we only fetches snapshots stats for one object. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **entity_hash** | **str**| Specifies the entity hash global id of the Object. This field is deprecated. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Specifies a list of region ids. Only records from clusters having these region ids will be returned. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. | [optional] 

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
> McmObjectSummaryResult get_mcm_object_summary(region_id=region_id, cluster_identifiers=cluster_identifiers, environments=environments)

Get the summary for a given object.

Get the objects summary across clusters.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_object_summary_result import McmObjectSummaryResult
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. (optional)
    environments = ['environments_example'] # List[str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protected objects protecting the specified environment types are returned. (optional)

    try:
        # Get the summary for a given object.
        api_response = api_instance.get_mcm_object_summary(region_id=region_id, cluster_identifiers=cluster_identifiers, environments=environments)
        print("The response of ObjectApi->get_mcm_object_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_mcm_object_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. | [optional] 
 **environments** | [**List[str]**](str.md)| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protected objects protecting the specified environment types are returned. | [optional] 

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
> McmObjectsActivity get_mcm_objects_activity(region_id=region_id, region_ids=region_ids, body=body)

Get Object activity on Helios.

Get object activity on Helios. Activity includes Protection Group Runs and Recoveries.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_mcm_objects_activity_req_params import GetMcmObjectsActivityReqParams
from cohesity_sdk.helios.models.mcm_objects_activity import McmObjectsActivity
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)
    body = cohesity_sdk.helios.GetMcmObjectsActivityReqParams() # GetMcmObjectsActivityReqParams | Request parameters to filter object activity. (optional)

    try:
        # Get Object activity on Helios.
        api_response = api_instance.get_mcm_objects_activity(region_id=region_id, region_ids=region_ids, body=body)
        print("The response of ObjectApi->get_mcm_objects_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_mcm_objects_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 
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
> McmObjectActivity get_mcm_objects_activity_by_id(id, region_id=region_id)

Get Object activity on Helios.

Get object activity on Helios by ID. Activity includes Protection Group Runs and Recoveries.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_object_activity import McmObjectActivity
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 'id_example' # str | Specifies the id of the Activity.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Object activity on Helios.
        api_response = api_instance.get_mcm_objects_activity_by_id(id, region_id=region_id)
        print("The response of ObjectApi->get_mcm_objects_activity_by_id:\n")
        pprint(api_response)
    except Exception as e:
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
> McmObjectLastRunActivities get_mcm_objects_last_run_activity(region_id=region_id, region_ids=region_ids, cluster_identifiers=cluster_identifiers, body=body)

Get last protection run of objects.

Get last protection run activity of objects.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_mcm_objects_last_run_req_params import GetMcmObjectsLastRunReqParams
from cohesity_sdk.helios.models.mcm_object_last_run_activities import McmObjectLastRunActivities
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[str] | Specifies a list of region ids. Only records from clusters having these region ids will be returned. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. (optional)
    body = cohesity_sdk.helios.GetMcmObjectsLastRunReqParams() # GetMcmObjectsLastRunReqParams | Request parameters to filter object last runs. (optional)

    try:
        # Get last protection run of objects.
        api_response = api_instance.get_mcm_objects_last_run_activity(region_id=region_id, region_ids=region_ids, cluster_identifiers=cluster_identifiers, body=body)
        print("The response of ObjectApi->get_mcm_objects_last_run_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_mcm_objects_last_run_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Specifies a list of region ids. Only records from clusters having these region ids will be returned. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. | [optional] 
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
> ObjectArchivalRunStats get_object_archival_run_stats(region_id=region_id, region_ids=region_ids, rpaas_region_ids=rpaas_region_ids, rpaas_global_vault_ids=rpaas_global_vault_ids, cluster_identifiers=cluster_identifiers, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, rpaas_only=rpaas_only)

Get the object archival run stats.

Get the stats for objects in archival runs.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_archival_run_stats import ObjectArchivalRunStats
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)
    rpaas_region_ids = ['rpaas_region_ids_example'] # List[str] | Filter by a list of region ids. This is used for Rpaas only. (optional)
    rpaas_global_vault_ids = ['rpaas_global_vault_ids_example'] # List[str] | Filter by a list of FortKnox global vault ids. This is used for FortKnox only. When rpaasGlobalVaultIds is specified, rpaasRegionIds will be ignored. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Filter by a list of cluster identifiers in format of clusterId:clusterIncarnationId. (optional)
    from_time_usecs = 56 # int | Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started after this value. The default value is 7 days ago from now. (optional)
    to_time_usecs = 56 # int | Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started before this value. The default value is the current time. (optional)
    rpaas_only = True # bool | Specifies whether the archival runs are only for RPaaS. (optional)

    try:
        # Get the object archival run stats.
        api_response = api_instance.get_object_archival_run_stats(region_id=region_id, region_ids=region_ids, rpaas_region_ids=rpaas_region_ids, rpaas_global_vault_ids=rpaas_global_vault_ids, cluster_identifiers=cluster_identifiers, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, rpaas_only=rpaas_only)
        print("The response of ObjectApi->get_object_archival_run_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_object_archival_run_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 
 **rpaas_region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. This is used for Rpaas only. | [optional] 
 **rpaas_global_vault_ids** | [**List[str]**](str.md)| Filter by a list of FortKnox global vault ids. This is used for FortKnox only. When rpaasGlobalVaultIds is specified, rpaasRegionIds will be ignored. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Filter by a list of cluster identifiers in format of clusterId:clusterIncarnationId. | [optional] 
 **from_time_usecs** | **int**| Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started after this value. The default value is 7 days ago from now. | [optional] 
 **to_time_usecs** | **int**| Specifies the time in Unix timestamp epoch in microsecond which filters all the recoveries started before this value. The default value is the current time. | [optional] 
 **rpaas_only** | **bool**| Specifies whether the archival runs are only for RPaaS. | [optional] 

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

# **get_object_run_by_run_id**
> ObjectProtectionRunSummary get_object_run_by_run_id(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id)

Get a run for an object.

Get a run for an object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_protection_run_summary import ObjectProtectionRunSummary
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies a unique id of the object.
    run_id = 'run_id_example' # str | Specifies the id of the run.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get a run for an object.
        api_response = api_instance.get_object_run_by_run_id(id, run_id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->get_object_run_by_run_id:\n")
        pprint(api_response)
    except Exception as e:
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
> GetObjectRunsResponseBody get_object_runs(id, access_cluster_id=access_cluster_id, region_id=region_id, run_id=run_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, run_types=run_types, local_backup_object_status=local_backup_object_status, replication_object_status=replication_object_status, archival_object_status=archival_object_status, cloud_spin_run_status=cloud_spin_run_status, num_runs=num_runs, pagination_cookie=pagination_cookie, exclude_non_restorable_runs=exclude_non_restorable_runs)

Get the list of runs for an object.

Get the runs for a particular object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_object_runs_response_body import GetObjectRunsResponseBody
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies a unique id of the object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    run_id = 'run_id_example' # str | Specifies a unique id of the run. (optional)
    start_time_usecs = 56 # int | Filter by a start time when the run starts. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
    end_time_usecs = 56 # int | Filter by a end time when the run starts. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. (optional)
    run_types = ['run_types_example'] # List[str] | Filter by run type. Only protection run matching the specified types will be returned. (optional)
    local_backup_object_status = ['local_backup_object_status_example'] # List[str] | Specifies a list of status for the object in the backup run. (optional)
    replication_object_status = ['replication_object_status_example'] # List[str] | Specifies a list of status for the object in the replication run. (optional)
    archival_object_status = ['archival_object_status_example'] # List[str] | Specifies a list of status for the object in the archival run. (optional)
    cloud_spin_run_status = ['cloud_spin_run_status_example'] # List[str] | Specifies a list of status for the object in the cloud spin run. (optional)
    num_runs = 56 # int | Specifies the max number of runs. If not specified, at most 100 runs will be returned. (optional)
    pagination_cookie = 'pagination_cookie_example' # str | Specifies the pagination cookie with which subsequent parts of the response can be fetched. Users can use this to get next runs (optional)
    exclude_non_restorable_runs = False # bool | Specifies whether to exclude non restorable runs. Run is treated restorable only if there is at least one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. (optional) (default to False)

    try:
        # Get the list of runs for an object.
        api_response = api_instance.get_object_runs(id, access_cluster_id=access_cluster_id, region_id=region_id, run_id=run_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, tenant_ids=tenant_ids, include_tenants=include_tenants, run_types=run_types, local_backup_object_status=local_backup_object_status, replication_object_status=replication_object_status, archival_object_status=archival_object_status, cloud_spin_run_status=cloud_spin_run_status, num_runs=num_runs, pagination_cookie=pagination_cookie, exclude_non_restorable_runs=exclude_non_restorable_runs)
        print("The response of ObjectApi->get_object_runs:\n")
        pprint(api_response)
    except Exception as e:
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
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Group Runs which were created by all tenants which the current user has permission to see. If false, then only Protection Group Runs created by the current user will be returned. | [optional] 
 **run_types** | [**List[str]**](str.md)| Filter by run type. Only protection run matching the specified types will be returned. | [optional] 
 **local_backup_object_status** | [**List[str]**](str.md)| Specifies a list of status for the object in the backup run. | [optional] 
 **replication_object_status** | [**List[str]**](str.md)| Specifies a list of status for the object in the replication run. | [optional] 
 **archival_object_status** | [**List[str]**](str.md)| Specifies a list of status for the object in the archival run. | [optional] 
 **cloud_spin_run_status** | [**List[str]**](str.md)| Specifies a list of status for the object in the cloud spin run. | [optional] 
 **num_runs** | **int**| Specifies the max number of runs. If not specified, at most 100 runs will be returned. | [optional] 
 **pagination_cookie** | **str**| Specifies the pagination cookie with which subsequent parts of the response can be fetched. Users can use this to get next runs | [optional] 
 **exclude_non_restorable_runs** | **bool**| Specifies whether to exclude non restorable runs. Run is treated restorable only if there is at least one object snapshot (which may be either a local or an archival snapshot) which is not deleted or expired. Default value is false. | [optional] [default to False]

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
> ObjectSnapshot get_object_snapshot_info(snapshot_id, access_cluster_id=access_cluster_id, region_id=region_id)

Get details of object snapshot.

Get details of object snapshot.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_snapshot import ObjectSnapshot
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | Specifies the snapshot id.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get details of object snapshot.
        api_response = api_instance.get_object_snapshot_info(snapshot_id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->get_object_snapshot_info:\n")
        pprint(api_response)
    except Exception as e:
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
> ObjectSnapshotVolumeInfo get_object_snapshot_volume_info(snapshot_id, access_cluster_id=access_cluster_id, region_id=region_id, include_supported_only=include_supported_only, point_in_time_usecs=point_in_time_usecs, use_cached_data=use_cached_data)

Get volume info of object snapshot.

Get volume info of object snapshot.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_snapshot_volume_info import ObjectSnapshotVolumeInfo
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | Specifies the snapshot id.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    include_supported_only = True # bool | Specifies whether to only return supported volumes. (optional)
    point_in_time_usecs = 3.4 # float | Specifies the point-in-time timestamp (in usecs from epoch) between snapshots for which the volume info is to be returned. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)

    try:
        # Get volume info of object snapshot.
        api_response = api_instance.get_object_snapshot_volume_info(snapshot_id, access_cluster_id=access_cluster_id, region_id=region_id, include_supported_only=include_supported_only, point_in_time_usecs=point_in_time_usecs, use_cached_data=use_cached_data)
        print("The response of ObjectApi->get_object_snapshot_volume_info:\n")
        pprint(api_response)
    except Exception as e:
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
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 

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
> GetObjectSnapshotsResponseBody get_object_snapshots(id, access_cluster_id=access_cluster_id, region_id=region_id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_start_from_time_usecs=run_start_from_time_usecs, run_start_to_time_usecs=run_start_to_time_usecs, snapshot_actions=snapshot_actions, run_types=run_types, protection_group_ids=protection_group_ids, run_instance_ids=run_instance_ids, region_ids=region_ids, object_action_keys=object_action_keys)

List the snapshots for a given object.

List the snapshots for a given object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_object_snapshots_response_body import GetObjectSnapshotsResponseBody
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the id of the Object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    from_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were taken after this value. (optional)
    to_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were taken before this value. (optional)
    run_start_from_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were run after this value. (optional)
    run_start_to_time_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter Object's snapshots which were run before this value. (optional)
    snapshot_actions = ['snapshot_actions_example'] # List[str] | Specifies a list of recovery actions. Only snapshots that applies to these actions will be returned. (optional)
    run_types = ['run_types_example'] # List[str] | Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. (optional)
    protection_group_ids = ['protection_group_ids_example'] # List[str] | If specified, this returns only the snapshots of the specified object ID, which belong to the provided protection group IDs. (optional)
    run_instance_ids = [56] # List[int] | Filter by a list run instance ids. If specified, only snapshots created by these protection runs will be returned. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)
    object_action_keys = ['object_action_keys_example'] # List[str] | Filter by ObjectActionKey, which uniquely represents protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey. When specified, only snapshots matching given action keys are returned for corresponding object. (optional)

    try:
        # List the snapshots for a given object.
        api_response = api_instance.get_object_snapshots(id, access_cluster_id=access_cluster_id, region_id=region_id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, run_start_from_time_usecs=run_start_from_time_usecs, run_start_to_time_usecs=run_start_to_time_usecs, snapshot_actions=snapshot_actions, run_types=run_types, protection_group_ids=protection_group_ids, run_instance_ids=run_instance_ids, region_ids=region_ids, object_action_keys=object_action_keys)
        print("The response of ObjectApi->get_object_snapshots:\n")
        pprint(api_response)
    except Exception as e:
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
 **snapshot_actions** | [**List[str]**](str.md)| Specifies a list of recovery actions. Only snapshots that applies to these actions will be returned. | [optional] 
 **run_types** | [**List[str]**](str.md)| Filter by run type. Only protection run matching the specified types will be returned. By default, CDP hydration snapshots are not included, unless explicitly queried using this field. | [optional] 
 **protection_group_ids** | [**List[str]**](str.md)| If specified, this returns only the snapshots of the specified object ID, which belong to the provided protection group IDs. | [optional] 
 **run_instance_ids** | [**List[int]**](int.md)| Filter by a list run instance ids. If specified, only snapshots created by these protection runs will be returned. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 
 **object_action_keys** | [**List[str]**](str.md)| Filter by ObjectActionKey, which uniquely represents protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey. When specified, only snapshots matching given action keys are returned for corresponding object. | [optional] 

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
> ObjectStats get_object_stats(id, access_cluster_id=access_cluster_id, region_id=region_id, region_ids=region_ids)

Get stats for a given object.

Get stats for a given object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_stats import ObjectStats
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the id of the Object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)

    try:
        # Get stats for a given object.
        api_response = api_instance.get_object_stats(id, access_cluster_id=access_cluster_id, region_id=region_id, region_ids=region_ids)
        print("The response of ObjectApi->get_object_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_object_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 

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
> ObjectWithChildren get_object_tree(id, access_cluster_id=access_cluster_id, region_id=region_id)

Get the objects tree hierarchy for for an Object.

Get the objects tree hierarchy for for an Object. If the object does not have a hierarchy then a single object will be returned.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_with_children import ObjectWithChildren
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the id of the Object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get the objects tree hierarchy for for an Object.
        api_response = api_instance.get_object_tree(id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->get_object_tree:\n")
        pprint(api_response)
    except Exception as e:
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
> ObjectsLastRun get_objects_last_run(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, pagination_cookie=pagination_cookie, count=count)

Get last protection run of objects.

Get last protection run of objects.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.objects_last_run import ObjectsLastRun
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = [56] # List[int] | Specifies a list of object ids, only last runs for these objects will be returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Objects which belongs to all tenants which the current user has permission to see. (optional)
    pagination_cookie = 'pagination_cookie_example' # str | Specifies the pagination cookie with which subsequent parts of the response can be fetched. (optional)
    count = 56 # int | Specifies the number of objects to be fetched for the specified pagination cookie. (optional)

    try:
        # Get last protection run of objects.
        api_response = api_instance.get_objects_last_run(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, pagination_cookie=pagination_cookie, count=count)
        print("The response of ObjectApi->get_objects_last_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_objects_last_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[int]**](int.md)| Specifies a list of object ids, only last runs for these objects will be returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
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
> GetPITRangesProtectedObjectResponseBody get_pit_ranges_for_protected_object(id, access_cluster_id=access_cluster_id, region_id=region_id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, protection_group_ids=protection_group_ids)

Get PIT ranges for an object

Returns the ranges in various types like time, SCN etc. within which the specified protected object can be restored to any Point in time.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_pit_ranges_protected_object_response_body import GetPITRangesProtectedObjectResponseBody
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the ID of the protected object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    from_time_usecs = 56 # int | If specified, return the restore ranges that lie after this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. (optional)
    to_time_usecs = 56 # int | If specified, return the restore ranges that lie before this timestamp. This parameter is specified as the timestamp in Unix time epoch in microseconds. (optional)
    protection_group_ids = ['protection_group_ids_example'] # List[str] | If specified, return only the points in time corresponding to these protection group IDs. (optional)

    try:
        # Get PIT ranges for an object
        api_response = api_instance.get_pit_ranges_for_protected_object(id, access_cluster_id=access_cluster_id, region_id=region_id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, protection_group_ids=protection_group_ids)
        print("The response of ObjectApi->get_pit_ranges_for_protected_object:\n")
        pprint(api_response)
    except Exception as e:
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
 **protection_group_ids** | [**List[str]**](str.md)| If specified, return only the points in time corresponding to these protection group IDs. | [optional] 

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
> ProtectedObjectInfo get_protected_object_of_any_type_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, object_action_key=object_action_key, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects)

Get an Object.

Get Object configurations for given object id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.protected_object_info import ProtectedObjectInfo
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the id of the Object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    object_action_key = ['object_action_key_example'] # List[str] | Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id and this vec's size needs to be same as 'id'. (optional)
    only_protected_objects = True # bool | If true, the response will include only objects which have been protected. (optional)
    storage_domain_id = 56 # int | Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. (optional)
    environments = ['environments_example'] # List[str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protected objects protecting the specified environment types are returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. (optional)
    include_last_run_info = True # bool | If true, the response will include information about the last protection run on this object. (optional)
    only_auto_protected_objects = True # bool | If true, the response will include only the auto protected objects. (optional)
    only_leaf_objects = True # bool | If true, the response will include only the leaf level objects. (optional)

    try:
        # Get an Object.
        api_response = api_instance.get_protected_object_of_any_type_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, object_action_key=object_action_key, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects)
        print("The response of ObjectApi->get_protected_object_of_any_type_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_protected_object_of_any_type_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Object. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **object_action_key** | [**List[str]**](str.md)| Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id and this vec&#39;s size needs to be same as &#39;id&#39;. | [optional] 
 **only_protected_objects** | **bool**| If true, the response will include only objects which have been protected. | [optional] 
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. | [optional] 
 **environments** | [**List[str]**](str.md)| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protected objects protecting the specified environment types are returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
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
> GetProtectedObjectsResponse get_protected_objects_of_any_type(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, ids=ids, object_action_keys=object_action_keys, policy_ids=policy_ids, parent_id=parent_id, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects, region_ids=region_ids, max_count=max_count, cookie=cookie)

Get Objects.

Get Objects Configurations.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_protected_objects_response import GetProtectedObjectsResponse
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    ids = [56] # List[int] | Filter by a list of Object ids. (optional)
    object_action_keys = ['object_action_keys_example'] # List[str] | Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id. The vec's size needs to be of either length one or same as the length of 'ids'. If the length of objectActionKey is one, it will be repeated as many number of times equal to the length of objectIds, as mandated by backend validation. If the length of objectActionKey and object ids are same then it will be passed as it is. (optional)
    policy_ids = ['policy_ids_example'] # List[str] | Filter by Policy ids that are associated with Protected Objects. (optional)
    parent_id = 56 # int | Filter by Parent Id. Parent id is a unique object Id which may contain protected objects underneath in the source tree. (optional)
    only_protected_objects = True # bool | If true, the response will include only objects which have been protected. (optional)
    storage_domain_id = 56 # int | Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. (optional)
    environments = ['environments_example'] # List[str] | Filter by environment types such as 'kVMware', 'kView', etc. Only Protected objects protecting the specified environment types are returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. (optional)
    include_last_run_info = True # bool | If true, the response will include information about the last protection run on this object. (optional)
    only_auto_protected_objects = True # bool | If true, the response will include only the auto protected objects. (optional)
    only_leaf_objects = True # bool | If true, the response will include only the leaf level objects. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)
    max_count = 56 # int | Specifies the max number of objects to return. (optional)
    cookie = 'cookie_example' # str | Specifies the pagination cookie. (optional)

    try:
        # Get Objects.
        api_response = api_instance.get_protected_objects_of_any_type(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, ids=ids, object_action_keys=object_action_keys, policy_ids=policy_ids, parent_id=parent_id, only_protected_objects=only_protected_objects, storage_domain_id=storage_domain_id, environments=environments, tenant_ids=tenant_ids, include_tenants=include_tenants, include_last_run_info=include_last_run_info, only_auto_protected_objects=only_auto_protected_objects, only_leaf_objects=only_leaf_objects, region_ids=region_ids, max_count=max_count, cookie=cookie)
        print("The response of ObjectApi->get_protected_objects_of_any_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_protected_objects_of_any_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **ids** | [**List[int]**](int.md)| Filter by a list of Object ids. | [optional] 
 **object_action_keys** | [**List[str]**](str.md)| Filter by ObjectActionKey, uniquely represent protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey, when specified Only objects of given action_key are returned for corresponding object id. The vec&#39;s size needs to be of either length one or same as the length of &#39;ids&#39;. If the length of objectActionKey is one, it will be repeated as many number of times equal to the length of objectIds, as mandated by backend validation. If the length of objectActionKey and object ids are same then it will be passed as it is. | [optional] 
 **policy_ids** | [**List[str]**](str.md)| Filter by Policy ids that are associated with Protected Objects. | [optional] 
 **parent_id** | **int**| Filter by Parent Id. Parent id is a unique object Id which may contain protected objects underneath in the source tree. | [optional] 
 **only_protected_objects** | **bool**| If true, the response will include only objects which have been protected. | [optional] 
 **storage_domain_id** | **int**| Filter by Storage Domain id. Only Objects protected to this Storage Domain will be returned. | [optional] 
 **environments** | [**List[str]**](str.md)| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, etc. Only Protected objects protecting the specified environment types are returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Objects which were protected by all tenants which the current user has permission to see. If false, then only objects protected by the current user will be returned. | [optional] 
 **include_last_run_info** | **bool**| If true, the response will include information about the last protection run on this object. | [optional] 
 **only_auto_protected_objects** | **bool**| If true, the response will include only the auto protected objects. | [optional] 
 **only_leaf_objects** | **bool**| If true, the response will include only the leaf level objects. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 
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
> SnapshotDiffResult get_snapshot_diff(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Get diff between two snapshots of a given object.

Get diff (files added/deleted) between two snapshots of a given object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.snapshot_diff_params import SnapshotDiffParams
from cohesity_sdk.helios.models.snapshot_diff_result import SnapshotDiffResult
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | 
    body = cohesity_sdk.helios.SnapshotDiffParams() # SnapshotDiffParams | 
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get diff between two snapshots of a given object.
        api_response = api_instance.get_snapshot_diff(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->get_snapshot_diff:\n")
        pprint(api_response)
    except Exception as e:
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
> SourceHierarchyObjectSummaries get_source_hierarchy_objects(source_id, access_cluster_id=access_cluster_id, region_id=region_id, parent_id=parent_id, tenant_ids=tenant_ids, include_tenants=include_tenants, vmware_object_types=vmware_object_types, netapp_object_types=netapp_object_types, o365_object_types=o365_object_types, cassandra_object_types=cassandra_object_types, mongodb_object_types=mongodb_object_types, couchbase_object_types=couchbase_object_types, hdfs_object_types=hdfs_object_types, hbase_object_types=hbase_object_types, hive_object_types=hive_object_types, hyperv_object_types=hyperv_object_types, azure_object_types=azure_object_types, kvm_object_types=kvm_object_types, aws_object_types=aws_object_types, gcp_object_types=gcp_object_types, acropolis_object_types=acropolis_object_types, generic_nas_object_types=generic_nas_object_types, isilon_object_types=isilon_object_types, flashblade_object_types=flashblade_object_types, elastifile_object_types=elastifile_object_types, gpfs_object_types=gpfs_object_types, pure_object_types=pure_object_types, nimble_object_types=nimble_object_types, physical_object_types=physical_object_types, kubernetes_object_types=kubernetes_object_types, exchange_object_types=exchange_object_types, ad_object_types=ad_object_types, mssql_object_types=mssql_object_types, oracle_object_types=oracle_object_types, use_cached_data=use_cached_data)

List objects on a source which can be used for data protection.

List objects which can be used for data protection.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_hierarchy_object_summaries import SourceHierarchyObjectSummaries
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    source_id = 56 # int | Specifies the source ID for which objects should be returned.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    parent_id = 56 # int | Specifies the parent ID under which objects should be returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Objects which belongs to all tenants which the current user has permission to see. (optional)
    vmware_object_types = ['vmware_object_types_example'] # List[str] | Specifies the VMware object types to filter objects. (optional)
    netapp_object_types = ['netapp_object_types_example'] # List[str] | Specifies the Netapp object types to filter objects. (optional)
    o365_object_types = ['o365_object_types_example'] # List[str] | Specifies the Office 365 object types to filter objects. (optional)
    cassandra_object_types = ['cassandra_object_types_example'] # List[str] | Specifies the Cassandra object types to filter objects. (optional)
    mongodb_object_types = ['mongodb_object_types_example'] # List[str] | Specifies the Mongo DB object types to filter objects. (optional)
    couchbase_object_types = ['couchbase_object_types_example'] # List[str] | Specifies the Couchbase object types to filter objects. (optional)
    hdfs_object_types = ['hdfs_object_types_example'] # List[str] | Specifies the HDFS object types to filter objects. (optional)
    hbase_object_types = ['hbase_object_types_example'] # List[str] | Specifies the Hbase object types to filter objects. (optional)
    hive_object_types = ['hive_object_types_example'] # List[str] | Specifies the Hive object types to filter objects. (optional)
    hyperv_object_types = ['hyperv_object_types_example'] # List[str] | Specifies the HyperV object types to filter objects. (optional)
    azure_object_types = ['azure_object_types_example'] # List[str] | Specifies the Azure object types to filter objects. (optional)
    kvm_object_types = ['kvm_object_types_example'] # List[str] | Specifies the KVM object types to filter objects. (optional)
    aws_object_types = ['aws_object_types_example'] # List[str] | Specifies the AWS object types to filter objects. (optional)
    gcp_object_types = ['gcp_object_types_example'] # List[str] | Specifies the GCP object types to filter objects. (optional)
    acropolis_object_types = ['acropolis_object_types_example'] # List[str] | Specifies the Acropolis object types to filter objects. (optional)
    generic_nas_object_types = ['generic_nas_object_types_example'] # List[str] | Specifies the generic NAS object types to filter objects. (optional)
    isilon_object_types = ['isilon_object_types_example'] # List[str] | Specifies the Isilon object types to filter objects. (optional)
    flashblade_object_types = ['flashblade_object_types_example'] # List[str] | Specifies the Flashblade object types to filter objects. (optional)
    elastifile_object_types = ['elastifile_object_types_example'] # List[str] | Specifies the Elastifile object types to filter objects. (optional)
    gpfs_object_types = ['gpfs_object_types_example'] # List[str] | Specifies the GPFS object types to filter objects. (optional)
    pure_object_types = ['pure_object_types_example'] # List[str] | Specifies the Pure object types to filter objects. (optional)
    nimble_object_types = ['nimble_object_types_example'] # List[str] | Specifies the Nimble object types to filter objects. (optional)
    physical_object_types = ['physical_object_types_example'] # List[str] | Specifies the Physical object types to filter objects. (optional)
    kubernetes_object_types = ['kubernetes_object_types_example'] # List[str] | Specifies the Kubernetes object types to filter objects. (optional)
    exchange_object_types = ['exchange_object_types_example'] # List[str] | Specifies the Exchange object types to filter objects. (optional)
    ad_object_types = ['ad_object_types_example'] # List[str] | Specifies the AD object types to filter objects. (optional)
    mssql_object_types = ['mssql_object_types_example'] # List[str] | Specifies the MSSQL object types to filter objects. (optional)
    oracle_object_types = ['oracle_object_types_example'] # List[str] | Specifies the Oracle object types to filter objects. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)

    try:
        # List objects on a source which can be used for data protection.
        api_response = api_instance.get_source_hierarchy_objects(source_id, access_cluster_id=access_cluster_id, region_id=region_id, parent_id=parent_id, tenant_ids=tenant_ids, include_tenants=include_tenants, vmware_object_types=vmware_object_types, netapp_object_types=netapp_object_types, o365_object_types=o365_object_types, cassandra_object_types=cassandra_object_types, mongodb_object_types=mongodb_object_types, couchbase_object_types=couchbase_object_types, hdfs_object_types=hdfs_object_types, hbase_object_types=hbase_object_types, hive_object_types=hive_object_types, hyperv_object_types=hyperv_object_types, azure_object_types=azure_object_types, kvm_object_types=kvm_object_types, aws_object_types=aws_object_types, gcp_object_types=gcp_object_types, acropolis_object_types=acropolis_object_types, generic_nas_object_types=generic_nas_object_types, isilon_object_types=isilon_object_types, flashblade_object_types=flashblade_object_types, elastifile_object_types=elastifile_object_types, gpfs_object_types=gpfs_object_types, pure_object_types=pure_object_types, nimble_object_types=nimble_object_types, physical_object_types=physical_object_types, kubernetes_object_types=kubernetes_object_types, exchange_object_types=exchange_object_types, ad_object_types=ad_object_types, mssql_object_types=mssql_object_types, oracle_object_types=oracle_object_types, use_cached_data=use_cached_data)
        print("The response of ObjectApi->get_source_hierarchy_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_source_hierarchy_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| Specifies the source ID for which objects should be returned. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **parent_id** | **int**| Specifies the parent ID under which objects should be returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Objects which belongs to all tenants which the current user has permission to see. | [optional] 
 **vmware_object_types** | [**List[str]**](str.md)| Specifies the VMware object types to filter objects. | [optional] 
 **netapp_object_types** | [**List[str]**](str.md)| Specifies the Netapp object types to filter objects. | [optional] 
 **o365_object_types** | [**List[str]**](str.md)| Specifies the Office 365 object types to filter objects. | [optional] 
 **cassandra_object_types** | [**List[str]**](str.md)| Specifies the Cassandra object types to filter objects. | [optional] 
 **mongodb_object_types** | [**List[str]**](str.md)| Specifies the Mongo DB object types to filter objects. | [optional] 
 **couchbase_object_types** | [**List[str]**](str.md)| Specifies the Couchbase object types to filter objects. | [optional] 
 **hdfs_object_types** | [**List[str]**](str.md)| Specifies the HDFS object types to filter objects. | [optional] 
 **hbase_object_types** | [**List[str]**](str.md)| Specifies the Hbase object types to filter objects. | [optional] 
 **hive_object_types** | [**List[str]**](str.md)| Specifies the Hive object types to filter objects. | [optional] 
 **hyperv_object_types** | [**List[str]**](str.md)| Specifies the HyperV object types to filter objects. | [optional] 
 **azure_object_types** | [**List[str]**](str.md)| Specifies the Azure object types to filter objects. | [optional] 
 **kvm_object_types** | [**List[str]**](str.md)| Specifies the KVM object types to filter objects. | [optional] 
 **aws_object_types** | [**List[str]**](str.md)| Specifies the AWS object types to filter objects. | [optional] 
 **gcp_object_types** | [**List[str]**](str.md)| Specifies the GCP object types to filter objects. | [optional] 
 **acropolis_object_types** | [**List[str]**](str.md)| Specifies the Acropolis object types to filter objects. | [optional] 
 **generic_nas_object_types** | [**List[str]**](str.md)| Specifies the generic NAS object types to filter objects. | [optional] 
 **isilon_object_types** | [**List[str]**](str.md)| Specifies the Isilon object types to filter objects. | [optional] 
 **flashblade_object_types** | [**List[str]**](str.md)| Specifies the Flashblade object types to filter objects. | [optional] 
 **elastifile_object_types** | [**List[str]**](str.md)| Specifies the Elastifile object types to filter objects. | [optional] 
 **gpfs_object_types** | [**List[str]**](str.md)| Specifies the GPFS object types to filter objects. | [optional] 
 **pure_object_types** | [**List[str]**](str.md)| Specifies the Pure object types to filter objects. | [optional] 
 **nimble_object_types** | [**List[str]**](str.md)| Specifies the Nimble object types to filter objects. | [optional] 
 **physical_object_types** | [**List[str]**](str.md)| Specifies the Physical object types to filter objects. | [optional] 
 **kubernetes_object_types** | [**List[str]**](str.md)| Specifies the Kubernetes object types to filter objects. | [optional] 
 **exchange_object_types** | [**List[str]**](str.md)| Specifies the Exchange object types to filter objects. | [optional] 
 **ad_object_types** | [**List[str]**](str.md)| Specifies the AD object types to filter objects. | [optional] 
 **mssql_object_types** | [**List[str]**](str.md)| Specifies the MSSQL object types to filter objects. | [optional] 
 **oracle_object_types** | [**List[str]**](str.md)| Specifies the Oracle object types to filter objects. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 

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

# **mcm_get_tenant_object_ids**
> McmTenantObjectIds mcm_get_tenant_object_ids(body, region_id=region_id)

GetTenantObjectIds

Get the object IDs for a given DMaaS tenant given a list of object hashes.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_tenant_object_ids import McmTenantObjectIds
from cohesity_sdk.helios.models.mcm_tenant_object_ids_params import McmTenantObjectIdsParams
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    body = cohesity_sdk.helios.McmTenantObjectIdsParams() # McmTenantObjectIdsParams | Specifies the parameters to fetch object IDs.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # GetTenantObjectIds
        api_response = api_instance.mcm_get_tenant_object_ids(body, region_id=region_id)
        print("The response of ObjectApi->mcm_get_tenant_object_ids:\n")
        pprint(api_response)
    except Exception as e:
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

# **objects_actions**
> objects_actions(body, access_cluster_id=access_cluster_id, region_id=region_id)

Actions on Objects

Specifies the request to perform various actions on multiple objects.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.objects_action_request import ObjectsActionRequest
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    body = cohesity_sdk.helios.ObjectsActionRequest() # ObjectsActionRequest | Specifies the parameters to execute actions on given list of objects.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Actions on Objects
        api_instance.objects_actions(body, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling ObjectApi->objects_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectsActionRequest**](ObjectsActionRequest.md)| Specifies the parameters to execute actions on given list of objects. | 
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
> perform_action_on_object(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Perform an action on an object.

Perform an action on an object. Depending on the object environment type, different actions are available.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_action_request import ObjectActionRequest
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the id of the Object.
    body = cohesity_sdk.helios.ObjectActionRequest() # ObjectActionRequest | Specifies the parameters to perform an action on an object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform an action on an object.
        api_instance.perform_action_on_object(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
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
> ObjectSnapshot update_object_snapshot(id, snapshot_id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update an object snapshot.

Update an object snapshot.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.object_snapshot import ObjectSnapshot
from cohesity_sdk.helios.models.update_object_snapshot_request import UpdateObjectSnapshotRequest
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
    api_instance = cohesity_sdk.helios.ObjectApi(api_client)
    id = 56 # int | Specifies the id of the Object.
    snapshot_id = 'snapshot_id_example' # str | Specifies the id of the snapshot.<br> Note: 1. If the snapshotid of one of the apps is specified, it applies for all the databases in the Protection Run.<br> 2. In case of volume based jobs, please specify the snapshotid of the source not the database. if source snapshot is specified, applied to source snapshot. if database snapshotid is specified in case of volume based jobs, then it is applicable for host's snapshot.
    body = cohesity_sdk.helios.UpdateObjectSnapshotRequest() # UpdateObjectSnapshotRequest | Specifies the parameters update an object snapshot.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update an object snapshot.
        api_response = api_instance.update_object_snapshot(id, snapshot_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ObjectApi->update_object_snapshot:\n")
        pprint(api_response)
    except Exception as e:
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

