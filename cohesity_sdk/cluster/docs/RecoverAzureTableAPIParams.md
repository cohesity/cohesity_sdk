# RecoverAzureTableAPIParams

Specifies the parameters to recover Azure Table API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureTableAPI**](AzureTargetParamsForRecoverAzureTableAPI.md) |  | [optional] 
**snapshots** | [**List[RecoverAzureTableAPISnapshotParams]**](RecoverAzureTableAPISnapshotParams.md) | Specifies the details of the azure table api objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_table_api_params import RecoverAzureTableAPIParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureTableAPIParams from a JSON string
recover_azure_table_api_params_instance = RecoverAzureTableAPIParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureTableAPIParams.to_json())

# convert the object into a dict
recover_azure_table_api_params_dict = recover_azure_table_api_params_instance.to_dict()
# create an instance of RecoverAzureTableAPIParams from a dict
recover_azure_table_api_params_from_dict = RecoverAzureTableAPIParams.from_dict(recover_azure_table_api_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


