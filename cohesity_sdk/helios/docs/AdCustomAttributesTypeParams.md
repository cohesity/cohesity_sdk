# AdCustomAttributesTypeParams

Specifies the properties accociated to a CustomAttributes type user id mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_option** | [**FallbackUserIdMappingParams**](FallbackUserIdMappingParams.md) | Specifies a fallback user id mapping param in case the primary config does not work. | 
**gid_attr_name** | **str** | Specifies the custom field name in Active Directory user properties to get the GID. | 
**uid_attr_name** | **str** | Specifies the custom field name in Active Directory user properties to get the UID. | 

## Example

```python
from cohesity_sdk.helios.models.ad_custom_attributes_type_params import AdCustomAttributesTypeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdCustomAttributesTypeParams from a JSON string
ad_custom_attributes_type_params_instance = AdCustomAttributesTypeParams.from_json(json)
# print the JSON string representation of the object
print(AdCustomAttributesTypeParams.to_json())

# convert the object into a dict
ad_custom_attributes_type_params_dict = ad_custom_attributes_type_params_instance.to_dict()
# create an instance of AdCustomAttributesTypeParams from a dict
ad_custom_attributes_type_params_from_dict = AdCustomAttributesTypeParams.from_dict(ad_custom_attributes_type_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


