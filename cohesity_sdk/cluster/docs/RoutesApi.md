# cohesity_sdk.RoutesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_static_route**](RoutesApi.md#add_static_route) | **POST** /network/routes | Configure a static route
[**delete_static_route**](RoutesApi.md#delete_static_route) | **DELETE** /network/routes/{routeId} | Delete a static route
[**list_static_routes**](RoutesApi.md#list_static_routes) | **GET** /network/routes | List all static routes
[**update_static_route**](RoutesApi.md#update_static_route) | **PUT** /network/routes/{routeId} | Update a static route


# **add_static_route**
> StaticRouteParams add_static_route(body)

Configure a static route

Configure a static route on an interface.

### Example

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_static_route**
> delete_static_route(route_id)

Delete a static route

Delete a static route on a network interface.

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

route_id = "routeId_example" # str | Specify the unique identifier for the route.

# example passing only required values which don't have defaults set
try:
	# Delete a static route
	client.routes.delete_static_route(route_id)
except ApiException as e:
	print("Exception when calling RoutesApi->delete_static_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**| Specify the unique identifier for the route. |

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_static_routes**
> StaticRoutes list_static_routes()

List all static routes

List the static routes for the Cohesity Cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.static_routes import StaticRoutes
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

interface_groups = [
        "interfaceGroups_example",
    ] # [str] | Specifies the network interfaces name to filter. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List all static routes
	api_response = client.routes.list_static_routes(interface_groups=interface_groups)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RoutesApi->list_static_routes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_groups** | **[str]**| Specifies the network interfaces name to filter. | [optional]

### Return type

[**StaticRoutes**](StaticRoutes.md)

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

# **update_static_route**
> StaticRouteParams update_static_route(route_id, body)

Update a static route

Update static route details.

### Example

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

route_id = "routeId_example" # str | Specify the unique identifier for the route.
body = StaticRouteParams(
        description="description_example",
        destination_network="destination_network_example",
        interface="interface_example",
        interface_group="interface_group_example",
        mtu=1,
        next_hop="next_hop_example",
        node_group_name="node_group_name_example",
    ) # StaticRouteParams | Specifies the update request parameters.

# example passing only required values which don't have defaults set
try:
	# Update a static route
	api_response = client.routes.update_static_route(route_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RoutesApi->update_static_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**| Specify the unique identifier for the route. |
 **body** | [**StaticRouteParams**](StaticRouteParams.md)| Specifies the update request parameters. |

### Return type

[**StaticRouteParams**](StaticRouteParams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

