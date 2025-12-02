# AzureDbObjectRecoveryParams

Specifies common parameters for Azure database object recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_database_name** | **str** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 
**original_database_name** | **str** | Specifies the original name of the object to be restored, as it exists in the source. | 
**overwrite** | **bool** | Specifies whether to overwrite an existing object with the same name at the destination. If true, any existing object will be replaced; if false or unset, the restore may fail if a conflict occurs. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_db_object_recovery_params import AzureDbObjectRecoveryParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDbObjectRecoveryParams from a JSON string
azure_db_object_recovery_params_instance = AzureDbObjectRecoveryParams.from_json(json)
# print the JSON string representation of the object
print(AzureDbObjectRecoveryParams.to_json())

# convert the object into a dict
azure_db_object_recovery_params_dict = azure_db_object_recovery_params_instance.to_dict()
# create an instance of AzureDbObjectRecoveryParams from a dict
azure_db_object_recovery_params_from_dict = AzureDbObjectRecoveryParams.from_dict(azure_db_object_recovery_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


