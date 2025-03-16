# AssociateEntityMetadataRequest

Specifies the parameters to associate metadata with entities in the entity hierarchy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_list** | [**List[EntityMetadataParams]**](EntityMetadataParams.md) | Specifies a list of entity and associated metadata mappings. | 
**source_id** | **int** | Specifies the source id of the entities vector whose metadata is being updated. | 

## Example

```python
from cohesity_sdk.helios.models.associate_entity_metadata_request import AssociateEntityMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateEntityMetadataRequest from a JSON string
associate_entity_metadata_request_instance = AssociateEntityMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(AssociateEntityMetadataRequest.to_json())

# convert the object into a dict
associate_entity_metadata_request_dict = associate_entity_metadata_request_instance.to_dict()
# create an instance of AssociateEntityMetadataRequest from a dict
associate_entity_metadata_request_from_dict = AssociateEntityMetadataRequest.from_dict(associate_entity_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


