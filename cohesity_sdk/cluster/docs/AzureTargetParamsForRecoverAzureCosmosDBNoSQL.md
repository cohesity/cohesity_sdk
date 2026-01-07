# AzureTargetParamsForRecoverAzureCosmosDBNoSQL

Specifies the recovery target params for Azure CosmosDB NoSQL target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool, none_type** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**ingest_rate_cap** | **float, none_type** | Specifies the ingest rate cap for the recovery. Default value is 0.4. | [optional] 
**new_source_config** | [**RecoverAzureDbNewSourceConfig**](RecoverAzureDbNewSourceConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


