# RecoverPureGroupTargetParams

Specifies the target object parameters to recover the Pure San group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies whether to recover to a new source. | 
**new_source_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the new destination Source configuration parameters where the Pure group will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the Source configuration if Pure group is being recovered to Original Source. If not specified, all the configuration parameters will be retained. | [optional] 
**use_thin_clone** | **bool, none_type** | Specifies whether to use thin clone to restore storage array snapshots. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

