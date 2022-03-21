# VcenterRegistrationParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | **str, none_type** | Specifies the CA certificate to enable SSL communication between host and cluster. | [optional] 
**use_vm_bios_uuid** | **bool, none_type** | Specifies to use VM BIOS UUID to track virtual machines in the host. | [optional] 
**min_free_datastore_space_for_backup_gb** | **int, none_type** | Specifies the minimum free space (in GB) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 
**throttling_params** | [**VmwareThrottlingParams**](VmwareThrottlingParams.md) |  | [optional] 
**data_store_params** | [**[DatastoreParams], none_type**](DatastoreParams.md) | Specifies datastore specific parameters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


