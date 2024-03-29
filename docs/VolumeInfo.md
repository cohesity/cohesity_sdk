# VolumeInfo

Specifies info of logical volume (filesystem).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filesystem_type** | **str, none_type** | Specifies the filesystem type. | [optional] 
**filesystem_uuid** | **str, none_type** | Specifies the filesystem uuid. | [optional] 
**is_dedupe** | **bool, none_type** | Specifies if this is NTFS dedupe volume | [optional] 
**is_supported** | **bool, none_type** | Specifies if this volume is supported. | [optional] 
**logical_volume_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the logical volume info. This fields is for &#39;LVM&#39; and &#39;LDM&#39; volume type only. | [optional] 
**name** | **str, none_type** | Specifies the volume name. | [optional] 
**volume_guid** | **str, none_type** | Specifies the volume guid. | [optional] 
**volume_size_in_bytes** | **int, none_type** | Specifies volume size in bytes. | [optional] 
**volume_type** | **str, none_type** | Specifies the volume type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


