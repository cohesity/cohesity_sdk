# GoogleWorkspaceProtectionGroupObjectParams

Specifies the object parameters to create a Google Workspace Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.google_workspace_protection_group_object_params import GoogleWorkspaceProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProtectionGroupObjectParams from a JSON string
google_workspace_protection_group_object_params_instance = GoogleWorkspaceProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProtectionGroupObjectParams.to_json())

# convert the object into a dict
google_workspace_protection_group_object_params_dict = google_workspace_protection_group_object_params_instance.to_dict()
# create an instance of GoogleWorkspaceProtectionGroupObjectParams from a dict
google_workspace_protection_group_object_params_from_dict = GoogleWorkspaceProtectionGroupObjectParams.from_dict(google_workspace_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


