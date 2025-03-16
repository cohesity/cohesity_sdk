# Vault

Specifies the fields of vault.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_vault_id** | **str** | Specifies Global vault id. | [optional] 
**region_id** | **str** | Specifies id of region where vault resides. | [optional] 
**region_name** | **str** | Specifies name of region where vault resides. | [optional] 
**vault_name** | **str** | Specifies name of vault. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vault import Vault

# TODO update the JSON string below
json = "{}"
# create an instance of Vault from a JSON string
vault_instance = Vault.from_json(json)
# print the JSON string representation of the object
print(Vault.to_json())

# convert the object into a dict
vault_dict = vault_instance.to_dict()
# create an instance of Vault from a dict
vault_from_dict = Vault.from_dict(vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


