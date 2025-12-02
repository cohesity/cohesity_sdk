# RecoverAzureEntraIdParams

Specifies the parameters to recover Azure Entra ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_target_params** | [**AzureTargetParamsForRecoverAzureEntraId**](AzureTargetParamsForRecoverAzureEntraId.md) |  | [optional] 
**object_attributes** | [**List[RecoverAzureEntraIdObjectParams]**](RecoverAzureEntraIdObjectParams.md) | Specifies the details of the azure entra id objects attributes to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_entra_id_params import RecoverAzureEntraIdParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureEntraIdParams from a JSON string
recover_azure_entra_id_params_instance = RecoverAzureEntraIdParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureEntraIdParams.to_json())

# convert the object into a dict
recover_azure_entra_id_params_dict = recover_azure_entra_id_params_instance.to_dict()
# create an instance of RecoverAzureEntraIdParams from a dict
recover_azure_entra_id_params_from_dict = RecoverAzureEntraIdParams.from_dict(recover_azure_entra_id_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


