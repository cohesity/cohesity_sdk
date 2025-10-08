# OraclePdbRestoreParams

Specifies information about the list of pdbs to be restored.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_duplicate_pdb** | **bool, none_type** | Specifies if the PDB should be ignored if a PDB already exists with same name. | [optional] 
**include_in_restore** | **bool, none_type** | Specifies whether to restore or skip the provided PDBs list. | [optional] 
**pdb_objects** | [**[OraclePdbObjectInfo], none_type**](OraclePdbObjectInfo.md) | Specifies list of PDB objects to restore. | [optional] 
**rename_pdb_map** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies the new PDB name mapping to existing PDBs. | [optional] 
**restore_to_existing_cdb** | **bool, none_type** | Specifies if pdbs should be restored to an existing CDB. | [optional] 
**source_cdb_keystore_password** | **str, none_type** | Specifies the keystore password of the source CDB. | [optional] 
**target_cdb_keystore_password** | **str, none_type** | Specifies the keystore password of the target CDB. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


