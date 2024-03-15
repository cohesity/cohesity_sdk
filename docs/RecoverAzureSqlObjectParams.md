# RecoverAzureSqlObjectParams

Specifies details of recovery object to be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_database_name** | **str, none_type** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 
**overwrite_database** | **bool, none_type** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**restored_database_sku** | [**AzureSqlSkuOptions**](AzureSqlSkuOptions.md) |  | [optional] 
**sql_package_options** | [**AzureSqlPackageOptions**](AzureSqlPackageOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


