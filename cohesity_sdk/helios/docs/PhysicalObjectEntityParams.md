# PhysicalObjectEntityParams

Specifies the common parameters for physical objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_system_backup** | **bool** | Specifies if system backup was enabled for the source in a particular run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.physical_object_entity_params import PhysicalObjectEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalObjectEntityParams from a JSON string
physical_object_entity_params_instance = PhysicalObjectEntityParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalObjectEntityParams.to_json())

# convert the object into a dict
physical_object_entity_params_dict = physical_object_entity_params_instance.to_dict()
# create an instance of PhysicalObjectEntityParams from a dict
physical_object_entity_params_from_dict = PhysicalObjectEntityParams.from_dict(physical_object_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


