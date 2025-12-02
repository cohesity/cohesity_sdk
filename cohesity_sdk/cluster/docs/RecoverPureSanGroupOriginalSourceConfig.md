# RecoverPureSanGroupOriginalSourceConfig

Specifies the network config parameters to be applied for Pure group if recovering to original Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_recovered_group_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**resource_pool** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_pure_san_group_original_source_config import RecoverPureSanGroupOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureSanGroupOriginalSourceConfig from a JSON string
recover_pure_san_group_original_source_config_instance = RecoverPureSanGroupOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverPureSanGroupOriginalSourceConfig.to_json())

# convert the object into a dict
recover_pure_san_group_original_source_config_dict = recover_pure_san_group_original_source_config_instance.to_dict()
# create an instance of RecoverPureSanGroupOriginalSourceConfig from a dict
recover_pure_san_group_original_source_config_from_dict = RecoverPureSanGroupOriginalSourceConfig.from_dict(recover_pure_san_group_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


