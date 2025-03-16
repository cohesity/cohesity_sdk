# cohesity_sdk.helios.TaggingServiceApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_snapshots_tags**](TaggingServiceApi.md#add_snapshots_tags) | **POST** /mcm/tags/snapshots | Adds specified tags to snapshots.
[**get_snapshots_tags**](TaggingServiceApi.md#get_snapshots_tags) | **POST** /mcm/tags/snapshots/status | Get the tags of snapshots.
[**remove_snapshots_tags**](TaggingServiceApi.md#remove_snapshots_tags) | **DELETE** /mcm/tags/snapshots | Removes specified tags of snapshots.


# **add_snapshots_tags**
> List[SnapshotTags] add_snapshots_tags(body, region_id=region_id)

Adds specified tags to snapshots.

Adds the tag labels specified in the parameters, to the snapshots.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.snapshot_tags import SnapshotTags
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
    api_instance = cohesity_sdk.helios.TaggingServiceApi(api_client)
    body = [cohesity_sdk.helios.SnapshotTags()] # List[SnapshotTags] | SnapshotTagsList specifies list of snapshots and tags to add to each of those. Only the tags to be added are specified. Existing tags will remain added. Response  will contain all tags associated with snapshots after addition.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Adds specified tags to snapshots.
        api_response = api_instance.add_snapshots_tags(body, region_id=region_id)
        print("The response of TaggingServiceApi->add_snapshots_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaggingServiceApi->add_snapshots_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[SnapshotTags]**](SnapshotTags.md)| SnapshotTagsList specifies list of snapshots and tags to add to each of those. Only the tags to be added are specified. Existing tags will remain added. Response  will contain all tags associated with snapshots after addition. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**List[SnapshotTags]**](SnapshotTags.md)

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
> List[SnapshotTags] get_snapshots_tags(body, region_id=region_id)

Get the tags of snapshots.

Gets tag labels (if tagged) of snapshots, specified by parameters. Else, just returns back snapshots info, without any labels.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.snapshot import Snapshot
from cohesity_sdk.helios.models.snapshot_tags import SnapshotTags
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
    api_instance = cohesity_sdk.helios.TaggingServiceApi(api_client)
    body = [cohesity_sdk.helios.Snapshot()] # List[Snapshot] | SnapshotsList represents list of snapshots identified by various parameters like clusterId, protectionGroupId, objectId etc.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get the tags of snapshots.
        api_response = api_instance.get_snapshots_tags(body, region_id=region_id)
        print("The response of TaggingServiceApi->get_snapshots_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaggingServiceApi->get_snapshots_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[Snapshot]**](Snapshot.md)| SnapshotsList represents list of snapshots identified by various parameters like clusterId, protectionGroupId, objectId etc. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**List[SnapshotTags]**](SnapshotTags.md)

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
> remove_snapshots_tags(body, region_id=region_id)

Removes specified tags of snapshots.

Removes the tag labels specified in the parameters, from the snapshots.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.snapshot_tags import SnapshotTags
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
    api_instance = cohesity_sdk.helios.TaggingServiceApi(api_client)
    body = [cohesity_sdk.helios.SnapshotTags()] # List[SnapshotTags] | SnapshotTagsList specifies list of snapshots and associated tags to remove from each of those. Only the tags to be removed are specified. Other existing tags will remain added. Response will contain tags associated with snapshots after removing specified tags.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Removes specified tags of snapshots.
        api_instance.remove_snapshots_tags(body, region_id=region_id)
    except Exception as e:
        print("Exception when calling TaggingServiceApi->remove_snapshots_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[SnapshotTags]**](SnapshotTags.md)| SnapshotTagsList specifies list of snapshots and associated tags to remove from each of those. Only the tags to be removed are specified. Other existing tags will remain added. Response will contain tags associated with snapshots after removing specified tags. | 
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

