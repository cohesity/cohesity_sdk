# FirewallProfiles

Specifies the firewall profile & their attachments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**List[FirewallProfile]**](FirewallProfile.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.firewall_profiles import FirewallProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallProfiles from a JSON string
firewall_profiles_instance = FirewallProfiles.from_json(json)
# print the JSON string representation of the object
print(FirewallProfiles.to_json())

# convert the object into a dict
firewall_profiles_dict = firewall_profiles_instance.to_dict()
# create an instance of FirewallProfiles from a dict
firewall_profiles_from_dict = FirewallProfiles.from_dict(firewall_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


