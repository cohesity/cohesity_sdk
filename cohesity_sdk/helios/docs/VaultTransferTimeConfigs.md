# VaultTransferTimeConfigs

List of FortKnox vaults transfer time configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_time_configs** | [**List[VaultTransferTimeConfig]**](VaultTransferTimeConfig.md) | List of FortKnox vaults transfer time configurations. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vault_transfer_time_configs import VaultTransferTimeConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of VaultTransferTimeConfigs from a JSON string
vault_transfer_time_configs_instance = VaultTransferTimeConfigs.from_json(json)
# print the JSON string representation of the object
print(VaultTransferTimeConfigs.to_json())

# convert the object into a dict
vault_transfer_time_configs_dict = vault_transfer_time_configs_instance.to_dict()
# create an instance of VaultTransferTimeConfigs from a dict
vault_transfer_time_configs_from_dict = VaultTransferTimeConfigs.from_dict(vault_transfer_time_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


