# UptieringTarget

Specifies the target data tiering details for uptier job. This is in beta phase. Please use target inside CommonDataTieringTaskParams, present directly under data tiering request body. If target is present inside CommonDataTieringTaskParams, this target will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downtiered_data_locations** | [**List[DowntieredDataLocation]**](DowntieredDataLocation.md) | Specifies a list of mapping between sources and its corresponding viewNames and mountPaths, where the sources were downtiered. | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain ID where the view will be kept. | 

## Example

```python
from cohesity_sdk.models.uptiering_target import UptieringTarget

# TODO update the JSON string below
json = "{}"
# create an instance of UptieringTarget from a JSON string
uptiering_target_instance = UptieringTarget.from_json(json)
# print the JSON string representation of the object
print(UptieringTarget.to_json())

# convert the object into a dict
uptiering_target_dict = uptiering_target_instance.to_dict()
# create an instance of UptieringTarget from a dict
uptiering_target_from_dict = UptieringTarget.from_dict(uptiering_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


