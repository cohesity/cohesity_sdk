# ViewRecoverFileAndFolderInfo

Specifies the info about the view files and folders to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str** | Specifies the absolute path to the file or folder. | 
**destination_dir** | **str** | Specifies the destination directory where the file/directory was copied. | [optional] [readonly] 
**is_directory** | **bool** | Specifies whether this is a directory or not. | [optional] 
**is_view_file_recovery** | **bool** | Specify if the recovery is of type view file/folder. | [optional] 
**messages** | **List[str]** | Specify error messages about the file during recovery. | [optional] [readonly] 
**status** | **str** | Specifies the recovery status for this file or folder. | [optional] [readonly] 
**inode_id** | **int** | Specifies the source inode number of the file being recovered. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_recover_file_and_folder_info import ViewRecoverFileAndFolderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ViewRecoverFileAndFolderInfo from a JSON string
view_recover_file_and_folder_info_instance = ViewRecoverFileAndFolderInfo.from_json(json)
# print the JSON string representation of the object
print(ViewRecoverFileAndFolderInfo.to_json())

# convert the object into a dict
view_recover_file_and_folder_info_dict = view_recover_file_and_folder_info_instance.to_dict()
# create an instance of ViewRecoverFileAndFolderInfo from a dict
view_recover_file_and_folder_info_from_dict = ViewRecoverFileAndFolderInfo.from_dict(view_recover_file_and_folder_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


