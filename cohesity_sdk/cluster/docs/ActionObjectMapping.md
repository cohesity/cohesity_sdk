# ActionObjectMapping

Specifies the object paring for performing action on list of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_object_id** | **int** | Specifies the destination object id. | [optional] 
**source_object_id** | **int** | Specifies the source object id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.action_object_mapping import ActionObjectMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ActionObjectMapping from a JSON string
action_object_mapping_instance = ActionObjectMapping.from_json(json)
# print the JSON string representation of the object
print(ActionObjectMapping.to_json())

# convert the object into a dict
action_object_mapping_dict = action_object_mapping_instance.to_dict()
# create an instance of ActionObjectMapping from a dict
action_object_mapping_from_dict = ActionObjectMapping.from_dict(action_object_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


