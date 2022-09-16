# RecoverProtectionGroupRunParams

Specifies the Protection Group Run params to recover. All the VM's that are successfully backed up by specified Runs will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_run_id** | **str, none_type** | Specifies the Protection Group Run id from which to recover VMs. All the VM&#39;s that are successfully protected by this Run will be recovered. | 
**protection_group_instance_id** | **int, none_type** | Specifies the Protection Group Instance id. | 
**archival_target_id** | **int, none_type** | Specifies the archival target id. If specified and Protection Group run has an archival snapshot then VMs are recovered from the specified archival snapshot. If not specified (default), VMs are recovered from local snapshot. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the local Protection Group id. In case of recovering a replication Run, this field should be provided with local Protection Group id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


