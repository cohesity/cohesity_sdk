# ProtectionSummary

Specifies a summary of an object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_archival_run_status** | **str** | Specifies the status of last archival run. | [optional] 
**last_backup_run_status** | **str** | Specifies the status of last local back up run. | [optional] 
**last_replication_run_status** | **str** | Specifies the status of last replication run. | [optional] 
**last_run_sla_violated** | **bool** | Specifies if the sla is violated in last run. | [optional] 
**policy_id** | **str** | Specifies the policy id for this protection. | [optional] 
**policy_name** | **str** | Specifies the policy name for this group. | [optional] 
**storage_domain_id** | **str** | Specifies the storage domain id of this protection. Format is clusterId:clusterIncarnationId:storageDomainId. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_summary import ProtectionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionSummary from a JSON string
protection_summary_instance = ProtectionSummary.from_json(json)
# print the JSON string representation of the object
print(ProtectionSummary.to_json())

# convert the object into a dict
protection_summary_dict = protection_summary_instance.to_dict()
# create an instance of ProtectionSummary from a dict
protection_summary_from_dict = ProtectionSummary.from_dict(protection_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


