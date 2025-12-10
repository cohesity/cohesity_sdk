# RecoverAzureCosmosDBNoSQLParams

Specifies the parameters to recover Azure CosmosDB NoSQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureCosmosDBNoSQL**](AzureTargetParamsForRecoverAzureCosmosDBNoSQL.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureCosmosDBNoSQLSnapshotParams]**](RecoverAzureCosmosDBNoSQLSnapshotParams.md) | Specifies the details of the azure cosmosdb nosql objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_cosmos_dbno_sql_params import RecoverAzureCosmosDBNoSQLParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureCosmosDBNoSQLParams from a JSON string
recover_azure_cosmos_dbno_sql_params_instance = RecoverAzureCosmosDBNoSQLParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureCosmosDBNoSQLParams.to_json())

# convert the object into a dict
recover_azure_cosmos_dbno_sql_params_dict = recover_azure_cosmos_dbno_sql_params_instance.to_dict()
# create an instance of RecoverAzureCosmosDBNoSQLParams from a dict
recover_azure_cosmos_dbno_sql_params_from_dict = RecoverAzureCosmosDBNoSQLParams.from_dict(recover_azure_cosmos_dbno_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


