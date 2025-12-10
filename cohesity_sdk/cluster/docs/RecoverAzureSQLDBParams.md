# RecoverAzureSQLDBParams

Specifies the parameters to recover Azure SQL Database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureSQLDB**](AzureTargetParamsForRecoverAzureSQLDB.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureSQLDBSnapshotParams]**](RecoverAzureSQLDBSnapshotParams.md) | Specifies the details of the azure SQL Database objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_sqldb_params import RecoverAzureSQLDBParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureSQLDBParams from a JSON string
recover_azure_sqldb_params_instance = RecoverAzureSQLDBParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureSQLDBParams.to_json())

# convert the object into a dict
recover_azure_sqldb_params_dict = recover_azure_sqldb_params_instance.to_dict()
# create an instance of RecoverAzureSQLDBParams from a dict
recover_azure_sqldb_params_from_dict = RecoverAzureSQLDBParams.from_dict(recover_azure_sqldb_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


