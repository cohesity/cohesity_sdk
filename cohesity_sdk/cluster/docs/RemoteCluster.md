# RemoteCluster

Specifies a Remote Cluster config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_register_target** | **bool, none_type** | Specifies if the Tx clusters should be automatically registered at the Rx site. | [optional]  if omitted the server will use the default value of False
**cluster_id** | **int, none_type** | Specifies the Remote Cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int, none_type** | Specifies the Remote Cluster incarnation id. | [optional] [readonly] 
**cluster_name** | **str, none_type** | Specifies the Remote Cluster name. | [optional] [readonly] 
**description** | **str, none_type** | Specifies any additional information if needed. | [optional] 
**is_auto_registered** | **bool, none_type** | Specifies if the Remote Cluster was registered automatically or manually. | [optional] [readonly] 
**local_addresses** | **[str]** | Specifies the IP addresses of the interfaces in the local Cluster which will be used for communicating with the remote Cluster. | [optional] [readonly] 
**network_interface** | **str, none_type** | Specifies the name of the network interfaces to use for communicating with the Remote Cluster. | [optional] 
**purpose** | **[str], none_type** | Specifies the purpose for which the remote cluster is being registered. | [optional] 
**replication_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the replication config for a Remote Cluster. Required when usedForReplication is set to true. | [optional] 
**node_addresses** | **[str]** | Specifies the VIP or IP addresses of the Nodes on the Remote Cluster to connect with. Hostnames are not supported. | [optional] 
**password** | **str, none_type** | Specifies the password for Cohesity user to use when connecting to the Remote Cluster. | [optional] 
**username** | **str** | Specifies the Cohesity user name used to connect to the Remote Cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


