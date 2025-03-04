# AwsCloudGovParams

Specifies the parameters which are specific to AWS related External Targets with Cloud Type Gov.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**AwsAuthenticationMethodsParams**](AwsAuthenticationMethodsParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.aws_cloud_gov_params import AwsCloudGovParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCloudGovParams from a JSON string
aws_cloud_gov_params_instance = AwsCloudGovParams.from_json(json)
# print the JSON string representation of the object
print(AwsCloudGovParams.to_json())

# convert the object into a dict
aws_cloud_gov_params_dict = aws_cloud_gov_params_instance.to_dict()
# create an instance of AwsCloudGovParams from a dict
aws_cloud_gov_params_from_dict = AwsCloudGovParams.from_dict(aws_cloud_gov_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


