# M365CsmParams

Specifies the Microsoft 365 Backup Storage parameters for the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_controller_activation_time_secs** | **int** | Specifies the backup controller activation epoch time for the Microsoft 365 Backup Controller App. | [optional] 
**backup_controller_client_id** | **str** | Specifies the Client ID for the Cohesity owned Azure App used for Microsoft 365 Backup Storage Service. | [optional] 
**backup_controller_tenant_id** | **str** | Specifies the host Entra tenant ID for the Cohesity owned Azure App used for Microsoft 365 Backup Storage service. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.m365_csm_params import M365CsmParams

# TODO update the JSON string below
json = "{}"
# create an instance of M365CsmParams from a JSON string
m365_csm_params_instance = M365CsmParams.from_json(json)
# print the JSON string representation of the object
print(M365CsmParams.to_json())

# convert the object into a dict
m365_csm_params_dict = m365_csm_params_instance.to_dict()
# create an instance of M365CsmParams from a dict
m365_csm_params_from_dict = M365CsmParams.from_dict(m365_csm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


