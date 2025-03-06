# RecoveredOrClonedVmsRenameConfig

Specifies the prefix and suffix to be added to VMs that are recovered or cloned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Specifies the prefix string to be added to recovered or cloned object names. | [optional] 
**suffix** | **str** | Specifies the suffix string to be added to recovered or cloned object names. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recovered_or_cloned_vms_rename_config import RecoveredOrClonedVmsRenameConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveredOrClonedVmsRenameConfig from a JSON string
recovered_or_cloned_vms_rename_config_instance = RecoveredOrClonedVmsRenameConfig.from_json(json)
# print the JSON string representation of the object
print(RecoveredOrClonedVmsRenameConfig.to_json())

# convert the object into a dict
recovered_or_cloned_vms_rename_config_dict = recovered_or_cloned_vms_rename_config_instance.to_dict()
# create an instance of RecoveredOrClonedVmsRenameConfig from a dict
recovered_or_cloned_vms_rename_config_from_dict = RecoveredOrClonedVmsRenameConfig.from_dict(recovered_or_cloned_vms_rename_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


