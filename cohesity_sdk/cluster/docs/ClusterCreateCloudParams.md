# ClusterCreateCloudParams

Params for Cloud Edition Cluster Creation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ips** | **[str], none_type** |  | 
**cluster_partition_hostname** | **str, none_type** | Hostname of the cluster partition. | [optional] 
**cluster_size** | **str, none_type** | Specifies the size of the cloud platforms. | [optional] 
**disk_all_nodes_reachable** | **[bool], none_type** | All nodes reachable property of the disks to designate. | [optional] 
**disk_component_exclusive** | **[str], none_type** | Component exclusive property of the disks to designate. | [optional] 
**disk_self_fault_tolerant** | **[bool], none_type** | Self fault tolerant property of the disks to designate. | [optional] 
**disk_serials** | **[str], none_type** | Serial number of the disks to designate properties. | [optional] 
**disk_tiers** | **[str], none_type** | Optional field. Tiers of the Disks to designate. | [optional] 
**enable_cloud_rf1** | **bool, none_type** | Specifies whether or not to enable software encryption | [optional] 
**encryption_config** | [**EncryptionConfigurationParams**](EncryptionConfigurationParams.md) |  | [optional] 
**ip_preference** | **int, none_type** | Specifies IP preference | [optional] 
**metadata_fault_tolerance** | **int, none_type** | Specifies the metadata fault tolerance. | [optional] 
**trust_domain** | **str, none_type** | Specifies Trust Domain used for Service Identity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


