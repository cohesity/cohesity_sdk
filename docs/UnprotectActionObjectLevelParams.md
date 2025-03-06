# UnprotectActionObjectLevelParams

Specifies the request parameters for Unprotect action on a Protected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**delete_all_snapshots** | **bool** | Specifies whether to delete all snapshots along with unprotecting object protection. If set to true, all snapshots will be deleted and no more recoverable. | [optional] 
**force_unprotect** | **bool** | If specified as true then it will cancel the ongoing runs and immediatly unprotect. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.unprotect_action_object_level_params import UnprotectActionObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of UnprotectActionObjectLevelParams from a JSON string
unprotect_action_object_level_params_instance = UnprotectActionObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(UnprotectActionObjectLevelParams.to_json())

# convert the object into a dict
unprotect_action_object_level_params_dict = unprotect_action_object_level_params_instance.to_dict()
# create an instance of UnprotectActionObjectLevelParams from a dict
unprotect_action_object_level_params_from_dict = UnprotectActionObjectLevelParams.from_dict(unprotect_action_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


