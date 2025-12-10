# ServiceAccountImpersonationParams

Specifies the service account impersonation authentication method parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_to_impersonate_email** | **str** | Specifies the email of the service account to impersonate. | 

## Example

```python
from cohesity_sdk.cluster.models.service_account_impersonation_params import ServiceAccountImpersonationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountImpersonationParams from a JSON string
service_account_impersonation_params_instance = ServiceAccountImpersonationParams.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountImpersonationParams.to_json())

# convert the object into a dict
service_account_impersonation_params_dict = service_account_impersonation_params_instance.to_dict()
# create an instance of ServiceAccountImpersonationParams from a dict
service_account_impersonation_params_from_dict = ServiceAccountImpersonationParams.from_dict(service_account_impersonation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


