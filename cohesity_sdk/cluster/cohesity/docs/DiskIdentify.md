# DiskIdentify

Specifies the parameters needed to identify disk.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identify** | **bool** | Turn on/off led light if it is set to true/false | 
**disk_id** | **int, none_type** | Specifies the disk id of the disk. This parameter is incompatible with &#39;nodeId&#39; and &#39;serialNumber&#39;. | [optional] 
**node_id** | **int, none_type** | Specifies the node id of node that disk belongs to. This parameter is incompatible with &#39;diskId&#39;. Must be used together with &#39;serialNumber&#39;. | [optional] 
**serial_number** | **str, none_type** | Specifies serial number of disk. This parameter is incompatible with &#39;diskId&#39;. Must be used together with &#39;nodeId&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


