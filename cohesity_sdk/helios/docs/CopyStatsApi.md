# cohesity_sdk.helios.CopyStatsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_copy_stats**](CopyStatsApi.md#get_copy_stats) | **POST** /mcm/data-protect/copystats/details | Get copy details.


# **get_copy_stats**
> List[CopyStats] get_copy_stats(body, region_id=region_id)

Get copy details.

Obtain the details of copy given the list of filters

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.copy_stats import CopyStats
from cohesity_sdk.helios.models.get_copy_stat_params import GetCopyStatParams
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
    api_instance = cohesity_sdk.helios.CopyStatsApi(api_client)
    body = cohesity_sdk.helios.GetCopyStatParams() # GetCopyStatParams | Copy stats filter parameters.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get copy details.
        api_response = api_instance.get_copy_stats(body, region_id=region_id)
        print("The response of CopyStatsApi->get_copy_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopyStatsApi->get_copy_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetCopyStatParams**](GetCopyStatParams.md)| Copy stats filter parameters. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**List[CopyStats]**](CopyStats.md)

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

