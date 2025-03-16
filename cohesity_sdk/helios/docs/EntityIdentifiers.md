# EntityIdentifiers

Specifies the identifiers for an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentation_link** | **str** | Specifies the link to documentation or additional information about the entity. This URL can be used to access more detailed information, guidelines, or metadata related to the entity id. It helps in understanding the context or usage of the entity id. | [optional] 
**key** | **str** | Specifies the type of identifier. For example, a Virtual Machine (VM) can be identified through various types of IDs, such as UUID, Managed Object Reference (moref), or other unique identifiers. | [optional] 
**value** | **str** | Specifies the value of the identifier corresponding to the type specified in the key. | [optional] 
**version** | **int** | Specifies the version number associated with this EntityIdentifier | [optional] 

## Example

```python
from cohesity_sdk.helios.models.entity_identifiers import EntityIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of EntityIdentifiers from a JSON string
entity_identifiers_instance = EntityIdentifiers.from_json(json)
# print the JSON string representation of the object
print(EntityIdentifiers.to_json())

# convert the object into a dict
entity_identifiers_dict = entity_identifiers_instance.to_dict()
# create an instance of EntityIdentifiers from a dict
entity_identifiers_from_dict = EntityIdentifiers.from_dict(entity_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


