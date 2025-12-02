# IBMAuthenticationMethodsParams

Specifies the authentication method for IBM COS External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_params** | [**APIKeyParams**](APIKeyParams.md) |  | [optional] 
**authentication_type** | **str** | Specifies the IBM COS external target authentication type. Specific authetication parameters will be used accordingly. | 
**trusted_profile_params** | [**TrustedProfileParams**](TrustedProfileParams.md) |  | [optional] 
**trusted_profile_with_s2_s_policy_params** | [**TrustedProfileWithS2SPolicyParams**](TrustedProfileWithS2SPolicyParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_authentication_methods_params import IBMAuthenticationMethodsParams

# TODO update the JSON string below
json = "{}"
# create an instance of IBMAuthenticationMethodsParams from a JSON string
ibm_authentication_methods_params_instance = IBMAuthenticationMethodsParams.from_json(json)
# print the JSON string representation of the object
print(IBMAuthenticationMethodsParams.to_json())

# convert the object into a dict
ibm_authentication_methods_params_dict = ibm_authentication_methods_params_instance.to_dict()
# create an instance of IBMAuthenticationMethodsParams from a dict
ibm_authentication_methods_params_from_dict = IBMAuthenticationMethodsParams.from_dict(ibm_authentication_methods_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


