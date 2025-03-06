# RecoverO365Params

Specifies the recovery options specific to Office 365 environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_chats_params** | [**DownloadChatsParams**](DownloadChatsParams.md) |  | [optional] 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | [optional] 
**recover_mailbox_params** | [**RecoverMailboxParams**](RecoverMailboxParams.md) |  | [optional] 
**recover_ms_group_params** | [**RecoverMsGroupParams**](RecoverMsGroupParams.md) |  | [optional] 
**recover_ms_team_params** | [**RecoverMsTeamParams**](RecoverMsTeamParams.md) |  | [optional] 
**recover_one_drive_params** | [**RecoverOneDriveParams**](RecoverOneDriveParams.md) |  | [optional] 
**recover_public_folders_params** | [**RecoverPublicFoldersParams**](RecoverPublicFoldersParams.md) |  | [optional] 
**recover_site_params** | [**RecoverSiteParams**](RecoverSiteParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_o365_params import RecoverO365Params

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverO365Params from a JSON string
recover_o365_params_instance = RecoverO365Params.from_json(json)
# print the JSON string representation of the object
print(RecoverO365Params.to_json())

# convert the object into a dict
recover_o365_params_dict = recover_o365_params_instance.to_dict()
# create an instance of RecoverO365Params from a dict
recover_o365_params_from_dict = RecoverO365Params.from_dict(recover_o365_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


