# VaultTransferTimeConfig

Parameters for FortKnox vault transfer time configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_vault_id** | **str** | Global vault id of a FortKnox vault. | 
**transfer_time_config_params** | [**TransferTimeConfigParamsList**](TransferTimeConfigParamsList.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vault_transfer_time_config import VaultTransferTimeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VaultTransferTimeConfig from a JSON string
vault_transfer_time_config_instance = VaultTransferTimeConfig.from_json(json)
# print the JSON string representation of the object
print(VaultTransferTimeConfig.to_json())

# convert the object into a dict
vault_transfer_time_config_dict = vault_transfer_time_config_instance.to_dict()
# create an instance of VaultTransferTimeConfig from a dict
vault_transfer_time_config_from_dict = VaultTransferTimeConfig.from_dict(vault_transfer_time_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


