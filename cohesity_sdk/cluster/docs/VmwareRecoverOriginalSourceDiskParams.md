# VmwareRecoverOriginalSourceDiskParams

Specifies disk specific parameters for performing a disk recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_uuid** | **str, none_type** | Specifies the UUID of the source disk being recovered. | 
**overwrite_original_disk** | **bool, none_type** | Specifies whether or not to overwrite the original disk. If this is set to true, then datastoreId should not be specified. Otherwise, datastoreId must be specified. | [optional] 
**datastore_id** | **int, none_type** | Specifies the ID of the datastore on which the specified disk will be spun up. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


