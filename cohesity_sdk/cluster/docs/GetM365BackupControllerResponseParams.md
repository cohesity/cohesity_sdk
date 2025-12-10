# GetM365BackupControllerResponseParams

Specifies the Backup Controller info for the registered M365 Backup Controller by the Cohesity App for against a specific tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**List[M365BackupControllerObject]**](M365BackupControllerObject.md) | Specifies the array of Backup Controller objects. For now this is guaranteed to have only 1 object which will specify the service app info. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_m365_backup_controller_response_params import GetM365BackupControllerResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetM365BackupControllerResponseParams from a JSON string
get_m365_backup_controller_response_params_instance = GetM365BackupControllerResponseParams.from_json(json)
# print the JSON string representation of the object
print(GetM365BackupControllerResponseParams.to_json())

# convert the object into a dict
get_m365_backup_controller_response_params_dict = get_m365_backup_controller_response_params_instance.to_dict()
# create an instance of GetM365BackupControllerResponseParams from a dict
get_m365_backup_controller_response_params_from_dict = GetM365BackupControllerResponseParams.from_dict(get_m365_backup_controller_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


