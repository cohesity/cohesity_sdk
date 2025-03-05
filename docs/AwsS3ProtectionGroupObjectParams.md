# AwsS3ProtectionGroupObjectParams

Specifies the object parameters to create an AWS S3 Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.aws_s3_protection_group_object_params import AwsS3ProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3ProtectionGroupObjectParams from a JSON string
aws_s3_protection_group_object_params_instance = AwsS3ProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsS3ProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_s3_protection_group_object_params_dict = aws_s3_protection_group_object_params_instance.to_dict()
# create an instance of AwsS3ProtectionGroupObjectParams from a dict
aws_s3_protection_group_object_params_from_dict = AwsS3ProtectionGroupObjectParams.from_dict(aws_s3_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


