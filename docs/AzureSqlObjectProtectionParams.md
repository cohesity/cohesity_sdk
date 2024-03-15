# AzureSqlObjectProtectionParams

Specifies the parameters which are specific to Azure SQL Object Protection Groups using Azure native APIs. Atlease one of objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_database** | **bool, none_type** | If set to true, a copy of the database is created during backup, and the backup is performed from the copied database. This backup will be transactionally consistent. If set to false, the backup is performed from the production database while transactions are in progress. In this case, the backup will be transactionally inconsistent, and recovery can fail or the recovered database may be in an inconsistent state. | [optional] 
**copy_database_sku** | [**AzureSqlSkuOptions**](AzureSqlSkuOptions.md) |  | [optional] 
**disk_type** | **str, none_type** | Specifies azure managed storage disk to be used for object protection. By default Premium LRS is being used to support Azure SQL workloads. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the ids of the objects to be excluded in the Object Protection. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**objects** | [**[AzureObjectLevelParams]**](AzureObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**sql_package_options** | [**AzureSqlPackageOptions**](AzureSqlPackageOptions.md) |  | [optional] 
**temp_disk_size_gb** | **int, none_type** | Specifies the size of the disk we will attach to rigel to use for exporting this DB(in GB). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


