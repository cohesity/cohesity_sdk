# AdLdapProviderTypeParams

Specifies the properties associated to a LdapProvider type user id mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_option** | [**FallbackUserIdMappingParams**](FallbackUserIdMappingParams.md) | Specifies a fallback user id mapping param in case the primary config does not work. | 

## Example

```python
from cohesity_sdk.helios.models.ad_ldap_provider_type_params import AdLdapProviderTypeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdLdapProviderTypeParams from a JSON string
ad_ldap_provider_type_params_instance = AdLdapProviderTypeParams.from_json(json)
# print the JSON string representation of the object
print(AdLdapProviderTypeParams.to_json())

# convert the object into a dict
ad_ldap_provider_type_params_dict = ad_ldap_provider_type_params_instance.to_dict()
# create an instance of AdLdapProviderTypeParams from a dict
ad_ldap_provider_type_params_from_dict = AdLdapProviderTypeParams.from_dict(ad_ldap_provider_type_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


