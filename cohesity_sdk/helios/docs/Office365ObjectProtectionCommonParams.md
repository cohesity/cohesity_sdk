# Office365ObjectProtectionCommonParams

Specifies the parameters which are specific to Microsoft 365 Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[Office365ObjectProtectionObjectParams]**](Office365ObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.office365_object_protection_common_params import Office365ObjectProtectionCommonParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ObjectProtectionCommonParams from a JSON string
office365_object_protection_common_params_instance = Office365ObjectProtectionCommonParams.from_json(json)
# print the JSON string representation of the object
print(Office365ObjectProtectionCommonParams.to_json())

# convert the object into a dict
office365_object_protection_common_params_dict = office365_object_protection_common_params_instance.to_dict()
# create an instance of Office365ObjectProtectionCommonParams from a dict
office365_object_protection_common_params_from_dict = Office365ObjectProtectionCommonParams.from_dict(office365_object_protection_common_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


