# RemoteClusterParams

Specifies the parameters to update a Remote Cluster config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_register_target** | **bool, none_type** | Specifies if the Tx clusters should be automatically registered at the Rx site. | [optional]  if omitted the server will use the default value of False
**cluster_id** | **int, none_type** | Specifies the Remote Cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int, none_type** | Specifies the Remote Cluster incarnation id. | [optional] [readonly] 
**cluster_name** | **str, none_type** | Specifies the Remote Cluster name. | [optional] [readonly] 
**description** | **str, none_type** | Specifies any additional information if needed. | [optional] 
**effective_aes_encryption_mode** | **str, none_type** | Specifies the effective AES Encryption mode negotiated between local and the remote cluster. | [optional] 
**is_auto_registered** | **bool, none_type** | Specifies if the Remote Cluster was registered automatically or manually. | [optional] [readonly] 
**local_addresses** | **[str]** | Specifies the IP addresses of the interfaces in the local Cluster which will be used for communicating with the remote Cluster. | [optional] [readonly] 
**multi_tenancy_enabled** | **bool, none_type** | Specifies if the Remote Cluster has Multi-Tenancy enabled. | [optional] 
**network_interface** | **str, none_type** | Specifies the name of the network interfaces to use for communicating with the Remote Cluster. | [optional] 
**purpose** | **[str], none_type** | Specifies the purpose for which the remote cluster is being registered. | [optional] 
**replication_params** | [**ReplicationParams**](ReplicationParams.md) |  | [optional] 
**supported_aes_encryption_mode** | **str, none_type** | Specifies the AES Encryption mode of the remote cluster. | [optional] 
**tenant_storage_domain_sharing_enabled** | **bool, none_type** | Specifies if Tenant Storage Domain sharing is enabled on the Remote Cluster. | [optional] 
**tls_enabled** | **bool, none_type** | Specifies if TLS is enabled on the Remote Cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


