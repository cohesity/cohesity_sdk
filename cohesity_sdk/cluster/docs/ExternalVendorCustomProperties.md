# ExternalVendorCustomProperties

Specifies the list of custom properties associated with the tenant. External vendors can choose to set the following properties using provided key and value fields. The input values must always be in the string format and each key must be unique. API callers should make sure that no sensitive information such as passwords is sent in these fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the unique key for custom property. | [optional] 
**value** | **str** | Specifies the value for the above custom key. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.external_vendor_custom_properties import ExternalVendorCustomProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalVendorCustomProperties from a JSON string
external_vendor_custom_properties_instance = ExternalVendorCustomProperties.from_json(json)
# print the JSON string representation of the object
print(ExternalVendorCustomProperties.to_json())

# convert the object into a dict
external_vendor_custom_properties_dict = external_vendor_custom_properties_instance.to_dict()
# create an instance of ExternalVendorCustomProperties from a dict
external_vendor_custom_properties_from_dict = ExternalVendorCustomProperties.from_dict(external_vendor_custom_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


