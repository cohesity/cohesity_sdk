# NimbleProtectionGroupParams

Specifies the parameters which are specific to Nimble related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[NimbleProtectionGroupObjectParams]**](NimbleProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.nimble_protection_group_params import NimbleProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of NimbleProtectionGroupParams from a JSON string
nimble_protection_group_params_instance = NimbleProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(NimbleProtectionGroupParams.to_json())

# convert the object into a dict
nimble_protection_group_params_dict = nimble_protection_group_params_instance.to_dict()
# create an instance of NimbleProtectionGroupParams from a dict
nimble_protection_group_params_from_dict = NimbleProtectionGroupParams.from_dict(nimble_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


