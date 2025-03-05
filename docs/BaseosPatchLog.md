# BaseosPatchLog

Baseos patch Log and status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **str** | Baseos patch Log file. | [optional] 
**status** | **str** | Baseos patch application status | [optional] 

## Example

```python
from cohesity_sdk.models.baseos_patch_log import BaseosPatchLog

# TODO update the JSON string below
json = "{}"
# create an instance of BaseosPatchLog from a JSON string
baseos_patch_log_instance = BaseosPatchLog.from_json(json)
# print the JSON string representation of the object
print(BaseosPatchLog.to_json())

# convert the object into a dict
baseos_patch_log_dict = baseos_patch_log_instance.to_dict()
# create an instance of BaseosPatchLog from a dict
baseos_patch_log_from_dict = BaseosPatchLog.from_dict(baseos_patch_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


