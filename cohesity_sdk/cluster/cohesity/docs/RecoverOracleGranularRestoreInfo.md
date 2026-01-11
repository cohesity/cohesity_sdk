# RecoverOracleGranularRestoreInfo

Specifies information about list of objects (PDBs) to restore.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**granularity_type** | **str, none_type** | Specifies type of granular restore. | [optional]  if omitted the server will use the default value of "kPDB"
**pdb_restore_params** | [**OraclePdbRestoreParams**](OraclePdbRestoreParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


