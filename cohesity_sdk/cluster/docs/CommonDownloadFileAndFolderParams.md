# CommonDownloadFileAndFolderParams

Specifies the parameters to download files and folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_path** | **str** | Specifies the path location to download the files and folders. | [optional] 
**expiry_time_usecs** | **int** | Specifies the time upto which the download link is available. | [optional] 
**files_and_folders** | [**List[CommonRecoverFileAndFolderInfo]**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_download_file_and_folder_params import CommonDownloadFileAndFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDownloadFileAndFolderParams from a JSON string
common_download_file_and_folder_params_instance = CommonDownloadFileAndFolderParams.from_json(json)
# print the JSON string representation of the object
print(CommonDownloadFileAndFolderParams.to_json())

# convert the object into a dict
common_download_file_and_folder_params_dict = common_download_file_and_folder_params_instance.to_dict()
# create an instance of CommonDownloadFileAndFolderParams from a dict
common_download_file_and_folder_params_from_dict = CommonDownloadFileAndFolderParams.from_dict(common_download_file_and_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


