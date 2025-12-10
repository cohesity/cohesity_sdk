# OIDCStandardConfiguration

Specifies the parameters for configuring OpenIDConnect configuration for an Identity Provider(IdP). This includes the minimal configuration with the assumption that the IdP supports well-known URI as specified by the RFC 5785.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the identifier for the client application that will be created at IDP side when configuring the Open IDP. | 
**issuer** | **str** | Specifies the URL for the Issuer which identifies the FQDN of the issuer. The issuer must make a JSON document available at the path formed by concatenating this issuerUrl with the string /.well-known/openid-configuration as defined by RFC 5785. | 

## Example

```python
from cohesity_sdk.cluster.models.oidc_standard_configuration import OIDCStandardConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCStandardConfiguration from a JSON string
oidc_standard_configuration_instance = OIDCStandardConfiguration.from_json(json)
# print the JSON string representation of the object
print(OIDCStandardConfiguration.to_json())

# convert the object into a dict
oidc_standard_configuration_dict = oidc_standard_configuration_instance.to_dict()
# create an instance of OIDCStandardConfiguration from a dict
oidc_standard_configuration_from_dict = OIDCStandardConfiguration.from_dict(oidc_standard_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


