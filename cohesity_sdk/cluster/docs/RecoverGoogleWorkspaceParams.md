# RecoverGoogleWorkspaceParams

Specifies the recovery options specific to Google Workspace environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | [optional] 
**recover_gmail_params** | [**RecoverGmailParams**](RecoverGmailParams.md) |  | [optional] 
**recover_google_drive_params** | [**RecoverGoogleDriveParams**](RecoverGoogleDriveParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_google_workspace_params import RecoverGoogleWorkspaceParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGoogleWorkspaceParams from a JSON string
recover_google_workspace_params_instance = RecoverGoogleWorkspaceParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGoogleWorkspaceParams.to_json())

# convert the object into a dict
recover_google_workspace_params_dict = recover_google_workspace_params_instance.to_dict()
# create an instance of RecoverGoogleWorkspaceParams from a dict
recover_google_workspace_params_from_dict = RecoverGoogleWorkspaceParams.from_dict(recover_google_workspace_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


