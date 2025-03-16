# HyperVObjectProtectionResponse

Specifies the input for a protection object in the HyperV environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups_copy_only** | **bool** | Specifies whether the backups should be copy-only. | [optional] 
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects to not be protected by this Protection Group. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.hyper_v_object_protection_response import HyperVObjectProtectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVObjectProtectionResponse from a JSON string
hyper_v_object_protection_response_instance = HyperVObjectProtectionResponse.from_json(json)
# print the JSON string representation of the object
print(HyperVObjectProtectionResponse.to_json())

# convert the object into a dict
hyper_v_object_protection_response_dict = hyper_v_object_protection_response_instance.to_dict()
# create an instance of HyperVObjectProtectionResponse from a dict
hyper_v_object_protection_response_from_dict = HyperVObjectProtectionResponse.from_dict(hyper_v_object_protection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


