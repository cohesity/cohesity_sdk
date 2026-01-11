# TargetsConfiguration

Specifies the replication, archival and cloud spin targets of Protection Policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_targets** | [**[ArchivalConfig]**](ArchivalConfig.md) |  | [optional] 
**cloud_spin_targets** | [**[CloudSpinConfig]**](CloudSpinConfig.md) |  | [optional] 
**onprem_deploy_targets** | [**[OnpremDeployConfig]**](OnpremDeployConfig.md) |  | [optional] 
**onprem_vault_targets** | [**[OnpremVaultConfig]**](OnpremVaultConfig.md) |  | [optional] 
**replication_targets** | [**[ReplicationConfig]**](ReplicationConfig.md) |  | [optional] 
**rpaas_targets** | [**[RpaasConfig]**](RpaasConfig.md) |  | [optional] 
**source_targets** | [**SourceConfig**](SourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


