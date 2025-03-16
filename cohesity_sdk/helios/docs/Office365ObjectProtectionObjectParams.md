# Office365ObjectProtectionObjectParams

Specifies the object parameters to create a Microsoft 365 Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the ID of the objects to be excluded in the Object Protection. | [optional] 
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**should_auto_protect_object** | **bool** | Specifies if the object has to be autoprotected. This is applicable only for sharepoint sites. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.office365_object_protection_object_params import Office365ObjectProtectionObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ObjectProtectionObjectParams from a JSON string
office365_object_protection_object_params_instance = Office365ObjectProtectionObjectParams.from_json(json)
# print the JSON string representation of the object
print(Office365ObjectProtectionObjectParams.to_json())

# convert the object into a dict
office365_object_protection_object_params_dict = office365_object_protection_object_params_instance.to_dict()
# create an instance of Office365ObjectProtectionObjectParams from a dict
office365_object_protection_object_params_from_dict = Office365ObjectProtectionObjectParams.from_dict(office365_object_protection_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


