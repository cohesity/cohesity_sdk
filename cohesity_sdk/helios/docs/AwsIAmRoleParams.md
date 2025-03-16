# AwsIAmRoleParams

Specifies the parameters which are specific to IAmRole Authentication Method for AWS External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Specifies the Account Id of the external target. | [optional] 
**i_am_role** | **str** | Specifies the I Am Role of the external target. | 

## Example

```python
from cohesity_sdk.helios.models.aws_iam_role_params import AwsIAmRoleParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsIAmRoleParams from a JSON string
aws_iam_role_params_instance = AwsIAmRoleParams.from_json(json)
# print the JSON string representation of the object
print(AwsIAmRoleParams.to_json())

# convert the object into a dict
aws_iam_role_params_dict = aws_iam_role_params_instance.to_dict()
# create an instance of AwsIAmRoleParams from a dict
aws_iam_role_params_from_dict = AwsIAmRoleParams.from_dict(aws_iam_role_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


