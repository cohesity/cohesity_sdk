# PrimaryArchivalTarget

Specifies the primary archival settings. Mainly used for cloud direct archive (CAD) policy where primary backup is stored on archival target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int, none_type** | Specifies the Archival target id to take primary backup. | 
**target_name** | **str, none_type** | Specifies the Archival target name where Snapshots are copied. | [optional] [readonly] 
**tier_settings** | [**TierLevelSettings**](TierLevelSettings.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


