# RemoveDisk

Specifies details of disk removal response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_cleared_pre_check_result** | **bool, none_type** | If true, pre check results have been cleared. | [optional]  if omitted the server will use the default value of False
**id** | **int, none_type** | Specifies id of the disk. | [optional] 
**marked_for_removal** | **bool, none_type** | If true, Disk is marked for removal. | [optional] 
**timestamp_secs** | **int, none_type** | Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds). | [optional] 
**validation_checks** | [**[PreCheckValidation], none_type**](PreCheckValidation.md) | Specifies the pre-check validations results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


