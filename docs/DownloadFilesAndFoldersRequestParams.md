# DownloadFilesAndFoldersRequestParams

Specifies the parameters to create a download files and folders Recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**List[FilesAndFoldersObject]**](FilesAndFoldersObject.md) | Specifies the list of files and folders to download. | 
**glacier_retrieval_type** | **str** | Specifies the glacier retrieval type when restoring or downloding files or folders from a Glacier-based cloud snapshot. | [optional] 
**name** | **str** | Specifies the name of the recovery task. This field must be set and must be a unique name. | 
**object** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | 
**parent_recovery_id** | **str** | If current recovery is child task triggered through another parent recovery operation, then this field will specify the id of the parent recovery. | [optional] 

## Example

```python
from cohesity_sdk.models.download_files_and_folders_request_params import DownloadFilesAndFoldersRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadFilesAndFoldersRequestParams from a JSON string
download_files_and_folders_request_params_instance = DownloadFilesAndFoldersRequestParams.from_json(json)
# print the JSON string representation of the object
print(DownloadFilesAndFoldersRequestParams.to_json())

# convert the object into a dict
download_files_and_folders_request_params_dict = download_files_and_folders_request_params_instance.to_dict()
# create an instance of DownloadFilesAndFoldersRequestParams from a dict
download_files_and_folders_request_params_from_dict = DownloadFilesAndFoldersRequestParams.from_dict(download_files_and_folders_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


