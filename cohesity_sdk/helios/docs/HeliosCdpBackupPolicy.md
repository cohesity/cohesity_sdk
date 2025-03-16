# HeliosCdpBackupPolicy

Specifies CDP (Continious Data Protection) backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**HeliosCdpRetention**](HeliosCdpRetention.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_cdp_backup_policy import HeliosCdpBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosCdpBackupPolicy from a JSON string
helios_cdp_backup_policy_instance = HeliosCdpBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosCdpBackupPolicy.to_json())

# convert the object into a dict
helios_cdp_backup_policy_dict = helios_cdp_backup_policy_instance.to_dict()
# create an instance of HeliosCdpBackupPolicy from a dict
helios_cdp_backup_policy_from_dict = HeliosCdpBackupPolicy.from_dict(helios_cdp_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


