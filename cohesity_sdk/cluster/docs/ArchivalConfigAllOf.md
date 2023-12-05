# ArchivalConfigAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int, none_type** | Specifies the Archival target to copy the Snapshots to. | 
**extended_retention** | [**[ExtendedRetentionPolicy], none_type**](ExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the archived backup. Archived backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**target_name** | **str, none_type** | Specifies the Archival target name where Snapshots are copied. | [optional] [readonly] 
**target_type** | **str, none_type** | Specifies the Archival target type where Snapshots are copied. | [optional] [readonly] 
**tier_settings** | [**TierLevelSettings**](TierLevelSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


