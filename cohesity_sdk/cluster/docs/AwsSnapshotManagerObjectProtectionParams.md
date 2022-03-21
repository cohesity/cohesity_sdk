# AwsSnapshotManagerObjectProtectionParams

Specifies the parameters which are specific to AWS Object Protection using AWS native snapshot orchestration with snapshot manager. Atlease one of tags or objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[AwsObjectLevelParams]**](AwsObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 
**create_ami** | **bool, none_type** | Specifies whether AMI should be created after taking snapshots of the instance. | [optional] 
**ami_creation_frequency** | **int, none_type** | The frequency of AMI creation. This should be set if the option to create AMI is set. A value of n creates an AMI from the snapshots after every n runs. eg. n &#x3D; 2 implies every alternate backup run starting from the first will create an AMI. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


