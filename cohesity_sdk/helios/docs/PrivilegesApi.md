# cohesity_sdk.PrivilegesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_privileges**](PrivilegesApi.md#get_privileges) | **GET** /privileges | Get Privileges.


# **get_privileges**
> Privileges get_privileges()

Get Privileges.

Get Privileges.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.privileges import Privileges
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
names = [
        "names_example",
    ] # [str] | Filter by a list of Privilege names. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Privileges.
	api_response = client.privileges.get_privileges(access_cluster_id=access_cluster_id, region_id=region_id, names=names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PrivilegesApi->get_privileges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **names** | **[str]**| Filter by a list of Privilege names. | [optional]

### Return type

[**Privileges**](Privileges.md)

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

