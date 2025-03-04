# AwsS3ProtectionGroupParams

Specifies the parameters which are specific to AWS S3 Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_object_level_acls** | **bool** | Specifies whether to backup object level acls. Default value is false. | [optional] 
**objects** | [**List[AwsS3ProtectionGroupObjectParams]**](AwsS3ProtectionGroupObjectParams.md) | Specifies the objects to be protected. | [optional] 
**skip_on_error** | **bool** | Specifies whether to skip files on error or not. Default value is false. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**storage_class** | **List[str]** | Specifies the AWS S3 Storage classes to backup. | [optional] 

## Example

```python
from cohesity_sdk.models.aws_s3_protection_group_params import AwsS3ProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3ProtectionGroupParams from a JSON string
aws_s3_protection_group_params_instance = AwsS3ProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsS3ProtectionGroupParams.to_json())

# convert the object into a dict
aws_s3_protection_group_params_dict = aws_s3_protection_group_params_instance.to_dict()
# create an instance of AwsS3ProtectionGroupParams from a dict
aws_s3_protection_group_params_from_dict = AwsS3ProtectionGroupParams.from_dict(aws_s3_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


