# CreatePrincipalRequestParams

Specifies the parameters for adding principals to Users and Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_type** | **str** | Specifies the category of the user or group being added to the Cohesity Cluster. | 
**sso_user_principal_params** | [**List[SSOUserPrincipalParameters]**](SSOUserPrincipalParameters.md) | Specifies the properties to be added for the SSO user created on the Cohesity Cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_principal_request_params import CreatePrincipalRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrincipalRequestParams from a JSON string
create_principal_request_params_instance = CreatePrincipalRequestParams.from_json(json)
# print the JSON string representation of the object
print(CreatePrincipalRequestParams.to_json())

# convert the object into a dict
create_principal_request_params_dict = create_principal_request_params_instance.to_dict()
# create an instance of CreatePrincipalRequestParams from a dict
create_principal_request_params_from_dict = CreatePrincipalRequestParams.from_dict(create_principal_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


