# MfaOptOutConfig

Specifies the fields which must be specified when opting out of MFA.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eula_read** | **bool** | Specifies whether or not the eula for opting out of MFA has been read. | 
**reason** | **str** | Specifies the reason for opting out of MFA. | 
**reason_other** | **str** | Specifies additional details of why MFA has been disabled. This is required if &#39;Other&#39; was specified in the &#39;reason&#39; field. | [optional] 
**timestamp_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when the opt out option was specified. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.mfa_opt_out_config import MfaOptOutConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MfaOptOutConfig from a JSON string
mfa_opt_out_config_instance = MfaOptOutConfig.from_json(json)
# print the JSON string representation of the object
print(MfaOptOutConfig.to_json())

# convert the object into a dict
mfa_opt_out_config_dict = mfa_opt_out_config_instance.to_dict()
# create an instance of MfaOptOutConfig from a dict
mfa_opt_out_config_from_dict = MfaOptOutConfig.from_dict(mfa_opt_out_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


