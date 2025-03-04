# CommonSourceRegistrationParams

Specifies common parameters to register a source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 

## Example

```python
from cohesity_sdk.models.common_source_registration_params import CommonSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSourceRegistrationParams from a JSON string
common_source_registration_params_instance = CommonSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(CommonSourceRegistrationParams.to_json())

# convert the object into a dict
common_source_registration_params_dict = common_source_registration_params_instance.to_dict()
# create an instance of CommonSourceRegistrationParams from a dict
common_source_registration_params_from_dict = CommonSourceRegistrationParams.from_dict(common_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


