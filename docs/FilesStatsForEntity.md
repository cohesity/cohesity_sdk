# FilesStatsForEntity

Specifies the files stats for an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id of the entity. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id of the entity. | [optional] 
**entity_id** | **int** | Specifies the entity id. | [optional] 
**entity_name** | **str** | Specifies the entity name. | [optional] 
**entity_type** | **str** | Specifies the entity type. | [optional] 
**files_stats** | [**List[FileStats]**](FileStats.md) | Specifies a list of files stats for the entity. | [optional] 

## Example

```python
from cohesity_sdk.models.files_stats_for_entity import FilesStatsForEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FilesStatsForEntity from a JSON string
files_stats_for_entity_instance = FilesStatsForEntity.from_json(json)
# print the JSON string representation of the object
print(FilesStatsForEntity.to_json())

# convert the object into a dict
files_stats_for_entity_dict = files_stats_for_entity_instance.to_dict()
# create an instance of FilesStatsForEntity from a dict
files_stats_for_entity_from_dict = FilesStatsForEntity.from_dict(files_stats_for_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


