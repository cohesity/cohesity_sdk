# CommonArchivalExternalTargetParams

Specifies the common parameters which are specific to Archival purpose type External Targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption** | [**EncryptionSettings**](EncryptionSettings.md) |  | 
**storage_type** | **str, none_type** | Specifies the Storage type of the External Target. Nas option in archival_target_storage_type will soon be deprecated. Please use NAS instead. | 
**cad_config** | [**CloudArchivalDirectConfig**](CloudArchivalDirectConfig.md) |  | [optional] 
**target_bandwidth_throttlings** | [**TargetBandwidthThrottlings**](TargetBandwidthThrottlings.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


