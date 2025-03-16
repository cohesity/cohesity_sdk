# TransferTimeConfiguration

Parameters for FortKnox vault transfer time configuration. Backup to the FortKnox vaults happen only during transfer times.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_vault_id** | **str** | Global vault id of a FortKnox vault. | 
**region_id** | **str** | This field is deprecated. Please use globalVaultId field instead. Id of FortKnox region. | [optional] 
**transfer_time_config_params** | [**TransferTimeConfigParams**](TransferTimeConfigParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_configuration import TransferTimeConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeConfiguration from a JSON string
transfer_time_configuration_instance = TransferTimeConfiguration.from_json(json)
# print the JSON string representation of the object
print(TransferTimeConfiguration.to_json())

# convert the object into a dict
transfer_time_configuration_dict = transfer_time_configuration_instance.to_dict()
# create an instance of TransferTimeConfiguration from a dict
transfer_time_configuration_from_dict = TransferTimeConfiguration.from_dict(transfer_time_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


