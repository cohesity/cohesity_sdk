# OracleProtectionGroupDbParams

Specifies the parameters of individual databases to create Oracle Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_id** | **int, none_type** | Specifies the id of the Oracle database. | [optional] 
**database_name** | **str, none_type** | Specifies the name of the Oracle database. | [optional] [readonly] 
**db_channels** | [**[OracleDbChannel], none_type**](OracleDbChannel.md) | Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


