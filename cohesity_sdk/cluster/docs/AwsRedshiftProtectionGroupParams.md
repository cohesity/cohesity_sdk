# AwsRedshiftProtectionGroupParams

Specifies the parameters which are specific to AWS Redshift related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str** | The Cloud Storage bucket name for Redshift backup. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_redshift_tag_ids** | **List[List[int]]** | Array of arrays of Tag Ids that Specify Redshift databases to Exclude. | [optional] 
**objects** | [**List[AwsRedshiftProtectionGroupObjectParams]**](AwsRedshiftProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**redshift_tag_ids** | **List[List[int]]** | Array of arrays of Tag Ids that specify Redshift databases to Protect. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_redshift_protection_group_params import AwsRedshiftProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRedshiftProtectionGroupParams from a JSON string
aws_redshift_protection_group_params_instance = AwsRedshiftProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsRedshiftProtectionGroupParams.to_json())

# convert the object into a dict
aws_redshift_protection_group_params_dict = aws_redshift_protection_group_params_instance.to_dict()
# create an instance of AwsRedshiftProtectionGroupParams from a dict
aws_redshift_protection_group_params_from_dict = AwsRedshiftProtectionGroupParams.from_dict(aws_redshift_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


