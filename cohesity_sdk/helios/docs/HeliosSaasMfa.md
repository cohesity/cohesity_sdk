# HeliosSaasMfa

Specifies MFA configuration for an account in the Helios SaaS environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_period_end_time_usecs** | **int** | Specifies the end time of the grace period for this customer in microseconds since the epoch. | [optional] [readonly] 
**grace_period_start_time_usecs** | **int** | Specifies the start time of the grace period for this customer in microseconds since the epoch. | [optional] [readonly] 
**mfa_status** | **str** | Specifies the current MFA status. | 
**opt_out_config** | [**MfaOptOutConfig**](MfaOptOutConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_saas_mfa import HeliosSaasMfa

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosSaasMfa from a JSON string
helios_saas_mfa_instance = HeliosSaasMfa.from_json(json)
# print the JSON string representation of the object
print(HeliosSaasMfa.to_json())

# convert the object into a dict
helios_saas_mfa_dict = helios_saas_mfa_instance.to_dict()
# create an instance of HeliosSaasMfa from a dict
helios_saas_mfa_from_dict = HeliosSaasMfa.from_dict(helios_saas_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


