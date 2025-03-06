# CommonAuthenticationMethodParams

Specifies the cloud category parameter which are specific to AWS related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** | Specifies the AWS External Target Authentication type. | 

## Example

```python
from cohesity_sdk.cluster.models.common_authentication_method_params import CommonAuthenticationMethodParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAuthenticationMethodParams from a JSON string
common_authentication_method_params_instance = CommonAuthenticationMethodParams.from_json(json)
# print the JSON string representation of the object
print(CommonAuthenticationMethodParams.to_json())

# convert the object into a dict
common_authentication_method_params_dict = common_authentication_method_params_instance.to_dict()
# create an instance of CommonAuthenticationMethodParams from a dict
common_authentication_method_params_from_dict = CommonAuthenticationMethodParams.from_dict(common_authentication_method_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


