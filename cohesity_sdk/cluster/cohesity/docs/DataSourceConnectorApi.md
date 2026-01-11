# cohesity_sdk.cluster.DataSourceConnectorApi

All URIs are relative to *http://localhost/v2*

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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import data_source_connector
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_source_connector.DataSourceConnectorApi(api_client)
    connector_id = "connectorId_example" # str | Specifies the unique ID of the connector which is to be deleted.

    # example passing only required values which don't have defaults set
    try:
        # Delete a data-source connector using its ID
        api_instance.delete_data_source_connector(connector_id)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import data_source_connector
from cohesity_sdk.cluster.cohesity.model.connector_metadata import ConnectorMetadata
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_source_connector.DataSourceConnectorApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_connector_metadata()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import data_source_connector
from cohesity_sdk.cluster.cohesity.model.data_source_connector_list import DataSourceConnectorList
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_source_connector.DataSourceConnectorApi(api_client)
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
        api_response = api_instance.get_data_source_connectors(connector_ids=connector_ids, connector_names=connector_names, tenant_id=tenant_id, connection_id=connection_id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import data_source_connector
from cohesity_sdk.cluster.cohesity.model.data_source_connector import DataSourceConnector
from cohesity_sdk.cluster.cohesity.model.patch_data_source_connector_request import PatchDataSourceConnectorRequest
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_source_connector.DataSourceConnectorApi(api_client)
    connector_id = "connectorId_example" # str, none_type | Specifies the unique ID of the connector which is to be patched.
    body = PatchDataSourceConnectorRequest(
        connector_name="connector_name_example",
    ) # PatchDataSourceConnectorRequest | Specifies the properties of a data-source connector to patch.

    # example passing only required values which don't have defaults set
    try:
        # Patch a data-source connector using its ID
        api_response = api_instance.patch_data_source_connector(connector_id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import data_source_connector
from cohesity_sdk.cluster.cohesity.model.connector_metadata import ConnectorMetadata
from cohesity_sdk.cluster.cohesity.model.create_or_update_connector_metadata_request import CreateOrUpdateConnectorMetadataRequest
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_source_connector.DataSourceConnectorApi(api_client)
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
        api_response = api_instance.update_connector_metadata(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

