# GetKubernetesStatusResponse

Kubernetes Infra Overall Health Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_kubernetes_version** | **str** | specifies the current Kubernetes version | [optional] 
**health_status** | **str** | Kubernetes Infra Health Status | [optional] 
**overall_k8_s_state** | **str** | Kubernetes Infra Overall State | [optional] 
**status_reason** | **str** | Reason Text for the Status | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_kubernetes_status_response import GetKubernetesStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetKubernetesStatusResponse from a JSON string
get_kubernetes_status_response_instance = GetKubernetesStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetKubernetesStatusResponse.to_json())

# convert the object into a dict
get_kubernetes_status_response_dict = get_kubernetes_status_response_instance.to_dict()
# create an instance of GetKubernetesStatusResponse from a dict
get_kubernetes_status_response_from_dict = GetKubernetesStatusResponse.from_dict(get_kubernetes_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


