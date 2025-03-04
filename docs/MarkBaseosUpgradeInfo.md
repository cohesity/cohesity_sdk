# MarkBaseosUpgradeInfo

Specifies info about BaseOS upgrade operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies optional message related to operation status. | [optional] 
**set_operation** | **bool** | Specifies whether the operation is set or not. | 

## Example

```python
from cohesity_sdk.models.mark_baseos_upgrade_info import MarkBaseosUpgradeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarkBaseosUpgradeInfo from a JSON string
mark_baseos_upgrade_info_instance = MarkBaseosUpgradeInfo.from_json(json)
# print the JSON string representation of the object
print(MarkBaseosUpgradeInfo.to_json())

# convert the object into a dict
mark_baseos_upgrade_info_dict = mark_baseos_upgrade_info_instance.to_dict()
# create an instance of MarkBaseosUpgradeInfo from a dict
mark_baseos_upgrade_info_from_dict = MarkBaseosUpgradeInfo.from_dict(mark_baseos_upgrade_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


