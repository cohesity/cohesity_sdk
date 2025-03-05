# ArchivalRun

Specifies information about archival run for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_results** | [**List[ArchivalTargetResult]**](ArchivalTargetResult.md) | Archival result for an archival target. | [optional] 

## Example

```python
from cohesity_sdk.models.archival_run import ArchivalRun

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalRun from a JSON string
archival_run_instance = ArchivalRun.from_json(json)
# print the JSON string representation of the object
print(ArchivalRun.to_json())

# convert the object into a dict
archival_run_dict = archival_run_instance.to_dict()
# create an instance of ArchivalRun from a dict
archival_run_from_dict = ArchivalRun.from_dict(archival_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


