# AddFortknoxVaultAzureParams

Fortknox Azure vault related params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **str** | ID that identifies a region. | 
**vault_params** | [**FortknoxAzureVaultReqParams**](FortknoxAzureVaultReqParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_fortknox_vault_azure_params import AddFortknoxVaultAzureParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddFortknoxVaultAzureParams from a JSON string
add_fortknox_vault_azure_params_instance = AddFortknoxVaultAzureParams.from_json(json)
# print the JSON string representation of the object
print(AddFortknoxVaultAzureParams.to_json())

# convert the object into a dict
add_fortknox_vault_azure_params_dict = add_fortknox_vault_azure_params_instance.to_dict()
# create an instance of AddFortknoxVaultAzureParams from a dict
add_fortknox_vault_azure_params_from_dict = AddFortknoxVaultAzureParams.from_dict(add_fortknox_vault_azure_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


