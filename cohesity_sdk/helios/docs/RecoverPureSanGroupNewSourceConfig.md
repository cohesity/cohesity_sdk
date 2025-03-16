# RecoverPureSanGroupNewSourceConfig

Specifies the new destination Source configuration where the Pure group will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_recovered_group_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) | Specifies params to rename the recovered SAN group. If not specified, the original names of the group are preserved. | [optional] 
**resource_pool** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the resource pool to recover the Pure SAN Volume to. This field must be specified if recoverToNewSource is true. | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the id of the new target parent source to recover the Pure SAN group to. This field must be specified if recoverToNewSource is true. | 

## Example

```python
from cohesity_sdk.helios.models.recover_pure_san_group_new_source_config import RecoverPureSanGroupNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureSanGroupNewSourceConfig from a JSON string
recover_pure_san_group_new_source_config_instance = RecoverPureSanGroupNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverPureSanGroupNewSourceConfig.to_json())

# convert the object into a dict
recover_pure_san_group_new_source_config_dict = recover_pure_san_group_new_source_config_instance.to_dict()
# create an instance of RecoverPureSanGroupNewSourceConfig from a dict
recover_pure_san_group_new_source_config_from_dict = RecoverPureSanGroupNewSourceConfig.from_dict(recover_pure_san_group_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


