# CommonObjectsActionParams

Specifies the common action params needed for performing bulk actions on list of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_map** | [**List[ActionObjectMapping]**](ActionObjectMapping.md) | Specifies the objectMap that will be used to perform bulk actions such as linking and unlinking. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_objects_action_params import CommonObjectsActionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonObjectsActionParams from a JSON string
common_objects_action_params_instance = CommonObjectsActionParams.from_json(json)
# print the JSON string representation of the object
print(CommonObjectsActionParams.to_json())

# convert the object into a dict
common_objects_action_params_dict = common_objects_action_params_instance.to_dict()
# create an instance of CommonObjectsActionParams from a dict
common_objects_action_params_from_dict = CommonObjectsActionParams.from_dict(common_objects_action_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


