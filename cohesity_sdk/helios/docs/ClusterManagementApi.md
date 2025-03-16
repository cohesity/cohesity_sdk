# cohesity_sdk.helios.ClusterManagementApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_upgrades_info**](ClusterManagementApi.md#clusters_upgrades_info) | **GET** /mcm/cluster-mgmt/upgrades/info | Fetch upgrade info.
[**compatible_clusters_for_release**](ClusterManagementApi.md#compatible_clusters_for_release) | **GET** /mcm/cluster-mgmt/compatible-clusters | Fetch compatible clusters for release version.
[**create_clusters_upgrades**](ClusterManagementApi.md#create_clusters_upgrades) | **POST** /mcm/cluster-mgmt/upgrades | Initiates instant and scheduled cluster upgrade.
[**delete_clusters_upgrades**](ClusterManagementApi.md#delete_clusters_upgrades) | **DELETE** /mcm/cluster-mgmt/upgrades | Cancels scheduled cluster upgrades.
[**fetch_clusters_upgrades**](ClusterManagementApi.md#fetch_clusters_upgrades) | **GET** /mcm/cluster-mgmt/upgrades | Fetch the cluster upgrade details.
[**get_clusters_info**](ClusterManagementApi.md#get_clusters_info) | **GET** /mcm/cluster-mgmt/info | Clusters information with upgrade details.
[**get_releases**](ClusterManagementApi.md#get_releases) | **GET** /mcm/cluster-mgmt/releases | Get all releases present in the db.
[**update_clusters_upgrades**](ClusterManagementApi.md#update_clusters_upgrades) | **PUT** /mcm/cluster-mgmt/upgrades | Updates scheduled cluster upgrades.


# **clusters_upgrades_info**
> List[UpgradeInfo] clusters_upgrades_info(region_id=region_id, cluster_identifiers=cluster_identifiers)

Fetch upgrade info.

Get progress details and logs for a cluster upgrade. Logs will in json string format.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.upgrade_info import UpgradeInfo
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Fetch upgrade progress details for a list of cluster identifiers in format clusterId:clusterIncarnationId. (optional)

    try:
        # Fetch upgrade info.
        api_response = api_instance.clusters_upgrades_info(region_id=region_id, cluster_identifiers=cluster_identifiers)
        print("The response of ClusterManagementApi->clusters_upgrades_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->clusters_upgrades_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Fetch upgrade progress details for a list of cluster identifiers in format clusterId:clusterIncarnationId. | [optional] 

### Return type

[**List[UpgradeInfo]**](UpgradeInfo.md)

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

# **compatible_clusters_for_release**
> List[CompatibleCluster] compatible_clusters_for_release(region_id=region_id, release_version=release_version)

Fetch compatible clusters for release version.

Get list of clusters that are compatible for an upgrade to the specified release version.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.compatible_cluster import CompatibleCluster
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    release_version = 'release_version_example' # str |  (optional)

    try:
        # Fetch compatible clusters for release version.
        api_response = api_instance.compatible_clusters_for_release(region_id=region_id, release_version=release_version)
        print("The response of ClusterManagementApi->compatible_clusters_for_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->compatible_clusters_for_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **release_version** | **str**|  | [optional] 

### Return type

[**List[CompatibleCluster]**](CompatibleCluster.md)

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

# **create_clusters_upgrades**
> List[UpgradeResponse] create_clusters_upgrades(region_id=region_id, body=body)

Initiates instant and scheduled cluster upgrade.

Initiates instant and scheduled cluster upgrade.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.upgrade_response import UpgradeResponse
from cohesity_sdk.helios.models.upgrades import Upgrades
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    body = cohesity_sdk.helios.Upgrades() # Upgrades | Request body params in order to start an upgrade (optional)

    try:
        # Initiates instant and scheduled cluster upgrade.
        api_response = api_instance.create_clusters_upgrades(region_id=region_id, body=body)
        print("The response of ClusterManagementApi->create_clusters_upgrades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->create_clusters_upgrades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **body** | [**Upgrades**](Upgrades.md)| Request body params in order to start an upgrade | [optional] 

### Return type

[**List[UpgradeResponse]**](UpgradeResponse.md)

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

# **delete_clusters_upgrades**
> List[UpgradeCancelResponse] delete_clusters_upgrades(region_id=region_id, cluster_identifiers=cluster_identifiers)

Cancels scheduled cluster upgrades.

Cancels scheduled cluster upgrades.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.upgrade_cancel_response import UpgradeCancelResponse
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. (optional)

    try:
        # Cancels scheduled cluster upgrades.
        api_response = api_instance.delete_clusters_upgrades(region_id=region_id, cluster_identifiers=cluster_identifiers)
        print("The response of ClusterManagementApi->delete_clusters_upgrades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->delete_clusters_upgrades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional] 

### Return type

[**List[UpgradeCancelResponse]**](UpgradeCancelResponse.md)

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

# **fetch_clusters_upgrades**
> List[UpgradeDetail] fetch_clusters_upgrades(region_id=region_id, cluster_ids=cluster_ids)

Fetch the cluster upgrade details.

Fetch the cluster upgrade details.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.upgrade_detail import UpgradeDetail
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    cluster_ids = ['cluster_ids_example'] # List[str] |  (optional)

    try:
        # Fetch the cluster upgrade details.
        api_response = api_instance.fetch_clusters_upgrades(region_id=region_id, cluster_ids=cluster_ids)
        print("The response of ClusterManagementApi->fetch_clusters_upgrades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->fetch_clusters_upgrades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **cluster_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[UpgradeDetail]**](UpgradeDetail.md)

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

# **get_clusters_info**
> ClusterDetails get_clusters_info(region_id=region_id)

Clusters information with upgrade details.

Get clusters information and their upgrade details.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.cluster_details import ClusterDetails
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Clusters information with upgrade details.
        api_response = api_instance.get_clusters_info(region_id=region_id)
        print("The response of ClusterManagementApi->get_clusters_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->get_clusters_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**ClusterDetails**](ClusterDetails.md)

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

# **get_releases**
> Releases get_releases(region_id=region_id)

Get all releases present in the db.

Get all releases present in the db.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.releases import Releases
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get all releases present in the db.
        api_response = api_instance.get_releases(region_id=region_id)
        print("The response of ClusterManagementApi->get_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->get_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**Releases**](Releases.md)

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

# **update_clusters_upgrades**
> List[UpgradeResponse] update_clusters_upgrades(region_id=region_id, body=body)

Updates scheduled cluster upgrades.

Updates scheduled cluster upgrades.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.upgrade_response import UpgradeResponse
from cohesity_sdk.helios.models.upgrades import Upgrades
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ClusterManagementApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    body = cohesity_sdk.helios.Upgrades() # Upgrades | Request body params in order to start an upgrade (optional)

    try:
        # Updates scheduled cluster upgrades.
        api_response = api_instance.update_clusters_upgrades(region_id=region_id, body=body)
        print("The response of ClusterManagementApi->update_clusters_upgrades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterManagementApi->update_clusters_upgrades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **body** | [**Upgrades**](Upgrades.md)| Request body params in order to start an upgrade | [optional] 

### Return type

[**List[UpgradeResponse]**](UpgradeResponse.md)

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

