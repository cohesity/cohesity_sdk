# Keystones

Specifies a list of Keystones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keystones** | [**List[Keystone]**](Keystone.md) | Specifies a list of Keystones. | [optional] 

## Example

```python
from cohesity_sdk.models.keystones import Keystones

# TODO update the JSON string below
json = "{}"
# create an instance of Keystones from a JSON string
keystones_instance = Keystones.from_json(json)
# print the JSON string representation of the object
print(Keystones.to_json())

# convert the object into a dict
keystones_dict = keystones_instance.to_dict()
# create an instance of Keystones from a dict
keystones_from_dict = Keystones.from_dict(keystones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


