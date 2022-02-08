# cohesity_sdk.NetworkResetApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_reset_states**](NetworkResetApi.md#get_network_reset_states) | **GET** /networkReset/status | List of nodes reset states.
[**reset_nodes_network**](NetworkResetApi.md#reset_nodes_network) | **POST** /networkReset | Set or cancel cluster reset state. This is destructive operation.


# **get_network_reset_states**
> ResetStates get_network_reset_states()

List of nodes reset states.

Get networking reset state status.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.reset_states import ResetStates
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# List of nodes reset states.
	api_response = client.network_reset.get_network_reset_states()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkResetApi->get_network_reset_states: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResetStates**](ResetStates.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_nodes_network**
> reset_nodes_network(body)

Set or cancel cluster reset state. This is destructive operation.

This is destructive operation. Reset nodes' networking in cluster to factory state or cancel the reset operation.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.reset_or_restore_networking import ResetOrRestoreNetworking
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ResetOrRestoreNetworking(
        operation="network-reset",
    ) # ResetOrRestoreNetworking | Request to reset or restore cluster networking.

# example passing only required values which don't have defaults set
try:
	# Set or cancel cluster reset state. This is destructive operation.
	client.network_reset.reset_nodes_network(body)
except ApiException as e:
	print("Exception when calling NetworkResetApi->reset_nodes_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetOrRestoreNetworking**](ResetOrRestoreNetworking.md)| Request to reset or restore cluster networking. |

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
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

