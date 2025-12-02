# VcdPolicyParams

Specifies the parameters of a VCD compute policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the compute policy. | [optional] [readonly] 
**vcd_uuid** | **str** | Specifies the UUID assigned by the VCD to the compute policy. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vcd_policy_params import VcdPolicyParams

# TODO update the JSON string below
json = "{}"
# create an instance of VcdPolicyParams from a JSON string
vcd_policy_params_instance = VcdPolicyParams.from_json(json)
# print the JSON string representation of the object
print(VcdPolicyParams.to_json())

# convert the object into a dict
vcd_policy_params_dict = vcd_policy_params_instance.to_dict()
# create an instance of VcdPolicyParams from a dict
vcd_policy_params_from_dict = VcdPolicyParams.from_dict(vcd_policy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


