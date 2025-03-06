# RemoteClusterParams

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

## Example

```python
from cohesity_sdk.cluster.models.remote_cluster_params import RemoteClusterParams

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteClusterParams from a JSON string
remote_cluster_params_instance = RemoteClusterParams.from_json(json)
# print the JSON string representation of the object
print(RemoteClusterParams.to_json())

# convert the object into a dict
remote_cluster_params_dict = remote_cluster_params_instance.to_dict()
# create an instance of RemoteClusterParams from a dict
remote_cluster_params_from_dict = RemoteClusterParams.from_dict(remote_cluster_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


