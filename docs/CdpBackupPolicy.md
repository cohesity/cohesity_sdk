# CdpBackupPolicy

Specifies CDP (Continious Data Protection) backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**CdpRetention**](CdpRetention.md) |  | 

## Example

```python
from cohesity_sdk.models.cdp_backup_policy import CdpBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CdpBackupPolicy from a JSON string
cdp_backup_policy_instance = CdpBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(CdpBackupPolicy.to_json())

# convert the object into a dict
cdp_backup_policy_dict = cdp_backup_policy_instance.to_dict()
# create an instance of CdpBackupPolicy from a dict
cdp_backup_policy_from_dict = CdpBackupPolicy.from_dict(cdp_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


