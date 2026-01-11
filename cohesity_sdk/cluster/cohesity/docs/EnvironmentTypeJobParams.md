# EnvironmentTypeJobParams

Specifies the policy level additional environment specific backup params. If this is not specified, default actions will be taken, for example for NAS environments, all objects within the source will be backed up.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_snapshot_params** | [**AwsSnapshotManagerParams**](AwsSnapshotManagerParams.md) |  | [optional] 
**exchange_params** | [**ExchangeEnvJobParams**](ExchangeEnvJobParams.md) |  | [optional] 
**externally_triggered_job_params** | [**ExternallyTriggeredJobParams**](ExternallyTriggeredJobParams.md) |  | [optional] 
**hyperv_params** | [**HypervEnvJobParams**](HypervEnvJobParams.md) |  | [optional] 
**nas_params** | [**NasEnvJobParams**](NasEnvJobParams.md) |  | [optional] 
**office365_params** | [**O365EnvJobParams**](O365EnvJobParams.md) |  | [optional] 
**oracle_params** | [**OracleEnvJobParams**](OracleEnvJobParams.md) |  | [optional] 
**physical_params** | [**PhysicalEnvJobParams**](PhysicalEnvJobParams.md) |  | [optional] 
**pure_params** | [**SanEnvJobParams**](SanEnvJobParams.md) |  | [optional] 
**sql_params** | [**CommonMSSQLProtectionGroupParams**](CommonMSSQLProtectionGroupParams.md) |  | [optional] 
**vmware_params** | [**VmwareEnvJobParams**](VmwareEnvJobParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


