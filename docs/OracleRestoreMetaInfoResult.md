# OracleRestoreMetaInfoResult

Result to store oracle meta-info from snapshot id and other oracle params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohesity_pfile_param_map** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies map for cohesity controlled pfile params. | [optional] 
**inherited_pfile_param_map** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies map for inherited pfile params. | [optional] 
**restricted_pfile_param_map** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies map for restricted pfile params. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.oracle_restore_meta_info_result import OracleRestoreMetaInfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of OracleRestoreMetaInfoResult from a JSON string
oracle_restore_meta_info_result_instance = OracleRestoreMetaInfoResult.from_json(json)
# print the JSON string representation of the object
print(OracleRestoreMetaInfoResult.to_json())

# convert the object into a dict
oracle_restore_meta_info_result_dict = oracle_restore_meta_info_result_instance.to_dict()
# create an instance of OracleRestoreMetaInfoResult from a dict
oracle_restore_meta_info_result_from_dict = OracleRestoreMetaInfoResult.from_dict(oracle_restore_meta_info_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


