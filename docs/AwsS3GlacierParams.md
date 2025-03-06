# AwsS3GlacierParams

Specifies the parameters which are specific to AWS related External Targets with storage class S3 Glacier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_type** | **str** | Specifies the AWS External Target type. | 
**aws_cloud_gov_params** | [**AwsCloudGovParams**](AwsCloudGovParams.md) |  | [optional] 
**aws_cloud_standard_params** | [**AwsCloudStandardParams**](AwsCloudStandardParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_s3_glacier_params import AwsS3GlacierParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3GlacierParams from a JSON string
aws_s3_glacier_params_instance = AwsS3GlacierParams.from_json(json)
# print the JSON string representation of the object
print(AwsS3GlacierParams.to_json())

# convert the object into a dict
aws_s3_glacier_params_dict = aws_s3_glacier_params_instance.to_dict()
# create an instance of AwsS3GlacierParams from a dict
aws_s3_glacier_params_from_dict = AwsS3GlacierParams.from_dict(aws_s3_glacier_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


