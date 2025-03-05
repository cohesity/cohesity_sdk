# DataTieringTagConfig

Array of data tiering tag objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the ID of the data tiering analysis group. | [optional] [readonly] 
**tags_info** | [**List[DataTieringTagObject]**](DataTieringTagObject.md) | Array of Tag objects. | 

## Example

```python
from cohesity_sdk.models.data_tiering_tag_config import DataTieringTagConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringTagConfig from a JSON string
data_tiering_tag_config_instance = DataTieringTagConfig.from_json(json)
# print the JSON string representation of the object
print(DataTieringTagConfig.to_json())

# convert the object into a dict
data_tiering_tag_config_dict = data_tiering_tag_config_instance.to_dict()
# create an instance of DataTieringTagConfig from a dict
data_tiering_tag_config_from_dict = DataTieringTagConfig.from_dict(data_tiering_tag_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


