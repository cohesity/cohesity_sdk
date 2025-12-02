# SSOUserPrincipalParameters

Specifies the configuration parameters required to be added for SSO User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the name of the SSO Domain. | [optional] 
**name** | **str** | Specifies the name of the principal, that will be referenced by the SSO User. The name of the principal is used for naming the new user on the Cohesity Cluster. | [optional] 
**restricted** | **bool** | Specifies Whether the principal is a restricted principal. A restricted principal can only view the objects having permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles associated with the user or group,such as &#39;&#39;Admin&#39;&#39;, &#39;&#39;Ops&#39;&#39; or &#39;&#39;View&#39;&#39;. The Cohesity roles determine privileges on the Cohesity Cluster for the group or user. | [optional] 
**tenant_id** | **str** | Specifies the tenant id if the principal is being added for a tenant. If this is not set, the principal is added at the cluster level. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sso_user_principal_parameters import SSOUserPrincipalParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SSOUserPrincipalParameters from a JSON string
sso_user_principal_parameters_instance = SSOUserPrincipalParameters.from_json(json)
# print the JSON string representation of the object
print(SSOUserPrincipalParameters.to_json())

# convert the object into a dict
sso_user_principal_parameters_dict = sso_user_principal_parameters_instance.to_dict()
# create an instance of SSOUserPrincipalParameters from a dict
sso_user_principal_parameters_from_dict = SSOUserPrincipalParameters.from_dict(sso_user_principal_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


