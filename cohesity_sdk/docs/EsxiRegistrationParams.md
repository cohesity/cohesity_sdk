# EsxiRegistrationParams

Specifies parameters to register VMware ESXi host.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Specifies the username to access target entity. | 
**password** | **str** | Specifies the password to access target entity. | 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**description** | **str, none_type** | Specifies the description of the source being registered. | [optional] 
**min_free_datastore_space_for_backup_gb** | **int, none_type** | Specifies the minimum free space (in GB) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 
**min_free_datastore_space_for_backup_percentage** | **int, none_type** | Specifies the minimum free space (in percentage) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 
**max_concurrent_streams** | **int, none_type** | If this value is &gt; 0 and the number of streams concurrently active on a datastore is equal to it, then any further requests to access the datastore would be denied until the number of active streams reduces. This applies for all the datastores in the specified host. | [optional] 
**data_store_params** | [**[DatastoreParams], none_type**](DatastoreParams.md) | Specifies the datastore specific params. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


