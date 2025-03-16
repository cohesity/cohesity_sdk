# HeliosBmrBackupPolicy

Specifies the BMR schedule in case of physical source protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**HeliosRetention**](HeliosRetention.md) |  | [optional] 
**schedule** | [**HeliosBmrSchedule**](HeliosBmrSchedule.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_bmr_backup_policy import HeliosBmrBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosBmrBackupPolicy from a JSON string
helios_bmr_backup_policy_instance = HeliosBmrBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(HeliosBmrBackupPolicy.to_json())

# convert the object into a dict
helios_bmr_backup_policy_dict = helios_bmr_backup_policy_instance.to_dict()
# create an instance of HeliosBmrBackupPolicy from a dict
helios_bmr_backup_policy_from_dict = HeliosBmrBackupPolicy.from_dict(helios_bmr_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


