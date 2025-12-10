# cohesity_sdk.cluster.DataSourceConnectorApi

All URIs are relative to */v2*

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.DataSourceConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | Specifies the unique ID of the connector which is to be deleted.

    try:
        # Delete a data-source connector using its ID
        api_instance.delete_data_source_connector(connector_id)
    except Exception as e:
        print("Exception when calling DataSourceConnectorApi->delete_data_source_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| Specifies the unique ID of the connector which is to be deleted. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.connector_metadata import ConnectorMetadata
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.DataSourceConnectorApi(api_client)

    try:
        api_response = api_instance.get_connector_metadata()
        print("The response of DataSourceConnectorApi->get_connector_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectorApi->get_connector_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConnectorMetadata**](ConnectorMetadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> DataSourceConnectorList get_data_source_connectors(connector_ids=connector_ids, connector_names=connector_names, tenant_id=tenant_id, connection_id=connection_id)

Get data-source connectors

**Privileges:** ```DATA_SOURCE_CONNECTOR_VIEW, CLUSTER_VIEW``` <br><br>Gets all specified data-source connectors.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.data_source_connector_list import DataSourceConnectorList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.DataSourceConnectorApi(api_client)
    connector_ids = ['connector_ids_example'] # List[str] | Specifies the unique IDs of the connectors which are to be fetched. (optional)
    connector_names = ['connector_names_example'] # List[str] | Specifies the names of the connectors which are to be fetched. (optional)
    tenant_id = 'tenant_id_example' # str | Specifies the ID of the tenant for which the connectors are to be fetched. (optional)
    connection_id = 'connection_id_example' # str | Specifies the ID of the connection, connectors belonging to which are to be fetched. (optional)

    try:
        # Get data-source connectors
        api_response = api_instance.get_data_source_connectors(connector_ids=connector_ids, connector_names=connector_names, tenant_id=tenant_id, connection_id=connection_id)
        print("The response of DataSourceConnectorApi->get_data_source_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectorApi->get_data_source_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_ids** | [**List[str]**](str.md)| Specifies the unique IDs of the connectors which are to be fetched. | [optional] 
 **connector_names** | [**List[str]**](str.md)| Specifies the names of the connectors which are to be fetched. | [optional] 
 **tenant_id** | **str**| Specifies the ID of the tenant for which the connectors are to be fetched. | [optional] 
 **connection_id** | **str**| Specifies the ID of the connection, connectors belonging to which are to be fetched. | [optional] 

### Return type

[**DataSourceConnectorList**](DataSourceConnectorList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.data_source_connector import DataSourceConnector
from cohesity_sdk.cluster.models.patch_data_source_connector_request import PatchDataSourceConnectorRequest
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.DataSourceConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | Specifies the unique ID of the connector which is to be patched.
    body = cohesity_sdk.cluster.PatchDataSourceConnectorRequest() # PatchDataSourceConnectorRequest | Specifies the properties of a data-source connector to patch.

    try:
        # Patch a data-source connector using its ID
        api_response = api_instance.patch_data_source_connector(connector_id, body)
        print("The response of DataSourceConnectorApi->patch_data_source_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectorApi->patch_data_source_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| Specifies the unique ID of the connector which is to be patched. | 
 **body** | [**PatchDataSourceConnectorRequest**](PatchDataSourceConnectorRequest.md)| Specifies the properties of a data-source connector to patch. | 

### Return type

[**DataSourceConnector**](DataSourceConnector.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.connector_metadata import ConnectorMetadata
from cohesity_sdk.cluster.models.create_or_update_connector_metadata_request import CreateOrUpdateConnectorMetadataRequest
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.DataSourceConnectorApi(api_client)
    body = cohesity_sdk.cluster.CreateOrUpdateConnectorMetadataRequest() # CreateOrUpdateConnectorMetadataRequest | Specifies information about the connectors.

    try:
        api_response = api_instance.update_connector_metadata(body)
        print("The response of DataSourceConnectorApi->update_connector_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectorApi->update_connector_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateConnectorMetadataRequest**](CreateOrUpdateConnectorMetadataRequest.md)| Specifies information about the connectors. | 

### Return type

[**ConnectorMetadata**](ConnectorMetadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

