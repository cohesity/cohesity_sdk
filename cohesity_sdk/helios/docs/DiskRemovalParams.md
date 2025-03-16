# DiskRemovalParams

Specifies parameters to initiate/cancel disk removal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel** | **bool** | If true, cancels disk removal which is already in progress. | 
**is_validate_only** | **bool** | Specifies whether request is for pre-check validations only | [optional] [default to False]

## Example

```python
from cohesity_sdk.helios.models.disk_removal_params import DiskRemovalParams

# TODO update the JSON string below
json = "{}"
# create an instance of DiskRemovalParams from a JSON string
disk_removal_params_instance = DiskRemovalParams.from_json(json)
# print the JSON string representation of the object
print(DiskRemovalParams.to_json())

# convert the object into a dict
disk_removal_params_dict = disk_removal_params_instance.to_dict()
# create an instance of DiskRemovalParams from a dict
disk_removal_params_from_dict = DiskRemovalParams.from_dict(disk_removal_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


