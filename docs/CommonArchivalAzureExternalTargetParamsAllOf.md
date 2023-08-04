# CommonArchivalAzureExternalTargetParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_class** | **str, none_type** | Specifies the Azure External Target storage class. | 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the Azure external target | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_worm_enabled** | **bool, none_type** | Specifies whether write once read many (WORM) protection is enabled for the Azure container or not. | [optional] 
**worm_specific_target_params** | [**WormSpecificTargetParams**](WormSpecificTargetParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


