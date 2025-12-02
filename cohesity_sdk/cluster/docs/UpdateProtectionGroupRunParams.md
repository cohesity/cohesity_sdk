# UpdateProtectionGroupRunParams

Specifies the params to update a Protection Group Run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_snapshot_config** | [**UpdateArchivalSnapshotConfig**](UpdateArchivalSnapshotConfig.md) |  | [optional] 
**local_snapshot_config** | [**UpdateLocalSnapshotConfig**](UpdateLocalSnapshotConfig.md) |  | [optional] 
**replication_snapshot_config** | [**UpdateReplicationSnapshotConfig**](UpdateReplicationSnapshotConfig.md) |  | [optional] 
**run_id** | **str** | Specifies a unique Protection Group Run id. | 

## Example

```python
from cohesity_sdk.cluster.models.update_protection_group_run_params import UpdateProtectionGroupRunParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProtectionGroupRunParams from a JSON string
update_protection_group_run_params_instance = UpdateProtectionGroupRunParams.from_json(json)
# print the JSON string representation of the object
print(UpdateProtectionGroupRunParams.to_json())

# convert the object into a dict
update_protection_group_run_params_dict = update_protection_group_run_params_instance.to_dict()
# create an instance of UpdateProtectionGroupRunParams from a dict
update_protection_group_run_params_from_dict = UpdateProtectionGroupRunParams.from_dict(update_protection_group_run_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


