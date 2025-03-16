# SnapshotRetentionPolicy

Describes the snapshot retention policy struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_of_days_to_keep** | **int** | Number of days to keep the snapshot. | [optional] 
**num_of_versions_to_keep** | **int** | Number of snapshot versions to keep. | [optional] 
**suspended** | **bool** | Bool to denote if the policy is suspended. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.snapshot_retention_policy import SnapshotRetentionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRetentionPolicy from a JSON string
snapshot_retention_policy_instance = SnapshotRetentionPolicy.from_json(json)
# print the JSON string representation of the object
print(SnapshotRetentionPolicy.to_json())

# convert the object into a dict
snapshot_retention_policy_dict = snapshot_retention_policy_instance.to_dict()
# create an instance of SnapshotRetentionPolicy from a dict
snapshot_retention_policy_from_dict = SnapshotRetentionPolicy.from_dict(snapshot_retention_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


