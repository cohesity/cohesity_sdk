# AcropolisProtectionGroupObjectParams

Specifies an object protected by a Acropolis Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**List[AcropolisDiskInfo]**](AcropolisDiskInfo.md) | Specifies a list of disks to exclude from being protected. This is only applicable to VM objects. | [optional] 
**id** | **int** | Specifies the ID of the object. | 
**include_disks** | [**List[AcropolisDiskInfo]**](AcropolisDiskInfo.md) | Specifies a list of disks to include in the protection. This is only applicable to VM objects. | [optional] 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.acropolis_protection_group_object_params import AcropolisProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AcropolisProtectionGroupObjectParams from a JSON string
acropolis_protection_group_object_params_instance = AcropolisProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AcropolisProtectionGroupObjectParams.to_json())

# convert the object into a dict
acropolis_protection_group_object_params_dict = acropolis_protection_group_object_params_instance.to_dict()
# create an instance of AcropolisProtectionGroupObjectParams from a dict
acropolis_protection_group_object_params_from_dict = AcropolisProtectionGroupObjectParams.from_dict(acropolis_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


