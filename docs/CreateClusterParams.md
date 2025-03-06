# CreateClusterParams

Specifies the parameters required to create cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_cluster_params** | [**ClusterCreateCloudParams**](ClusterCreateCloudParams.md) |  | [optional] 
**enable_encryption** | **bool** | Specifies whether or not to enable encryption. If encryption is enabled, all data on the Cluster will be encrypted. This can only be enabled at Cluster creation time and cannot be disabled later. | [default to True]
**name** | **str** | Specifies the name of the new cluster. | 
**network_config** | [**ClusterCreateNetworkConfig**](ClusterCreateNetworkConfig.md) |  | 
**physical_cluster_params** | [**ClusterCreatePhysicalParams**](ClusterCreatePhysicalParams.md) |  | [optional] 
**proxy_server_config** | [**ClusterProxyServerConfig**](ClusterProxyServerConfig.md) |  | [optional] 
**rigel_cluster_params** | [**ClusterCreateRigelParams**](ClusterCreateRigelParams.md) |  | [optional] 
**type** | **str** | Specifies the type of the new cluster. | 
**virtual_cluster_params** | [**ClusterCreateVirtualParams**](ClusterCreateVirtualParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_cluster_params import CreateClusterParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterParams from a JSON string
create_cluster_params_instance = CreateClusterParams.from_json(json)
# print the JSON string representation of the object
print(CreateClusterParams.to_json())

# convert the object into a dict
create_cluster_params_dict = create_cluster_params_instance.to_dict()
# create an instance of CreateClusterParams from a dict
create_cluster_params_from_dict = CreateClusterParams.from_dict(create_cluster_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


