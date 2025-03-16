# SfdcObjectProtectionResponseParams

Specifies the response parameters specific to Sfdc object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[SfdcObjectProtectionObjectParams]**](SfdcObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 

## Example

```python
from cohesity_sdk.helios.models.sfdc_object_protection_response_params import SfdcObjectProtectionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcObjectProtectionResponseParams from a JSON string
sfdc_object_protection_response_params_instance = SfdcObjectProtectionResponseParams.from_json(json)
# print the JSON string representation of the object
print(SfdcObjectProtectionResponseParams.to_json())

# convert the object into a dict
sfdc_object_protection_response_params_dict = sfdc_object_protection_response_params_instance.to_dict()
# create an instance of SfdcObjectProtectionResponseParams from a dict
sfdc_object_protection_response_params_from_dict = SfdcObjectProtectionResponseParams.from_dict(sfdc_object_protection_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


