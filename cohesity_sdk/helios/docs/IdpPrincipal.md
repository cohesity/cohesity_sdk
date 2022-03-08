# IdpPrincipal

Specifies the parameters of an IDP Principal.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Principal. | 
**idp_id** | **int, none_type** | Specifies the IDP of the IDP with which this principal is associated. | 
**principal_type** | **str, none_type** | Specifies the type of this principal. It can be a &#39;User&#39; or a &#39;Group&#39;. | 
**roles** | **[str]** | Specifies a list of roles associated with this Principal. | [optional] 
**clusters** | **[str]** | Specifies a list of clusters associated with this Principal. They should be in a string with the format &#39;{cluster ID}:{cluster incarnation ID}&#39;. | [optional] 
**is_active** | **bool, none_type** | Specifies whether or not this principal is currently active. | [optional] 
**created_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds since the epoch when this Principal was created. | [optional] [readonly] 
**last_updated_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds since the epoch when this Principal was updated. | [optional] [readonly] 
**effective_time_usecs** | **int, none_type** | Specifies the starting timestamp in microseconds since the epoch when this principal will be able to log in. | [optional] 
**expired_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds since the epoch when this principal will no longer be able to log in. | [optional] 
**sid** | **str, none_type** | Specifies the unique SID of the principal. | [optional] [readonly] 
**profiles** | [**[McmTenantProfile]**](McmTenantProfile.md) | Specifies the list of tenant profiles associated to this principal if any. | [optional] 
**tenant_accesses** | [**[TenantAccess]**](TenantAccess.md) | Specifies the list of tenant access associated to this principal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


