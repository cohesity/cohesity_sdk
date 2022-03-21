# cohesity_sdk.InternalApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_bulletin_board**](InternalApi.md#refresh_bulletin_board) | **POST** /refresh-bulletin-board | Refresh bulletin board from Helios.


# **refresh_bulletin_board**
> refresh_bulletin_board()

Refresh bulletin board from Helios.

Refresh bulletin board from Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Refresh bulletin board from Helios.
	client.internal.refresh_bulletin_board()
except ApiException as e:
	print("Exception when calling InternalApi->refresh_bulletin_board: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

