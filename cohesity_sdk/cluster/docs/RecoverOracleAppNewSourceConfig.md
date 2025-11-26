# RecoverOracleAppNewSourceConfig

Specifies the new destination Source configuration where the databases will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the source id of target host where databases will be recovered. This source id can be a physical host or virtual machine. | 
**recover_database_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies recovery parameters when recovering to a database | [optional] 
**recover_view_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies recovery parameters when recovering to a view. | [optional] 
**recovery_target** | **str, none_type** | Specifies if recovery target is a database or a view. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


