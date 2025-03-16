# SnapshotDiffResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_operations** | [**List[FileOperation]**](FileOperation.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from cohesity_sdk.helios.models.snapshot_diff_result import SnapshotDiffResult

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDiffResult from a JSON string
snapshot_diff_result_instance = SnapshotDiffResult.from_json(json)
# print the JSON string representation of the object
print(SnapshotDiffResult.to_json())

# convert the object into a dict
snapshot_diff_result_dict = snapshot_diff_result_instance.to_dict()
# create an instance of SnapshotDiffResult from a dict
snapshot_diff_result_from_dict = SnapshotDiffResult.from_dict(snapshot_diff_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


