# HyperVObjectProtectionRequestParams

Specifies the parameters which are specific to HyperV object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent. | [optional] 
**fallback_to_crash_consistent_snapshot** | **bool** | Specifies whether or not to fallback to a crash consistent snapshot in the event that an app consistent snapshot fails. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[HyperVObjectProtectionRequest]**](HyperVObjectProtectionRequest.md) | Specifies the objects to include in the backup. | 

## Example

```python
from cohesity_sdk.cluster.models.hyper_v_object_protection_request_params import HyperVObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVObjectProtectionRequestParams from a JSON string
hyper_v_object_protection_request_params_instance = HyperVObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(HyperVObjectProtectionRequestParams.to_json())

# convert the object into a dict
hyper_v_object_protection_request_params_dict = hyper_v_object_protection_request_params_instance.to_dict()
# create an instance of HyperVObjectProtectionRequestParams from a dict
hyper_v_object_protection_request_params_from_dict = HyperVObjectProtectionRequestParams.from_dict(hyper_v_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


