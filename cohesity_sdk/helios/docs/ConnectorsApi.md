# cohesity_sdk.ConnectorsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bifrost_connector**](ConnectorsApi.md#create_bifrost_connector) | **POST** /connector-hybrid-extender | Create a Bifrost connector on the cluster.
[**create_rigel_connector**](ConnectorsApi.md#create_rigel_connector) | **POST** /connector-rigel | Create a Rigel connector on the cluster.
[**delete_bifrost_connector**](ConnectorsApi.md#delete_bifrost_connector) | **DELETE** /connector-hybrid-extender/{id} | Delete a Bifrost connector.
[**delete_rigel_connector**](ConnectorsApi.md#delete_rigel_connector) | **DELETE** /connector-rigel/{id} | Delete a Rigel connector.
[**get_bifrost_connector**](ConnectorsApi.md#get_bifrost_connector) | **GET** /connector-hybrid-extender | Get Bifrost connectors on the cluster.
[**get_bifrost_connector_by_id**](ConnectorsApi.md#get_bifrost_connector_by_id) | **GET** /connector-hybrid-extender/{id} | Get a Bifrost connector by the id.
[**get_rigel_connector**](ConnectorsApi.md#get_rigel_connector) | **GET** /connector-rigel | Get Rigel connectors on the cluster.
[**get_rigel_connector_by_id**](ConnectorsApi.md#get_rigel_connector_by_id) | **GET** /connector-rigel/{id} | Get a Rigel connector by the id.
[**update_bifrost_connector**](ConnectorsApi.md#update_bifrost_connector) | **PUT** /connector-hybrid-extender/{id} | Update a Bifrost connector.
[**update_rigel_connector**](ConnectorsApi.md#update_rigel_connector) | **PUT** /connector-rigel/{id} | Update a Rigel connector.


# **create_bifrost_connector**
> BifrostConnector create_bifrost_connector(body)

Create a Bifrost connector on the cluster.

Create a Bifrost connector on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_bifrost_connector_request import CreateOrUpdateBifrostConnectorRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.bifrost_connector import BifrostConnector
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateOrUpdateBifrostConnectorRequest(
        connection_id=1,
        tenant_id="tenant_id_example",
        name="name_example",
    ) # CreateOrUpdateBifrostConnectorRequest | Specifies the parameters to create a connector.

# example passing only required values which don't have defaults set
try:
	# Create a Bifrost connector on the cluster.
	api_response = client.connectors.create_bifrost_connector(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->create_bifrost_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateBifrostConnectorRequest**](CreateOrUpdateBifrostConnectorRequest.md)| Specifies the parameters to create a connector. |

### Return type

[**BifrostConnector**](BifrostConnector.md)

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

# **create_rigel_connector**
> RigelConnector create_rigel_connector(body)

Create a Rigel connector on the cluster.

Create a Rigel connector on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.rigel_connector import RigelConnector
from cohesity_sdk.helios.model.create_rigel_connector_request import CreateRigelConnectorRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateRigelConnectorRequest() # CreateRigelConnectorRequest | Specifies the parameters to create a connector.

# example passing only required values which don't have defaults set
try:
	# Create a Rigel connector on the cluster.
	api_response = client.connectors.create_rigel_connector(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->create_rigel_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRigelConnectorRequest**](CreateRigelConnectorRequest.md)| Specifies the parameters to create a connector. |

### Return type

[**RigelConnector**](RigelConnector.md)

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

# **delete_bifrost_connector**
> delete_bifrost_connector(id)

Delete a Bifrost connector.

Delete a Bifrost connector.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int, none_type | Specifies the id of connector.

# example passing only required values which don't have defaults set
try:
	# Delete a Bifrost connector.
	client.connectors.delete_bifrost_connector(id)
except ApiException as e:
	print("Exception when calling ConnectorsApi->delete_bifrost_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of connector. |

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

# **delete_rigel_connector**
> delete_rigel_connector(id, body)

Delete a Rigel connector.

Delete a Rigel connector.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.delete_rigel_connector_request import DeleteRigelConnectorRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int, none_type | Specifies the id of connector.
body = DeleteRigelConnectorRequest(
        tenant_id="tenant_id_example",
    ) # DeleteRigelConnectorRequest | Specifies the parameters to delete a connector.

# example passing only required values which don't have defaults set
try:
	# Delete a Rigel connector.
	client.connectors.delete_rigel_connector(id, body)
except ApiException as e:
	print("Exception when calling ConnectorsApi->delete_rigel_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of connector. |
 **body** | [**DeleteRigelConnectorRequest**](DeleteRigelConnectorRequest.md)| Specifies the parameters to delete a connector. |

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bifrost_connector**
> BifrostConnectors get_bifrost_connector()

Get Bifrost connectors on the cluster.

Get Bifrost connectors on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.bifrost_connectors import BifrostConnectors
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


ids = [
        1,
    ] # [int], none_type | Specifies the id of the connectors. (optional)
names = [
        "names_example",
    ] # [str], none_type | Specifies the name of the connectors. (optional)
tenant_id = "tenantId_example" # str, none_type | Specifies the id of the tenant which the connector belongs to. (optional)
connection_id = 1 # int, none_type | Specifies the Id of the connection which the connector belongs to. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Bifrost connectors on the cluster.
	api_response = client.connectors.get_bifrost_connector(ids=ids, names=names, tenant_id=tenant_id, connection_id=connection_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->get_bifrost_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int], none_type**| Specifies the id of the connectors. | [optional]
 **names** | **[str], none_type**| Specifies the name of the connectors. | [optional]
 **tenant_id** | **str, none_type**| Specifies the id of the tenant which the connector belongs to. | [optional]
 **connection_id** | **int, none_type**| Specifies the Id of the connection which the connector belongs to. | [optional]

### Return type

[**BifrostConnectors**](BifrostConnectors.md)

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

# **get_bifrost_connector_by_id**
> BifrostConnector get_bifrost_connector_by_id(id)

Get a Bifrost connector by the id.

Get a Bifrost connector by the id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.bifrost_connector import BifrostConnector
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int, none_type | Specifies the id of connector.
tenant_id = "tenantId_example" # str, none_type | Specifies the id of the tenant which the connector belongs to. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a Bifrost connector by the id.
	api_response = client.connectors.get_bifrost_connector_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->get_bifrost_connector_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a Bifrost connector by the id.
	api_response = client.connectors.get_bifrost_connector_by_id(id, tenant_id=tenant_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->get_bifrost_connector_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of connector. |
 **tenant_id** | **str, none_type**| Specifies the id of the tenant which the connector belongs to. | [optional]

### Return type

[**BifrostConnector**](BifrostConnector.md)

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

# **get_rigel_connector**
> RigelConnectors get_rigel_connector()

Get Rigel connectors on the cluster.

Get Rigel connectors on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.rigel_connectors import RigelConnectors
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


ids = [
        1,
    ] # [int], none_type | Specifies the id of the connector. (optional)
names = [
        "names_example",
    ] # [str], none_type | Specifies the name of the connectors. (optional)
tenant_id = "tenantId_example" # str, none_type | Specifies the id of the tenant which the connector belongs to. (optional)
connection_id = 1 # int, none_type | Specifies the Id of the connection which the connector belongs to. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Rigel connectors on the cluster.
	api_response = client.connectors.get_rigel_connector(ids=ids, names=names, tenant_id=tenant_id, connection_id=connection_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->get_rigel_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int], none_type**| Specifies the id of the connector. | [optional]
 **names** | **[str], none_type**| Specifies the name of the connectors. | [optional]
 **tenant_id** | **str, none_type**| Specifies the id of the tenant which the connector belongs to. | [optional]
 **connection_id** | **int, none_type**| Specifies the Id of the connection which the connector belongs to. | [optional]

### Return type

[**RigelConnectors**](RigelConnectors.md)

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

# **get_rigel_connector_by_id**
> RigelConnector get_rigel_connector_by_id(id)

Get a Rigel connector by the id.

Get a Rigel connector by the id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.rigel_connector import RigelConnector
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int, none_type | Specifies the id of connector.
tenant_id = "tenantId_example" # str, none_type | Specifies the id of the tenant which the connector belongs to. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a Rigel connector by the id.
	api_response = client.connectors.get_rigel_connector_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->get_rigel_connector_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a Rigel connector by the id.
	api_response = client.connectors.get_rigel_connector_by_id(id, tenant_id=tenant_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->get_rigel_connector_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of connector. |
 **tenant_id** | **str, none_type**| Specifies the id of the tenant which the connector belongs to. | [optional]

### Return type

[**RigelConnector**](RigelConnector.md)

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

# **update_bifrost_connector**
> BifrostConnector update_bifrost_connector(id, body)

Update a Bifrost connector.

Update a Bifrost connector.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_bifrost_connector_request import CreateOrUpdateBifrostConnectorRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.bifrost_connector import BifrostConnector
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int, none_type | Specifies the id of connector.
body = CreateOrUpdateBifrostConnectorRequest(
        connection_id=1,
        tenant_id="tenant_id_example",
        name="name_example",
    ) # CreateOrUpdateBifrostConnectorRequest | Specifies the parameters to update a connector.

# example passing only required values which don't have defaults set
try:
	# Update a Bifrost connector.
	api_response = client.connectors.update_bifrost_connector(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->update_bifrost_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of connector. |
 **body** | [**CreateOrUpdateBifrostConnectorRequest**](CreateOrUpdateBifrostConnectorRequest.md)| Specifies the parameters to update a connector. |

### Return type

[**BifrostConnector**](BifrostConnector.md)

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

# **update_rigel_connector**
> RigelConnector update_rigel_connector(id, body)

Update a Rigel connector.

Update a Rigel connector.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_rigel_connector_request import UpdateRigelConnectorRequest
from cohesity_sdk.helios.model.rigel_connector import RigelConnector
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int, none_type | Specifies the id of connector.
body = UpdateRigelConnectorRequest() # UpdateRigelConnectorRequest | Specifies the parameters to update a connector.

# example passing only required values which don't have defaults set
try:
	# Update a Rigel connector.
	api_response = client.connectors.update_rigel_connector(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ConnectorsApi->update_rigel_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int, none_type**| Specifies the id of connector. |
 **body** | [**UpdateRigelConnectorRequest**](UpdateRigelConnectorRequest.md)| Specifies the parameters to update a connector. |

### Return type

[**RigelConnector**](RigelConnector.md)

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

