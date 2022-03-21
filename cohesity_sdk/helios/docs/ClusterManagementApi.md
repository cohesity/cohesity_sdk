# cohesity_sdk.ClusterManagementApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_release_details**](ClusterManagementApi.md#clusters_release_details) | **GET** /mcm/cluster-mgmt/releases | Get releases available.
[**clusters_upgrades_info**](ClusterManagementApi.md#clusters_upgrades_info) | **GET** /mcm/cluster-mgmt/upgrades/info | Fetch upgrade info.
[**create_clusters_upgrades**](ClusterManagementApi.md#create_clusters_upgrades) | **POST** /mcm/cluster-mgmt/upgrades | Initiates instant and scheduled cluster upgrade.
[**delete_clusters_upgrades**](ClusterManagementApi.md#delete_clusters_upgrades) | **DELETE** /mcm/cluster-mgmt/upgrades | Cancels scheduled cluster upgrades.
[**fetch_clusters_upgrades**](ClusterManagementApi.md#fetch_clusters_upgrades) | **GET** /mcm/cluster-mgmt/upgrades | Fetch the cluster upgrade details.
[**get_clusters_info**](ClusterManagementApi.md#get_clusters_info) | **GET** /mcm/cluster-mgmt/info | Clusters information with upgrade details.
[**update_clusters_upgrades**](ClusterManagementApi.md#update_clusters_upgrades) | **PUT** /mcm/cluster-mgmt/upgrades | Updates scheduled cluster upgrades.


# **clusters_release_details**
> ReleasesAvailable clusters_release_details()

Get releases available.

Get releases available for clusters for an account for the downloads page.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.releases_available import ReleasesAvailable
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get releases available.
	api_response = client.cluster_management.clusters_release_details(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ClusterManagementApi->clusters_release_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ReleasesAvailable**](ReleasesAvailable.md)

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

# **clusters_upgrades_info**
> UpgradesInfo clusters_upgrades_info()

Fetch upgrade info.

Get progress details and logs for a cluster upgrade. Logs will in json string format.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.upgrades_info import UpgradesInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
cluster_ids = [
        "clusterIds_example",
    ] # [str] |  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Fetch upgrade info.
	api_response = client.cluster_management.clusters_upgrades_info(region_id=region_id, cluster_ids=cluster_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ClusterManagementApi->clusters_upgrades_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **cluster_ids** | **[str]**|  | [optional]

### Return type

[**UpgradesInfo**](UpgradesInfo.md)

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
> UpgradesResponse create_clusters_upgrades()

Initiates instant and scheduled cluster upgrade.

Initiates instant and scheduled cluster upgrade.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.upgrades_response import UpgradesResponse
from cohesity_sdk.helios.model.upgrades import Upgrades
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = Upgrades(
        clusters=[
            Upgrade(
                cluster_id=1,
                cluster_incarnation_id=1,
                current_version="current_version_example",
            ),
        ],
        target_version="target_version_example",
        time_stamp_to_upgrade_at_msecs=1,
        interval_for_rolling_upgrade_in_hours=1,
    ) # Upgrades | Request body params in order to start an upgrade (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Initiates instant and scheduled cluster upgrade.
	api_response = client.cluster_management.create_clusters_upgrades(region_id=region_id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ClusterManagementApi->create_clusters_upgrades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**Upgrades**](Upgrades.md)| Request body params in order to start an upgrade | [optional]

### Return type

[**UpgradesResponse**](UpgradesResponse.md)

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
> UpgradesCancelResponse delete_clusters_upgrades()

Cancels scheduled cluster upgrades.

Cancels scheduled cluster upgrades.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.upgrades_cancel_response import UpgradesCancelResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
cluster_ids = [
        "clusterIds_example",
    ] # [str], none_type |  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Cancels scheduled cluster upgrades.
	api_response = client.cluster_management.delete_clusters_upgrades(region_id=region_id, cluster_ids=cluster_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ClusterManagementApi->delete_clusters_upgrades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **cluster_ids** | **[str], none_type**|  | [optional]

### Return type

[**UpgradesCancelResponse**](UpgradesCancelResponse.md)

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
> UpgradesDetail fetch_clusters_upgrades()

Fetch the cluster upgrade details.

Fetch the cluster upgrade details.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.upgrades_detail import UpgradesDetail
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
cluster_ids = [
        "clusterIds_example",
    ] # [str], none_type |  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Fetch the cluster upgrade details.
	api_response = client.cluster_management.fetch_clusters_upgrades(region_id=region_id, cluster_ids=cluster_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ClusterManagementApi->fetch_clusters_upgrades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **cluster_ids** | **[str], none_type**|  | [optional]

### Return type

[**UpgradesDetail**](UpgradesDetail.md)

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
> ClustersInfo get_clusters_info()

Clusters information with upgrade details.

Get clusters information and their upgrade details.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.clusters_info import ClustersInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Clusters information with upgrade details.
	api_response = client.cluster_management.get_clusters_info(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ClusterManagementApi->get_clusters_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClustersInfo**](ClustersInfo.md)

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
> UpgradesResponse update_clusters_upgrades()

Updates scheduled cluster upgrades.

Updates scheduled cluster upgrades.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.upgrades_response import UpgradesResponse
from cohesity_sdk.helios.model.upgrades import Upgrades
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = Upgrades(
        clusters=[
            Upgrade(
                cluster_id=1,
                cluster_incarnation_id=1,
                current_version="current_version_example",
            ),
        ],
        target_version="target_version_example",
        time_stamp_to_upgrade_at_msecs=1,
        interval_for_rolling_upgrade_in_hours=1,
    ) # Upgrades | Request body params in order to start an upgrade (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Updates scheduled cluster upgrades.
	api_response = client.cluster_management.update_clusters_upgrades(region_id=region_id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ClusterManagementApi->update_clusters_upgrades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**Upgrades**](Upgrades.md)| Request body params in order to start an upgrade | [optional]

### Return type

[**UpgradesResponse**](UpgradesResponse.md)

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

