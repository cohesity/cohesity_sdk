# AwsCloudStandardParams

Specifies the parameters which are specific to AWS related External Targets with Cloud Type Standard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**AwsAuthenticationMethodsParams**](AwsAuthenticationMethodsParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_cloud_standard_params import AwsCloudStandardParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCloudStandardParams from a JSON string
aws_cloud_standard_params_instance = AwsCloudStandardParams.from_json(json)
# print the JSON string representation of the object
print(AwsCloudStandardParams.to_json())

# convert the object into a dict
aws_cloud_standard_params_dict = aws_cloud_standard_params_instance.to_dict()
# create an instance of AwsCloudStandardParams from a dict
aws_cloud_standard_params_from_dict = AwsCloudStandardParams.from_dict(aws_cloud_standard_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


