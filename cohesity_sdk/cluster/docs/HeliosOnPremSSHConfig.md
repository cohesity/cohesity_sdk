# HeliosOnPremSSHConfig

Params for a HeliosOnPremVM SSH access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_support_user_password_set** | **bool** | Specifies if SSH password is set for support user. | [optional] [readonly] 
**ssh_support_user_sudo_enabled** | **bool** | Specifies if SSH sudo access is set for support user. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.helios_on_prem_ssh_config import HeliosOnPremSSHConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosOnPremSSHConfig from a JSON string
helios_on_prem_ssh_config_instance = HeliosOnPremSSHConfig.from_json(json)
# print the JSON string representation of the object
print(HeliosOnPremSSHConfig.to_json())

# convert the object into a dict
helios_on_prem_ssh_config_dict = helios_on_prem_ssh_config_instance.to_dict()
# create an instance of HeliosOnPremSSHConfig from a dict
helios_on_prem_ssh_config_from_dict = HeliosOnPremSSHConfig.from_dict(helios_on_prem_ssh_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


