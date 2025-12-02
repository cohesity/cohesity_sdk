# RecoverAzureMySQLParams

Specifies the parameters to recover Azure MySQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureMySQL**](AzureTargetParamsForRecoverAzureMySQL.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureMySQLSnapshotParams]**](RecoverAzureMySQLSnapshotParams.md) | Specifies the details of the azure mysql objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_my_sql_params import RecoverAzureMySQLParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureMySQLParams from a JSON string
recover_azure_my_sql_params_instance = RecoverAzureMySQLParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureMySQLParams.to_json())

# convert the object into a dict
recover_azure_my_sql_params_dict = recover_azure_my_sql_params_instance.to_dict()
# create an instance of RecoverAzureMySQLParams from a dict
recover_azure_my_sql_params_from_dict = RecoverAzureMySQLParams.from_dict(recover_azure_my_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


