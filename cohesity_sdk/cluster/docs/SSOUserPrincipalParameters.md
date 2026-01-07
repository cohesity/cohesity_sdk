# SSOUserPrincipalParameters

Specifies the configuration parameters required to be added for SSO User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str, none_type** | Specifies the name of the SSO Domain. | [optional] 
**name** | **str, none_type** | Specifies the name of the principal, that will be referenced by the SSO User. The name of the principal is used for naming the new user on the Cohesity Cluster. | [optional] 
**restricted** | **bool, none_type** | Specifies Whether the principal is a restricted principal. A restricted principal can only view the objects having permissions to. | [optional] 
**roles** | **[str], none_type** | Specifies the Cohesity roles associated with the user or group,such as &#39;&#39;Admin&#39;&#39;, &#39;&#39;Ops&#39;&#39; or &#39;&#39;View&#39;&#39;. The Cohesity roles determine privileges on the Cohesity Cluster for the group or user. | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id if the principal is being added for a tenant. If this is not set, the principal is added at the cluster level. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


