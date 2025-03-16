# FortknoxVaultAzureResp

Information about each Fortknox vault that is being added.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **str** | ID that identifies a region. | [optional] 
**vault_params** | [**FortknoxAzureVaultRespParams**](FortknoxAzureVaultRespParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_vault_azure_resp import FortknoxVaultAzureResp

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxVaultAzureResp from a JSON string
fortknox_vault_azure_resp_instance = FortknoxVaultAzureResp.from_json(json)
# print the JSON string representation of the object
print(FortknoxVaultAzureResp.to_json())

# convert the object into a dict
fortknox_vault_azure_resp_dict = fortknox_vault_azure_resp_instance.to_dict()
# create an instance of FortknoxVaultAzureResp from a dict
fortknox_vault_azure_resp_from_dict = FortknoxVaultAzureResp.from_dict(fortknox_vault_azure_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


