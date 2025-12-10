# GCPAuthenticationMethodsParams

Specifies the authentication method for GCP External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** | Specifies the GCP external target authentication type. Specific authentication parameters will be used accordingly. | 
**service_account_attached_params** | [**ServiceAccountAttachedParams**](ServiceAccountAttachedParams.md) |  | [optional] 
**service_account_impersonation_params** | [**ServiceAccountImpersonationParams**](ServiceAccountImpersonationParams.md) |  | [optional] 
**service_account_key_params** | [**ServiceAccountKeyParams**](ServiceAccountKeyParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_authentication_methods_params import GCPAuthenticationMethodsParams

# TODO update the JSON string below
json = "{}"
# create an instance of GCPAuthenticationMethodsParams from a JSON string
gcp_authentication_methods_params_instance = GCPAuthenticationMethodsParams.from_json(json)
# print the JSON string representation of the object
print(GCPAuthenticationMethodsParams.to_json())

# convert the object into a dict
gcp_authentication_methods_params_dict = gcp_authentication_methods_params_instance.to_dict()
# create an instance of GCPAuthenticationMethodsParams from a dict
gcp_authentication_methods_params_from_dict = GCPAuthenticationMethodsParams.from_dict(gcp_authentication_methods_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


