# DataTieringShareInfo

Specifies the info for a particular share.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **int** | Specifies the id of the share. | 
**uptier_path** | **str** | Only applicable for uptiering tasks. Ignore the uptiering policy and uptier the directory pointed by the &#39;uptierPath&#39;. If path is &#39;/&#39;, then uptier everything  This will override the global uptier path. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_tiering_share_info import DataTieringShareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringShareInfo from a JSON string
data_tiering_share_info_instance = DataTieringShareInfo.from_json(json)
# print the JSON string representation of the object
print(DataTieringShareInfo.to_json())

# convert the object into a dict
data_tiering_share_info_dict = data_tiering_share_info_instance.to_dict()
# create an instance of DataTieringShareInfo from a dict
data_tiering_share_info_from_dict = DataTieringShareInfo.from_dict(data_tiering_share_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


