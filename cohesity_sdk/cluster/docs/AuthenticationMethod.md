# AuthenticationMethod

Specifies the authentication method for IBMCOS APIs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Specifies the API key if the authenticationType is kApiKey. | [optional] 
**authentication_type** | **str** | Specifies the authentication type for IBMCOS APIs. | 
**tenant_crn** | **str** | Specifies the teneant CRN if the authenticationType is kTrustedProfileWithS2SPolicy. | [optional] 
**trusted_profile_id** | **str** | Specifies the trusted profile id if the authenticationType is kTrustedProfile. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.authentication_method import AuthenticationMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationMethod from a JSON string
authentication_method_instance = AuthenticationMethod.from_json(json)
# print the JSON string representation of the object
print(AuthenticationMethod.to_json())

# convert the object into a dict
authentication_method_dict = authentication_method_instance.to_dict()
# create an instance of AuthenticationMethod from a dict
authentication_method_from_dict = AuthenticationMethod.from_dict(authentication_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


