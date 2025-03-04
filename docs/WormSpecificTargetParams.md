# WormSpecificTargetParams

Specifies the parameters which specific to WORM and needs to passed when WORM is enabled for archival External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Specifies the application id of worm enabled external target. | [optional] 
**encrypted_application_key** | **str** | Specifies the encrypted application key of worm enabled external target. | [optional] 
**resource_group** | **str** | Specifies the resource group of worm enabled external target. | [optional] 
**subscription_id** | **str** | Specifies the subscription id of worm enabled external target. | [optional] 
**tenant_id** | **str** | Specifies the tenant id of worm enabled external target. | [optional] 

## Example

```python
from cohesity_sdk.models.worm_specific_target_params import WormSpecificTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of WormSpecificTargetParams from a JSON string
worm_specific_target_params_instance = WormSpecificTargetParams.from_json(json)
# print the JSON string representation of the object
print(WormSpecificTargetParams.to_json())

# convert the object into a dict
worm_specific_target_params_dict = worm_specific_target_params_instance.to_dict()
# create an instance of WormSpecificTargetParams from a dict
worm_specific_target_params_from_dict = WormSpecificTargetParams.from_dict(worm_specific_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


