# cohesity_sdk.MarketplaceAppApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_marketplace_app_ui_details**](MarketplaceAppApi.md#get_marketplace_app_ui_details) | **GET** /marketplace-app-ui-details | Get Marketplace App UI details.


# **get_marketplace_app_ui_details**
> get_marketplace_app_ui_details()

Get Marketplace App UI details.

Get the Marketplace App UI IP and Port.

### Example

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

app_instance_id = "appInstanceId_example" # str | Specifies marketplace app instance ID (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Marketplace App UI details.
	client.marketplace_app.get_marketplace_app_ui_details(app_instance_id=app_instance_id)
except ApiException as e:
	print("Exception when calling MarketplaceAppApi->get_marketplace_app_ui_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **str**| Specifies marketplace app instance ID | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * userPrivileges - Specifies all the privileges of the current user <br>  * userRoles - Specifies all the roles of the current user <br>  * appIp - Specifies the marketplace app UI IP <br>  * appPort - Specifies the marketplace app UI Port <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

