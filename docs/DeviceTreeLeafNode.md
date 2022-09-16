# DeviceTreeLeafNode

Specifies the parameters of a leaf node in device tree.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_name** | **str, none_type** | Specifies the disk name. | [optional] 
**partition_number** | **int, none_type** | Specifies the paritition number. | [optional] 
**offset_bytes** | **int, none_type** | Specifies the offset in bytes where data for the LVM volume (for which this device tree is being build) starts relative to the start of the partition. | [optional] 
**length_bytes** | **int, none_type** | Specifies The length of data in bytes for the LVM volume (for which this device tree is being built). It does not include size of the LVM meta data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


