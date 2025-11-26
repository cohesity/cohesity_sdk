# cohesity_sdk.RoutesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_static_route**](RoutesApi.md#add_static_route) | **POST** /network/routes | Configure a static route


# **add_static_route**
> StaticRouteParams add_static_route(body)

Configure a static route

Configure a static route on an interface.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.static_route_params import StaticRouteParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = StaticRouteParams(
        description="description_example",
        destination_network="destination_network_example",
        interface="interface_example",
        interface_group="interface_group_example",
        mtu=1,
        next_hop="next_hop_example",
        node_group_name="node_group_name_example",
    ) # StaticRouteParams | Specifies the parameters to configure a static route on an interface.

# example passing only required values which don't have defaults set
try:
	# Configure a static route
	api_response = client.routes.add_static_route(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RoutesApi->add_static_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StaticRouteParams**](StaticRouteParams.md)| Specifies the parameters to configure a static route on an interface. |

### Return type

[**StaticRouteParams**](StaticRouteParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

