# UdaObjectParams

Specifies the common parameters for UDA objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_entity_support** | **bool** | Specifies whether this Object belongs to a source having entity support. | [optional] 
**source_type** | **str** | Specifies the source type for Universal Data Adapter object. | [optional] 

## Example

```python
from cohesity_sdk.models.uda_object_params import UdaObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaObjectParams from a JSON string
uda_object_params_instance = UdaObjectParams.from_json(json)
# print the JSON string representation of the object
print(UdaObjectParams.to_json())

# convert the object into a dict
uda_object_params_dict = uda_object_params_instance.to_dict()
# create an instance of UdaObjectParams from a dict
uda_object_params_from_dict = UdaObjectParams.from_dict(uda_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


