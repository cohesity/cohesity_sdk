# OraclePdbObjectInfo

Specifies information PDB object to restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_id** | **str** | Specifies pluggable database id. | 
**db_name** | **str** | Specifies name of the DB. | 

## Example

```python
from cohesity_sdk.cluster.models.oracle_pdb_object_info import OraclePdbObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OraclePdbObjectInfo from a JSON string
oracle_pdb_object_info_instance = OraclePdbObjectInfo.from_json(json)
# print the JSON string representation of the object
print(OraclePdbObjectInfo.to_json())

# convert the object into a dict
oracle_pdb_object_info_dict = oracle_pdb_object_info_instance.to_dict()
# create an instance of OraclePdbObjectInfo from a dict
oracle_pdb_object_info_from_dict = OraclePdbObjectInfo.from_dict(oracle_pdb_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


