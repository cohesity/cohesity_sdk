# SfdcObjectProtectionObjectParams

Specifies the object parameters to create an Sfdc Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the ids of the objects to be excluded in the Object Protection. | [optional] 
**field_exclusion_list** | [**List[SfdcObjectFieldExclusion]**](SfdcObjectFieldExclusion.md) | Specifies the list of field names to be excluded in an Sfdc object. A user can specify multiple such entries in this list. | [optional] 
**id** | **int** | Specifies the id of the Sfdc Org being protected. This cannot be the id of a leaf level object. By default, the Sfdc Org is auto-protected. | 

## Example

```python
from cohesity_sdk.models.sfdc_object_protection_object_params import SfdcObjectProtectionObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcObjectProtectionObjectParams from a JSON string
sfdc_object_protection_object_params_instance = SfdcObjectProtectionObjectParams.from_json(json)
# print the JSON string representation of the object
print(SfdcObjectProtectionObjectParams.to_json())

# convert the object into a dict
sfdc_object_protection_object_params_dict = sfdc_object_protection_object_params_instance.to_dict()
# create an instance of SfdcObjectProtectionObjectParams from a dict
sfdc_object_protection_object_params_from_dict = SfdcObjectProtectionObjectParams.from_dict(sfdc_object_protection_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


