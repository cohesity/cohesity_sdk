# FilesStats

Specifies the files stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_size_distribution** | [**List[FileCount]**](FileCount.md) | Specifies the aggregated distribution by size of files stored in the Cohesity cluster. | [optional] 
**files_stats** | [**List[FilesStatsForEntity]**](FilesStatsForEntity.md) | Specifies a list of file stats for entities. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.files_stats import FilesStats

# TODO update the JSON string below
json = "{}"
# create an instance of FilesStats from a JSON string
files_stats_instance = FilesStats.from_json(json)
# print the JSON string representation of the object
print(FilesStats.to_json())

# convert the object into a dict
files_stats_dict = files_stats_instance.to_dict()
# create an instance of FilesStats from a dict
files_stats_from_dict = FilesStats.from_dict(files_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


