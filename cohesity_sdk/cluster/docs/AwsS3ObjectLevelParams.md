# AwsS3ObjectLevelParams

Specifies the Aws S3 object level settings for object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**object_prefix_exclusions** | **List[str]** | Specifies the list of prefix paths excluded. Objects containing any of these prefixes in their path will be excluded. | [optional] 
**object_prefix_inclusions** | **List[str]** | Specifies the list of prefix paths included. Objects containing any of these prefixes in their path will be included. Among inclusion and exclusion, inclusion will take precedence. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_s3_object_level_params import AwsS3ObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3ObjectLevelParams from a JSON string
aws_s3_object_level_params_instance = AwsS3ObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(AwsS3ObjectLevelParams.to_json())

# convert the object into a dict
aws_s3_object_level_params_dict = aws_s3_object_level_params_instance.to_dict()
# create an instance of AwsS3ObjectLevelParams from a dict
aws_s3_object_level_params_from_dict = AwsS3ObjectLevelParams.from_dict(aws_s3_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


