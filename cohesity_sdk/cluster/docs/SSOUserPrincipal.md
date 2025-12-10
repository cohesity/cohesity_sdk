# SSOUserPrincipal

Specifies the details of the SSO principal added for the sso user on the Cohesity Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the name of the Domain where the referenced principal is stored. | [optional] 
**last_updated_time_msecs** | **int** | Specifies the epoch time in milliseconds when the group or user was last modified on the Cohesity Cluster. | [optional] 
**name** | **str** | Specifies the name of the principal, that will be referenced by the user. | [optional] 
**restricted** | **bool** | Specifies Whether the principal is a restricted principal. A restricted principal can only view the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles associated with the user or group | [optional] 
**tenant_id** | **str** | Specifies the tenant id if the principal is added for a tenant. If this is not set, the principal is added at the cluster level. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sso_user_principal import SSOUserPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of SSOUserPrincipal from a JSON string
sso_user_principal_instance = SSOUserPrincipal.from_json(json)
# print the JSON string representation of the object
print(SSOUserPrincipal.to_json())

# convert the object into a dict
sso_user_principal_dict = sso_user_principal_instance.to_dict()
# create an instance of SSOUserPrincipal from a dict
sso_user_principal_from_dict = SSOUserPrincipal.from_dict(sso_user_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


