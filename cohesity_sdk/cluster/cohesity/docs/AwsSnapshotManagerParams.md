# AwsSnapshotManagerParams

Specifies job parameters applicable for all 'kVMware' Environment type Protection Sources in a Protection Job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ami_creation_frequency** | **int, none_type** | Specifies the frequency of AMI creation. This should be set if the option to create AMI is set. A value of n creates an AMI from the snapshots after every n runs. eg. n &#x3D; 2 implies every alternate backup run starting from the first will create an AMI. | [optional] 
**create_ami** | **bool, none_type** | If true, creates an AMI after taking snapshots of the instance. It should be set only while backing up EC2 instances. CreateAmi creates AMI for the protection job. | [optional] 
**volume_exclusion_params** | [**EbsVolumeExclusionParams**](EbsVolumeExclusionParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


