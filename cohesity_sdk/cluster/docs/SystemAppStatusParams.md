# SystemAppStatusParams

Specifies the status of each system app on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | Specifies the number of available replicas. | [optional] 
**configured_replicas** | **int** | Specifies the number of configured replicas. | [optional] 
**name** | **str** | Specifies the name of the system app. | [optional] 
**ready_replicas** | **int** | Specifies the number of ready replicas. | [optional] 
**service_endpoint** | **str** | Specifies the service endpoint. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.system_app_status_params import SystemAppStatusParams

# TODO update the JSON string below
json = "{}"
# create an instance of SystemAppStatusParams from a JSON string
system_app_status_params_instance = SystemAppStatusParams.from_json(json)
# print the JSON string representation of the object
print(SystemAppStatusParams.to_json())

# convert the object into a dict
system_app_status_params_dict = system_app_status_params_instance.to_dict()
# create an instance of SystemAppStatusParams from a dict
system_app_status_params_from_dict = SystemAppStatusParams.from_dict(system_app_status_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


