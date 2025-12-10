# AzureEntraIDObjectProtectionParams

Specifies the parameters which are specific to Azure Entra ID Object Protection Groups using Azure native APIs. Atlease one of objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_object_types** | **List[str]** | Specifies the list of object types to be excluded from protection. | [optional] 
**objects** | [**List[AzureObjectLevelParams]**](AzureObjectLevelParams.md) | Specifies the objects to be protected. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_entra_id_object_protection_params import AzureEntraIDObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureEntraIDObjectProtectionParams from a JSON string
azure_entra_id_object_protection_params_instance = AzureEntraIDObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(AzureEntraIDObjectProtectionParams.to_json())

# convert the object into a dict
azure_entra_id_object_protection_params_dict = azure_entra_id_object_protection_params_instance.to_dict()
# create an instance of AzureEntraIDObjectProtectionParams from a dict
azure_entra_id_object_protection_params_from_dict = AzureEntraIDObjectProtectionParams.from_dict(azure_entra_id_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


