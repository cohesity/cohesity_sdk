# AwsNativeObjectProtectionParams

Specifies the parameters which are specific to AWS Object Protection Groups using AWS native snapshot APIs. Atlease one of tags or objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[AwsObjectLevelParams]**](AwsObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


