# DataTieringTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Specifies label of tag. | [optional] 
**value** | **str** | Specifies value of tag. | [optional] 

## Example

```python
from cohesity_sdk.models.data_tiering_tag import DataTieringTag

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringTag from a JSON string
data_tiering_tag_instance = DataTieringTag.from_json(json)
# print the JSON string representation of the object
print(DataTieringTag.to_json())

# convert the object into a dict
data_tiering_tag_dict = data_tiering_tag_instance.to_dict()
# create an instance of DataTieringTag from a dict
data_tiering_tag_from_dict = DataTieringTag.from_dict(data_tiering_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


