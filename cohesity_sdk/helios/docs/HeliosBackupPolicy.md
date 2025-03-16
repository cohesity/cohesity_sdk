# HeliosBackupPolicy

Specifies the backup schedule and retentions of a Protection Policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bmr** | [**HeliosBmrBackupPolicy**](HeliosBmrBackupPolicy.md) |  | [optional] 
**cdp** | [**HeliosCdpBackupPolicy**](HeliosCdpBackupPolicy.md) |  | [optional] 
**log** | [**HeliosLogBackupPolicy**](HeliosLogBackupPolicy.md) |  | [optional] 
**regular** | [**HeliosRegularBackupPolicy**](HeliosRegularBackupPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_backup_policy import HeliosBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosBackupPolicy from a JSON string
helios_backup_policy_instance = HeliosBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosBackupPolicy.to_json())

# convert the object into a dict
helios_backup_policy_dict = helios_backup_policy_instance.to_dict()
# create an instance of HeliosBackupPolicy from a dict
helios_backup_policy_from_dict = HeliosBackupPolicy.from_dict(helios_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


