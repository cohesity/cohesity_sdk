# GoogleWorkspaceObjectProtectionParams

Specifies the parameters which are specific to Google Workspace Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gmail_object_protection_params** | [**GoogleWorkspaceGmailObjectProtectionParams**](GoogleWorkspaceGmailObjectProtectionParams.md) |  | [optional] 
**google_drive_object_protection_params** | [**GoogleWorkspaceGoogleDriveObjectProtectionParams**](GoogleWorkspaceGoogleDriveObjectProtectionParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the Google Workspace Object Protection type. | 

## Example

```python
from cohesity_sdk.cluster.models.google_workspace_object_protection_params import GoogleWorkspaceObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceObjectProtectionParams from a JSON string
google_workspace_object_protection_params_instance = GoogleWorkspaceObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceObjectProtectionParams.to_json())

# convert the object into a dict
google_workspace_object_protection_params_dict = google_workspace_object_protection_params_instance.to_dict()
# create an instance of GoogleWorkspaceObjectProtectionParams from a dict
google_workspace_object_protection_params_from_dict = GoogleWorkspaceObjectProtectionParams.from_dict(google_workspace_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


