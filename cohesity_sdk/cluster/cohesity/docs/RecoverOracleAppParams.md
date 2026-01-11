# RecoverOracleAppParams

Specifies the parameters to recover Oracle databases.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kOracle"
**oracle_target_params** | [**CommonRecoverOracleAppTargetParams**](CommonRecoverOracleAppTargetParams.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


