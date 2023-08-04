# MSSQLVolumeProtectionGroupHostParams

Specifies the host specific parameters for a host container in this protection group. Objects specified here should only be MSSQL root containers and will not be protected unless they are also specified in the 'objects' list. This list is just for specifying source level settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **int, none_type** | Specifies the id of the host container on which databases are hosted. | 
**host_name** | **str, none_type** | Specifies the name of the host container on which databases are hosted. | [optional] [readonly] 
**volume_guids** | **[str], none_type** | Specifies the list of volume GUIDs to be protected. If not specified, all the volumes of the host will be protected. Note that volumes of host on which databases are hosted are protected even if its not mentioned in this list. | [optional] 
**enable_system_backup** | **bool, none_type** | Specifies whether to enable system/bmr backup using 3rd party tools installed on agent host. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


