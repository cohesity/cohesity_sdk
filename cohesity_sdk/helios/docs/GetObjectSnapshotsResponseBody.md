# GetObjectSnapshotsResponseBody

Specifies the list of object snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**List[ObjectSnapshot]**](ObjectSnapshot.md) | Specifies the list of snapshots. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_object_snapshots_response_body import GetObjectSnapshotsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectSnapshotsResponseBody from a JSON string
get_object_snapshots_response_body_instance = GetObjectSnapshotsResponseBody.from_json(json)
# print the JSON string representation of the object
print(GetObjectSnapshotsResponseBody.to_json())

# convert the object into a dict
get_object_snapshots_response_body_dict = get_object_snapshots_response_body_instance.to_dict()
# create an instance of GetObjectSnapshotsResponseBody from a dict
get_object_snapshots_response_body_from_dict = GetObjectSnapshotsResponseBody.from_dict(get_object_snapshots_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


