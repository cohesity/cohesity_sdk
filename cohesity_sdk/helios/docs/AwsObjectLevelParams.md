# AwsObjectLevelParams

Specifies the Aws object level settings for object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects (can include tags) under a parent object which has been included for protection. | [optional] 
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_object_level_params import AwsObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsObjectLevelParams from a JSON string
aws_object_level_params_instance = AwsObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(AwsObjectLevelParams.to_json())

# convert the object into a dict
aws_object_level_params_dict = aws_object_level_params_instance.to_dict()
# create an instance of AwsObjectLevelParams from a dict
aws_object_level_params_from_dict = AwsObjectLevelParams.from_dict(aws_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


