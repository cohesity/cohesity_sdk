# CommonProtectionGroupResponseParams

Specifies the parameters which are common between all Protection Group responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_in_blackouts** | **bool** | Specifies whether currently executing jobs should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a protection job. | [optional] 
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**cluster_id** | **str** | Specifies the cluster ID. | [optional] 
**description** | **str** | Specifies a description of the Protection Group. | [optional] 
**end_time_usecs** | **int** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**environment** | **str** | Specifies the environment of the Protection Group. | [optional] 
**id** | **str** | Specifies the ID of the Protection Group. | [optional] 
**invalid_entities** | [**List[MissingEntityParams]**](MissingEntityParams.md) | Specifies the Information about invalid entities. An entity will be considered invalid if it is part of an active protection group but has lost compatibility for the given backup type. | [optional] 
**is_active** | **bool** | Specifies if the Protection Group is active or not. | [optional] 
**is_deleted** | **bool** | Specifies if the Protection Group has been deleted. | [optional] 
**is_paused** | **bool** | Specifies if the the Protection Group is paused. New runs are not scheduled for the paused Protection Groups. Active run if any is not impacted. | [optional] 
**is_protect_once** | **bool** | Specifies if the the Protection Group is using a protect once type of policy. This field is helpful to identify run happen for this group. | [optional] 
**last_modified_timestamp_usecs** | **int** | Specifies the last time this protection group was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the protection group was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error. | [optional] 
**last_run** | [**ProtectionGroupRun**](ProtectionGroupRun.md) |  | [optional] 
**missing_entities** | [**List[MissingEntityParams]**](MissingEntityParams.md) | Specifies the Information about missing entities. | [optional] 
**name** | **str** | Specifies the name of the Protection Group. | [optional] 
**num_protected_objects** | **int** | Specifies the number of protected objects of the Protection Group. | [optional] 
**pause_in_blackouts** | **bool** | Specifies whether currently executing jobs should be paused if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if &#39;abortInBlackouts&#39; is sent as true. | [optional] 
**permissions** | [**List[Tenant]**](Tenant.md) | Specifies the list of tenants that have permissions for this protection group. | [optional] 
**policy_id** | **str** | Specifies the unique id of the Protection Policy associated with the Protection Group. The Policy provides retry settings Protection Schedules, Priority, SLA, etc. | [optional] 
**priority** | **str** | Specifies the priority of the Protection Group. | [optional] 
**qos_policy** | **str** | Specifies whether the Protection Group will be written to HDD or SSD. | [optional] 
**region_id** | **str** | Specifies the region ID. | [optional] 
**sla** | [**List[SlaRule]**](SlaRule.md) | Specifies the SLA parameters for this Protection Group. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain (View Box) ID where this Protection Group writes data. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_protection_group_response_params import CommonProtectionGroupResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonProtectionGroupResponseParams from a JSON string
common_protection_group_response_params_instance = CommonProtectionGroupResponseParams.from_json(json)
# print the JSON string representation of the object
print(CommonProtectionGroupResponseParams.to_json())

# convert the object into a dict
common_protection_group_response_params_dict = common_protection_group_response_params_instance.to_dict()
# create an instance of CommonProtectionGroupResponseParams from a dict
common_protection_group_response_params_from_dict = CommonProtectionGroupResponseParams.from_dict(common_protection_group_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


