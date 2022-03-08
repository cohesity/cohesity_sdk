# cohesity_sdk.HeliosObjectsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mcm_object_snapshots**](HeliosObjectsApi.md#get_mcm_object_snapshots) | **GET** /mcm/data-protect/objects/snapshots | List the snapshots for a given object.
[**get_mcm_object_stats**](HeliosObjectsApi.md#get_mcm_object_stats) | **GET** /mcm/data-protect/objects/stats | Get stats for a given object.
[**get_mcm_object_summary**](HeliosObjectsApi.md#get_mcm_object_summary) | **GET** /mcm/objects/summary | Get the summary for a given object.
[**get_mcm_objects_activity**](HeliosObjectsApi.md#get_mcm_objects_activity) | **POST** /mcm/data-protect/objects/activity | Get Object activity on Helios.
[**mcm_get_tenant_object_ids**](HeliosObjectsApi.md#mcm_get_tenant_object_ids) | **POST** /mcm/tenants/object-ids | GetTenantObjectIds


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
	api_response = client.helios_objects.get_mcm_object_snapshots(global_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->get_mcm_object_snapshots: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the snapshots for a given object.
	api_response = client.helios_objects.get_mcm_object_snapshots(global_id, region_id=region_id, uuid=uuid, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->get_mcm_object_snapshots: %s\n" % e)
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
	api_response = client.helios_objects.get_mcm_object_stats(global_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->get_mcm_object_stats: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get stats for a given object.
	api_response = client.helios_objects.get_mcm_object_stats(global_id, region_id=region_id, entity_hash=entity_hash, region_ids=region_ids, cluster_identifiers=cluster_identifiers)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->get_mcm_object_stats: %s\n" % e)
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
	api_response = client.helios_objects.get_mcm_object_summary(region_id=region_id, cluster_identifiers=cluster_identifiers, environments=environments)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->get_mcm_object_summary: %s\n" % e)
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
        ),
        restore_params={},
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
	api_response = client.helios_objects.get_mcm_objects_activity(region_id=region_id, region_ids=region_ids, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->get_mcm_objects_activity: %s\n" % e)
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
	api_response = client.helios_objects.mcm_get_tenant_object_ids(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->mcm_get_tenant_object_ids: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# GetTenantObjectIds
	api_response = client.helios_objects.mcm_get_tenant_object_ids(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosObjectsApi->mcm_get_tenant_object_ids: %s\n" % e)
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

