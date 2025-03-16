# ObjectIdentifier

Specifies the basic info to identify an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str** | Specifies the environment of the object. | [optional] 
**id** | **int** | Specifies object id. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**source_id** | **int** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str** | Specifies registered source name to which object belongs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_identifier import ObjectIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectIdentifier from a JSON string
object_identifier_instance = ObjectIdentifier.from_json(json)
# print the JSON string representation of the object
print(ObjectIdentifier.to_json())

# convert the object into a dict
object_identifier_dict = object_identifier_instance.to_dict()
# create an instance of ObjectIdentifier from a dict
object_identifier_from_dict = ObjectIdentifier.from_dict(object_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


