# PhysicalSnapshotParams

Specifies parameters of Physical type snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_system_backup** | **bool** | Specifies if system backup was enabled for the source in that particular run. | [optional] 
**protection_type** | **str** | Specifies the protection type of Physical snapshots. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.physical_snapshot_params import PhysicalSnapshotParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalSnapshotParams from a JSON string
physical_snapshot_params_instance = PhysicalSnapshotParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalSnapshotParams.to_json())

# convert the object into a dict
physical_snapshot_params_dict = physical_snapshot_params_instance.to_dict()
# create an instance of PhysicalSnapshotParams from a dict
physical_snapshot_params_from_dict = PhysicalSnapshotParams.from_dict(physical_snapshot_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


