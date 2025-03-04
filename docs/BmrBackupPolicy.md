# BmrBackupPolicy

Specifies the BMR schedule in case of physical source protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**Retention**](Retention.md) |  | 
**schedule** | [**BmrSchedule**](BmrSchedule.md) |  | 

## Example

```python
from cohesity_sdk.models.bmr_backup_policy import BmrBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of BmrBackupPolicy from a JSON string
bmr_backup_policy_instance = BmrBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(BmrBackupPolicy.to_json())

# convert the object into a dict
bmr_backup_policy_dict = bmr_backup_policy_instance.to_dict()
# create an instance of BmrBackupPolicy from a dict
bmr_backup_policy_from_dict = BmrBackupPolicy.from_dict(bmr_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


