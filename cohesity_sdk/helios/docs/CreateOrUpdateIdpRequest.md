# CreateOrUpdateIdpRequest

Specifies the request to create or update an Identity Provider Configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the vendor providing IDP service. | 
**domain** | **str, none_type** | Specifies a unique name for this IdP configuration. | 
**sso_url** | **str, none_type** | Specifies the SSO URL of the IdP service for the customer. This is the URL given by IdP when the customer created an account. For example, dev-332534.oktapreview.com. | 
**issuer_id** | **str, none_type** | Specifies the IdP provided Issuer ID for the app. For example, exkh1aov1nhHrgFhN0h7. | 
**certificate** | **str, none_type** | Specifies the certificate generated for the app by the IdP service when the Helios is registered as an app. This is required to verify the SAML response. | 
**sf_account_id** | **str, none_type** | Specifies the salesforce account ID linked to this IDP. Either of TenantId or SfAccountId would be set for IdP. | [optional] [readonly] 
**default_roles** | **[str], none_type** | Specifies a list of default roles assigned to an IdP user if rolesSamlAttributeName is not given. | [optional] 
**default_clusters** | **[str], none_type** | Specifies a list of default clusterIds assigned to an IdP user if clustersSamlAttributeName is not given. &#39;All&#39; must be specified to give access to all clusters. | [optional] 
**sign_request** | **bool, none_type** | Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false. Set this flag to true if the IdP site is configured to expect the SAML request from Helios signed. If this is set to true, users must get the Helios certificate and upload it on the IdP site. | [optional] 
**is_enabled** | **bool, none_type** | Specifies a flag to enable or disable this IdP service. When it is set to true, IdP service is enabled. When it is set to false, IdP service is disabled. Default value is true. | [optional] 
**tenant_id** | **str, none_type** | Specifies the Tenant Id if the IdP is configured for a Tenant. Either of TenantId or SfAccountId would be set for IdP. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


