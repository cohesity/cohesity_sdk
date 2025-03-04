# ChassisRackConfigParams

Specifies the chassis serial to rack id mapping configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_serial** | **str** | Specifies the chassis serial. | [optional] 
**rack_id** | **int** | Specifies the rack id. | [optional] 

## Example

```python
from cohesity_sdk.models.chassis_rack_config_params import ChassisRackConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of ChassisRackConfigParams from a JSON string
chassis_rack_config_params_instance = ChassisRackConfigParams.from_json(json)
# print the JSON string representation of the object
print(ChassisRackConfigParams.to_json())

# convert the object into a dict
chassis_rack_config_params_dict = chassis_rack_config_params_instance.to_dict()
# create an instance of ChassisRackConfigParams from a dict
chassis_rack_config_params_from_dict = ChassisRackConfigParams.from_dict(chassis_rack_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


