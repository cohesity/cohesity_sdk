# OIDCStandardConfiguration

Specifies the parameters for configuring OpenIDConnect configuration for an Identity Provider(IdP). This includes the minimal configuration with the assumption that the IdP supports well-known URI as specified by the RFC 5785.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the identifier for the client application that will be created at IDP side when configuring the Open IDP. | 
**issuer** | **str** | Specifies the URL for the Issuer which identifies the FQDN of the issuer. The issuer must make a JSON document available at the path formed by concatenating this issuerUrl with the string /.well-known/openid-configuration as defined by RFC 5785. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


