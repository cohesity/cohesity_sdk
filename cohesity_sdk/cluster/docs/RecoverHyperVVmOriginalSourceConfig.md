# RecoverHyperVVmOriginalSourceConfig

Specifies the Source configuration if VM's are being recovered to Original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverHyperVVmOriginalSourceNetworkConfig**](RecoverHyperVVmOriginalSourceNetworkConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_hyper_vvm_original_source_config import RecoverHyperVVmOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHyperVVmOriginalSourceConfig from a JSON string
recover_hyper_vvm_original_source_config_instance = RecoverHyperVVmOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverHyperVVmOriginalSourceConfig.to_json())

# convert the object into a dict
recover_hyper_vvm_original_source_config_dict = recover_hyper_vvm_original_source_config_instance.to_dict()
# create an instance of RecoverHyperVVmOriginalSourceConfig from a dict
recover_hyper_vvm_original_source_config_from_dict = RecoverHyperVVmOriginalSourceConfig.from_dict(recover_hyper_vvm_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


