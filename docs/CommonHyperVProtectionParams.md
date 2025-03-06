# CommonHyperVProtectionParams

Specifies the common parameters which are specific to HyperV related protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent. | [optional] 
**fallback_to_crash_consistent_snapshot** | **bool** | Specifies whether or not to fallback to a crash consistent snapshot in the event that an app consistent snapshot fails. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_hyper_v_protection_params import CommonHyperVProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonHyperVProtectionParams from a JSON string
common_hyper_v_protection_params_instance = CommonHyperVProtectionParams.from_json(json)
# print the JSON string representation of the object
print(CommonHyperVProtectionParams.to_json())

# convert the object into a dict
common_hyper_v_protection_params_dict = common_hyper_v_protection_params_instance.to_dict()
# create an instance of CommonHyperVProtectionParams from a dict
common_hyper_v_protection_params_from_dict = CommonHyperVProtectionParams.from_dict(common_hyper_v_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


