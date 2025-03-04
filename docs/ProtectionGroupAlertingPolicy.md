# ProtectionGroupAlertingPolicy

Specifies a policy for alerting users of the status of a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_targets** | [**List[AlertTarget]**](AlertTarget.md) | Specifies a list of targets to receive the alerts. | [optional] 
**backup_run_status** | **List[str]** | Specifies the run status for which the user would like to receive alerts. | 
**raise_object_level_failure_alert** | **bool** | Specifies whether object level alerts are raised for backup failures after the backup run. | [optional] 
**raise_object_level_failure_alert_after_each_attempt** | **bool** | Specifies whether object level alerts are raised for backup failures after each backup attempt. | [optional] 
**raise_object_level_failure_alert_after_last_attempt** | **bool** | Specifies whether object level alerts are raised for backup failures after last backup attempt. | [optional] 

## Example

```python
from cohesity_sdk.models.protection_group_alerting_policy import ProtectionGroupAlertingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroupAlertingPolicy from a JSON string
protection_group_alerting_policy_instance = ProtectionGroupAlertingPolicy.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroupAlertingPolicy.to_json())

# convert the object into a dict
protection_group_alerting_policy_dict = protection_group_alerting_policy_instance.to_dict()
# create an instance of ProtectionGroupAlertingPolicy from a dict
protection_group_alerting_policy_from_dict = ProtectionGroupAlertingPolicy.from_dict(protection_group_alerting_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


