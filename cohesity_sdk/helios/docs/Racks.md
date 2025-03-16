# Racks

Specifies info about list of racks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**racks** | [**List[Rack]**](Rack.md) | Specifies list of racks | [optional] 

## Example

```python
from cohesity_sdk.helios.models.racks import Racks

# TODO update the JSON string below
json = "{}"
# create an instance of Racks from a JSON string
racks_instance = Racks.from_json(json)
# print the JSON string representation of the object
print(Racks.to_json())

# convert the object into a dict
racks_dict = racks_instance.to_dict()
# create an instance of Racks from a dict
racks_from_dict = Racks.from_dict(racks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


