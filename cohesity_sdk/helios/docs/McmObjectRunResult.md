# McmObjectRunResult

Run results for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_snapshot_info** | [**BackupRun**](BackupRun.md) |  | [optional] 
**object** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_run_result import McmObjectRunResult

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectRunResult from a JSON string
mcm_object_run_result_instance = McmObjectRunResult.from_json(json)
# print the JSON string representation of the object
print(McmObjectRunResult.to_json())

# convert the object into a dict
mcm_object_run_result_dict = mcm_object_run_result_instance.to_dict()
# create an instance of McmObjectRunResult from a dict
mcm_object_run_result_from_dict = McmObjectRunResult.from_dict(mcm_object_run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


