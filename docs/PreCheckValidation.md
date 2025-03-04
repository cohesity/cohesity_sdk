# PreCheckValidation

Specifies details of pre-check validations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_passed** | **bool** | Specifies validation passed or failed | [optional] 
**message** | **str** | Specifies the validation failure message | [optional] 
**validation** | **str** | Specifies validation type | [optional] 

## Example

```python
from cohesity_sdk.models.pre_check_validation import PreCheckValidation

# TODO update the JSON string below
json = "{}"
# create an instance of PreCheckValidation from a JSON string
pre_check_validation_instance = PreCheckValidation.from_json(json)
# print the JSON string representation of the object
print(PreCheckValidation.to_json())

# convert the object into a dict
pre_check_validation_dict = pre_check_validation_instance.to_dict()
# create an instance of PreCheckValidation from a dict
pre_check_validation_from_dict = PreCheckValidation.from_dict(pre_check_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


