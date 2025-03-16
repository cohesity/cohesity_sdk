# ObjectStringIdentifier

Specifies an ID generated to uniquely identify an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**int_id** | **int** | Specifies the unique integer entity id. This is unique across one cluster. Two different Cohesity clusters may have same int_id for two different entities. | [optional] 
**string_ids** | [**StringEntityIds**](StringEntityIds.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_string_identifier import ObjectStringIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStringIdentifier from a JSON string
object_string_identifier_instance = ObjectStringIdentifier.from_json(json)
# print the JSON string representation of the object
print(ObjectStringIdentifier.to_json())

# convert the object into a dict
object_string_identifier_dict = object_string_identifier_instance.to_dict()
# create an instance of ObjectStringIdentifier from a dict
object_string_identifier_from_dict = ObjectStringIdentifier.from_dict(object_string_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


