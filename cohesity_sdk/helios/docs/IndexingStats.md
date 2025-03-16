# IndexingStats

Metric related to file indexes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_document_count** | **int** | Specifies the number of files deleted for this run. | [optional] 
**new_document_count** | **int** | Specifies the number of files added for this run. | [optional] 
**not_updated_document_count** | **int** | Specifies the number of files not updated for this run. | [optional] 
**total_files** | **int** | Specifies the count of files in this run. | [optional] 
**updated_document_count** | **int** | Specifies the number of files updated for this run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.indexing_stats import IndexingStats

# TODO update the JSON string below
json = "{}"
# create an instance of IndexingStats from a JSON string
indexing_stats_instance = IndexingStats.from_json(json)
# print the JSON string representation of the object
print(IndexingStats.to_json())

# convert the object into a dict
indexing_stats_dict = indexing_stats_instance.to_dict()
# create an instance of IndexingStats from a dict
indexing_stats_from_dict = IndexingStats.from_dict(indexing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


