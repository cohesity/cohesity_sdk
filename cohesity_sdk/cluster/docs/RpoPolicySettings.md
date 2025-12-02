# RpoPolicySettings

Specifies all the additional settings that are applicable only to an RPO policy. This can include storage domain, settings of different environments, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerting_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**backup_qos_principal** | **str** | Specifies whether the data will be written to HDD or SSD. | [optional] 
**env_backup_params** | [**EnvironmentTypeJobParams**](EnvironmentTypeJobParams.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain to which data will be written | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.rpo_policy_settings import RpoPolicySettings

# TODO update the JSON string below
json = "{}"
# create an instance of RpoPolicySettings from a JSON string
rpo_policy_settings_instance = RpoPolicySettings.from_json(json)
# print the JSON string representation of the object
print(RpoPolicySettings.to_json())

# convert the object into a dict
rpo_policy_settings_dict = rpo_policy_settings_instance.to_dict()
# create an instance of RpoPolicySettings from a dict
rpo_policy_settings_from_dict = RpoPolicySettings.from_dict(rpo_policy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


