# IbmFlashSystemProtectionGroupParams

Specifies the parameters which are specific to IBM Flash System related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_safe_guarded_copy_snapshot** | **bool** | Specifies whether the safeguarded copy snapshots are allowed or not | [optional] 
**objects** | [**List[IbmFlashSystemProtectionGroupObjectParams]**](IbmFlashSystemProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.ibm_flash_system_protection_group_params import IbmFlashSystemProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of IbmFlashSystemProtectionGroupParams from a JSON string
ibm_flash_system_protection_group_params_instance = IbmFlashSystemProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(IbmFlashSystemProtectionGroupParams.to_json())

# convert the object into a dict
ibm_flash_system_protection_group_params_dict = ibm_flash_system_protection_group_params_instance.to_dict()
# create an instance of IbmFlashSystemProtectionGroupParams from a dict
ibm_flash_system_protection_group_params_from_dict = IbmFlashSystemProtectionGroupParams.from_dict(ibm_flash_system_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


