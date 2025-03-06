# KubernetesPvcInfo

Specifies the parameters which are related to Kubernetes PVC.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the pvc. | [optional] [readonly] 
**name** | **str** | Name of the pvc. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_pvc_info import KubernetesPvcInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesPvcInfo from a JSON string
kubernetes_pvc_info_instance = KubernetesPvcInfo.from_json(json)
# print the JSON string representation of the object
print(KubernetesPvcInfo.to_json())

# convert the object into a dict
kubernetes_pvc_info_dict = kubernetes_pvc_info_instance.to_dict()
# create an instance of KubernetesPvcInfo from a dict
kubernetes_pvc_info_from_dict = KubernetesPvcInfo.from_dict(kubernetes_pvc_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


