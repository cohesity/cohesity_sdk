# FleetConfig

Specifies various resources while deploying fleet params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleet_network_params** | [**FleetNetworkParams**](FleetNetworkParams.md) |  | [optional] 
**fleet_subnet_type** | **str** | Specifies the subnet type of the fleet. | [optional] 
**fleet_tags** | [**List[FleetTags]**](FleetTags.md) | Specifies the network security groups within above VPC. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fleet_config import FleetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConfig from a JSON string
fleet_config_instance = FleetConfig.from_json(json)
# print the JSON string representation of the object
print(FleetConfig.to_json())

# convert the object into a dict
fleet_config_dict = fleet_config_instance.to_dict()
# create an instance of FleetConfig from a dict
fleet_config_from_dict = FleetConfig.from_dict(fleet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


