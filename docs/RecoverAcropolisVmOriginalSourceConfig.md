# RecoverAcropolisVmOriginalSourceConfig

Specifies the Source configuration if VM's are being recovered to Original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverAcropolisVmOriginalSourceNetworkConfig**](RecoverAcropolisVmOriginalSourceNetworkConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_acropolis_vm_original_source_config import RecoverAcropolisVmOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAcropolisVmOriginalSourceConfig from a JSON string
recover_acropolis_vm_original_source_config_instance = RecoverAcropolisVmOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAcropolisVmOriginalSourceConfig.to_json())

# convert the object into a dict
recover_acropolis_vm_original_source_config_dict = recover_acropolis_vm_original_source_config_instance.to_dict()
# create an instance of RecoverAcropolisVmOriginalSourceConfig from a dict
recover_acropolis_vm_original_source_config_from_dict = RecoverAcropolisVmOriginalSourceConfig.from_dict(recover_acropolis_vm_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


