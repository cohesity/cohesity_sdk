# AwsIAmUserParams

Specifies the parameters which are specific to IAmUSer Authentication Method for AWS External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Specifies the Access Key Id of the external target. | 
**secret_access_key** | **str** | Specifies the Secret Access Key of the external target. | [optional] 

## Example

```python
from cohesity_sdk.models.aws_iam_user_params import AwsIAmUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsIAmUserParams from a JSON string
aws_iam_user_params_instance = AwsIAmUserParams.from_json(json)
# print the JSON string representation of the object
print(AwsIAmUserParams.to_json())

# convert the object into a dict
aws_iam_user_params_dict = aws_iam_user_params_instance.to_dict()
# create an instance of AwsIAmUserParams from a dict
aws_iam_user_params_from_dict = AwsIAmUserParams.from_dict(aws_iam_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


