# cohesity_sdk.MiscellaneousApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_objects**](MiscellaneousApi.md#filter_objects) | **POST** /data-protect/filter/objects | List all the filtered objects.


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

# example passing only required values which don't have defaults set
try:
	# List all the filtered objects.
	api_response = client.miscellaneous.filter_objects(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling MiscellaneousApi->filter_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilterObjectsRequest**](FilterObjectsRequest.md)| Specifies the parameters to filter objects. |

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

