# GoogleWorkspaceObjectProtectionObjectParams

Specifies the object parameters to create a Google Workspace Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the ID of the objects to be excluded in the Object Protection. | [optional] 
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.google_workspace_object_protection_object_params import GoogleWorkspaceObjectProtectionObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceObjectProtectionObjectParams from a JSON string
google_workspace_object_protection_object_params_instance = GoogleWorkspaceObjectProtectionObjectParams.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceObjectProtectionObjectParams.to_json())

# convert the object into a dict
google_workspace_object_protection_object_params_dict = google_workspace_object_protection_object_params_instance.to_dict()
# create an instance of GoogleWorkspaceObjectProtectionObjectParams from a dict
google_workspace_object_protection_object_params_from_dict = GoogleWorkspaceObjectProtectionObjectParams.from_dict(google_workspace_object_protection_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


