# M365BackupControllerBillingResponseParams

Specifies the response parameters for triggering enable MBS service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_period_end_time_secs** | **float** | The expiration time of the grace period in epoch secs. | [optional] 
**id** | **str** | Specifies the Service App ID | [optional] 
**last_modified_by** | [**IdentitySet**](IdentitySet.md) |  | [optional] 
**last_modified_time_secs** | **float** | Timestamp of the last modification of the entity in epoch secs. | [optional] 
**restore_allowed_till_time_secs** | **float** | The expiration time of the restoration allowed period in epoch secs. | [optional] 
**status** | **str** | Specifies the Status of service. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.m365_backup_controller_billing_response_params import M365BackupControllerBillingResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of M365BackupControllerBillingResponseParams from a JSON string
m365_backup_controller_billing_response_params_instance = M365BackupControllerBillingResponseParams.from_json(json)
# print the JSON string representation of the object
print(M365BackupControllerBillingResponseParams.to_json())

# convert the object into a dict
m365_backup_controller_billing_response_params_dict = m365_backup_controller_billing_response_params_instance.to_dict()
# create an instance of M365BackupControllerBillingResponseParams from a dict
m365_backup_controller_billing_response_params_from_dict = M365BackupControllerBillingResponseParams.from_dict(m365_backup_controller_billing_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


