# AwsS3ObjectLevelParams

Specifies the Aws S3 object level settings for object protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**exclude_object_ids** | **[int, none_type]** | Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects (can include tags) under a parent object which has been included for protection. | [optional] 
**object_prefix_exclusions** | **[str]** | Specifies the list of prefix paths excluded. Objects containing any of these prefixes in their path will be excluded. | [optional] 
**object_prefix_inclusions** | **[str]** | Specifies the list of prefix paths included. Objects containing any of these prefixes in their path will be included. Among inclusion and exclusion, inclusion will take precedence. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


