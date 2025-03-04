# AwsUseSTSParams

Specifies the parameters which are specific to UseSTS Authentication Method for AWS External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_blob** | **str** | Credential blob to use when interacting with credential endpoint. | [optional] 
**auth_endpoint** | **str** | Specifies the credential endpoint to use to generate the security token. | 

## Example

```python
from cohesity_sdk.models.aws_use_sts_params import AwsUseSTSParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsUseSTSParams from a JSON string
aws_use_sts_params_instance = AwsUseSTSParams.from_json(json)
# print the JSON string representation of the object
print(AwsUseSTSParams.to_json())

# convert the object into a dict
aws_use_sts_params_dict = aws_use_sts_params_instance.to_dict()
# create an instance of AwsUseSTSParams from a dict
aws_use_sts_params_from_dict = AwsUseSTSParams.from_dict(aws_use_sts_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


