# RecoverSqlParams

Specifies the recovery options specific to Sql environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**recover_app_files_params** | [**[RecoverSqlAppFilesParams], none_type**](RecoverSqlAppFilesParams.md) | Specifies parameters for recovering SQL databases as flat files. Includes options to set the destination path and control whether existing files should be overwritten. | [optional] 
**recover_app_params** | [**[RecoverSqlAppParams], none_type**](RecoverSqlAppParams.md) | Specifies the parameters to recover Sql databases. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


