# FleetNetworkParams

Specifies various network params for the fleet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet** | **str** | Specifies subnet for the fleet. | 
**vpc** | **str** | Specifies vpc for the fleet. | 

## Example

```python
from cohesity_sdk.models.fleet_network_params import FleetNetworkParams

# TODO update the JSON string below
json = "{}"
# create an instance of FleetNetworkParams from a JSON string
fleet_network_params_instance = FleetNetworkParams.from_json(json)
# print the JSON string representation of the object
print(FleetNetworkParams.to_json())

# convert the object into a dict
fleet_network_params_dict = fleet_network_params_instance.to_dict()
# create an instance of FleetNetworkParams from a dict
fleet_network_params_from_dict = FleetNetworkParams.from_dict(fleet_network_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


