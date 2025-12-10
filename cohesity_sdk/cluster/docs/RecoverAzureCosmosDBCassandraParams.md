# RecoverAzureCosmosDBCassandraParams

Specifies the parameters to recover Azure CosmosDB Cassandra.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureCosmosDBCassandra**](AzureTargetParamsForRecoverAzureCosmosDBCassandra.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureCosmosDBCassandraSnapshotParams]**](RecoverAzureCosmosDBCassandraSnapshotParams.md) | Specifies the details of the azure cosmosdb cassandra objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_cosmos_db_cassandra_params import RecoverAzureCosmosDBCassandraParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureCosmosDBCassandraParams from a JSON string
recover_azure_cosmos_db_cassandra_params_instance = RecoverAzureCosmosDBCassandraParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureCosmosDBCassandraParams.to_json())

# convert the object into a dict
recover_azure_cosmos_db_cassandra_params_dict = recover_azure_cosmos_db_cassandra_params_instance.to_dict()
# create an instance of RecoverAzureCosmosDBCassandraParams from a dict
recover_azure_cosmos_db_cassandra_params_from_dict = RecoverAzureCosmosDBCassandraParams.from_dict(recover_azure_cosmos_db_cassandra_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


