# RecoverRDSPostgresCustomServerConfig

Specifies the configuration for recovering RDS Objects to the custom target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Specifies the Ip in which to deploy the Rds objects. | 
**port** | **int, none_type** | Specifies the port to use to connect to the server. | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**standard_credentials** | [**Credentials**](Credentials.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


