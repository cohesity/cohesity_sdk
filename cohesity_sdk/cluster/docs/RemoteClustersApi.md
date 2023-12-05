# cohesity_sdk.RemoteClustersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_odp_remote_cluster**](RemoteClustersApi.md#create_odp_remote_cluster) | **POST** /odp-remote-clusters | Create an ODP Remote Cluster config.
[**delete_remote_cluster**](RemoteClustersApi.md#delete_remote_cluster) | **DELETE** /remote-clusters/{clusterId} | Unregister a Remote Cluster.
[**get_odp_remote_cluster_by_id**](RemoteClustersApi.md#get_odp_remote_cluster_by_id) | **GET** /odp-remote-clusters/{clusterId} | Get ODP Remote Cluster config by id.
[**get_odp_remote_clusters**](RemoteClustersApi.md#get_odp_remote_clusters) | **GET** /odp-remote-clusters | Get ODP Remote Cluster configs.
[**get_remote_cluster_by_id**](RemoteClustersApi.md#get_remote_cluster_by_id) | **GET** /remote-clusters/{clusterId} | Get Remote Cluster config by id.
[**get_remote_clusters**](RemoteClustersApi.md#get_remote_clusters) | **GET** /remote-clusters | Get all registered Remote Clusters.
[**get_replication_encryption_key**](RemoteClustersApi.md#get_replication_encryption_key) | **GET** /replicationEncryptionKey | Get Replication Encryption Key
[**register_remote_cluster**](RemoteClustersApi.md#register_remote_cluster) | **POST** /remote-clusters | Register a Remote Cluster.
[**update_odp_remote_cluster**](RemoteClustersApi.md#update_odp_remote_cluster) | **PUT** /odp-remote-clusters/{clusterId} | Update an ODP Remote Cluster config.
[**update_remote_cluster**](RemoteClustersApi.md#update_remote_cluster) | **PUT** /remote-clusters/{clusterId} | Update a Remote Cluster config.
[**validate_remote_cluster**](RemoteClustersApi.md#validate_remote_cluster) | **POST** /remote-clusters/validate | Validate Remote Cluster config.


# **create_odp_remote_cluster**
> OdpRemoteCluster create_odp_remote_cluster(body)

Create an ODP Remote Cluster config.

Create an ODP Remote Cluster config.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_odp_remote_cluster_params import CreateOdpRemoteClusterParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.odp_remote_cluster import OdpRemoteCluster
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = CreateOdpRemoteClusterParams() # CreateOdpRemoteClusterParams | Specifies the request to create ODP Remote Cluster config.

# example passing only required values which don't have defaults set
try:
	# Create an ODP Remote Cluster config.
	api_response = client.remote_clusters.create_odp_remote_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->create_odp_remote_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOdpRemoteClusterParams**](CreateOdpRemoteClusterParams.md)| Specifies the request to create ODP Remote Cluster config. |

### Return type

[**OdpRemoteCluster**](OdpRemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_cluster**
> delete_remote_cluster(cluster_id)

Unregister a Remote Cluster.

Unregister an external Remote Cluster.

### Example

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

cluster_id = 1 # int | Specifies the cluster id of the Remote Cluster to unregister.

# example passing only required values which don't have defaults set
try:
	# Unregister a Remote Cluster.
	client.remote_clusters.delete_remote_cluster(cluster_id)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->delete_remote_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Remote Cluster to unregister. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_odp_remote_cluster_by_id**
> OdpRemoteCluster get_odp_remote_cluster_by_id(cluster_id)

Get ODP Remote Cluster config by id.

Get ODP Remote Cluster config by id.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.odp_remote_cluster import OdpRemoteCluster
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

cluster_id = 1 # int | Specifies the id of ODP Remote Cluster to fetch.

# example passing only required values which don't have defaults set
try:
	# Get ODP Remote Cluster config by id.
	api_response = client.remote_clusters.get_odp_remote_cluster_by_id(cluster_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->get_odp_remote_cluster_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the id of ODP Remote Cluster to fetch. |

### Return type

[**OdpRemoteCluster**](OdpRemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_odp_remote_clusters**
> OdpRemoteClusters get_odp_remote_clusters()

Get ODP Remote Cluster configs.

Get ODP Remote Cluster configs.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.odp_remote_clusters import OdpRemoteClusters
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

cluster_ids = [
        1,
    ] # [int] | Specifies a list of ODP Remote Cluster ids to filter. (optional)
cluster_names = [
        "clusterNames_example",
    ] # [str] | Specifies a list of ODP Remote Cluster names to filter. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which ODP Remote Clusters are to be returned. (optional)
include_tenants = True # bool | If true, the response will include ODP Remote Clusters which were created by all tenants which the current user has permission to see. If false, then only ODP Remote Clusters created by the current user will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get ODP Remote Cluster configs.
	api_response = client.remote_clusters.get_odp_remote_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->get_odp_remote_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_ids** | **[int]**| Specifies a list of ODP Remote Cluster ids to filter. | [optional]
 **cluster_names** | **[str]**| Specifies a list of ODP Remote Cluster names to filter. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which ODP Remote Clusters are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include ODP Remote Clusters which were created by all tenants which the current user has permission to see. If false, then only ODP Remote Clusters created by the current user will be returned. | [optional]

### Return type

[**OdpRemoteClusters**](OdpRemoteClusters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_cluster_by_id**
> RemoteCluster get_remote_cluster_by_id(cluster_id)

Get Remote Cluster config by id.

Get Remote Cluster config by cluster id.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.remote_cluster import RemoteCluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

cluster_id = 1 # int | Specifies the cluster id of Remote Cluster to fetch.

# example passing only required values which don't have defaults set
try:
	# Get Remote Cluster config by id.
	api_response = client.remote_clusters.get_remote_cluster_by_id(cluster_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->get_remote_cluster_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of Remote Cluster to fetch. |

### Return type

[**RemoteCluster**](RemoteCluster.md)

### Authorization

No authorization required

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
> RemoteClusters get_remote_clusters()

Get all registered Remote Clusters.

List the Remote Clusters that are registered on this local Cluster and that matches the filter criteria specified using parameters.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_clusters import RemoteClusters
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

cluster_ids = [
        1,
    ] # [int] | Specifies a list of Remote Cluster ids to filter. (optional)
cluster_names = [
        "clusterNames_example",
    ] # [str] | Specifies a list of Remote Cluster names to filter. (optional)
node_addresses = [
        "nodeAddresses_example",
    ] # [str] | Specifies a list of Remote Cluster IPs to filter. (optional)
purpose = [
        "Replication",
    ] # [str] | Specifies the purpose for which the remote cluster is being registered. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get all registered Remote Clusters.
	api_response = client.remote_clusters.get_remote_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names, node_addresses=node_addresses, purpose=purpose)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->get_remote_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_ids** | **[int]**| Specifies a list of Remote Cluster ids to filter. | [optional]
 **cluster_names** | **[str]**| Specifies a list of Remote Cluster names to filter. | [optional]
 **node_addresses** | **[str]**| Specifies a list of Remote Cluster IPs to filter. | [optional]
 **purpose** | **[str]**| Specifies the purpose for which the remote cluster is being registered. | [optional]

### Return type

[**RemoteClusters**](RemoteClusters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_encryption_key**
> ReplicationEncryptionKey get_replication_encryption_key()

Get Replication Encryption Key

List the Replication Encryption Key. It is used for encrypting replication data between this Cluster and a remote Cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.replication_encryption_key import ReplicationEncryptionKey
from cohesity_sdk.cluster.model.error import Error
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
	# Get Replication Encryption Key
	api_response = client.remote_clusters.get_replication_encryption_key()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->get_replication_encryption_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ReplicationEncryptionKey**](ReplicationEncryptionKey.md)

### Authorization

No authorization required

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
> RemoteCluster register_remote_cluster(body)

Register a Remote Cluster.

Register a Remote Cluster on this local cluster for remote access and/or replication.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.remote_cluster import RemoteCluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.register_remote_cluster_params import RegisterRemoteClusterParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = RegisterRemoteClusterParams() # RegisterRemoteClusterParams | Specifies the request to register Remote Cluster.

# example passing only required values which don't have defaults set
try:
	# Register a Remote Cluster.
	api_response = client.remote_clusters.register_remote_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->register_remote_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterRemoteClusterParams**](RegisterRemoteClusterParams.md)| Specifies the request to register Remote Cluster. |

### Return type

[**RemoteCluster**](RemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_odp_remote_cluster**
> OdpRemoteCluster update_odp_remote_cluster(cluster_id, body)

Update an ODP Remote Cluster config.

Update an ODP Remote Cluster config.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_odp_remote_cluster_params import UpdateOdpRemoteClusterParams
from cohesity_sdk.cluster.model.odp_remote_cluster import OdpRemoteCluster
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

cluster_id = 1 # int | Specifies the id of ODP Remote Cluster to update.
body = UpdateOdpRemoteClusterParams(
        all_endpoints_reachable=True,
        cluster_id_stale=True,
        cluster_name="cluster_name_example",
        compression_enabled=True,
        interface_group_name="interface_group_name_example",
        key_encryption_key="key_encryption_key_example",
        remote_tenant_id="remote_tenant_id_example",
        storage_domain_pairs=[
            StorageDomainPair(
                local_storage_domain_id=1,
                remote_storage_domain_id=1,
            ),
        ],
        tenant_id="tenant_id_example",
        use_bifrost_broker_channel=True,
        used_for_replication=True,
    ) # UpdateOdpRemoteClusterParams | Specifies the request to update ODP Remote Cluster config.

# example passing only required values which don't have defaults set
try:
	# Update an ODP Remote Cluster config.
	api_response = client.remote_clusters.update_odp_remote_cluster(cluster_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->update_odp_remote_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the id of ODP Remote Cluster to update. |
 **body** | [**UpdateOdpRemoteClusterParams**](UpdateOdpRemoteClusterParams.md)| Specifies the request to update ODP Remote Cluster config. |

### Return type

[**OdpRemoteCluster**](OdpRemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_cluster**
> RemoteCluster update_remote_cluster(cluster_id, body)

Update a Remote Cluster config.

Update the connection settings of the specified Remote Cluster that is registered on this Cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.remote_cluster import RemoteCluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_remote_cluster_params import UpdateRemoteClusterParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

cluster_id = 1 # int | Specifies the cluster id of the Remote Cluster to update.
body = UpdateRemoteClusterParams() # UpdateRemoteClusterParams | Specifies the request to update Remote Cluster config.

# example passing only required values which don't have defaults set
try:
	# Update a Remote Cluster config.
	api_response = client.remote_clusters.update_remote_cluster(cluster_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->update_remote_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the cluster id of the Remote Cluster to update. |
 **body** | [**UpdateRemoteClusterParams**](UpdateRemoteClusterParams.md)| Specifies the request to update Remote Cluster config. |

### Return type

[**RemoteCluster**](RemoteCluster.md)

### Authorization

No authorization required

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
> validate_remote_cluster(body)

Validate Remote Cluster config.

Validate a Remote Cluster credentials.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.validate_remote_cluster_connection_param import ValidateRemoteClusterConnectionParam
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = ValidateRemoteClusterConnectionParam(
        node_addresses=[
            "node_addresses_example",
        ],
        password="password_example",
        username="username_example",
    ) # ValidateRemoteClusterConnectionParam | Specifies the request to validate Remote Cluster.

# example passing only required values which don't have defaults set
try:
	# Validate Remote Cluster config.
	client.remote_clusters.validate_remote_cluster(body)
except ApiException as e:
	print("Exception when calling RemoteClustersApi->validate_remote_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateRemoteClusterConnectionParam**](ValidateRemoteClusterConnectionParam.md)| Specifies the request to validate Remote Cluster. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

