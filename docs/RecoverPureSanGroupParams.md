# RecoverPureSanGroupParams

Specifies the parameters to recover Pure SAN group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pure_target_params** | [**RecoverPureGroupTargetParams**](RecoverPureGroupTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding target params must be filled out. | 

## Example

```python
from cohesity_sdk.models.recover_pure_san_group_params import RecoverPureSanGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureSanGroupParams from a JSON string
recover_pure_san_group_params_instance = RecoverPureSanGroupParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPureSanGroupParams.to_json())

# convert the object into a dict
recover_pure_san_group_params_dict = recover_pure_san_group_params_instance.to_dict()
# create an instance of RecoverPureSanGroupParams from a dict
recover_pure_san_group_params_from_dict = RecoverPureSanGroupParams.from_dict(recover_pure_san_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


