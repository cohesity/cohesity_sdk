# cohesity_sdk.cluster.FortknoxOnpremApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_primary_cluster_api_key**](FortknoxOnpremApi.md#check_primary_cluster_api_key) | **POST** /fortknox-onprem-primary-clusters/{clusterId}/apiKey/check | Check the API key for the Primary Cluster.
[**create_fortknox_onprem_primary_cluster_connection**](FortknoxOnpremApi.md#create_fortknox_onprem_primary_cluster_connection) | **POST** /fortknox-onprem-primary-clusters/connections | Create connection for a Fortknox Onprem primary cluster.
[**delete_fortknox_onprem_primary_cluster**](FortknoxOnpremApi.md#delete_fortknox_onprem_primary_cluster) | **DELETE** /fortknox-onprem-primary-clusters/{clusterId} | Unregister an Fortknox Onprem Primary Cluster.
[**get_fortknox_onprem_primary_cluster_by_id**](FortknoxOnpremApi.md#get_fortknox_onprem_primary_cluster_by_id) | **GET** /fortknox-onprem-primary-clusters/{clusterId} | Get a Fortknox Onprem Primary Cluster by id.
[**get_fortknox_onprem_primary_clusters**](FortknoxOnpremApi.md#get_fortknox_onprem_primary_clusters) | **GET** /fortknox-onprem-primary-clusters | Get all registered Fortknox Onprem Primary Clusters.
[**get_fortknox_onprem_vault_cluster_by_id**](FortknoxOnpremApi.md#get_fortknox_onprem_vault_cluster_by_id) | **GET** /fortknox-onprem-vault-clusters/{clusterId} | Get a Fortknox Onprem Vault Cluster by id.
[**get_fortknox_onprem_vault_clusters**](FortknoxOnpremApi.md#get_fortknox_onprem_vault_clusters) | **GET** /fortknox-onprem-vault-clusters | Get all registered Fortknox Onprem Vault Clusters.
[**get_fortknox_onprem_vaulting_activities**](FortknoxOnpremApi.md#get_fortknox_onprem_vaulting_activities) | **GET** /fortknox-onprem/vaulting/activities | Get a list of Fortknox Onprem vaulting activities.
[**get_is_vault_cluster**](FortknoxOnpremApi.md#get_is_vault_cluster) | **GET** /fortknox-onprem-clusters/is-vault-cluster | Get whether the cluster is a vault cluster.
[**list_fortknox_onprem_vault_cluster_prechecks**](FortknoxOnpremApi.md#list_fortknox_onprem_vault_cluster_prechecks) | **GET** /fortknox-onprem-vault-clusters/precheck-options | Get all precheck options required for vault configuration.
[**list_fortknox_vault_prechecks**](FortknoxOnpremApi.md#list_fortknox_vault_prechecks) | **GET** /fortknox-onprem-clusters/precheck-options | Get all precheck options required for vault configuration.
[**refresh_primary_cluster_api_key**](FortknoxOnpremApi.md#refresh_primary_cluster_api_key) | **PUT** /fortknox-onprem-primary-clusters/{clusterId}/apiKey | Refresh the API key for the Primary Cluster.
[**register_fortknox_onprem_primary_cluster**](FortknoxOnpremApi.md#register_fortknox_onprem_primary_cluster) | **POST** /fortknox-onprem-primary-clusters | Register a Fortknox Onprem Primary Cluster.
[**update_fortknox_onprem_primary_cluster**](FortknoxOnpremApi.md#update_fortknox_onprem_primary_cluster) | **PUT** /fortknox-onprem-primary-clusters/{clusterId} | Update the registration of a Fortknox Onprem Primary Cluster.
[**update_fortknox_onprem_primary_cluster_connection**](FortknoxOnpremApi.md#update_fortknox_onprem_primary_cluster_connection) | **PUT** /fortknox-onprem-primary-clusters/{clusterId}/connections | Update connection for a Fortknox Onprem primary cluster.
[**update_is_vault_cluster**](FortknoxOnpremApi.md#update_is_vault_cluster) | **PUT** /fortknox-onprem-clusters/is-vault-cluster | Update whether the cluster is a vault cluster.


# **check_primary_cluster_api_key**
> CheckAPIKeyResult check_primary_cluster_api_key(cluster_id)

Check the API key for the Primary Cluster.

```No Privileges Required``` <br><br>Check whether the API key for the specified Primary Cluster is still valid.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.check_api_key_result import CheckAPIKeyResult
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_id = 1 # int | Specifies the cluster id of the Fortknox Onprem Primary Cluster to update.

    # example passing only required values which don't have defaults set
    try:
        # Check the API key for the Primary Cluster.
        api_response = api_instance.check_primary_cluster_api_key(cluster_id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->check_primary_cluster_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Fortknox Onprem Primary Cluster to update. |

### Return type

[**CheckAPIKeyResult**](CheckAPIKeyResult.md)

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

# **create_fortknox_onprem_primary_cluster_connection**
> ClusterIdentifier create_fortknox_onprem_primary_cluster_connection(body)

Create connection for a Fortknox Onprem primary cluster.

**Privileges:** ```FORTKNOX_ONPREM_VAULTING``` <br><br>Create connection for a Fortknox Onprem Primary Cluster. This API can only be called on the Vault Clusters. This API will exchange CA certs and fetch the API key of the primary cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.cluster_identifier import ClusterIdentifier
from cohesity_sdk.cluster.cohesity.model.create_or_update_primary_cluster_connection_params import CreateOrUpdatePrimaryClusterConnectionParams
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    body = CreateOrUpdatePrimaryClusterConnectionParams() # CreateOrUpdatePrimaryClusterConnectionParams | Specifies the request to create connection for a Fortknox Onprem Primary Cluster.

    # example passing only required values which don't have defaults set
    try:
        # Create connection for a Fortknox Onprem primary cluster.
        api_response = api_instance.create_fortknox_onprem_primary_cluster_connection(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->create_fortknox_onprem_primary_cluster_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdatePrimaryClusterConnectionParams**](CreateOrUpdatePrimaryClusterConnectionParams.md)| Specifies the request to create connection for a Fortknox Onprem Primary Cluster. |

### Return type

[**ClusterIdentifier**](ClusterIdentifier.md)

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

# **delete_fortknox_onprem_primary_cluster**
> delete_fortknox_onprem_primary_cluster(cluster_id)

Unregister an Fortknox Onprem Primary Cluster.

**Privileges:** ```FORTKNOX_ONPREM_VAULTING``` <br><br>Unregister a Fortknox Onprem Primary Cluster. This API can only be called on the Vault Clusters. The Vault Cluster will be removed from the Primary Cluster automatically.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_id = 1 # int | Specifies the cluster id of the Fortknox Onprem Primary Cluster to unregister.

    # example passing only required values which don't have defaults set
    try:
        # Unregister an Fortknox Onprem Primary Cluster.
        api_instance.delete_fortknox_onprem_primary_cluster(cluster_id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->delete_fortknox_onprem_primary_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Fortknox Onprem Primary Cluster to unregister. |

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

# **get_fortknox_onprem_primary_cluster_by_id**
> FortknoxOnpremPrimaryCluster get_fortknox_onprem_primary_cluster_by_id(cluster_id)

Get a Fortknox Onprem Primary Cluster by id.

```No Privileges Required``` <br><br>Get a Fortknox Onprem Primary Cluster by cluster id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_primary_cluster import FortknoxOnpremPrimaryCluster
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_id = 1 # int | Specifies the cluster id of Fortknox Onprem Primary Cluster to fetch.

    # example passing only required values which don't have defaults set
    try:
        # Get a Fortknox Onprem Primary Cluster by id.
        api_response = api_instance.get_fortknox_onprem_primary_cluster_by_id(cluster_id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->get_fortknox_onprem_primary_cluster_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of Fortknox Onprem Primary Cluster to fetch. |

### Return type

[**FortknoxOnpremPrimaryCluster**](FortknoxOnpremPrimaryCluster.md)

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

# **get_fortknox_onprem_primary_clusters**
> FortknoxOnpremPrimaryClusters get_fortknox_onprem_primary_clusters()

Get all registered Fortknox Onprem Primary Clusters.

```No Privileges Required``` <br><br>List the Fortknox Onprem Primary Clusters that are registered on this local Cluster and that matches the filter criteria specified using parameters.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_primary_clusters import FortknoxOnpremPrimaryClusters
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_ids = [
        1,
    ] # [int] | Specifies a list of Cluster ids to filter. (optional)
    cluster_names = [
        "clusterNames_example",
    ] # [str] | Specifies a list of Cluster names to filter. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all registered Fortknox Onprem Primary Clusters.
        api_response = api_instance.get_fortknox_onprem_primary_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->get_fortknox_onprem_primary_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_ids** | **[int]**| Specifies a list of Cluster ids to filter. | [optional]
 **cluster_names** | **[str]**| Specifies a list of Cluster names to filter. | [optional]

### Return type

[**FortknoxOnpremPrimaryClusters**](FortknoxOnpremPrimaryClusters.md)

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

# **get_fortknox_onprem_vault_cluster_by_id**
> FortknoxOnpremVaultCluster get_fortknox_onprem_vault_cluster_by_id(cluster_id)

Get a Fortknox Onprem Vault Cluster by id.

```No Privileges Required``` <br><br>Get a Fortknox Onprem Vault Cluster by cluster id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_vault_cluster import FortknoxOnpremVaultCluster
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_id = 1 # int | Specifies the cluster id of Fortknox Onprem Vault Cluster to fetch.

    # example passing only required values which don't have defaults set
    try:
        # Get a Fortknox Onprem Vault Cluster by id.
        api_response = api_instance.get_fortknox_onprem_vault_cluster_by_id(cluster_id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->get_fortknox_onprem_vault_cluster_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of Fortknox Onprem Vault Cluster to fetch. |

### Return type

[**FortknoxOnpremVaultCluster**](FortknoxOnpremVaultCluster.md)

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

# **get_fortknox_onprem_vault_clusters**
> FortknoxOnpremVaultClusters get_fortknox_onprem_vault_clusters()

Get all registered Fortknox Onprem Vault Clusters.

```No Privileges Required``` <br><br>List the Fortknox Onprem Vault Clusters that are registered on this local Cluster and that matches the filter criteria specified using parameters.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_vault_clusters import FortknoxOnpremVaultClusters
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_ids = [
        1,
    ] # [int] | Specifies a list of Cluster ids to filter. (optional)
    cluster_names = [
        "clusterNames_example",
    ] # [str] | Specifies a list of Cluster names to filter. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all registered Fortknox Onprem Vault Clusters.
        api_response = api_instance.get_fortknox_onprem_vault_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->get_fortknox_onprem_vault_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_ids** | **[int]**| Specifies a list of Cluster ids to filter. | [optional]
 **cluster_names** | **[str]**| Specifies a list of Cluster names to filter. | [optional]

### Return type

[**FortknoxOnpremVaultClusters**](FortknoxOnpremVaultClusters.md)

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

# **get_fortknox_onprem_vaulting_activities**
> FortknoxOnpremVaultingActivities get_fortknox_onprem_vaulting_activities()

Get a list of Fortknox Onprem vaulting activities.

```No Privileges Required``` <br><br>Get a list of Fortknox Onprem vaulting activities.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_vaulting_activities import FortknoxOnpremVaultingActivities
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    start_time_usecs = 1 # int | Start time for time range filter. Specify the start time as a Unix epoch Timestamp (in microseconds), only vaulting runs started after this time will be returned. By default, it is set to 7 days prior to the current time. (optional)
    end_time_usecs = 1 # int | End time for time range filter. Specify the end time as a Unix epoch Timestamp (in microseconds), only vaulting runs started before this time will be returned. By default, it is the current time. (optional)
    statuses = [
        "Accepted",
    ] # [str] | Specifies a list of Fortknox Onprem vaulting replication runs status, runs matching the status will be returned.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Paused' indicates that the ongoing run has been paused.<br> 'Skipped' indicates that the run was skipped. (optional)
    source_cluster_ids = [
        1,
    ] # [int] | sourceClusterIds contains ids of the source clusters for which vaulting replication runs are to be returned. (optional)
    pagination_cookie = "paginationCookie_example" # str, none_type | Specifies the cookie to fetch the next page of results (optional)
    max_runs = 1 # int, none_type | Specifies the max number of runs to return. If not specified, at most 100 runs will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of Fortknox Onprem vaulting activities.
        api_response = api_instance.get_fortknox_onprem_vaulting_activities(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, statuses=statuses, source_cluster_ids=source_cluster_ids, pagination_cookie=pagination_cookie, max_runs=max_runs)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->get_fortknox_onprem_vaulting_activities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_usecs** | **int**| Start time for time range filter. Specify the start time as a Unix epoch Timestamp (in microseconds), only vaulting runs started after this time will be returned. By default, it is set to 7 days prior to the current time. | [optional]
 **end_time_usecs** | **int**| End time for time range filter. Specify the end time as a Unix epoch Timestamp (in microseconds), only vaulting runs started before this time will be returned. By default, it is the current time. | [optional]
 **statuses** | **[str]**| Specifies a list of Fortknox Onprem vaulting replication runs status, runs matching the status will be returned.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Paused&#39; indicates that the ongoing run has been paused.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional]
 **source_cluster_ids** | **[int]**| sourceClusterIds contains ids of the source clusters for which vaulting replication runs are to be returned. | [optional]
 **pagination_cookie** | **str, none_type**| Specifies the cookie to fetch the next page of results | [optional]
 **max_runs** | **int, none_type**| Specifies the max number of runs to return. If not specified, at most 100 runs will be returned. | [optional]

### Return type

[**FortknoxOnpremVaultingActivities**](FortknoxOnpremVaultingActivities.md)

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

# **get_is_vault_cluster**
> IsVaultClusterParams get_is_vault_cluster()

Get whether the cluster is a vault cluster.

```No Privileges Required``` <br><br>Get whether the cluster is a vault cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.is_vault_cluster_params import IsVaultClusterParams
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get whether the cluster is a vault cluster.
        api_response = api_instance.get_is_vault_cluster()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->get_is_vault_cluster: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**IsVaultClusterParams**](IsVaultClusterParams.md)

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

# **list_fortknox_onprem_vault_cluster_prechecks**
> PrecheckOptions list_fortknox_onprem_vault_cluster_prechecks()

Get all precheck options required for vault configuration.

**Privileges:** ```CLUSTER_VIEW``` <br><br>List the Fortknox Onprem options which are prechecks for configuring fortknox onprem vault cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.precheck_options import PrecheckOptions
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all precheck options required for vault configuration.
        api_response = api_instance.list_fortknox_onprem_vault_cluster_prechecks()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->list_fortknox_onprem_vault_cluster_prechecks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PrecheckOptions**](PrecheckOptions.md)

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

# **list_fortknox_vault_prechecks**
> PrecheckOptions list_fortknox_vault_prechecks()

Get all precheck options required for vault configuration.

```Unknown Privileges``` <br><br>List the Fortknox Onprem options which are prechecks for configuring fortknox onprem vault.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.precheck_options import PrecheckOptions
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all precheck options required for vault configuration.
        api_response = api_instance.list_fortknox_vault_prechecks()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->list_fortknox_vault_prechecks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PrecheckOptions**](PrecheckOptions.md)

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

# **refresh_primary_cluster_api_key**
> refresh_primary_cluster_api_key(cluster_id, body)

Refresh the API key for the Primary Cluster.

**Privileges:** ```FORTKNOX_ONPREM_VAULTING``` <br><br>Refresh the API key for the Primary Cluster specified by the id. It will extend expiry time and rotate the key for an expiring API key, or create a new API key if the original key is deleted or the owner of the key no longer exists.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.common_credentials_params import CommonCredentialsParams
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_id = 1 # int | Specifies the cluster id of the Fortknox Onprem Primary Cluster to update.
    body = CommonCredentialsParams(
        password="password_example",
        username="username_example",
    ) # CommonCredentialsParams | Specifies the request to refresh the API key of a Fortknox Onprem Primary Cluster.

    # example passing only required values which don't have defaults set
    try:
        # Refresh the API key for the Primary Cluster.
        api_instance.refresh_primary_cluster_api_key(cluster_id, body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->refresh_primary_cluster_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Fortknox Onprem Primary Cluster to update. |
 **body** | [**CommonCredentialsParams**](CommonCredentialsParams.md)| Specifies the request to refresh the API key of a Fortknox Onprem Primary Cluster. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_fortknox_onprem_primary_cluster**
> FortknoxOnpremPrimaryCluster register_fortknox_onprem_primary_cluster(body)

Register a Fortknox Onprem Primary Cluster.

**Privileges:** ```FORTKNOX_ONPREM_VAULTING``` <br><br>Register the Fortknox Onprem Primary Cluster on this cluster. This API can only be called on the Vault Clusters and the Vault Cluster will be registered on the Primary Cluster automatically.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.create_fortknox_onprem_primary_cluster_params import CreateFortknoxOnpremPrimaryClusterParams
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_primary_cluster import FortknoxOnpremPrimaryCluster
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    body = CreateFortknoxOnpremPrimaryClusterParams() # CreateFortknoxOnpremPrimaryClusterParams | Specifies the request to register a Fortknox Onprem Primary Cluster.

    # example passing only required values which don't have defaults set
    try:
        # Register a Fortknox Onprem Primary Cluster.
        api_response = api_instance.register_fortknox_onprem_primary_cluster(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->register_fortknox_onprem_primary_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFortknoxOnpremPrimaryClusterParams**](CreateFortknoxOnpremPrimaryClusterParams.md)| Specifies the request to register a Fortknox Onprem Primary Cluster. |

### Return type

[**FortknoxOnpremPrimaryCluster**](FortknoxOnpremPrimaryCluster.md)

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

# **update_fortknox_onprem_primary_cluster**
> FortknoxOnpremPrimaryCluster update_fortknox_onprem_primary_cluster(cluster_id, body)

Update the registration of a Fortknox Onprem Primary Cluster.

**Privileges:** ```FORTKNOX_ONPREM_VAULTING``` <br><br>Update the registration of the Fortknox Onprem Primary Cluster specified by the cluster id. This API can only be called on the Vault Clusters. The updates will be relayed to the Primary Cluster automatically.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_primary_cluster import FortknoxOnpremPrimaryCluster
from cohesity_sdk.cluster.cohesity.model.fortknox_onprem_cluster_common_params import FortknoxOnpremClusterCommonParams
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_id = 1 # int | Specifies the cluster id of the Fortknox Onprem Primary Cluster to update.
    body = FortknoxOnpremClusterCommonParams() # FortknoxOnpremClusterCommonParams | Specifies the request to update Fortknox Onprem Primary Cluster config.

    # example passing only required values which don't have defaults set
    try:
        # Update the registration of a Fortknox Onprem Primary Cluster.
        api_response = api_instance.update_fortknox_onprem_primary_cluster(cluster_id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->update_fortknox_onprem_primary_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Fortknox Onprem Primary Cluster to update. |
 **body** | [**FortknoxOnpremClusterCommonParams**](FortknoxOnpremClusterCommonParams.md)| Specifies the request to update Fortknox Onprem Primary Cluster config. |

### Return type

[**FortknoxOnpremPrimaryCluster**](FortknoxOnpremPrimaryCluster.md)

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

# **update_fortknox_onprem_primary_cluster_connection**
> ClusterIdentifier update_fortknox_onprem_primary_cluster_connection(cluster_id, body)

Update connection for a Fortknox Onprem primary cluster.

**Privileges:** ```FORTKNOX_ONPREM_VAULTING``` <br><br>Update connection for a Fortknox Onprem Primary Cluster. This API can only be called on the Vault Clusters.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.cluster_identifier import ClusterIdentifier
from cohesity_sdk.cluster.cohesity.model.create_or_update_primary_cluster_connection_params import CreateOrUpdatePrimaryClusterConnectionParams
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    cluster_id = 1 # int | Specifies the cluster id of the Fortknox Onprem Primary Cluster to update.
    body = CreateOrUpdatePrimaryClusterConnectionParams() # CreateOrUpdatePrimaryClusterConnectionParams | Specifies the request to update connection for a Fortknox Onprem Primary Cluster.

    # example passing only required values which don't have defaults set
    try:
        # Update connection for a Fortknox Onprem primary cluster.
        api_response = api_instance.update_fortknox_onprem_primary_cluster_connection(cluster_id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->update_fortknox_onprem_primary_cluster_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Fortknox Onprem Primary Cluster to update. |
 **body** | [**CreateOrUpdatePrimaryClusterConnectionParams**](CreateOrUpdatePrimaryClusterConnectionParams.md)| Specifies the request to update connection for a Fortknox Onprem Primary Cluster. |

### Return type

[**ClusterIdentifier**](ClusterIdentifier.md)

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

# **update_is_vault_cluster**
> IsVaultClusterParams update_is_vault_cluster(body)

Update whether the cluster is a vault cluster.

**Privileges:** ```FORTKNOX_ONPREM_VAULTING``` <br><br>Update whether the cluster is a vault cluster. If a cluster is already vault cluster, it cannot be deconfigured.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import fortknox_onprem
from cohesity_sdk.cluster.cohesity.model.is_vault_cluster_params import IsVaultClusterParams
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
    api_instance = fortknox_onprem.FortknoxOnpremApi(api_client)
    body = IsVaultClusterParams(
        is_vault_cluster=True,
    ) # IsVaultClusterParams | Params to update whether the cluster is a vault cluster.

    # example passing only required values which don't have defaults set
    try:
        # Update whether the cluster is a vault cluster.
        api_response = api_instance.update_is_vault_cluster(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling FortknoxOnpremApi->update_is_vault_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsVaultClusterParams**](IsVaultClusterParams.md)| Params to update whether the cluster is a vault cluster. |

### Return type

[**IsVaultClusterParams**](IsVaultClusterParams.md)

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

