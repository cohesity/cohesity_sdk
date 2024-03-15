# IdentityConfig

Identity Provider Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str, none_type** | Specifies domain of idp configuration | 
**identity_provider_type** | **str, none_type** | Specifies the type of identity provider. | 
**id** | **int, none_type** | Specifies the ID of the IDP. | [optional] [readonly] 
**is_enabled** | **bool, none_type** | Specifies a flag to enable or disable this idp service. When it is set to true, idp service is enabled. When it is set to false, idp service is disabled. By defaut idp is enabled i.e the value is true. | [optional]  if omitted the server will use the default value of True
**last_modified_timestamp_usecs** | **int, none_type** | Specifies the last time this configuration was modified in microseconds since the epoch. This is may be specified for PUT operations to prevent stale requests from being written. If it is specified during a PUT operation then the request will be rejected if the specified time does not match the actual last modified time. | [optional] 
**o_auth2_params** | [**OAuth2Provider**](OAuth2Provider.md) |  | [optional] 
**open_id_connect_params** | [**OpenIdProvider**](OpenIdProvider.md) |  | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id if the idp is configured for a tenant. If this is not set, this idp configuration is used for the cluster level users and for all users of tenants not having an idp configuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


