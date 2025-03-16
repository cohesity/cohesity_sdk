# HeliosExtendedRetentionPolicy

Specifies additional retention policies to apply to backup snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Specifies the unique identifier for the extedned  retention getting added. This field should only be set if policy is getting updated. | [optional] 
**retention** | [**HeliosRetention**](HeliosRetention.md) |  | [optional] 
**run_type** | **str** | The backup run type to which this extended retention applies to. If this is not set, the extended retention will be applicable to all non-log backup types. Currently, the only value that can be set here is Full. &#39;Regular&#39; indicates a incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a Regular schedule captures all the blocks. &#39;Full&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;Log&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;System&#39; indicates a system backup. System backups are used to do bare metal recovery of the system to a specific point in time. | [optional] 
**schedule** | [**HeliosExtendedRetentionSchedule**](HeliosExtendedRetentionSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_extended_retention_policy import HeliosExtendedRetentionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosExtendedRetentionPolicy from a JSON string
helios_extended_retention_policy_instance = HeliosExtendedRetentionPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosExtendedRetentionPolicy.to_json())

# convert the object into a dict
helios_extended_retention_policy_dict = helios_extended_retention_policy_instance.to_dict()
# create an instance of HeliosExtendedRetentionPolicy from a dict
helios_extended_retention_policy_from_dict = HeliosExtendedRetentionPolicy.from_dict(helios_extended_retention_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


