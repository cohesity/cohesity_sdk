# RecoverPureGroupTargetParams

Specifies the target object parameters to recover the Pure San group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverPureSanGroupNewSourceConfig**](RecoverPureSanGroupNewSourceConfig.md) | Specifies the new destination Source configuration parameters where the Pure group will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | [**RecoverPureSanGroupOriginalSourceConfig**](RecoverPureSanGroupOriginalSourceConfig.md) | Specifies the Source configuration if Pure group is being recovered to Original Source. If not specified, all the configuration parameters will be retained. | [optional] 
**recover_to_new_source** | **bool** | Specifies whether to recover to a new source. | 
**use_thin_clone** | **bool** | Specifies whether to use thin clone to restore storage array snapshots. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_pure_group_target_params import RecoverPureGroupTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureGroupTargetParams from a JSON string
recover_pure_group_target_params_instance = RecoverPureGroupTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPureGroupTargetParams.to_json())

# convert the object into a dict
recover_pure_group_target_params_dict = recover_pure_group_target_params_instance.to_dict()
# create an instance of RecoverPureGroupTargetParams from a dict
recover_pure_group_target_params_from_dict = RecoverPureGroupTargetParams.from_dict(recover_pure_group_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


