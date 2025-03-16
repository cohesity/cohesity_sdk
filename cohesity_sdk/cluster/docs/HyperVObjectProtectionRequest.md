# HyperVObjectProtectionRequest

Specifies the HyperV object level settings for object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups_copy_only** | **bool** | Specifies whether the backups should be copy-only. | [optional] 
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects to not be protected by this Protection Group. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 

## Example

```python
from cohesity_sdk.cluster.models.hyper_v_object_protection_request import HyperVObjectProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVObjectProtectionRequest from a JSON string
hyper_v_object_protection_request_instance = HyperVObjectProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(HyperVObjectProtectionRequest.to_json())

# convert the object into a dict
hyper_v_object_protection_request_dict = hyper_v_object_protection_request_instance.to_dict()
# create an instance of HyperVObjectProtectionRequest from a dict
hyper_v_object_protection_request_from_dict = HyperVObjectProtectionRequest.from_dict(hyper_v_object_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


