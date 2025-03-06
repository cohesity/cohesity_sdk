# RecoverVmwareVAppOriginalSourceConfig

Specifies the Source configuration if vApps are being recovered to Original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverVmwareVmOriginalSourceNetworkConfig**](RecoverVmwareVmOriginalSourceNetworkConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_v_app_original_source_config import RecoverVmwareVAppOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVAppOriginalSourceConfig from a JSON string
recover_vmware_v_app_original_source_config_instance = RecoverVmwareVAppOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVAppOriginalSourceConfig.to_json())

# convert the object into a dict
recover_vmware_v_app_original_source_config_dict = recover_vmware_v_app_original_source_config_instance.to_dict()
# create an instance of RecoverVmwareVAppOriginalSourceConfig from a dict
recover_vmware_v_app_original_source_config_from_dict = RecoverVmwareVAppOriginalSourceConfig.from_dict(recover_vmware_v_app_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


