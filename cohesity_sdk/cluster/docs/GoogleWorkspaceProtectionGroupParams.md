# GoogleWorkspaceProtectionGroupParams

Specifies the parameters which are specific to Google Workspace related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**google_drive_protection_type_params** | **object** | Specifies the parameters which are specific to Google Workspace Google Drive related Protection Groups. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[GoogleWorkspaceProtectionGroupObjectParams]**](GoogleWorkspaceProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**protection_types** | **str** | Specifies the Google Workspace Protection Group types. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.google_workspace_protection_group_params import GoogleWorkspaceProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProtectionGroupParams from a JSON string
google_workspace_protection_group_params_instance = GoogleWorkspaceProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProtectionGroupParams.to_json())

# convert the object into a dict
google_workspace_protection_group_params_dict = google_workspace_protection_group_params_instance.to_dict()
# create an instance of GoogleWorkspaceProtectionGroupParams from a dict
google_workspace_protection_group_params_from_dict = GoogleWorkspaceProtectionGroupParams.from_dict(google_workspace_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


