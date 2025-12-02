# ResourceInstance

This object represents information about a specific resource instance belonging to a specific group, version and kind.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | The id of the specific entity to be backed up or restored. | [optional] 
**name** | **str** | The name of the specific entity/resource to be backed up or restored. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.resource_instance import ResourceInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceInstance from a JSON string
resource_instance_instance = ResourceInstance.from_json(json)
# print the JSON string representation of the object
print(ResourceInstance.to_json())

# convert the object into a dict
resource_instance_dict = resource_instance_instance.to_dict()
# create an instance of ResourceInstance from a dict
resource_instance_from_dict = ResourceInstance.from_dict(resource_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


