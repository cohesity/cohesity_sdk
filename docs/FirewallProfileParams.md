# FirewallProfileParams

Specifies the firewall profile & their attachments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action. | 
**description** | **str** | Specifies a description for the profile attachments. | [optional] 
**direction** | **str** | Specifies the packet direction settings. | [optional] 
**interface_groups** | **List[str]** | Specifies the network interface groups. | [optional] 
**name** | **str** | Specifies the name of the profile. | 
**ports** | **List[str]** | Specifies the port along with the protocol settings. | [optional] 
**subnets** | **List[str]** | Specifies the subnets. | [optional] 

## Example

```python
from cohesity_sdk.models.firewall_profile_params import FirewallProfileParams

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallProfileParams from a JSON string
firewall_profile_params_instance = FirewallProfileParams.from_json(json)
# print the JSON string representation of the object
print(FirewallProfileParams.to_json())

# convert the object into a dict
firewall_profile_params_dict = firewall_profile_params_instance.to_dict()
# create an instance of FirewallProfileParams from a dict
firewall_profile_params_from_dict = FirewallProfileParams.from_dict(firewall_profile_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


