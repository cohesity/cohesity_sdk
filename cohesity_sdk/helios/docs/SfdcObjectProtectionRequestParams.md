# SfdcObjectProtectionRequestParams

Specifies the request parameters specific to Sfdc object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[SfdcObjectProtectionObjectParams]**](SfdcObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 

## Example

```python
from cohesity_sdk.helios.models.sfdc_object_protection_request_params import SfdcObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcObjectProtectionRequestParams from a JSON string
sfdc_object_protection_request_params_instance = SfdcObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(SfdcObjectProtectionRequestParams.to_json())

# convert the object into a dict
sfdc_object_protection_request_params_dict = sfdc_object_protection_request_params_instance.to_dict()
# create an instance of SfdcObjectProtectionRequestParams from a dict
sfdc_object_protection_request_params_from_dict = SfdcObjectProtectionRequestParams.from_dict(sfdc_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


