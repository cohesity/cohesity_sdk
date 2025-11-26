# RecoverRDSPostgresParams

Specifies the parameters to recover RDS Postgres.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAWS"
**aws_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params for recovering to an Aws target. | [optional] 
**overwrite_database** | **bool, none_type** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**prefix** | **str, none_type** | Specifies the prefix to be prepended to the object name after the recovery. | [optional] 
**suffix** | **str, none_type** | Specifies the suffix to be appended to the object name after the recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


