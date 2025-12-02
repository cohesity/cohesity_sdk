# CommonBackupParams

Specifies the common parameters for backup. These parameters are common across protection group and object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_in_blackouts** | **bool** | Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**end_time_usecs** | **int** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**policy_config** | [**PolicyConfig**](PolicyConfig.md) |  | [optional] 
**policy_id** | **str** | Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup. | [optional] 
**priority** | **str** | Specifies the priority for the objects backup. | [optional] 
**qos_policy** | **str** | Specifies whether object backup will be written to HDD or SSD. | [optional] 
**skip_rigel_for_backup** | **bool** | Specifies whether to skip Rigel for backup or not. | [optional] 
**sla** | [**List[SlaRule]**](SlaRule.md) | Specifies the SLA parameters for list of objects. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_backup_params import CommonBackupParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonBackupParams from a JSON string
common_backup_params_instance = CommonBackupParams.from_json(json)
# print the JSON string representation of the object
print(CommonBackupParams.to_json())

# convert the object into a dict
common_backup_params_dict = common_backup_params_instance.to_dict()
# create an instance of CommonBackupParams from a dict
common_backup_params_from_dict = CommonBackupParams.from_dict(common_backup_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


