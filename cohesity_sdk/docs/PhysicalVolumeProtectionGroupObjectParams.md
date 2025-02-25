# PhysicalVolumeProtectionGroupObjectParams

Specifies object parameters for creating physical volume Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object protected. | 
**enable_system_backup** | **bool, none_type** | Specifies whether or not to take a system backup. Applicable only for windows sources. | [optional] 
**excluded_vss_writers** | **[str], none_type** | Specifies writer names which should be excluded from physical volume based backups for a given source. | [optional] 
**name** | **str, none_type** | Specifies the name of the object protected. | [optional] [readonly] 
**volume_guids** | **[str]** | Specifies the list of GUIDs of volumes protected. If empty, then all volumes will be protected by default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


