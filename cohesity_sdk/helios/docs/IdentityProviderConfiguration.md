# IdentityProviderConfiguration

Identity provider configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_id** | **str, none_type** | Specifies identity provider issuer id | 
**sso_url** | **str, none_type** | Specifies the identity provider SSO url | 
**certificate** | **str, none_type** | Specifies the certificate generated for the app by the idp service when the cluster is registered as an app. This is required to verify the SAML response. | 
**roles** | **[str], none_type** | Specifies the default roles assined for all SSO users | [optional] 
**saml_attribute_name** | **str, none_type** | Specifies the SAML attribute name that contains a comma separated list of cluster roles. This sets the default roles for all SSO users. Either this field or roles must be set, this field takes higher precedence than the roles field. | [optional] 
**allow_local_user_login** | **bool, none_type** | Specifies if local user login is allowed. When idp is configured, only idp users are allowed to login to the cluster, local login is disabled except for users with admin role. If this flag is set to true, local (non-idp) logins are allowed for all local and AD users. Local or AD users with admin role can login always independent of this flag&#39;s setting. By default there is no local authentication i.e the value is false. | [optional] 
**sign_request** | **bool, none_type** | Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false, set this flag to true if the idp site is configured to expect the SAML request from the Cluster signed. If this is set to true, users must get the cluster&#39;s certificate and upload it on the idp site. | [optional] 
**is_enabled** | **bool, none_type** | Specifies a flag to enable or disable this idp service. When it is set to true, idp service is enabled. When it is set to false, idp service is disabled. By defaut idp is enabled i.e the value is true. | [optional] 
**id** | **int, none_type** | Specifies id of idp configuration | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id if the idp is configured for a tenant. If this is not set, this idp configuration is used for the cluster level users and for all users of tenants not having an idp configuration. | [optional] 
**name** | **str, none_type** | Specifies name of the vendor providing idp service | [optional] 
**domain** | **str, none_type** | Specifies domain of idp configuration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


