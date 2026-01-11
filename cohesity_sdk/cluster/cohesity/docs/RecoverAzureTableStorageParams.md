# RecoverAzureTableStorageParams

Specifies the parameters to recover Azure Table Storage.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverAzureTableStorageSnapshotParams], none_type**](RecoverAzureTableStorageSnapshotParams.md) | Specifies the details of the azure table storage objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAzure"
**azure_target_params** | [**AzureTargetParamsForRecoverAzureTableStorage**](AzureTargetParamsForRecoverAzureTableStorage.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


