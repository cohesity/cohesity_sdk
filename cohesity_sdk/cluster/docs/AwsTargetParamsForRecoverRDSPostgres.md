# AwsTargetParamsForRecoverRDSPostgres

Specifies the recovery target params for RDS Postgres target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_known_source** | **bool, none_type** | Specifies whether the recovery should be performed to a known or a custom target. | 
**custom_server_config** | [**RecoverRDSPostgresCustomServerConfig**](RecoverRDSPostgresCustomServerConfig.md) |  | [optional] 
**known_source_config** | [**RecoverRDSPostgresToKnownSourceConfig**](RecoverRDSPostgresToKnownSourceConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


