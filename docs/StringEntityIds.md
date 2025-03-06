# StringEntityIds

Specifies the model to uniquely id an entity. This model also specifies the previous ids for a given entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_id** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**latest_source_generated_ids** | [**List[EntityIdentifiers]**](EntityIdentifiers.md) | Specifies the latest source-generated ID for an entity. It provides the most current identifier assigned by the primary source system. | [optional] 
**previous_ids** | [**List[VersionInfo]**](VersionInfo.md) | Specifies all the StringIds previously assigned to this entity. Note that it doesn&#39;t contain the latest id. | [optional] 
**previous_source_generated_ids** | [**List[EntityIdentifiers]**](EntityIdentifiers.md) | Specifies a list of previously assigned source-generated IDs for an entity. It helps in tracking the historical identifiers that were assigned by the primary source system. This can be useful for audit trails, debugging, or migration purposes. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.string_entity_ids import StringEntityIds

# TODO update the JSON string below
json = "{}"
# create an instance of StringEntityIds from a JSON string
string_entity_ids_instance = StringEntityIds.from_json(json)
# print the JSON string representation of the object
print(StringEntityIds.to_json())

# convert the object into a dict
string_entity_ids_dict = string_entity_ids_instance.to_dict()
# create an instance of StringEntityIds from a dict
string_entity_ids_from_dict = StringEntityIds.from_dict(string_entity_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


