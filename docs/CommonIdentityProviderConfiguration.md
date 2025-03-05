# CommonIdentityProviderConfiguration

Identity provider configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_local_user_login** | **bool** | Specifies if local user login is allowed. When idp is configured, only idp users are allowed to login to the cluster, local login is disabled except for users with admin role. If this flag is set to true, local (non-idp) logins are allowed for all local and AD users. Local or AD users with admin role can login always independent of this flag&#39;s setting. By default there is no local authentication i.e the value is false. | [optional] 
**certificate** | **str** | Specifies the certificate generated for the app by the idp service when the cluster is registered as an app. This is required to verify the SAML response. | 
**certificate_filename** | **str** | Specifies the filename used for the certificate. The default value is idp_certificate.pem | [optional] 
**is_enabled** | **bool** | Specifies a flag to enable or disable this idp service. When it is set to true, idp service is enabled. When it is set to false, idp service is disabled. By defaut idp is enabled i.e the value is true. | [optional] 
**issuer_id** | **str** | Specifies identity provider issuer id | 
**roles** | **List[str]** | Specifies the default roles assined for all SSO users | [optional] 
**saml_attribute_name** | **str** | Specifies the SAML attribute name that contains a comma separated list of cluster roles. This sets the default roles for all SSO users. Either this field or roles must be set, this field takes higher precedence than the roles field. | [optional] 
**sign_request** | **bool** | Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false, set this flag to true if the idp site is configured to expect the SAML request from the Cluster signed. If this is set to true, users must get the cluster&#39;s certificate and upload it on the idp site. | [optional] 
**sso_url** | **str** | Specifies the identity provider SSO url | 

## Example

```python
from cohesity_sdk.models.common_identity_provider_configuration import CommonIdentityProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CommonIdentityProviderConfiguration from a JSON string
common_identity_provider_configuration_instance = CommonIdentityProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print(CommonIdentityProviderConfiguration.to_json())

# convert the object into a dict
common_identity_provider_configuration_dict = common_identity_provider_configuration_instance.to_dict()
# create an instance of CommonIdentityProviderConfiguration from a dict
common_identity_provider_configuration_from_dict = CommonIdentityProviderConfiguration.from_dict(common_identity_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


