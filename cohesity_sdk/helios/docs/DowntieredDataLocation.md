# DowntieredDataLocation

Specifies a map between source Id and the corresponding viewName and mount path, where the source was downtiered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**mount_path** | **str** | Specifies the mount path inside the view. | [optional] 
**view_name** | **str** | Specifies the view name. | 

## Example

```python
from cohesity_sdk.helios.models.downtiered_data_location import DowntieredDataLocation

# TODO update the JSON string below
json = "{}"
# create an instance of DowntieredDataLocation from a JSON string
downtiered_data_location_instance = DowntieredDataLocation.from_json(json)
# print the JSON string representation of the object
print(DowntieredDataLocation.to_json())

# convert the object into a dict
downtiered_data_location_dict = downtiered_data_location_instance.to_dict()
# create an instance of DowntieredDataLocation from a dict
downtiered_data_location_from_dict = DowntieredDataLocation.from_dict(downtiered_data_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


