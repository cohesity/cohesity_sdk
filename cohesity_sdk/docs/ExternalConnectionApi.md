# cohesity_sdk.ExternalConnectionApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bifrost_connection**](ExternalConnectionApi.md#create_bifrost_connection) | **POST** /connection-bifrost | Create a connection of Bifrost on the cluster.
[**create_rigel_connection**](ExternalConnectionApi.md#create_rigel_connection) | **POST** /connection-rigel | Create a connection of Rigel on the cluster.
[**delete_bifrost_connection**](ExternalConnectionApi.md#delete_bifrost_connection) | **DELETE** /connection-bifrost/{id} | Delete a connection of Bifrost.
[**delete_rigel_connection**](ExternalConnectionApi.md#delete_rigel_connection) | **DELETE** /connection-rigel/{id} | Delete a connection of Rigel.
[**get_bifrost_connection**](ExternalConnectionApi.md#get_bifrost_connection) | **GET** /connection-bifrost | Get connections of Bifrost on the cluster.
[**get_bifrost_connection_by_id**](ExternalConnectionApi.md#get_bifrost_connection_by_id) | **GET** /connection-bifrost/{id} | Get a connection of Bifrost by the id.
[**get_connection_bandwidth**](ExternalConnectionApi.md#get_connection_bandwidth) | **GET** /connection-rigel/{id}/bandwidth | List the upload and download bandwidth limits for a connection.
[**get_rigel_connection**](ExternalConnectionApi.md#get_rigel_connection) | **GET** /connection-rigel | Get connections of Rigel on the cluster.
[**get_rigel_connection_by_id**](ExternalConnectionApi.md#get_rigel_connection_by_id) | **GET** /connection-rigel/{id} | Get a connection of Rigel by the id.
[**update_bifrost_connection**](ExternalConnectionApi.md#update_bifrost_connection) | **PUT** /connection-bifrost/{id} | Update a connection of Bifrost.
[**update_connection_bandwidth**](ExternalConnectionApi.md#update_connection_bandwidth) | **PUT** /connection-rigel/{id}/bandwidth | Updates bandwidth limits for a connection.
[**update_rigel_connection**](ExternalConnectionApi.md#update_rigel_connection) | **PUT** /connection-rigel/{id} | Update a connection of Rigel.


# **create_bifrost_connection**
> BifrostConnection create_bifrost_connection(body)

Create a connection of Bifrost on the cluster.

Create a connection of Bifrost on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_bifrost_connection_request import CreateBifrostConnectionRequest
from cohesity_sdk.cluster.model.bifrost_connection import BifrostConnection
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateBifrostConnectionRequest(
        name="name_example",
    ) # CreateBifrostConnectionRequest | Specifies the parameters to create a connection.

# example passing only required values which don't have defaults set
try:
	# Create a connection of Bifrost on the cluster.
	api_response = client.external_connection.create_bifrost_connection(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->create_bifrost_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBifrostConnectionRequest**](CreateBifrostConnectionRequest.md)| Specifies the parameters to create a connection. |

### Return type

[**BifrostConnection**](BifrostConnection.md)

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

# **create_rigel_connection**
> RigelConnection create_rigel_connection(body)

Create a connection of Rigel on the cluster.

Create a connection of Rigel on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_rigel_connection_request import CreateRigelConnectionRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rigel_connection import RigelConnection
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateRigelConnectionRequest() # CreateRigelConnectionRequest | Specifies the parameters to create a connection.

# example passing only required values which don't have defaults set
try:
	# Create a connection of Rigel on the cluster.
	api_response = client.external_connection.create_rigel_connection(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->create_rigel_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRigelConnectionRequest**](CreateRigelConnectionRequest.md)| Specifies the parameters to create a connection. |

### Return type

[**RigelConnection**](RigelConnection.md)

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

# **delete_bifrost_connection**
> delete_bifrost_connection(id)

Delete a connection of Bifrost.

Delete a connection of Bifrost.

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


id = 1 # int, none_type | Specifies the id of a Bifrost connection.

# example passing only required values which don't have defaults set
try:
	# Delete a connection of Bifrost.
	client.external_connection.delete_bifrost_connection(id)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->delete_bifrost_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of a Bifrost connection. |

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

# **delete_rigel_connection**
> delete_rigel_connection(id)

Delete a connection of Rigel.

Delete a connection of Rigel.

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


id = 1 # int, none_type | Specifies the id of the Rigel connection.

# example passing only required values which don't have defaults set
try:
	# Delete a connection of Rigel.
	client.external_connection.delete_rigel_connection(id)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->delete_rigel_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of the Rigel connection. |

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

# **get_bifrost_connection**
> BifrostConnections get_bifrost_connection()

Get connections of Bifrost on the cluster.

Get connections of Bifrost on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.bifrost_connections import BifrostConnections
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int], none_type | Specifies the id of the connections. (optional)
tenant_id = "tenantId_example" # str, none_type | Specifies the id of the tenant which the connection belongs to. (optional)
names = [
        "names_example",
    ] # [str], none_type | Specifies the name of the connections. (optional)
default_connection_only = True # bool, none_type | Only return the default Bifrost connections (exactly one default connection is internally created for each Bifrost enabled tenant). (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get connections of Bifrost on the cluster.
	api_response = client.external_connection.get_bifrost_connection(ids=ids, tenant_id=tenant_id, names=names, default_connection_only=default_connection_only)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->get_bifrost_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int], none_type**| Specifies the id of the connections. | [optional]
 **tenant_id** | **str, none_type**| Specifies the id of the tenant which the connection belongs to. | [optional]
 **names** | **[str], none_type**| Specifies the name of the connections. | [optional]
 **default_connection_only** | **bool, none_type**| Only return the default Bifrost connections (exactly one default connection is internally created for each Bifrost enabled tenant). | [optional]

### Return type

[**BifrostConnections**](BifrostConnections.md)

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

# **get_bifrost_connection_by_id**
> BifrostConnection get_bifrost_connection_by_id(id)

Get a connection of Bifrost by the id.

Get a connection of Bifrost by the id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.bifrost_connection import BifrostConnection
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int, none_type | Specifies the id of the Bifrost connection.

# example passing only required values which don't have defaults set
try:
	# Get a connection of Bifrost by the id.
	api_response = client.external_connection.get_bifrost_connection_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->get_bifrost_connection_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of the Bifrost connection. |

### Return type

[**BifrostConnection**](BifrostConnection.md)

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

# **get_connection_bandwidth**
> GetConnectionBandwidthResponseBody get_connection_bandwidth(id)

List the upload and download bandwidth limits for a connection.

Returns the upload and download bandwidth limits for a connection.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.get_connection_bandwidth_response_body import GetConnectionBandwidthResponseBody
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int, none_type | Connection Id for which bandwidth settings are to be returned.
tenant_id = "tenantId_example" # str | TenantId corresponding to the connection. (optional)

# example passing only required values which don't have defaults set
try:
	# List the upload and download bandwidth limits for a connection.
	api_response = client.external_connection.get_connection_bandwidth(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->get_connection_bandwidth: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the upload and download bandwidth limits for a connection.
	api_response = client.external_connection.get_connection_bandwidth(id, tenant_id=tenant_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->get_connection_bandwidth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Connection Id for which bandwidth settings are to be returned. |
 **tenant_id** | **str**| TenantId corresponding to the connection. | [optional]

### Return type

[**GetConnectionBandwidthResponseBody**](GetConnectionBandwidthResponseBody.md)

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

# **get_rigel_connection**
> RigelConnections get_rigel_connection()

Get connections of Rigel on the cluster.

Get connections of Rigel on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rigel_connections import RigelConnections
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int], none_type | Specifies the id of the connections. (optional)
tenant_id = "tenantId_example" # str, none_type | Specifies the id of the tenant which the connection belongs to. (optional)
names = [
        "names_example",
    ] # [str], none_type | Specifies the name of the connection. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get connections of Rigel on the cluster.
	api_response = client.external_connection.get_rigel_connection(ids=ids, tenant_id=tenant_id, names=names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->get_rigel_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int], none_type**| Specifies the id of the connections. | [optional]
 **tenant_id** | **str, none_type**| Specifies the id of the tenant which the connection belongs to. | [optional]
 **names** | **[str], none_type**| Specifies the name of the connection. | [optional]

### Return type

[**RigelConnections**](RigelConnections.md)

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

# **get_rigel_connection_by_id**
> RigelConnection get_rigel_connection_by_id(id)

Get a connection of Rigel by the id.

Get a connection of Rigel by the id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rigel_connection import RigelConnection
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int, none_type | Specifies the id of the Rigel connection.

# example passing only required values which don't have defaults set
try:
	# Get a connection of Rigel by the id.
	api_response = client.external_connection.get_rigel_connection_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->get_rigel_connection_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of the Rigel connection. |

### Return type

[**RigelConnection**](RigelConnection.md)

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

# **update_bifrost_connection**
> BifrostConnection update_bifrost_connection(id, body)

Update a connection of Bifrost.

Update a connection of Bifrost.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.bifrost_connection import BifrostConnection
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_bifrost_connection_request import UpdateBifrostConnectionRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int, none_type | Specifies the id of a Bifrost connection.
body = UpdateBifrostConnectionRequest() # UpdateBifrostConnectionRequest | Specifies the parameters to update a connection.

# example passing only required values which don't have defaults set
try:
	# Update a connection of Bifrost.
	api_response = client.external_connection.update_bifrost_connection(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->update_bifrost_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of a Bifrost connection. |
 **body** | [**UpdateBifrostConnectionRequest**](UpdateBifrostConnectionRequest.md)| Specifies the parameters to update a connection. |

### Return type

[**BifrostConnection**](BifrostConnection.md)

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

# **update_connection_bandwidth**
> GetConnectionBandwidthResponseBody update_connection_bandwidth(id, body)

Updates bandwidth limits for a connection.

Returns the updated connection bandwidth limits.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.get_connection_bandwidth_response_body import GetConnectionBandwidthResponseBody
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.connection_bandwidth_limits import ConnectionBandwidthLimits
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int, none_type | Connection Id for which bandwidth settings are to be returned
body = ConnectionBandwidthLimits(
        download=[
            BandwidthLimit(
                bytes_per_second=1,
                time_periods=TimeOfAWeek(
                    days=[
                        "Sunday",
                    ],
                    start_time=TimeOfDay(
                        hour=0,
                        minute=0,
                        time_zone="America/Los_Angeles",
                    ),
                    end_time=TimeOfDay(
                        hour=0,
                        minute=0,
                        time_zone="America/Los_Angeles",
                    ),
                    is_all_day=True,
                ),
            ),
        ],
        upload=[
            BandwidthLimit(
                bytes_per_second=1,
                time_periods=TimeOfAWeek(
                    days=[
                        "Sunday",
                    ],
                    start_time=TimeOfDay(
                        hour=0,
                        minute=0,
                        time_zone="America/Los_Angeles",
                    ),
                    end_time=TimeOfDay(
                        hour=0,
                        minute=0,
                        time_zone="America/Los_Angeles",
                    ),
                    is_all_day=True,
                ),
            ),
        ],
        tenant_id="tenant_id_example",
        timezone="timezone_example",
        connector_group_id=1,
    ) # ConnectionBandwidthLimits | Request to update connection bandwidth limits settings.

# example passing only required values which don't have defaults set
try:
	# Updates bandwidth limits for a connection.
	api_response = client.external_connection.update_connection_bandwidth(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->update_connection_bandwidth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Connection Id for which bandwidth settings are to be returned |
 **body** | [**ConnectionBandwidthLimits**](ConnectionBandwidthLimits.md)| Request to update connection bandwidth limits settings. |

### Return type

[**GetConnectionBandwidthResponseBody**](GetConnectionBandwidthResponseBody.md)

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

# **update_rigel_connection**
> RigelConnection update_rigel_connection(id, body)

Update a connection of Rigel.

Update a connection of Rigel.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_rigel_connection_request import UpdateRigelConnectionRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rigel_connection import RigelConnection
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int, none_type | Specifies the id of the Rigel connection.
body = UpdateRigelConnectionRequest() # UpdateRigelConnectionRequest | Specifies the parameters to update the connection.

# example passing only required values which don't have defaults set
try:
	# Update a connection of Rigel.
	api_response = client.external_connection.update_rigel_connection(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalConnectionApi->update_rigel_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of the Rigel connection. |
 **body** | [**UpdateRigelConnectionRequest**](UpdateRigelConnectionRequest.md)| Specifies the parameters to update the connection. |

### Return type

[**RigelConnection**](RigelConnection.md)

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

