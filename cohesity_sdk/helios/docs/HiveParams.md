# HiveParams

Specifies the recovery options specific to Hive environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_hive_params** | [**RecoverHiveParams**](RecoverHiveParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.hive_params import HiveParams

# TODO update the JSON string below
json = "{}"
# create an instance of HiveParams from a JSON string
hive_params_instance = HiveParams.from_json(json)
# print the JSON string representation of the object
print(HiveParams.to_json())

# convert the object into a dict
hive_params_dict = hive_params_instance.to_dict()
# create an instance of HiveParams from a dict
hive_params_from_dict = HiveParams.from_dict(hive_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


