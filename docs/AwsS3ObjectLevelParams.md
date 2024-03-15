# AwsS3ObjectLevelParams

Specifies the Aws S3 object level settings for object protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**object_prefix_exclusions** | **[str]** | Specifies the list of prefix paths excluded. Objects containing any of these prefixes in their path will be excluded. | [optional] 
**object_prefix_inclusions** | **[str]** | Specifies the list of prefix paths included. Objects containing any of these prefixes in their path will be included. Among inclusion and exclusion, inclusion will take precedence. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


