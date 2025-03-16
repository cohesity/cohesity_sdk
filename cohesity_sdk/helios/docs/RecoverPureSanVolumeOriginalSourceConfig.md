# RecoverPureSanVolumeOriginalSourceConfig

Specifies the network config parameters to be applied for Pure volumes if recovering to original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_recovered_volume_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) | Specifies params to rename the recovered SAN volumes. If not specified, the original names of the volumes are preserved. | [optional] 
**resource_pool** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the resource pool to recover the SAN Volume to. This field can be specified for cases where the resource pool can be altered on the original source. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_pure_san_volume_original_source_config import RecoverPureSanVolumeOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureSanVolumeOriginalSourceConfig from a JSON string
recover_pure_san_volume_original_source_config_instance = RecoverPureSanVolumeOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverPureSanVolumeOriginalSourceConfig.to_json())

# convert the object into a dict
recover_pure_san_volume_original_source_config_dict = recover_pure_san_volume_original_source_config_instance.to_dict()
# create an instance of RecoverPureSanVolumeOriginalSourceConfig from a dict
recover_pure_san_volume_original_source_config_from_dict = RecoverPureSanVolumeOriginalSourceConfig.from_dict(recover_pure_san_volume_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


