# ObjectProtectionGroupSummary

Specifies a summary of a protection group protecting this object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the protection group id. | [optional] 
**last_archival_run_status** | **str** | Specifies the status of last archival run. | [optional] 
**last_backup_run_status** | **str** | Specifies the status of last local back up run. | [optional] 
**last_replication_run_status** | **str** | Specifies the status of last replication run. | [optional] 
**last_run_sla_violated** | **bool** | Specifies if the sla is violated in last run. | [optional] 
**name** | **str** | Specifies the protection group name. | [optional] 
**policy_id** | **str** | Specifies the policy id for this group. | [optional] 
**policy_name** | **str** | Specifies the policy name for this group. | [optional] 
**protection_env_type** | **str** | Specifies the protection type of the job if any. | [optional] 
**storage_domain_id** | **str** | Specifies the storage domain id of this group. Format is clusterId:clusterIncarnationId:storageDomainId. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_protection_group_summary import ObjectProtectionGroupSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectProtectionGroupSummary from a JSON string
object_protection_group_summary_instance = ObjectProtectionGroupSummary.from_json(json)
# print the JSON string representation of the object
print(ObjectProtectionGroupSummary.to_json())

# convert the object into a dict
object_protection_group_summary_dict = object_protection_group_summary_instance.to_dict()
# create an instance of ObjectProtectionGroupSummary from a dict
object_protection_group_summary_from_dict = ObjectProtectionGroupSummary.from_dict(object_protection_group_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


