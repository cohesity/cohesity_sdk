# M365SelfServiceWorkloadParams

Specifies workload specific Self-Service configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_security_groups** | [**List[M365SelfServiceSecurityGroupInfo]**](M365SelfServiceSecurityGroupInfo.md) | Specifies the list of Security Groups whose members are to be allowed the Self-Service workflows. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.m365_self_service_workload_params import M365SelfServiceWorkloadParams

# TODO update the JSON string below
json = "{}"
# create an instance of M365SelfServiceWorkloadParams from a JSON string
m365_self_service_workload_params_instance = M365SelfServiceWorkloadParams.from_json(json)
# print the JSON string representation of the object
print(M365SelfServiceWorkloadParams.to_json())

# convert the object into a dict
m365_self_service_workload_params_dict = m365_self_service_workload_params_instance.to_dict()
# create an instance of M365SelfServiceWorkloadParams from a dict
m365_self_service_workload_params_from_dict = M365SelfServiceWorkloadParams.from_dict(m365_self_service_workload_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


