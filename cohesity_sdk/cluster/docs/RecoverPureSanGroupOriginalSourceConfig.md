# RecoverPureSanGroupOriginalSourceConfig

Specifies the network config parameters to be applied for Pure group if recovering to original Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_recovered_group_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies params to rename the recovered SAN group. If not specified, the original names of the group are preserved. | [optional] 
**resource_pool** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the resource pool to recover the SAN Volume to. This field can be specified for cases where the resource pool can be altered on the original source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


