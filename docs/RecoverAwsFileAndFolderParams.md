# RecoverAwsFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**[CommonRecoverFileAndFolderInfo], none_type**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAWS"
**aws_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to recover to an AWS target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


