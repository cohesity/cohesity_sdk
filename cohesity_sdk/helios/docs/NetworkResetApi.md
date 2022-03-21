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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.reset_states import ResetStates
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List of nodes reset states.
	api_response = client.network_reset.get_network_reset_states(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkResetApi->get_network_reset_states: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.reset_or_restore_networking import ResetOrRestoreNetworking
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ResetOrRestoreNetworking(
        operation="network-reset",
    ) # ResetOrRestoreNetworking | Request to reset or restore cluster networking.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Set or cancel cluster reset state. This is destructive operation.
	client.network_reset.reset_nodes_network(body)
except ApiException as e:
	print("Exception when calling NetworkResetApi->reset_nodes_network: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Set or cancel cluster reset state. This is destructive operation.
	client.network_reset.reset_nodes_network(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling NetworkResetApi->reset_nodes_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetOrRestoreNetworking**](ResetOrRestoreNetworking.md)| Request to reset or restore cluster networking. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
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
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

