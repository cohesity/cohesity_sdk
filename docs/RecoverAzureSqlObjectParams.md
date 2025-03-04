# RecoverAzureSqlObjectParams

Specifies details of recovery object to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_database_name** | **str** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 
**overwrite_database** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**restored_database_sku** | [**AzureSqlSkuOptions**](AzureSqlSkuOptions.md) |  | [optional] 
**sql_package_options** | [**AzureSqlPackageOptions**](AzureSqlPackageOptions.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_azure_sql_object_params import RecoverAzureSqlObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureSqlObjectParams from a JSON string
recover_azure_sql_object_params_instance = RecoverAzureSqlObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureSqlObjectParams.to_json())

# convert the object into a dict
recover_azure_sql_object_params_dict = recover_azure_sql_object_params_instance.to_dict()
# create an instance of RecoverAzureSqlObjectParams from a dict
recover_azure_sql_object_params_from_dict = RecoverAzureSqlObjectParams.from_dict(recover_azure_sql_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


