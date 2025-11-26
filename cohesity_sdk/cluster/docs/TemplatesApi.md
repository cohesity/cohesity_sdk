# cohesity_sdk.TemplatesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**download_art_file**](TemplatesApi.md#download_art_file) | **GET** /data-protect/templates/downloadArtFile | Download the azure resource template.


# **download_art_file**
> file_type download_art_file()

Download the azure resource template.

Download the azure resource template.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Download the azure resource template.
	api_response = client.templates.download_art_file()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TemplatesApi->download_art_file: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**file_type**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

