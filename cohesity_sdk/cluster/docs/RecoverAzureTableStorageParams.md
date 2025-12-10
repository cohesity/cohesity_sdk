# RecoverAzureTableStorageParams

Specifies the parameters to recover Azure Table Storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureTableStorage**](AzureTargetParamsForRecoverAzureTableStorage.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureTableStorageSnapshotParams]**](RecoverAzureTableStorageSnapshotParams.md) | Specifies the details of the azure table storage objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_table_storage_params import RecoverAzureTableStorageParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureTableStorageParams from a JSON string
recover_azure_table_storage_params_instance = RecoverAzureTableStorageParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureTableStorageParams.to_json())

# convert the object into a dict
recover_azure_table_storage_params_dict = recover_azure_table_storage_params_instance.to_dict()
# create an instance of RecoverAzureTableStorageParams from a dict
recover_azure_table_storage_params_from_dict = RecoverAzureTableStorageParams.from_dict(recover_azure_table_storage_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


