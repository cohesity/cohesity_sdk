# FirewallProfileNamesParams

Specifies the firewall profile names to be removed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Specifies the list of profile names to be removed. | 

## Example

```python
from cohesity_sdk.models.firewall_profile_names_params import FirewallProfileNamesParams

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallProfileNamesParams from a JSON string
firewall_profile_names_params_instance = FirewallProfileNamesParams.from_json(json)
# print the JSON string representation of the object
print(FirewallProfileNamesParams.to_json())

# convert the object into a dict
firewall_profile_names_params_dict = firewall_profile_names_params_instance.to_dict()
# create an instance of FirewallProfileNamesParams from a dict
firewall_profile_names_params_from_dict = FirewallProfileNamesParams.from_dict(firewall_profile_names_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


