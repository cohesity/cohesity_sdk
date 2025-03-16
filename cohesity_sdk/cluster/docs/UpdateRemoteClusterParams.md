# UpdateRemoteClusterParams

Specifies the parameters to update a Remote Cluster config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_register_target** | **bool** | Specifies if the Tx clusters should be automatically registered at the Rx site. | [optional] [default to False]
**cluster_id** | **int** | Specifies the Remote Cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int** | Specifies the Remote Cluster incarnation id. | [optional] [readonly] 
**cluster_name** | **str** | Specifies the Remote Cluster name. | [optional] [readonly] 
**description** | **str** | Specifies any additional information if needed. | [optional] 
**effective_aes_encryption_mode** | **str** | Specifies the effective AES Encryption mode negotiated between local and the remote cluster. | [optional] 
**is_auto_registered** | **bool** | Specifies if the Remote Cluster was registered automatically or manually. | [optional] [readonly] 
**local_addresses** | **List[str]** | Specifies the IP addresses of the interfaces in the local Cluster which will be used for communicating with the remote Cluster. | [optional] [readonly] 
**multi_tenancy_enabled** | **bool** | Specifies if the Remote Cluster has Multi-Tenancy enabled. | [optional] 
**network_interface** | **str** | Specifies the name of the network interfaces to use for communicating with the Remote Cluster. | [optional] 
**purpose** | **List[str]** | Specifies the purpose for which the remote cluster is being registered. | [optional] 
**replication_params** | [**ReplicationParams**](ReplicationParams.md) |  | [optional] 
**supported_aes_encryption_mode** | **str** | Specifies the AES Encryption mode of the remote cluster. | [optional] 
**tenant_storage_domain_sharing_enabled** | **bool** | Specifies if Tenant Storage Domain sharing is enabled on the Remote Cluster. | [optional] 
**tls_enabled** | **bool** | Specifies if TLS is enabled on the Remote Cluster. | [optional] 
**node_addresses** | **List[str]** | Specifies the VIP or IP addresses of the Nodes on the Remote Cluster to connect with. Hostnames are not supported. | [optional] 
**password** | **str** | Specifies the password for Cohesity user to use when connecting to the Remote Cluster. | [optional] 
**username** | **str** | Specifies the Cohesity user name used to connect to the Remote Cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_remote_cluster_params import UpdateRemoteClusterParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRemoteClusterParams from a JSON string
update_remote_cluster_params_instance = UpdateRemoteClusterParams.from_json(json)
# print the JSON string representation of the object
print(UpdateRemoteClusterParams.to_json())

# convert the object into a dict
update_remote_cluster_params_dict = update_remote_cluster_params_instance.to_dict()
# create an instance of UpdateRemoteClusterParams from a dict
update_remote_cluster_params_from_dict = UpdateRemoteClusterParams.from_dict(update_remote_cluster_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


