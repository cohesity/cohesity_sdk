# RecoverAzureEntraIdObjectParams

Specifies the object parameters to recover Azure Entra ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Specifies the type of the entra-id object. | 
**uuid** | **str** | Specifies Uuid of the selected azure entra-id object. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_entra_id_object_params import RecoverAzureEntraIdObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureEntraIdObjectParams from a JSON string
recover_azure_entra_id_object_params_instance = RecoverAzureEntraIdObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureEntraIdObjectParams.to_json())

# convert the object into a dict
recover_azure_entra_id_object_params_dict = recover_azure_entra_id_object_params_instance.to_dict()
# create an instance of RecoverAzureEntraIdObjectParams from a dict
recover_azure_entra_id_object_params_from_dict = RecoverAzureEntraIdObjectParams.from_dict(recover_azure_entra_id_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


