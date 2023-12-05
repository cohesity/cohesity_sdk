# OraclePdbRestoreParams

Specifies information about the list of pdbs to be restored.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_duplicate_pdb** | **bool, none_type** | Specifies if the PDB should be ignored if a PDB already exists with same name. | [optional] 
**pdb_objects** | [**[OraclePdbObjectInfo], none_type**](OraclePdbObjectInfo.md) | Specifies list of PDB objects to restore. | [optional] 
**rename_pdb_map** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies the new PDB name mapping to existing PDBs. | [optional] 
**restore_to_existing_cdb** | **bool, none_type** | Specifies if pdbs should be restored to an existing CDB. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


