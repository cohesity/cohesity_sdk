# Rack

Specifies information about rack.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_ids** | **List[int]** | List of chassis ids that are part of the rack. | [optional] 
**id** | **int** | Specifies unique id of the rack. | [optional] 
**location** | **str** | Specifies location of the rack. | [optional] 
**name** | **str** | Specifies name of the rack | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.rack import Rack

# TODO update the JSON string below
json = "{}"
# create an instance of Rack from a JSON string
rack_instance = Rack.from_json(json)
# print the JSON string representation of the object
print(Rack.to_json())

# convert the object into a dict
rack_dict = rack_instance.to_dict()
# create an instance of Rack from a dict
rack_from_dict = Rack.from_dict(rack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


