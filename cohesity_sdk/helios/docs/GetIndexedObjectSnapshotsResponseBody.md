# GetIndexedObjectSnapshotsResponseBody

Specifies the snapshots of an indexed object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**List[IndexedObjectSnapshot]**](IndexedObjectSnapshot.md) | Specifies a list of snapshots containing the indexed object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_indexed_object_snapshots_response_body import GetIndexedObjectSnapshotsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndexedObjectSnapshotsResponseBody from a JSON string
get_indexed_object_snapshots_response_body_instance = GetIndexedObjectSnapshotsResponseBody.from_json(json)
# print the JSON string representation of the object
print(GetIndexedObjectSnapshotsResponseBody.to_json())

# convert the object into a dict
get_indexed_object_snapshots_response_body_dict = get_indexed_object_snapshots_response_body_instance.to_dict()
# create an instance of GetIndexedObjectSnapshotsResponseBody from a dict
get_indexed_object_snapshots_response_body_from_dict = GetIndexedObjectSnapshotsResponseBody.from_dict(get_indexed_object_snapshots_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


