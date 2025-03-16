# HeliosMfa

Specifies MFA configuration for an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_type** | **str** | Specifies the deployment type of the helios instance. | 
**helios_on_prem_config** | [**HeliosOnPremMfa**](HeliosOnPremMfa.md) |  | [optional] 
**helios_saas_config** | [**HeliosSaasMfa**](HeliosSaasMfa.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_mfa import HeliosMfa

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosMfa from a JSON string
helios_mfa_instance = HeliosMfa.from_json(json)
# print the JSON string representation of the object
print(HeliosMfa.to_json())

# convert the object into a dict
helios_mfa_dict = helios_mfa_instance.to_dict()
# create an instance of HeliosMfa from a dict
helios_mfa_from_dict = HeliosMfa.from_dict(helios_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


