# AwsTargetParamsForRecoverS3

Specifies the parameters for an AWS recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_original_target** | **bool, none_type** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue restore on receiving error or not. Default is true. | [optional] 
**new_target_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the configuration for recovering to a new target. | [optional] 
**object_prefix** | **str, none_type** | Specifies the prefix to be added to all the objects being recovered. | [optional] 
**overwrite_existing** | **bool, none_type** | Specifies whether to override the existing objects. Default is false. | [optional] 
**preserve_attributes** | **bool, none_type** | Specifies whether to preserve the objects attributes at the time of restore. Default is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


