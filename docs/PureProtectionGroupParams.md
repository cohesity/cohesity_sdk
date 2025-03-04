# PureProtectionGroupParams

Specifies the parameters which are specific to Pure related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_snapshots_on_primary** | **int** | Specifies the number of snapshots to retain on the primary environment. If not specified, then snapshots will not be deleted from the primary environment. | [optional] 
**objects** | [**List[PureProtectionGroupObjectParams]**](PureProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.pure_protection_group_params import PureProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of PureProtectionGroupParams from a JSON string
pure_protection_group_params_instance = PureProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(PureProtectionGroupParams.to_json())

# convert the object into a dict
pure_protection_group_params_dict = pure_protection_group_params_instance.to_dict()
# create an instance of PureProtectionGroupParams from a dict
pure_protection_group_params_from_dict = PureProtectionGroupParams.from_dict(pure_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


