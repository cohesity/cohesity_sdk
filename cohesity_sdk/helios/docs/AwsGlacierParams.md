# AwsGlacierParams

Specifies the parameters which are specific to AWS related External Targets with storage class Glacier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_type** | **str** | Specifies the AWS External Target type. | 
**aws_cloud_c2_s_params** | [**AwsCloudC2SParams**](AwsCloudC2SParams.md) |  | [optional] 
**aws_cloud_gov_params** | [**AwsCloudGovParams**](AwsCloudGovParams.md) |  | [optional] 
**aws_cloud_standard_params** | [**AwsCloudStandardParams**](AwsCloudStandardParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_glacier_params import AwsGlacierParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsGlacierParams from a JSON string
aws_glacier_params_instance = AwsGlacierParams.from_json(json)
# print the JSON string representation of the object
print(AwsGlacierParams.to_json())

# convert the object into a dict
aws_glacier_params_dict = aws_glacier_params_instance.to_dict()
# create an instance of AwsGlacierParams from a dict
aws_glacier_params_from_dict = AwsGlacierParams.from_dict(aws_glacier_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


