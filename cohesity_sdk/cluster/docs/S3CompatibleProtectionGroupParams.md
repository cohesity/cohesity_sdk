# S3CompatibleProtectionGroupParams

Specifies the parameters which are specific to S3 Compatible related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_object_level_acls** | **bool** | Specifies whether to backup object level acls. Default value is false. | [optional] 
**objects** | [**List[S3CompatibleProtectionGroupObjectParams]**](S3CompatibleProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**protection_type** | **str** | Specifies the S3 Compatible Protection type. | [optional] [readonly] 
**source_id** | **int** | Specifies the parent id of the objects being protected. | [optional] [readonly] 
**source_name** | **str** | Specifies the parent source name of the objects being protected. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.s3_compatible_protection_group_params import S3CompatibleProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of S3CompatibleProtectionGroupParams from a JSON string
s3_compatible_protection_group_params_instance = S3CompatibleProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(S3CompatibleProtectionGroupParams.to_json())

# convert the object into a dict
s3_compatible_protection_group_params_dict = s3_compatible_protection_group_params_instance.to_dict()
# create an instance of S3CompatibleProtectionGroupParams from a dict
s3_compatible_protection_group_params_from_dict = S3CompatibleProtectionGroupParams.from_dict(s3_compatible_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


