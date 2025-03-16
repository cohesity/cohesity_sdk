# SfdcObjectProtectionParams

Specifies the parameters that are specific to Sfdc Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[SfdcObjectProtectionObjectParams]**](SfdcObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 

## Example

```python
from cohesity_sdk.helios.models.sfdc_object_protection_params import SfdcObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcObjectProtectionParams from a JSON string
sfdc_object_protection_params_instance = SfdcObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(SfdcObjectProtectionParams.to_json())

# convert the object into a dict
sfdc_object_protection_params_dict = sfdc_object_protection_params_instance.to_dict()
# create an instance of SfdcObjectProtectionParams from a dict
sfdc_object_protection_params_from_dict = SfdcObjectProtectionParams.from_dict(sfdc_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


