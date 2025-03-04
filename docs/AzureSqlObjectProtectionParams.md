# AzureSqlObjectProtectionParams

Specifies the parameters which are specific to Azure SQL Object Protection Groups using Azure native APIs. Atlease one of objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_database** | **bool** | If set to true, a copy of the database is created during backup, and the backup is performed from the copied database. This backup will be transactionally consistent. If set to false, the backup is performed from the production database while transactions are in progress. In this case, the backup will be transactionally inconsistent, and recovery can fail or the recovered database may be in an inconsistent state. | [optional] 
**copy_database_sku** | [**AzureSqlSkuOptions**](AzureSqlSkuOptions.md) |  | [optional] 
**disk_type** | **str** | Specifies azure managed storage disk to be used for object protection. By default Premium LRS is being used to support Azure SQL workloads. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the ids of the objects to be excluded in the Object Protection. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**objects** | [**List[AzureObjectLevelParams]**](AzureObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 
**sql_package_options** | [**AzureSqlPackageOptions**](AzureSqlPackageOptions.md) |  | [optional] 
**temp_disk_size_gb** | **int** | Specifies the size of the disk we will attach to rigel to use for exporting this DB(in GB). | [optional] 

## Example

```python
from cohesity_sdk.models.azure_sql_object_protection_params import AzureSqlObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlObjectProtectionParams from a JSON string
azure_sql_object_protection_params_instance = AzureSqlObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AzureSqlObjectProtectionParams.to_json())

# convert the object into a dict
azure_sql_object_protection_params_dict = azure_sql_object_protection_params_instance.to_dict()
# create an instance of AzureSqlObjectProtectionParams from a dict
azure_sql_object_protection_params_from_dict = AzureSqlObjectProtectionParams.from_dict(azure_sql_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


