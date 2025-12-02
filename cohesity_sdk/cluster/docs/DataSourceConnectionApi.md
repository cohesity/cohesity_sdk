# cohesity_sdk.cluster.DataSourceConnectionApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_source_connection**](DataSourceConnectionApi.md#create_data_source_connection) | **POST** /data-source-connections | Create a data-source connection
[**delete_data_source_connection**](DataSourceConnectionApi.md#delete_data_source_connection) | **DELETE** /data-source-connections/{connectionId} | Delete the data-source connection specified by the ID in the request path.
[**generate_data_source_connection_registration_token**](DataSourceConnectionApi.md#generate_data_source_connection_registration_token) | **POST** /data-source-connections/{connectionId}/registrationToken | Generate registration token for a data-source connection
[**get_connections_upgrade_config**](DataSourceConnectionApi.md#get_connections_upgrade_config) | **GET** /data-source-connections/upgrade-config | Get upgrade connections config.
[**get_data_source_connection_connectivity_endpoints**](DataSourceConnectionApi.md#get_data_source_connection_connectivity_endpoints) | **GET** /data-source-connections/connectivity-endpoints | Returns connectivity endpoints for data-source connections
[**get_data_source_connections**](DataSourceConnectionApi.md#get_data_source_connections) | **GET** /data-source-connections | Get data-source connections
[**patch_data_source_connection**](DataSourceConnectionApi.md#patch_data_source_connection) | **PATCH** /data-source-connections/{connectionId} | Patch a data-source connection using its ID
[**reset_connection_upgrade**](DataSourceConnectionApi.md#reset_connection_upgrade) | **POST** /data-source-connections/{connectionId}/reset-upgrade | Resets the upgrade for a data-source connection
[**update_connections_upgrade_config**](DataSourceConnectionApi.md#update_connections_upgrade_config) | **PUT** /data-source-connections/upgrade-config | Config for upgrading connections.


# **create_data_source_connection**
> DataSourceConnection create_data_source_connection(body=body)

Create a data-source connection

**Privileges:** ```DATA_SOURCE_CONNECTION_MODIFY``` <br><br>Creates a data-source connection which can be used to register and protect sources, to access filer services, etc.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_data_source_connection_request import CreateDataSourceConnectionRequest
from cohesity_sdk.cluster.models.data_source_connection import DataSourceConnection
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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    body = cohesity_sdk.cluster.CreateDataSourceConnectionRequest() # CreateDataSourceConnectionRequest | Specifies the request parameters to create a connection. (optional)

    try:
        # Create a data-source connection
        api_response = api_instance.create_data_source_connection(body=body)
        print("The response of DataSourceConnectionApi->create_data_source_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->create_data_source_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDataSourceConnectionRequest**](CreateDataSourceConnectionRequest.md)| Specifies the request parameters to create a connection. | [optional] 

### Return type

[**DataSourceConnection**](DataSourceConnection.md)

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

# **delete_data_source_connection**
> delete_data_source_connection(connection_id)

Delete the data-source connection specified by the ID in the request path.

**Privileges:** ```DATA_SOURCE_CONNECTION_MODIFY``` <br><br>Delete a data-source connection using its ID. After deleting a connection, any connectors within it won't be able to connect to the cluster. A connection should only be deleted after ensuring that no sources are using it.

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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    connection_id = 'connection_id_example' # str | Specifies the unique ID of the connection which is to be deleted.

    try:
        # Delete the data-source connection specified by the ID in the request path.
        api_instance.delete_data_source_connection(connection_id)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->delete_data_source_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Specifies the unique ID of the connection which is to be deleted. | 

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

# **generate_data_source_connection_registration_token**
> str generate_data_source_connection_registration_token(connection_id)

Generate registration token for a data-source connection

**Privileges:** ```DATA_SOURCE_CONNECTION_MODIFY``` <br><br>Generate a token to register connectors against the data-source connection specified by the ID in the request path. The same token can be used to register multiple connectors as long as the token is valid. Once the token expires, typically in a day, this API can be hit again to generate another token.

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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    connection_id = 'connection_id_example' # str | Specifies the unique ID of the connection for which the registration token is to be fetched.

    try:
        # Generate registration token for a data-source connection
        api_response = api_instance.generate_data_source_connection_registration_token(connection_id)
        print("The response of DataSourceConnectionApi->generate_data_source_connection_registration_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->generate_data_source_connection_registration_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Specifies the unique ID of the connection for which the registration token is to be fetched. | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The registration token. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections_upgrade_config**
> UpgradeConfig get_connections_upgrade_config()

Get upgrade connections config.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get upgrade connections config.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.upgrade_config import UpgradeConfig
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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)

    try:
        # Get upgrade connections config.
        api_response = api_instance.get_connections_upgrade_config()
        print("The response of DataSourceConnectionApi->get_connections_upgrade_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->get_connections_upgrade_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UpgradeConfig**](UpgradeConfig.md)

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

# **get_data_source_connection_connectivity_endpoints**
> ConnectivityEndpointList get_data_source_connection_connectivity_endpoints(connection_id=connection_id)

Returns connectivity endpoints for data-source connections

**Privileges:** ```DATA_SOURCE_CONNECTION_VIEW``` <br><br>Returns the set of endpoints that a data-source connector, connected to the cluster using the connection needs connectivity to. If no port is specified for an endpoint then default HTTPS port is used.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.connectivity_endpoint_list import ConnectivityEndpointList
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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    connection_id = 'connection_id_example' # str | Specifies the unique ID of the connection for which connectivity endpoints are to be fetched. (optional)

    try:
        # Returns connectivity endpoints for data-source connections
        api_response = api_instance.get_data_source_connection_connectivity_endpoints(connection_id=connection_id)
        print("The response of DataSourceConnectionApi->get_data_source_connection_connectivity_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->get_data_source_connection_connectivity_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Specifies the unique ID of the connection for which connectivity endpoints are to be fetched. | [optional] 

### Return type

[**ConnectivityEndpointList**](ConnectivityEndpointList.md)

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

# **get_data_source_connections**
> DataSourceConnectionList get_data_source_connections(connection_ids=connection_ids, tenant_id=tenant_id, connection_names=connection_names)

Get data-source connections

**Privileges:** ```DATA_SOURCE_CONNECTION_VIEW, CLUSTER_VIEW``` <br><br>Gets all specified data-source connections.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.data_source_connection_list import DataSourceConnectionList
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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    connection_ids = ['connection_ids_example'] # List[str] | Specifies the unique IDs of the connections which are to be fetched. (optional)
    tenant_id = 'tenant_id_example' # str | Specifies the ID of the tenant for which the connections are to be fetched. (optional)
    connection_names = ['connection_names_example'] # List[str] | Specifies the names of the connections which are to be fetched. (optional)

    try:
        # Get data-source connections
        api_response = api_instance.get_data_source_connections(connection_ids=connection_ids, tenant_id=tenant_id, connection_names=connection_names)
        print("The response of DataSourceConnectionApi->get_data_source_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->get_data_source_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_ids** | [**List[str]**](str.md)| Specifies the unique IDs of the connections which are to be fetched. | [optional] 
 **tenant_id** | **str**| Specifies the ID of the tenant for which the connections are to be fetched. | [optional] 
 **connection_names** | [**List[str]**](str.md)| Specifies the names of the connections which are to be fetched. | [optional] 

### Return type

[**DataSourceConnectionList**](DataSourceConnectionList.md)

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

# **patch_data_source_connection**
> DataSourceConnection patch_data_source_connection(connection_id, body)

Patch a data-source connection using its ID

**Privileges:** ```DATA_SOURCE_CONNECTION_MODIFY``` <br><br>Patch the data-source connection specified by the ID in the request path.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.data_source_connection import DataSourceConnection
from cohesity_sdk.cluster.models.patch_data_source_connection_request import PatchDataSourceConnectionRequest
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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    connection_id = 'connection_id_example' # str | Specifies the unique ID of the connection which is to be patched.
    body = cohesity_sdk.cluster.PatchDataSourceConnectionRequest() # PatchDataSourceConnectionRequest | Specifies the connection resource with the properties that can be patched.

    try:
        # Patch a data-source connection using its ID
        api_response = api_instance.patch_data_source_connection(connection_id, body)
        print("The response of DataSourceConnectionApi->patch_data_source_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->patch_data_source_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Specifies the unique ID of the connection which is to be patched. | 
 **body** | [**PatchDataSourceConnectionRequest**](PatchDataSourceConnectionRequest.md)| Specifies the connection resource with the properties that can be patched. | 

### Return type

[**DataSourceConnection**](DataSourceConnection.md)

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

# **reset_connection_upgrade**
> reset_connection_upgrade(connection_id)

Resets the upgrade for a data-source connection

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Helps unblock upgrades for the connection if the current connector getting upgraded is not responding for upgrade status which can cause rest of the connectors to be blocked. This should generally be used when the issue has been fixed for the connector or the connector has been removed from the connection.

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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    connection_id = 'connection_id_example' # str | Specifies the ID of the connection for which upgrade has to be reset.

    try:
        # Resets the upgrade for a data-source connection
        api_instance.reset_connection_upgrade(connection_id)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->reset_connection_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Specifies the ID of the connection for which upgrade has to be reset. | 

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

# **update_connections_upgrade_config**
> UpgradeConfig update_connections_upgrade_config(body)

Config for upgrading connections.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates the upgrade configuration for the data source connections. This supports both upgrade and patch operations. Upgrade can be used to set the connector to the specified version whereas patch can be used to update a connector within the same version. Connectors within a connection would be upgraded or patched in a rolling manner. Specific operation status for a connection can be fetched using GET data-source-connection. If the connection is removed from the config after the upgrade or patch is issued internally by the system, the connection's operation status would not be updated for success or failure. Note that this is a config and action would be taken asynchronously at a later point in time, accordingly. Fields suffixed with UpgradePackageUrl must be used to upgrade connectors and those suffixed with PatchPackageUrl must be used to patch connectors.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.upgrade_config import UpgradeConfig
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
    api_instance = cohesity_sdk.cluster.DataSourceConnectionApi(api_client)
    body = cohesity_sdk.cluster.UpgradeConfig() # UpgradeConfig | Specifies the config to upgrade connections.

    try:
        # Config for upgrading connections.
        api_response = api_instance.update_connections_upgrade_config(body)
        print("The response of DataSourceConnectionApi->update_connections_upgrade_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceConnectionApi->update_connections_upgrade_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeConfig**](UpgradeConfig.md)| Specifies the config to upgrade connections. | 

### Return type

[**UpgradeConfig**](UpgradeConfig.md)

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

