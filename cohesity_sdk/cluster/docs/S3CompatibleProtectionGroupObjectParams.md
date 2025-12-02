# S3CompatibleProtectionGroupObjectParams

Specifies the object parameters to create an S3 Compatible Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 

## Example

```python
from cohesity_sdk.cluster.models.s3_compatible_protection_group_object_params import S3CompatibleProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of S3CompatibleProtectionGroupObjectParams from a JSON string
s3_compatible_protection_group_object_params_instance = S3CompatibleProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(S3CompatibleProtectionGroupObjectParams.to_json())

# convert the object into a dict
s3_compatible_protection_group_object_params_dict = s3_compatible_protection_group_object_params_instance.to_dict()
# create an instance of S3CompatibleProtectionGroupObjectParams from a dict
s3_compatible_protection_group_object_params_from_dict = S3CompatibleProtectionGroupObjectParams.from_dict(s3_compatible_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


