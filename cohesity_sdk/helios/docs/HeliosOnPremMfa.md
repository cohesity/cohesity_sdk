# HeliosOnPremMfa

Specifies MFA configuration for a Helios on prem deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_types** | **List[str]** | Specifies the list of mechanism to receive the OTP code. Supported types are:   TOTP (Helios OnPrem Only) -&gt; Time based OTP.   Email OTP (Helios OnPrem Only) -&gt; OTP via Email.   Salesforce (Helios Only) -&gt; MFA setup via Salesforce.  | [optional] 
**mfa** | **bool** | Specifies whether MFA is enabled or disabled. | 
**retain_user_mfa_settings** | **bool** | Specifies whether user level MFA config needs to be retained when account level MFA is enabled or disabled. | [optional] [default to False]

## Example

```python
from cohesity_sdk.helios.models.helios_on_prem_mfa import HeliosOnPremMfa

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosOnPremMfa from a JSON string
helios_on_prem_mfa_instance = HeliosOnPremMfa.from_json(json)
# print the JSON string representation of the object
print(HeliosOnPremMfa.to_json())

# convert the object into a dict
helios_on_prem_mfa_dict = helios_on_prem_mfa_instance.to_dict()
# create an instance of HeliosOnPremMfa from a dict
helios_on_prem_mfa_from_dict = HeliosOnPremMfa.from_dict(helios_on_prem_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


