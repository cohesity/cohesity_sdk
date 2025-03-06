# AssociateEntityMetadataResult

Specifies the response for the AssociateEntityMetadataRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_list** | [**List[AssociateEntityMetadataResultParams]**](AssociateEntityMetadataResultParams.md) | Specifies the list of entity ids mapped to errors (if any). | [optional] 
**source_id** | **int** | Specifies the source id of the entities vector whose metadata is being updated. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.associate_entity_metadata_result import AssociateEntityMetadataResult

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateEntityMetadataResult from a JSON string
associate_entity_metadata_result_instance = AssociateEntityMetadataResult.from_json(json)
# print the JSON string representation of the object
print(AssociateEntityMetadataResult.to_json())

# convert the object into a dict
associate_entity_metadata_result_dict = associate_entity_metadata_result_instance.to_dict()
# create an instance of AssociateEntityMetadataResult from a dict
associate_entity_metadata_result_from_dict = AssociateEntityMetadataResult.from_dict(associate_entity_metadata_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


