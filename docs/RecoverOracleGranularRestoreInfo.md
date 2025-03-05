# RecoverOracleGranularRestoreInfo

Specifies information about list of objects (PDBs) to restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**granularity_type** | **str** | Specifies type of granular restore. | [optional] 
**pdb_restore_params** | [**OraclePdbRestoreParams**](OraclePdbRestoreParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_oracle_granular_restore_info import RecoverOracleGranularRestoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleGranularRestoreInfo from a JSON string
recover_oracle_granular_restore_info_instance = RecoverOracleGranularRestoreInfo.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleGranularRestoreInfo.to_json())

# convert the object into a dict
recover_oracle_granular_restore_info_dict = recover_oracle_granular_restore_info_instance.to_dict()
# create an instance of RecoverOracleGranularRestoreInfo from a dict
recover_oracle_granular_restore_info_from_dict = RecoverOracleGranularRestoreInfo.from_dict(recover_oracle_granular_restore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


