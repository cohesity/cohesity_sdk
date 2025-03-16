# RecoverPureSanVolumeNewSourceConfig

Specifies the new destination Source configuration where the Pure volume will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_recovered_volume_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**resource_pool** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_pure_san_volume_new_source_config import RecoverPureSanVolumeNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureSanVolumeNewSourceConfig from a JSON string
recover_pure_san_volume_new_source_config_instance = RecoverPureSanVolumeNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverPureSanVolumeNewSourceConfig.to_json())

# convert the object into a dict
recover_pure_san_volume_new_source_config_dict = recover_pure_san_volume_new_source_config_instance.to_dict()
# create an instance of RecoverPureSanVolumeNewSourceConfig from a dict
recover_pure_san_volume_new_source_config_from_dict = RecoverPureSanVolumeNewSourceConfig.from_dict(recover_pure_san_volume_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


