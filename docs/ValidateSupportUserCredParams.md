# ValidateSupportUserCredParams

Specifies the support user credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password of the user to validate. | 

## Example

```python
from cohesity_sdk.models.validate_support_user_cred_params import ValidateSupportUserCredParams

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateSupportUserCredParams from a JSON string
validate_support_user_cred_params_instance = ValidateSupportUserCredParams.from_json(json)
# print the JSON string representation of the object
print(ValidateSupportUserCredParams.to_json())

# convert the object into a dict
validate_support_user_cred_params_dict = validate_support_user_cred_params_instance.to_dict()
# create an instance of ValidateSupportUserCredParams from a dict
validate_support_user_cred_params_from_dict = ValidateSupportUserCredParams.from_dict(validate_support_user_cred_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


