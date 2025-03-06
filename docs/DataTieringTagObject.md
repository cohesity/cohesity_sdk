# DataTieringTagObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[DataTieringTag]**](DataTieringTag.md) | Array of tag label and value. | [optional] 
**type** | **str** | Specifies type of tag. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_tiering_tag_object import DataTieringTagObject

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringTagObject from a JSON string
data_tiering_tag_object_instance = DataTieringTagObject.from_json(json)
# print the JSON string representation of the object
print(DataTieringTagObject.to_json())

# convert the object into a dict
data_tiering_tag_object_dict = data_tiering_tag_object_instance.to_dict()
# create an instance of DataTieringTagObject from a dict
data_tiering_tag_object_from_dict = DataTieringTagObject.from_dict(data_tiering_tag_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


