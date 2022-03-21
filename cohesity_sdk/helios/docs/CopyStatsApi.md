# cohesity_sdk.CopyStatsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_copy_stats**](CopyStatsApi.md#get_copy_stats) | **POST** /mcm/data-protect/copystats/details | Get copy details.


# **get_copy_stats**
> GetCopyStatResponse get_copy_stats(body)

Get copy details.

Obtain the details of copy given the list of filters

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.get_copy_stat_params import GetCopyStatParams
from cohesity_sdk.helios.model.get_copy_stat_response import GetCopyStatResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = GetCopyStatParams(
        cluster_identifiers=[
            "cluster_identifiers_example",
        ],
        protection_group_ids=[
            "protection_group_ids_example",
        ],
        run_instance_ids=[
            1,
        ],
        from_run_start_time_usecs=1,
        to_run_start_time_usecs=1,
        object_ids=[
            1,
        ],
        snapshot_ids=[
            "snapshot_ids_example",
        ],
        tenant_ids=[
            "tenant_ids_example",
        ],
        region_ids=[
            "region_ids_example",
        ],
        tags=[
            SnapshotTag(
                id=1,
                label="label_example",
            ),
        ],
        has_anomaly_tag=True,
        locations=[
            "cluster",
        ],
        requested_data=[
            "storageMetrics",
        ],
        page_count=1,
        page_size=1,
    ) # GetCopyStatParams | Copy stats filter parameters.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get copy details.
	api_response = client.copy_stats.get_copy_stats(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CopyStatsApi->get_copy_stats: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get copy details.
	api_response = client.copy_stats.get_copy_stats(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CopyStatsApi->get_copy_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetCopyStatParams**](GetCopyStatParams.md)| Copy stats filter parameters. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**GetCopyStatResponse**](GetCopyStatResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Copy stat details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

