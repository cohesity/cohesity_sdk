# RecoverAzureSQLMIParams

Specifies the parameters to recover Azure SQL Managed Instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureSQLMI**](AzureTargetParamsForRecoverAzureSQLMI.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureSQLMISnapshotParams]**](RecoverAzureSQLMISnapshotParams.md) | Specifies the details of the azure SQL Managed Instance objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_sqlmi_params import RecoverAzureSQLMIParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureSQLMIParams from a JSON string
recover_azure_sqlmi_params_instance = RecoverAzureSQLMIParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureSQLMIParams.to_json())

# convert the object into a dict
recover_azure_sqlmi_params_dict = recover_azure_sqlmi_params_instance.to_dict()
# create an instance of RecoverAzureSQLMIParams from a dict
recover_azure_sqlmi_params_from_dict = RecoverAzureSQLMIParams.from_dict(recover_azure_sqlmi_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


