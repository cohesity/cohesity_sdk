# IdpPrincipal

Specifies the parameters of an IDP Principal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | **List[str]** | Specifies a list of clusters associated with this Principal. They should be in a string with the format &#39;{cluster ID}:{cluster incarnation ID}&#39;. | [optional] 
**created_time_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when this Principal was created. | [optional] [readonly] 
**effective_time_usecs** | **int** | Specifies the starting timestamp in microseconds since the epoch when this principal will be able to log in. | [optional] 
**expired_time_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when this principal will no longer be able to log in. | [optional] 
**idp_id** | **int** | Specifies the IDP of the IDP with which this principal is associated. | 
**is_active** | **bool** | Specifies whether or not this principal is currently active. | [optional] 
**last_updated_time_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when this Principal was updated. | [optional] [readonly] 
**name** | **str** | Specifies the name of the Principal. | 
**principal_type** | **str** | Specifies the type of this principal. It can be a &#39;User&#39; or a &#39;Group&#39;. | 
**profiles** | [**List[McmTenantProfile]**](McmTenantProfile.md) | Specifies the list of tenant profiles associated to this principal if any. | [optional] 
**roles** | **List[str]** | Specifies a list of roles associated with this Principal. | [optional] 
**sid** | **str** | Specifies the unique SID of the principal. | [optional] [readonly] 
**tenant_accesses** | [**List[TenantAccess]**](TenantAccess.md) | Specifies the list of tenant access associated to this principal. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.idp_principal import IdpPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of IdpPrincipal from a JSON string
idp_principal_instance = IdpPrincipal.from_json(json)
# print the JSON string representation of the object
print(IdpPrincipal.to_json())

# convert the object into a dict
idp_principal_dict = idp_principal_instance.to_dict()
# create an instance of IdpPrincipal from a dict
idp_principal_from_dict = IdpPrincipal.from_dict(idp_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


