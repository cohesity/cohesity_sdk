# EsxiRegistrationParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_store_params** | [**[DatastoreParams], none_type**](DatastoreParams.md) | Specifies the datastore specific params. | [optional] 
**max_concurrent_streams** | **int, none_type** | If this value is &gt; 0 and the number of streams concurrently active on a datastore is equal to it, then any further requests to access the datastore would be denied until the number of active streams reduces. This applies for all the datastores in the specified host. | [optional] 
**min_free_datastore_space_for_backup_gb** | **int, none_type** | Specifies the minimum free space (in GB) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 
**min_free_datastore_space_for_backup_percentage** | **int, none_type** | Specifies the minimum free space (in percentage) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


