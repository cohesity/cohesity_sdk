# AwsFleetParams

Specifies information about AWS fleets for registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_params** | [**FleetNetworkParams**](FleetNetworkParams.md) |  | [optional] 
**subnet_type** | **str** | Specifies the subnet type of the fleet. | 
**tags** | [**List[FleetTags]**](FleetTags.md) | Specifies the tag information for the fleet. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_fleet_params import AwsFleetParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsFleetParams from a JSON string
aws_fleet_params_instance = AwsFleetParams.from_json(json)
# print the JSON string representation of the object
print(AwsFleetParams.to_json())

# convert the object into a dict
aws_fleet_params_dict = aws_fleet_params_instance.to_dict()
# create an instance of AwsFleetParams from a dict
aws_fleet_params_from_dict = AwsFleetParams.from_dict(aws_fleet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


