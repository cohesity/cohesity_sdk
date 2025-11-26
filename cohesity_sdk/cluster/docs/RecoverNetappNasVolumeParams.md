# RecoverNetappNasVolumeParams

Specifies the parameters to recover Netapp NAS volumes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**elastifile_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for an Elastifile recovery target. | [optional] 
**flashblade_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for a Flashblade recovery target. | [optional] 
**generic_nas_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for a generic NAS recovery target. | [optional] 
**gpfs_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for a GPFS recovery target. | [optional] 
**is_from_source_initiated_protection** | **bool, none_type** | Specifies if the snapshot trying to recover is from a source initiated protection. | [optional] 
**isilon_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for an Isilon recovery target. | [optional] 
**netapp_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for a Netapp recovery target. | [optional] 
**view_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for a Cohesity view recovery target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


