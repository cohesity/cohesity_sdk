# IbmFlashSystemProtectionGroupObjectParams

Specifies the object parameters to create IBM FlashSystem Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.ibm_flash_system_protection_group_object_params import IbmFlashSystemProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of IbmFlashSystemProtectionGroupObjectParams from a JSON string
ibm_flash_system_protection_group_object_params_instance = IbmFlashSystemProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(IbmFlashSystemProtectionGroupObjectParams.to_json())

# convert the object into a dict
ibm_flash_system_protection_group_object_params_dict = ibm_flash_system_protection_group_object_params_instance.to_dict()
# create an instance of IbmFlashSystemProtectionGroupObjectParams from a dict
ibm_flash_system_protection_group_object_params_from_dict = IbmFlashSystemProtectionGroupObjectParams.from_dict(ibm_flash_system_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


