# UdaSnapshotMetadata

Specifies UDA snapshot metadata corresponding to a UDA source snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_encrypted** | **bool** | Shows if the backup for this snapshot is encrypted. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.uda_snapshot_metadata import UdaSnapshotMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UdaSnapshotMetadata from a JSON string
uda_snapshot_metadata_instance = UdaSnapshotMetadata.from_json(json)
# print the JSON string representation of the object
print(UdaSnapshotMetadata.to_json())

# convert the object into a dict
uda_snapshot_metadata_dict = uda_snapshot_metadata_instance.to_dict()
# create an instance of UdaSnapshotMetadata from a dict
uda_snapshot_metadata_from_dict = UdaSnapshotMetadata.from_dict(uda_snapshot_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


