# ConstructRestoreMetaInfoOracleParams

Params to fetch oracle restore meta info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dir** | **str** | Specifies the base directory of Oracle at destination. | [optional] 
**db_file_destination** | **str** | Specifies the location to put the database files(datafiles, logfiles etc.) | [optional] 
**db_name** | **str** | Specifies the name of the Oracle database that we restore to. | [optional] 
**home_dir** | **str** | Specifies the home directory of Oracle at destination. | [optional] 
**is_clone** | **bool** | Specifies whether operation is clone or not | [optional] 
**is_disaster_recovery** | **bool** | Specifies whether the recovery is of type Disaster Recovery. | [optional] 
**is_granular_restore** | **bool** | Specifies whether the operation is granular restore or not. | [optional] 
**is_recovery_validation** | **bool** | Specifies whether the operation is recovery validation or not. | [optional] 

## Example

```python
from cohesity_sdk.models.construct_restore_meta_info_oracle_params import ConstructRestoreMetaInfoOracleParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructRestoreMetaInfoOracleParams from a JSON string
construct_restore_meta_info_oracle_params_instance = ConstructRestoreMetaInfoOracleParams.from_json(json)
# print the JSON string representation of the object
print(ConstructRestoreMetaInfoOracleParams.to_json())

# convert the object into a dict
construct_restore_meta_info_oracle_params_dict = construct_restore_meta_info_oracle_params_instance.to_dict()
# create an instance of ConstructRestoreMetaInfoOracleParams from a dict
construct_restore_meta_info_oracle_params_from_dict = ConstructRestoreMetaInfoOracleParams.from_dict(construct_restore_meta_info_oracle_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


