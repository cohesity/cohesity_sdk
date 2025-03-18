# DataTieringObjectInfo

Specifies the data tiering analysis group run object details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**analysis_info** | [**DataTieringObjectAnalysisInfo**](DataTieringObjectAnalysisInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_tiering_object_info import DataTieringObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringObjectInfo from a JSON string
data_tiering_object_info_instance = DataTieringObjectInfo.from_json(json)
# print the JSON string representation of the object
print(DataTieringObjectInfo.to_json())

# convert the object into a dict
data_tiering_object_info_dict = data_tiering_object_info_instance.to_dict()
# create an instance of DataTieringObjectInfo from a dict
data_tiering_object_info_from_dict = DataTieringObjectInfo.from_dict(data_tiering_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


