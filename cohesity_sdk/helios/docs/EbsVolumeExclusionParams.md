# EbsVolumeExclusionParams

Specifies the parameters to exclude EBS volumes attached to EC2 instances at global and object level. A volume satisfying any of these criteria will be excluded.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_ids** | **[str], none_type** | Array of volume IDs that are to be excluded. This is only for object level exclusion. | [optional] 
**max_volume_size_bytes** | **int, none_type** | Any volume larger than this size will be excluded. | [optional] 
**volume_types** | **[str], none_type** | Array of volume types to exclude. Eg - gp2, gp3. | [optional] 
**device_names** | **[str], none_type** | Array of device names to exclude. Eg - /dev/sda. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


