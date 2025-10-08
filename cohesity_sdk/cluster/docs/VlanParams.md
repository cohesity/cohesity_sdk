# VlanParams

Specifies VLAN params associated with the backup/restore operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_vlan** | **bool, none_type** | If this is set to true, then even if VLANs are configured on the system, the partition VIPs will be used for the restore. | [optional] 
**interface_name** | **str, none_type** | Interface group to use for backup/restore. If this is not specified, primary interface group for the cluster will be used. | [optional] 
**vlan_id** | **int, none_type** | If this is set, then the Cohesity host name or the IP address associated with this VLAN is used for mounting Cohesity&#39;s view on the remote host. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


