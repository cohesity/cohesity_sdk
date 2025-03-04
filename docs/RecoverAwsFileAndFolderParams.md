# RecoverAwsFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverFileAndFolder**](AwsTargetParamsForRecoverFileAndFolder.md) |  | [optional] 
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.models.recover_aws_file_and_folder_params import RecoverAwsFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsFileAndFolderParams from a JSON string
recover_aws_file_and_folder_params_instance = RecoverAwsFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsFileAndFolderParams.to_json())

# convert the object into a dict
recover_aws_file_and_folder_params_dict = recover_aws_file_and_folder_params_instance.to_dict()
# create an instance of RecoverAwsFileAndFolderParams from a dict
recover_aws_file_and_folder_params_from_dict = RecoverAwsFileAndFolderParams.from_dict(recover_aws_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


