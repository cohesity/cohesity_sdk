# FirewallProfile

Specifies the firewall profile & their attachments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Attachment]**](Attachment.md) | Specifies the profile attachments. | [optional] 
**gateway_params** | [**List[GatewayParams]**](GatewayParams.md) | Specifies the port &amp; direction settings. | [optional] 
**name** | **str** | Specifies the name of the profile. | 

## Example

```python
from cohesity_sdk.models.firewall_profile import FirewallProfile

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallProfile from a JSON string
firewall_profile_instance = FirewallProfile.from_json(json)
# print the JSON string representation of the object
print(FirewallProfile.to_json())

# convert the object into a dict
firewall_profile_dict = firewall_profile_instance.to_dict()
# create an instance of FirewallProfile from a dict
firewall_profile_from_dict = FirewallProfile.from_dict(firewall_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


