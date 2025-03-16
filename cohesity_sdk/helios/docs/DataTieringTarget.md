# DataTieringTarget

Specifies the target data tiering details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | Specifies the mount path inside the view. | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain ID where the view will be kept. | 
**view_name** | **str** | Specifies the view name. | 

## Example

```python
from cohesity_sdk.helios.models.data_tiering_target import DataTieringTarget

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringTarget from a JSON string
data_tiering_target_instance = DataTieringTarget.from_json(json)
# print the JSON string representation of the object
print(DataTieringTarget.to_json())

# convert the object into a dict
data_tiering_target_dict = data_tiering_target_instance.to_dict()
# create an instance of DataTieringTarget from a dict
data_tiering_target_from_dict = DataTieringTarget.from_dict(data_tiering_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


