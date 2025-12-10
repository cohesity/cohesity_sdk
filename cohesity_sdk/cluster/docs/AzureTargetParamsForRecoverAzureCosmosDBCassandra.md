# AzureTargetParamsForRecoverAzureCosmosDBCassandra

Specifies the recovery target params for Azure CosmosDB Cassandra target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingest_rate_cap** | **float** | Specifies the ingest rate cap for the recovery. Default value is 0.4. | [optional] 
**new_source_config** | [**RecoverAzureDbNewSourceConfig**](RecoverAzureDbNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_cosmos_db_cassandra import AzureTargetParamsForRecoverAzureCosmosDBCassandra

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureCosmosDBCassandra from a JSON string
azure_target_params_for_recover_azure_cosmos_db_cassandra_instance = AzureTargetParamsForRecoverAzureCosmosDBCassandra.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureCosmosDBCassandra.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_cosmos_db_cassandra_dict = azure_target_params_for_recover_azure_cosmos_db_cassandra_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureCosmosDBCassandra from a dict
azure_target_params_for_recover_azure_cosmos_db_cassandra_from_dict = AzureTargetParamsForRecoverAzureCosmosDBCassandra.from_dict(azure_target_params_for_recover_azure_cosmos_db_cassandra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


