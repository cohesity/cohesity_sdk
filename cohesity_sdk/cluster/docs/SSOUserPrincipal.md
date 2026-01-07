# SSOUserPrincipal

Specifies the details of the SSO principal added for the sso user on the Cohesity Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str, none_type** | Specifies the name of the Domain where the referenced principal is stored. | [optional] 
**last_updated_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the group or user was last modified on the Cohesity Cluster. | [optional] 
**name** | **str, none_type** | Specifies the name of the principal, that will be referenced by the user. | [optional] 
**restricted** | **bool, none_type** | Specifies Whether the principal is a restricted principal. A restricted principal can only view the objects it has permissions to. | [optional] 
**roles** | **[str], none_type** | Specifies the Cohesity roles associated with the user or group | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id if the principal is added for a tenant. If this is not set, the principal is added at the cluster level. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


