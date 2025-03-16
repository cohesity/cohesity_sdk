# AwsS3ProtectionParams

Specifies the parameters which are specific to AWS Object Protection for AWS S3. Atlease one of tags or objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_object_level_acls** | **bool** | Specifies whether to backup object level acls. Default value is false. | [optional] 
**objects** | [**List[AwsS3ObjectLevelParams]**](AwsS3ObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**skip_on_error** | **bool** | Specifies whether to skip files on error or not. Default value is false. | [optional] 
**storage_class** | **List[str]** | Specifies the AWS S3 Storage classes to backup. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_s3_protection_params import AwsS3ProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3ProtectionParams from a JSON string
aws_s3_protection_params_instance = AwsS3ProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AwsS3ProtectionParams.to_json())

# convert the object into a dict
aws_s3_protection_params_dict = aws_s3_protection_params_instance.to_dict()
# create an instance of AwsS3ProtectionParams from a dict
aws_s3_protection_params_from_dict = AwsS3ProtectionParams.from_dict(aws_s3_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


