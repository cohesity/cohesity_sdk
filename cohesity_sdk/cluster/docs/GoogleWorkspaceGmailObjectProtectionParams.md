# GoogleWorkspaceGmailObjectProtectionParams

Specifies the params to create a User Gmail Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[GoogleWorkspaceObjectProtectionObjectParams]**](GoogleWorkspaceObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.google_workspace_gmail_object_protection_params import GoogleWorkspaceGmailObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceGmailObjectProtectionParams from a JSON string
google_workspace_gmail_object_protection_params_instance = GoogleWorkspaceGmailObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceGmailObjectProtectionParams.to_json())

# convert the object into a dict
google_workspace_gmail_object_protection_params_dict = google_workspace_gmail_object_protection_params_instance.to_dict()
# create an instance of GoogleWorkspaceGmailObjectProtectionParams from a dict
google_workspace_gmail_object_protection_params_from_dict = GoogleWorkspaceGmailObjectProtectionParams.from_dict(google_workspace_gmail_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


