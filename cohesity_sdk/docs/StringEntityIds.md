# StringEntityIds

Specifies the model to uniquely id an entity. This model also specifies the previous ids for a given entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_id** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**latest_source_generated_ids** | [**[EntityIdentifiers], none_type**](EntityIdentifiers.md) | Specifies the latest source-generated ID for an entity. It provides the most current identifier assigned by the primary source system. | [optional] 
**previous_ids** | [**[VersionInfo], none_type**](VersionInfo.md) | Specifies all the StringIds previously assigned to this entity. Note that it doesn&#39;t contain the latest id. | [optional] 
**previous_source_generated_ids** | [**[EntityIdentifiers], none_type**](EntityIdentifiers.md) | Specifies a list of previously assigned source-generated IDs for an entity. It helps in tracking the historical identifiers that were assigned by the primary source system. This can be useful for audit trails, debugging, or migration purposes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


