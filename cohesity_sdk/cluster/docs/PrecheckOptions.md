# PrecheckOptions

Specifies a list of precheck options for fortknox onprem vault configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cluster_storage_domains_encrypted** | **bool, none_type** | Specifies if encryption is enabled at cluster or all storage domains have encryption enabled. | [optional] 
**is_firewall_enabled** | **bool, none_type** | Specifies if firewall is enabled except for replication interface group with primary cluster IPs. | [optional] 
**is_local_user_mfa_enabled** | **bool, none_type** | Specifies if local user mfa is enabled. | [optional] 
**is_no_outgoing_replications_or_archivals** | **bool, none_type** | Specifies if the cluster does not have any policy with outgoing replication or archival. | [optional] 
**is_node_to_node_encryption_enabled** | **bool, none_type** | Specifies if node to node secure communication is enabled. | [optional] 
**is_support_channel_disabled** | **bool, none_type** | Specifies if support channel/reverse tunnel is disabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


