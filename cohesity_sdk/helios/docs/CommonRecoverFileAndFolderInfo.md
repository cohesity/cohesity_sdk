# CommonRecoverFileAndFolderInfo

Specifies the information about the specific file or folder to recover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str** | Specifies the absolute path to the file or folder. | 
**destination_dir** | **str** | Specifies the destination directory where the file/directory was copied. | [optional] [readonly] 
**is_directory** | **bool** | Specifies whether this is a directory or not. | [optional] 
**is_view_file_recovery** | **bool** | Specify if the recovery is of type view file/folder. | [optional] 
**messages** | **List[str]** | Specify error messages about the file during recovery. | [optional] [readonly] 
**status** | **str** | Specifies the recovery status for this file or folder. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.common_recover_file_and_folder_info import CommonRecoverFileAndFolderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommonRecoverFileAndFolderInfo from a JSON string
common_recover_file_and_folder_info_instance = CommonRecoverFileAndFolderInfo.from_json(json)
# print the JSON string representation of the object
print(CommonRecoverFileAndFolderInfo.to_json())

# convert the object into a dict
common_recover_file_and_folder_info_dict = common_recover_file_and_folder_info_instance.to_dict()
# create an instance of CommonRecoverFileAndFolderInfo from a dict
common_recover_file_and_folder_info_from_dict = CommonRecoverFileAndFolderInfo.from_dict(common_recover_file_and_folder_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


