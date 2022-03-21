# cohesity_sdk.TaggingServiceApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_snapshots_tags**](TaggingServiceApi.md#add_snapshots_tags) | **POST** /mcm/tags/snapshots | Adds specified tags to snapshots.
[**get_snapshots_tags**](TaggingServiceApi.md#get_snapshots_tags) | **POST** /mcm/tags/snapshots/status | Get the tags of snapshots.
[**remove_snapshots_tags**](TaggingServiceApi.md#remove_snapshots_tags) | **DELETE** /mcm/tags/snapshots | Removes specified tags of snapshots.


# **add_snapshots_tags**
> SnapshotTagsList add_snapshots_tags(body)

Adds specified tags to snapshots.

Adds the tag labels specified in the parameters, to the snapshots.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.snapshot_tags_list import SnapshotTagsList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = SnapshotTagsList([
        SnapshotTags(
            snapshot=Snapshot(
                snapshot_id="snapshot_id_example",
                cluster_id=1,
                incarnation_id=1,
                protection_group_id=1,
                run_id=1,
                object_id=1,
                run_start_time_usecs=1,
                tenant_ids=[
                    "tenant_ids_example",
                ],
            ),
            tags=[
                SnapshotTag(
                    id=1,
                    label="label_example",
                ),
            ],
        ),
    ]) # SnapshotTagsList | SnapshotTagsList specifies list of snapshots and tags to add to each of those. Only the tags to be added are specified. Existing tags will remain added. Response  will contain all tags associated with snapshots after addition.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Adds specified tags to snapshots.
	api_response = client.tagging_service.add_snapshots_tags(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TaggingServiceApi->add_snapshots_tags: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Adds specified tags to snapshots.
	api_response = client.tagging_service.add_snapshots_tags(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TaggingServiceApi->add_snapshots_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotTagsList**](SnapshotTagsList.md)| SnapshotTagsList specifies list of snapshots and tags to add to each of those. Only the tags to be added are specified. Existing tags will remain added. Response  will contain all tags associated with snapshots after addition. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SnapshotTagsList**](SnapshotTagsList.md)

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

# **get_snapshots_tags**
> SnapshotTagsList get_snapshots_tags(body)

Get the tags of snapshots.

Gets tag labels (if tagged) of snapshots, specified by parameters. Else, just returns back snapshots info, without any labels.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.snapshots_list import SnapshotsList
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.snapshot_tags_list import SnapshotTagsList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = SnapshotsList([
        Snapshot(
            snapshot_id="snapshot_id_example",
            cluster_id=1,
            incarnation_id=1,
            protection_group_id=1,
            run_id=1,
            object_id=1,
            run_start_time_usecs=1,
            tenant_ids=[
                "tenant_ids_example",
            ],
        ),
    ]) # SnapshotsList | SnapshotsList represents list of snapshots identified by various parameters like clusterId, protectionGroupId, objectId etc.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the tags of snapshots.
	api_response = client.tagging_service.get_snapshots_tags(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TaggingServiceApi->get_snapshots_tags: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the tags of snapshots.
	api_response = client.tagging_service.get_snapshots_tags(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TaggingServiceApi->get_snapshots_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotsList**](SnapshotsList.md)| SnapshotsList represents list of snapshots identified by various parameters like clusterId, protectionGroupId, objectId etc. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SnapshotTagsList**](SnapshotTagsList.md)

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

# **remove_snapshots_tags**
> remove_snapshots_tags(body)

Removes specified tags of snapshots.

Removes the tag labels specified in the parameters, from the snapshots.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.snapshot_tags_list import SnapshotTagsList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = SnapshotTagsList([
        SnapshotTags(
            snapshot=Snapshot(
                snapshot_id="snapshot_id_example",
                cluster_id=1,
                incarnation_id=1,
                protection_group_id=1,
                run_id=1,
                object_id=1,
                run_start_time_usecs=1,
                tenant_ids=[
                    "tenant_ids_example",
                ],
            ),
            tags=[
                SnapshotTag(
                    id=1,
                    label="label_example",
                ),
            ],
        ),
    ]) # SnapshotTagsList | SnapshotTagsList specifies list of snapshots and associated tags to remove from each of those. Only the tags to be removed are specified. Other existing tags will remain added. Response will contain tags associated with snapshots after removing specified tags.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Removes specified tags of snapshots.
	client.tagging_service.remove_snapshots_tags(body)
except ApiException as e:
	print("Exception when calling TaggingServiceApi->remove_snapshots_tags: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Removes specified tags of snapshots.
	client.tagging_service.remove_snapshots_tags(body, region_id=region_id)
except ApiException as e:
	print("Exception when calling TaggingServiceApi->remove_snapshots_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotTagsList**](SnapshotTagsList.md)| SnapshotTagsList specifies list of snapshots and associated tags to remove from each of those. Only the tags to be removed are specified. Other existing tags will remain added. Response will contain tags associated with snapshots after removing specified tags. |
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

