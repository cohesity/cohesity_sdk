# UnprotectActionObjectLevelResponse

Specifies the infomration about status of Unprotect action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.unprotect_action_object_level_response import UnprotectActionObjectLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnprotectActionObjectLevelResponse from a JSON string
unprotect_action_object_level_response_instance = UnprotectActionObjectLevelResponse.from_json(json)
# print the JSON string representation of the object
print(UnprotectActionObjectLevelResponse.to_json())

# convert the object into a dict
unprotect_action_object_level_response_dict = unprotect_action_object_level_response_instance.to_dict()
# create an instance of UnprotectActionObjectLevelResponse from a dict
unprotect_action_object_level_response_from_dict = UnprotectActionObjectLevelResponse.from_dict(unprotect_action_object_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


