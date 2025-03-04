# cohesity_sdk.RemoteClustersApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_remote_cluster**](RemoteClustersApi.md#delete_remote_cluster) | **DELETE** /remote-clusters/{clusterId} | Unregister a Remote Cluster.
[**get_remote_cluster_by_id**](RemoteClustersApi.md#get_remote_cluster_by_id) | **GET** /remote-clusters/{clusterId} | Get Remote Cluster config by id.
[**get_remote_clusters**](RemoteClustersApi.md#get_remote_clusters) | **GET** /remote-clusters | Get all registered Remote Clusters.
[**register_remote_cluster**](RemoteClustersApi.md#register_remote_cluster) | **POST** /remote-clusters | Register a Remote Cluster.
[**update_remote_cluster**](RemoteClustersApi.md#update_remote_cluster) | **PUT** /remote-clusters/{clusterId} | Update a Remote Cluster config.
[**validate_remote_cluster**](RemoteClustersApi.md#validate_remote_cluster) | **POST** /remote-clusters/validate | Validate Remote Cluster config.


# **delete_remote_cluster**
> delete_remote_cluster(cluster_id)

Unregister a Remote Cluster.

Unregister an external Remote Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteClustersApi(api_client)
    cluster_id = 56 # int | Specifies the cluster id of the Remote Cluster to unregister.

    try:
        # Unregister a Remote Cluster.
        api_instance.delete_remote_cluster(cluster_id)
    except Exception as e:
        print("Exception when calling RemoteClustersApi->delete_remote_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Remote Cluster to unregister. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_cluster_by_id**
> UpdateRemoteClusterParams get_remote_cluster_by_id(cluster_id)

Get Remote Cluster config by id.

Get Remote Cluster config by cluster id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.update_remote_cluster_params import UpdateRemoteClusterParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteClustersApi(api_client)
    cluster_id = 56 # int | Specifies the cluster id of Remote Cluster to fetch.

    try:
        # Get Remote Cluster config by id.
        api_response = api_instance.get_remote_cluster_by_id(cluster_id)
        print("The response of RemoteClustersApi->get_remote_cluster_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteClustersApi->get_remote_cluster_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of Remote Cluster to fetch. | 

### Return type

[**UpdateRemoteClusterParams**](UpdateRemoteClusterParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_clusters**
> RemoteClusters get_remote_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names, node_addresses=node_addresses, purpose=purpose, include_encrypted_credentials=include_encrypted_credentials)

Get all registered Remote Clusters.

List the Remote Clusters that are registered on this local Cluster and that matches the filter criteria specified using parameters.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.remote_clusters import RemoteClusters
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteClustersApi(api_client)
    cluster_ids = [56] # List[int] | Specifies a list of Remote Cluster ids to filter. (optional)
    cluster_names = ['cluster_names_example'] # List[str] | Specifies a list of Remote Cluster names to filter. (optional)
    node_addresses = ['node_addresses_example'] # List[str] | Specifies a list of Remote Cluster IPs to filter. (optional)
    purpose = ['purpose_example'] # List[str] | Specifies the purpose for which the remote cluster is being registered. (optional)
    include_encrypted_credentials = True # bool | If true, the response will include encrypted password. (optional)

    try:
        # Get all registered Remote Clusters.
        api_response = api_instance.get_remote_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names, node_addresses=node_addresses, purpose=purpose, include_encrypted_credentials=include_encrypted_credentials)
        print("The response of RemoteClustersApi->get_remote_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteClustersApi->get_remote_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_ids** | [**List[int]**](int.md)| Specifies a list of Remote Cluster ids to filter. | [optional] 
 **cluster_names** | [**List[str]**](str.md)| Specifies a list of Remote Cluster names to filter. | [optional] 
 **node_addresses** | [**List[str]**](str.md)| Specifies a list of Remote Cluster IPs to filter. | [optional] 
 **purpose** | [**List[str]**](str.md)| Specifies the purpose for which the remote cluster is being registered. | [optional] 
 **include_encrypted_credentials** | **bool**| If true, the response will include encrypted password. | [optional] 

### Return type

[**RemoteClusters**](RemoteClusters.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_remote_cluster**
> UpdateRemoteClusterParams register_remote_cluster(body)

Register a Remote Cluster.

Register a Remote Cluster on this local cluster for remote access and/or replication.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.register_remote_cluster_params import RegisterRemoteClusterParams
from cohesity_sdk.models.update_remote_cluster_params import UpdateRemoteClusterParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteClustersApi(api_client)
    body = cohesity_sdk.RegisterRemoteClusterParams() # RegisterRemoteClusterParams | Specifies the request to register Remote Cluster.

    try:
        # Register a Remote Cluster.
        api_response = api_instance.register_remote_cluster(body)
        print("The response of RemoteClustersApi->register_remote_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteClustersApi->register_remote_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterRemoteClusterParams**](RegisterRemoteClusterParams.md)| Specifies the request to register Remote Cluster. | 

### Return type

[**UpdateRemoteClusterParams**](UpdateRemoteClusterParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_cluster**
> UpdateRemoteClusterParams update_remote_cluster(cluster_id, body)

Update a Remote Cluster config.

Update the connection settings of the specified Remote Cluster that is registered on this Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.update_remote_cluster_params import UpdateRemoteClusterParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteClustersApi(api_client)
    cluster_id = 56 # int | Specifies the cluster id of the Remote Cluster to update.
    body = cohesity_sdk.UpdateRemoteClusterParams() # UpdateRemoteClusterParams | Specifies the request to update Remote Cluster config.

    try:
        # Update a Remote Cluster config.
        api_response = api_instance.update_remote_cluster(cluster_id, body)
        print("The response of RemoteClustersApi->update_remote_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteClustersApi->update_remote_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Remote Cluster to update. | 
 **body** | [**UpdateRemoteClusterParams**](UpdateRemoteClusterParams.md)| Specifies the request to update Remote Cluster config. | 

### Return type

[**UpdateRemoteClusterParams**](UpdateRemoteClusterParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_remote_cluster**
> RemoteClusterParams validate_remote_cluster(body, include_metadata=include_metadata)

Validate Remote Cluster config.

Validate a Remote Cluster credentials. If includeRemoteClusterMetadata is true, response will include the remote cluster metadata.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.remote_cluster_params import RemoteClusterParams
from cohesity_sdk.models.validate_remote_cluster_connection_param import ValidateRemoteClusterConnectionParam
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.RemoteClustersApi(api_client)
    body = cohesity_sdk.ValidateRemoteClusterConnectionParam() # ValidateRemoteClusterConnectionParam | Specifies the request to validate Remote Cluster.
    include_metadata = True # bool | Specifies if Remote Cluster metadata should be included in the response. (optional)

    try:
        # Validate Remote Cluster config.
        api_response = api_instance.validate_remote_cluster(body, include_metadata=include_metadata)
        print("The response of RemoteClustersApi->validate_remote_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteClustersApi->validate_remote_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateRemoteClusterConnectionParam**](ValidateRemoteClusterConnectionParam.md)| Specifies the request to validate Remote Cluster. | 
 **include_metadata** | **bool**| Specifies if Remote Cluster metadata should be included in the response. | [optional] 

### Return type

[**RemoteClusterParams**](RemoteClusterParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

