# cohesity_sdk.DataSourceConnectorApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_data_source_connector**](DataSourceConnectorApi.md#delete_data_source_connector) | **DELETE** /data-source-connectors/{connectorId} | Delete a data-source connector using its ID
[**get_connector_metadata**](DataSourceConnectorApi.md#get_connector_metadata) | **GET** /data-source-connectors/metadata | 
[**get_data_source_connectors**](DataSourceConnectorApi.md#get_data_source_connectors) | **GET** /data-source-connectors | Get data-source connectors
[**patch_data_source_connector**](DataSourceConnectorApi.md#patch_data_source_connector) | **PATCH** /data-source-connectors/{connectorId} | Patch a data-source connector using its ID
[**update_connector_metadata**](DataSourceConnectorApi.md#update_connector_metadata) | **PUT** /data-source-connectors/metadata | 


# **delete_data_source_connector**
> delete_data_source_connector(connector_id)

Delete a data-source connector using its ID

**Privileges:** ```DATA_SOURCE_CONNECTOR_MODIFY``` <br><br>Delete the data-source connector specified by the ID in the request path.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


connector_id = "connectorId_example" # str | Specifies the unique ID of the connector which is to be deleted.

# example passing only required values which don't have defaults set
try:
	# Delete a data-source connector using its ID
	client.data_source_connector.delete_data_source_connector(connector_id)
except ApiException as e:
	print("Exception when calling DataSourceConnectorApi->delete_data_source_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| Specifies the unique ID of the connector which is to be deleted. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_metadata**
> ConnectorMetadata get_connector_metadata()



**Privileges:** ```DATA_SOURCE_CONNECTION_VIEW, CLUSTER_VIEW``` <br><br>Get information about the available connectors.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.connector_metadata import ConnectorMetadata
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	api_response = client.data_source_connector.get_connector_metadata()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataSourceConnectorApi->get_connector_metadata: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectorMetadata**](ConnectorMetadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_connectors**
> DataSourceConnectorList get_data_source_connectors()

Get data-source connectors

**Privileges:** ```DATA_SOURCE_CONNECTOR_VIEW, CLUSTER_VIEW``` <br><br>Gets all specified data-source connectors.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.data_source_connector_list import DataSourceConnectorList
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


connector_ids = [
        "connectorIds_example",
    ] # [str], none_type | Specifies the unique IDs of the connectors which are to be fetched. (optional)
connector_names = [
        "connectorNames_example",
    ] # [str], none_type | Specifies the names of the connectors which are to be fetched. (optional)
tenant_id = "tenantId_example" # str, none_type | Specifies the ID of the tenant for which the connectors are to be fetched. (optional)
connection_id = "connectionId_example" # str, none_type | Specifies the ID of the connection, connectors belonging to which are to be fetched. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get data-source connectors
	api_response = client.data_source_connector.get_data_source_connectors(connector_ids=connector_ids, connector_names=connector_names, tenant_id=tenant_id, connection_id=connection_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataSourceConnectorApi->get_data_source_connectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_ids** | **[str], none_type**| Specifies the unique IDs of the connectors which are to be fetched. | [optional]
 **connector_names** | **[str], none_type**| Specifies the names of the connectors which are to be fetched. | [optional]
 **tenant_id** | **str, none_type**| Specifies the ID of the tenant for which the connectors are to be fetched. | [optional]
 **connection_id** | **str, none_type**| Specifies the ID of the connection, connectors belonging to which are to be fetched. | [optional]

### Return type

[**DataSourceConnectorList**](DataSourceConnectorList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_data_source_connector**
> DataSourceConnector patch_data_source_connector(connector_id, body)

Patch a data-source connector using its ID

**Privileges:** ```DATA_SOURCE_CONNECTOR_MODIFY``` <br><br>Patch the data-source connector specified by the ID in the request path.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.data_source_connector import DataSourceConnector
from cohesity_sdk.cluster.model.patch_data_source_connector_request import PatchDataSourceConnectorRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


connector_id = "connectorId_example" # str, none_type | Specifies the unique ID of the connector which is to be patched.
body = PatchDataSourceConnectorRequest(
        connector_name="connector_name_example",
    ) # PatchDataSourceConnectorRequest | Specifies the properties of a data-source connector to patch.

# example passing only required values which don't have defaults set
try:
	# Patch a data-source connector using its ID
	api_response = client.data_source_connector.patch_data_source_connector(connector_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataSourceConnectorApi->patch_data_source_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str, none_type**| Specifies the unique ID of the connector which is to be patched. |
 **body** | [**PatchDataSourceConnectorRequest**](PatchDataSourceConnectorRequest.md)| Specifies the properties of a data-source connector to patch. |

### Return type

[**DataSourceConnector**](DataSourceConnector.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector_metadata**
> ConnectorMetadata update_connector_metadata(body)



**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update information about the available connectors.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_or_update_connector_metadata_request import CreateOrUpdateConnectorMetadataRequest
from cohesity_sdk.cluster.model.connector_metadata import ConnectorMetadata
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateOrUpdateConnectorMetadataRequest(
        connector_metadata=ConnectorMetadata(
            connector_image_metadata=ConnectorImageMetadata(
                connector_image_file_list=[
                    ConnectorImageFile(
                        image_type="VSI",
                        url="url_example",
                    ),
                ],
            ),
        ),
    ) # CreateOrUpdateConnectorMetadataRequest | Specifies information about the connectors.

# example passing only required values which don't have defaults set
try:
	api_response = client.data_source_connector.update_connector_metadata(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataSourceConnectorApi->update_connector_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateConnectorMetadataRequest**](CreateOrUpdateConnectorMetadataRequest.md)| Specifies information about the connectors. |

### Return type

[**ConnectorMetadata**](ConnectorMetadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

