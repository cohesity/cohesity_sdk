# RecoverAzureVmOriginalSourceConfig

Specifies the Source configuration if VM's are being recovered to Original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_transfer_info** | [**DataTransferInfo**](DataTransferInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_azure_vm_original_source_config import RecoverAzureVmOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureVmOriginalSourceConfig from a JSON string
recover_azure_vm_original_source_config_instance = RecoverAzureVmOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureVmOriginalSourceConfig.to_json())

# convert the object into a dict
recover_azure_vm_original_source_config_dict = recover_azure_vm_original_source_config_instance.to_dict()
# create an instance of RecoverAzureVmOriginalSourceConfig from a dict
recover_azure_vm_original_source_config_from_dict = RecoverAzureVmOriginalSourceConfig.from_dict(recover_azure_vm_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


