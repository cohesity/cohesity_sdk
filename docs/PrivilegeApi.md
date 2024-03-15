# cohesity_sdk.PrivilegeApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_privileges**](PrivilegeApi.md#get_privileges) | **GET** /privileges | Get Privileges.


# **get_privileges**
> Privileges get_privileges()

Get Privileges.

Get Privileges.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.privileges import Privileges
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

names = [
        "names_example",
    ] # [str] | Filter by a list of Privilege names. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Privileges.
	api_response = client.privilege.get_privileges(names=names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PrivilegeApi->get_privileges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **[str]**| Filter by a list of Privilege names. | [optional]

### Return type

[**Privileges**](Privileges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

