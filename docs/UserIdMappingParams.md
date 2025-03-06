# UserIdMappingParams

Specifies how the Unix and Windows users are mapped in an Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**centrify_type_params** | [**AdCentrifyTypeParams**](AdCentrifyTypeParams.md) |  | [optional] 
**custom_attributes_type_params** | [**AdCustomAttributesTypeParams**](AdCustomAttributesTypeParams.md) |  | [optional] 
**fixed_type_params** | [**AdFixedTypeParams**](AdFixedTypeParams.md) |  | [optional] 
**ldap_provider_type_params** | [**AdLdapProviderTypeParams**](AdLdapProviderTypeParams.md) |  | [optional] 
**nis_provider_type_params** | [**AdNisProviderTypeParams**](AdNisProviderTypeParams.md) |  | [optional] 
**rfc2307_type_params** | [**AdRfc2307TypeParams**](AdRfc2307TypeParams.md) |  | [optional] 
**sfu30_type_params** | [**AdSfu30TypeParams**](AdSfu30TypeParams.md) |  | [optional] 
**type** | **str** | Specifies the type of the mapping. | 

## Example

```python
from cohesity_sdk.cluster.models.user_id_mapping_params import UserIdMappingParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdMappingParams from a JSON string
user_id_mapping_params_instance = UserIdMappingParams.from_json(json)
# print the JSON string representation of the object
print(UserIdMappingParams.to_json())

# convert the object into a dict
user_id_mapping_params_dict = user_id_mapping_params_instance.to_dict()
# create an instance of UserIdMappingParams from a dict
user_id_mapping_params_from_dict = UserIdMappingParams.from_dict(user_id_mapping_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


