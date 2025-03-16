# CommonIdpParams

Specifies the Identity Provider Configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Specifies the certificate generated for the app by the IdP service when the Helios is registered as an app. This is required to verify the SAML response. | 
**default_clusters** | **List[str]** | Specifies a list of default clusterIds assigned to an IdP user if clustersSamlAttributeName is not given. &#39;All&#39; must be specified to give access to all clusters. | [optional] 
**default_regions** | **List[str]** | Specifies a list of default regionIds assigned to an IdP user if regionsSamlAttributeName is not given. &#39;All&#39; must be specified to give access to all DataProtect as a Service regions. | [optional] 
**default_roles** | **List[str]** | Specifies a list of default roles assigned to an IdP user if rolesSamlAttributeName is not given. | [optional] 
**domain** | **str** | Specifies a unique name for this IdP configuration. | 
**is_enabled** | **bool** | Specifies a flag to enable or disable this IdP service. When it is set to true, IdP service is enabled. When it is set to false, IdP service is disabled. Default value is true. | [optional] 
**issuer_id** | **str** | Specifies the IdP provided Issuer ID for the app. For example, exkh1aov1nhHrgFhN0h7. | 
**name** | **str** | Specifies the name of the vendor providing IDP service. | 
**sf_account_id** | **str** | Specifies the salesforce account ID linked to this IDP. Either of TenantId or SfAccountId would be set for IdP. | [optional] [readonly] 
**sign_request** | **bool** | Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false. Set this flag to true if the IdP site is configured to expect the SAML request from Helios signed. If this is set to true, users must get the Helios certificate and upload it on the IdP site. | [optional] 
**sso_url** | **str** | Specifies the SSO URL of the IdP service for the customer. This is the URL given by IdP when the customer created an account. For example, dev-332534.oktapreview.com. | 
**tenant_id** | **str** | Specifies the Tenant Id if the IdP is configured for a Tenant. Either of TenantId or SfAccountId would be set for IdP. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.common_idp_params import CommonIdpParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonIdpParams from a JSON string
common_idp_params_instance = CommonIdpParams.from_json(json)
# print the JSON string representation of the object
print(CommonIdpParams.to_json())

# convert the object into a dict
common_idp_params_dict = common_idp_params_instance.to_dict()
# create an instance of CommonIdpParams from a dict
common_idp_params_from_dict = CommonIdpParams.from_dict(common_idp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


