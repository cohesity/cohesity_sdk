# VirtualDiskInformation

Specifies the details about a Virtual Disk within a VM, containing basic info about it and its corresponding controller.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **str, none_type** | Specifies original disk id. This is sufficient to identify the disk information. | [optional] 
**disk_info** | [**DiskInfo**](DiskInfo.md) |  | [optional] 
**disk_location** | [**Object**](Object.md) |  | [optional] 
**disk_size_in_bytes** | **int, none_type** | Specifies size of the virtual disk in bytes. | [optional] 
**file_path** | **str, none_type** | Specifies the original file path if applicable. | [optional] 
**mount_points** | **[str], none_type** | Specifies the list of mount points. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


