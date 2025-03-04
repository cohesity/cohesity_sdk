# SfdcProtectionGroupObjectParams

Specifies the object identifier to create SFDC Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the SFDC Object. | 
**name** | **str** | Specifies the name of the SFDC Object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.sfdc_protection_group_object_params import SfdcProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcProtectionGroupObjectParams from a JSON string
sfdc_protection_group_object_params_instance = SfdcProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(SfdcProtectionGroupObjectParams.to_json())

# convert the object into a dict
sfdc_protection_group_object_params_dict = sfdc_protection_group_object_params_instance.to_dict()
# create an instance of SfdcProtectionGroupObjectParams from a dict
sfdc_protection_group_object_params_from_dict = SfdcProtectionGroupObjectParams.from_dict(sfdc_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


