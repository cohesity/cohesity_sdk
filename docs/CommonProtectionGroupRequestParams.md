# CommonProtectionGroupRequestParams

Specifies the parameters which are common between all Protection Group requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_in_blackouts** | **bool** | Specifies whether currently executing jobs should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if &#39;pauseInBlackouts&#39; is set to true. | [optional] 
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a protection job. | [optional] 
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**description** | **str** | Specifies a description of the Protection Group. | [optional] 
**end_time_usecs** | **int** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Group. | 
**is_paused** | **bool** | Specifies if the the Protection Group is paused. New runs are not scheduled for the paused Protection Groups. Active run if any is not impacted. | [optional] 
**last_modified_timestamp_usecs** | **int** | Specifies the last time this protection group was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the protection group was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error. | [optional] 
**name** | **str** | Specifies the name of the Protection Group. | 
**pause_in_blackouts** | **bool** | Specifies whether currently executing jobs should be paused if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if &#39;abortInBlackouts&#39; is sent as true. | [optional] 
**policy_id** | **str** | Specifies the unique id of the Protection Policy associated with the Protection Group. The Policy provides retry settings Protection Schedules, Priority, SLA, etc. | 
**priority** | **str** | Specifies the priority of the Protection Group. | [optional] 
**qos_policy** | **str** | Specifies whether the Protection Group will be written to HDD or SSD. | [optional] 
**sla** | [**List[SlaRule]**](SlaRule.md) | Specifies the SLA parameters for this Protection Group. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain (View Box) ID where this Protection Group writes data. | [optional] 

## Example

```python
from cohesity_sdk.models.common_protection_group_request_params import CommonProtectionGroupRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonProtectionGroupRequestParams from a JSON string
common_protection_group_request_params_instance = CommonProtectionGroupRequestParams.from_json(json)
# print the JSON string representation of the object
print(CommonProtectionGroupRequestParams.to_json())

# convert the object into a dict
common_protection_group_request_params_dict = common_protection_group_request_params_instance.to_dict()
# create an instance of CommonProtectionGroupRequestParams from a dict
common_protection_group_request_params_from_dict = CommonProtectionGroupRequestParams.from_dict(common_protection_group_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


