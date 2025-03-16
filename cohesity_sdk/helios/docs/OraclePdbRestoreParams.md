# OraclePdbRestoreParams

Specifies information about the list of pdbs to be restored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_duplicate_pdb** | **bool** | Specifies if the PDB should be ignored if a PDB already exists with same name. | [optional] 
**include_in_restore** | **bool** | Specifies whether to restore or skip the provided PDBs list. | [optional] 
**pdb_objects** | [**List[OraclePdbObjectInfo]**](OraclePdbObjectInfo.md) | Specifies list of PDB objects to restore. | [optional] 
**rename_pdb_map** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the new PDB name mapping to existing PDBs. | [optional] 
**restore_to_existing_cdb** | **bool** | Specifies if pdbs should be restored to an existing CDB. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.oracle_pdb_restore_params import OraclePdbRestoreParams

# TODO update the JSON string below
json = "{}"
# create an instance of OraclePdbRestoreParams from a JSON string
oracle_pdb_restore_params_instance = OraclePdbRestoreParams.from_json(json)
# print the JSON string representation of the object
print(OraclePdbRestoreParams.to_json())

# convert the object into a dict
oracle_pdb_restore_params_dict = oracle_pdb_restore_params_instance.to_dict()
# create an instance of OraclePdbRestoreParams from a dict
oracle_pdb_restore_params_from_dict = OraclePdbRestoreParams.from_dict(oracle_pdb_restore_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


