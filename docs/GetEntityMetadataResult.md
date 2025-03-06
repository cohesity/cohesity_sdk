# GetEntityMetadataResult

Specifies the response for the GetEntityMetadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_list** | [**List[EntityMetadataParams]**](EntityMetadataParams.md) | Specifies the list of entities with thier metadata. | [optional] 
**source_id** | **int** | Specifies the source id of the entities whose metadata is being requested. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_entity_metadata_result import GetEntityMetadataResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityMetadataResult from a JSON string
get_entity_metadata_result_instance = GetEntityMetadataResult.from_json(json)
# print the JSON string representation of the object
print(GetEntityMetadataResult.to_json())

# convert the object into a dict
get_entity_metadata_result_dict = get_entity_metadata_result_instance.to_dict()
# create an instance of GetEntityMetadataResult from a dict
get_entity_metadata_result_from_dict = GetEntityMetadataResult.from_dict(get_entity_metadata_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


