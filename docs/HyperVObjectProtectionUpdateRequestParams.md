# HyperVObjectProtectionUpdateRequestParams

Specifies the parameters which are specific to HyperV object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent. | [optional] 
**fallback_to_crash_consistent_snapshot** | **bool** | Specifies whether or not to fallback to a crash consistent snapshot in the event that an app consistent snapshot fails. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**backups_copy_only** | **bool** | Specifies whether the backups should be copy-only. | [optional] 
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects to not be protected by this Protection Group. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 

## Example

```python
from cohesity_sdk.models.hyper_v_object_protection_update_request_params import HyperVObjectProtectionUpdateRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVObjectProtectionUpdateRequestParams from a JSON string
hyper_v_object_protection_update_request_params_instance = HyperVObjectProtectionUpdateRequestParams.from_json(json)
# print the JSON string representation of the object
print(HyperVObjectProtectionUpdateRequestParams.to_json())

# convert the object into a dict
hyper_v_object_protection_update_request_params_dict = hyper_v_object_protection_update_request_params_instance.to_dict()
# create an instance of HyperVObjectProtectionUpdateRequestParams from a dict
hyper_v_object_protection_update_request_params_from_dict = HyperVObjectProtectionUpdateRequestParams.from_dict(hyper_v_object_protection_update_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


