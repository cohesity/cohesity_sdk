# DowntieringTarget

Specifies the target data tiering details for downtier job. This is in beta phase. Please use target inside CommonDataTieringTaskParams, present directly under data tiering request body. If target is present inside CommonDataTieringTaskParams, this target will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downtiered_data_locations** | [**List[DowntieredDataLocation]**](DowntieredDataLocation.md) | Specifies a list of mapping between sources and its corresponding viewNames and mountPaths, where the sources were downtiered. | [optional] [readonly] 
**mount_path_prefix** | **str** | Specifies the mount path prefix inside the view. | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain ID where the view will be kept. | 
**view_name_prefix** | **str** | Specifies the view name prefix. | 

## Example

```python
from cohesity_sdk.models.downtiering_target import DowntieringTarget

# TODO update the JSON string below
json = "{}"
# create an instance of DowntieringTarget from a JSON string
downtiering_target_instance = DowntieringTarget.from_json(json)
# print the JSON string representation of the object
print(DowntieringTarget.to_json())

# convert the object into a dict
downtiering_target_dict = downtiering_target_instance.to_dict()
# create an instance of DowntieringTarget from a dict
downtiering_target_from_dict = DowntieringTarget.from_dict(downtiering_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


