# RecoverAzureSqlParams

Specifies the parameters to recover Azure SQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureSql**](AzureTargetParamsForRecoverAzureSql.md) | Specifies the params for recovering to an Azure target. | [optional] 
**snapshots** | [**List[RecoverAzureSqlSnapshotParams]**](RecoverAzureSqlSnapshotParams.md) | Specifies the details of the azure sql objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_azure_sql_params import RecoverAzureSqlParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureSqlParams from a JSON string
recover_azure_sql_params_instance = RecoverAzureSqlParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureSqlParams.to_json())

# convert the object into a dict
recover_azure_sql_params_dict = recover_azure_sql_params_instance.to_dict()
# create an instance of RecoverAzureSqlParams from a dict
recover_azure_sql_params_from_dict = RecoverAzureSqlParams.from_dict(recover_azure_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


