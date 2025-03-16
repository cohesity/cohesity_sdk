# FortknoxAzureVaultRespParams

Fortknox Azure vault related params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_class** | **str** | Specifies the Azure storage class. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_azure_vault_resp_params import FortknoxAzureVaultRespParams

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxAzureVaultRespParams from a JSON string
fortknox_azure_vault_resp_params_instance = FortknoxAzureVaultRespParams.from_json(json)
# print the JSON string representation of the object
print(FortknoxAzureVaultRespParams.to_json())

# convert the object into a dict
fortknox_azure_vault_resp_params_dict = fortknox_azure_vault_resp_params_instance.to_dict()
# create an instance of FortknoxAzureVaultRespParams from a dict
fortknox_azure_vault_resp_params_from_dict = FortknoxAzureVaultRespParams.from_dict(fortknox_azure_vault_resp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


