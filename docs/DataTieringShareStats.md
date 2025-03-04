# DataTieringShareStats

Specifies the source shares analysis stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_time_tag** | **str** | Specifies the access time bucket. | [optional] 
**file_count** | **int** | Specifies the file count. | [optional] 
**file_size_tag** | **str** | Specifies the file size bucket. | [optional] 
**file_type_tag** | **str** | Specifies the file type bucket. | [optional] 
**id** | **int** | Specifies the unique identifer for stat. | [optional] 
**mod_time_tag** | **str** | Specifies the modification time bucket. | [optional] 
**total_size** | **int** | Specifies the total count. | [optional] 

## Example

```python
from cohesity_sdk.models.data_tiering_share_stats import DataTieringShareStats

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringShareStats from a JSON string
data_tiering_share_stats_instance = DataTieringShareStats.from_json(json)
# print the JSON string representation of the object
print(DataTieringShareStats.to_json())

# convert the object into a dict
data_tiering_share_stats_dict = data_tiering_share_stats_instance.to_dict()
# create an instance of DataTieringShareStats from a dict
data_tiering_share_stats_from_dict = DataTieringShareStats.from_dict(data_tiering_share_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


