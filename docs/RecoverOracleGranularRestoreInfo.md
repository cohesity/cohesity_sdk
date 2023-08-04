# RecoverOracleGranularRestoreInfo

Specifies information about list of objects (PDBs) to restore.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**granularity_type** | **str, none_type** | Specifies type of granular restore. | [optional]  if omitted the server will use the default value of "kPDB"
**pdb_restore_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies information about the list of pdbs to be restored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


