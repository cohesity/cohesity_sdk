# cohesity_sdk.ExternalConnectionApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bifrost_connection**](ExternalConnectionApi.md#create_bifrost_connection) | **POST** /connection-bifrost | Create a connection of Bifrost on the cluster.
[**create_rigel_connection**](ExternalConnectionApi.md#create_rigel_connection) | **POST** /connection-rigel | Create a connection of Rigel on the cluster.
[**delete_bifrost_connection**](ExternalConnectionApi.md#delete_bifrost_connection) | **DELETE** /connection-bifrost/{id} | Delete a connection of Bifrost.
[**delete_rigel_connection**](ExternalConnectionApi.md#delete_rigel_connection) | **DELETE** /connection-rigel/{id} | Delete a connection of Rigel.
[**get_bifrost_connection**](ExternalConnectionApi.md#get_bifrost_connection) | **GET** /connection-bifrost | Get connections of Bifrost on the cluster.
[**get_bifrost_connection_by_id**](ExternalConnectionApi.md#get_bifrost_connection_by_id) | **GET** /connection-bifrost/{id} | Get a connection of Bifrost by the id.
[**get_rigel_connection**](ExternalConnectionApi.md#get_rigel_connection) | **GET** /connection-rigel | Get connections of Rigel on the cluster.
[**get_rigel_connection_by_id**](ExternalConnectionApi.md#get_rigel_connection_by_id) | **GET** /connection-rigel/{id} | Get a connection of Rigel by the id.
[**update_bifrost_connection**](ExternalConnectionApi.md#update_bifrost_connection) | **PUT** /connection-bifrost/{id} | Update a connection of Bifrost.
[**update_rigel_connection**](ExternalConnectionApi.md#update_rigel_connection) | **PUT** /connection-rigel/{id} | Update a connection of Rigel.


# **create_bifrost_connection**
> BifrostConnection create_bifrost_connection(body)

Create a connection of Bifrost on the cluster.

Create a connection of Bifrost on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.bifrost_connection import BifrostConnection
from cohesity_sdk.cohesity_client_v2.model.create_or_update_bifrost_connection_request import CreateOrUpdateBifrostConnectionRequest
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateOrUpdateBifrostConnectionRequest(
        tenant_id="tenant_id_example",
        name="name_example",
        subnet=ConnectionSubnet(
            ip="ip_example",
            mask_bits=1,
        ),
        certificate_version=1,
    ) # CreateOrUpdateBifrostConnectionRequest | Specifies the parameters to create a connection.

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
 **body** | [**CreateOrUpdateBifrostConnectionRequest**](CreateOrUpdateBifrostConnectionRequest.md)| Specifies the parameters to create a connection. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.rigel_connection import RigelConnection
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.create_rigel_connection_request import CreateRigelConnectionRequest
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.bifrost_connections import BifrostConnections
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get connections of Bifrost on the cluster.
	api_response = client.external_connection.get_bifrost_connection(ids=ids, tenant_id=tenant_id, names=names)
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.bifrost_connection import BifrostConnection
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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

# **get_rigel_connection**
> RigelConnections get_rigel_connection()

Get connections of Rigel on the cluster.

Get connections of Rigel on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.rigel_connections import RigelConnections
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.rigel_connection import RigelConnection
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.bifrost_connection import BifrostConnection
from cohesity_sdk.cohesity_client_v2.model.create_or_update_bifrost_connection_request import CreateOrUpdateBifrostConnectionRequest
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int, none_type | Specifies the id of a Bifrost connection.
body = CreateOrUpdateBifrostConnectionRequest(
        tenant_id="tenant_id_example",
        name="name_example",
        subnet=ConnectionSubnet(
            ip="ip_example",
            mask_bits=1,
        ),
        certificate_version=1,
    ) # CreateOrUpdateBifrostConnectionRequest | Specifies the parameters to update a connection.

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
 **body** | [**CreateOrUpdateBifrostConnectionRequest**](CreateOrUpdateBifrostConnectionRequest.md)| Specifies the parameters to update a connection. |

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

# **update_rigel_connection**
> RigelConnection update_rigel_connection(id, body)

Update a connection of Rigel.

Update a connection of Rigel.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.rigel_connection import RigelConnection
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.update_rigel_connection_request import UpdateRigelConnectionRequest
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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

