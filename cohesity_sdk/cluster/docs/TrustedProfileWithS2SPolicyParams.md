# TrustedProfileWithS2SPolicyParams

Specifies the trusted profile with service-to-service(S2S) policy authentication method parameters. A trusted profile ID must be provided using cluster metadata API for external targets to use this method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_domain_crn** | **str** | Specifies the cluster domain CRN for the trusted profile with S2S policy. | [optional] 
**connector_domain_crn** | **str** | Specifies the connector domain CRN for the trusted profile with S2S policy. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.trusted_profile_with_s2_s_policy_params import TrustedProfileWithS2SPolicyParams

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedProfileWithS2SPolicyParams from a JSON string
trusted_profile_with_s2_s_policy_params_instance = TrustedProfileWithS2SPolicyParams.from_json(json)
# print the JSON string representation of the object
print(TrustedProfileWithS2SPolicyParams.to_json())

# convert the object into a dict
trusted_profile_with_s2_s_policy_params_dict = trusted_profile_with_s2_s_policy_params_instance.to_dict()
# create an instance of TrustedProfileWithS2SPolicyParams from a dict
trusted_profile_with_s2_s_policy_params_from_dict = TrustedProfileWithS2SPolicyParams.from_dict(trusted_profile_with_s2_s_policy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


