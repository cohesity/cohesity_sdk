# ClusterCreateCloudParams

Params for DataProtect for Cloud Cluster Creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_partition_hostname** | **str** | Hostname of the cluster partition. | [optional] 
**cluster_size** | **str** | Specifies the size of the cloud platforms. | [optional] 
**disk_all_nodes_reachable** | **List[bool]** | All nodes reachable property of the disks to designate. | [optional] 
**disk_component_exclusive** | **List[str]** | Component exclusive property of the disks to designate. | [optional] 
**disk_self_fault_tolerant** | **List[bool]** | Self fault tolerant property of the disks to designate. | [optional] 
**disk_serials** | **List[str]** | Serial number of the disks to designate properties. | [optional] 
**disk_tiers** | **List[str]** | Optional field. Tiers of the Disks to designate. | [optional] 
**enable_cloud_rf1** | **bool** | Specifies whether or not to enable software encryption | [optional] 
**encryption_config** | [**EncryptionConfigurationParams**](EncryptionConfigurationParams.md) |  | [optional] 
**ip_preference** | **int** | Specifies IP preference | [optional] 
**metadata_fault_tolerance** | **int** | Specifies the metadata fault tolerance. | [optional] 
**node_ips** | **List[str]** |  | 
**trust_domain** | **str** | Specifies Trust Domain used for Service Identity | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_create_cloud_params import ClusterCreateCloudParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateCloudParams from a JSON string
cluster_create_cloud_params_instance = ClusterCreateCloudParams.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateCloudParams.to_json())

# convert the object into a dict
cluster_create_cloud_params_dict = cluster_create_cloud_params_instance.to_dict()
# create an instance of ClusterCreateCloudParams from a dict
cluster_create_cloud_params_from_dict = ClusterCreateCloudParams.from_dict(cluster_create_cloud_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


