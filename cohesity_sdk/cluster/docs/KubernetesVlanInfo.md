# KubernetesVlanInfo

Specifies Vlan information for Kubernetes protection source for Protection Source in Kubernetes environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_annotations** | [**List[KubernetesServiceAnnotationObject]**](KubernetesServiceAnnotationObject.md) | Specifies annotations to be put on services for IP allocation. Applicable only when service is of type LoadBalancer. | [optional] 
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_vlan_info import KubernetesVlanInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesVlanInfo from a JSON string
kubernetes_vlan_info_instance = KubernetesVlanInfo.from_json(json)
# print the JSON string representation of the object
print(KubernetesVlanInfo.to_json())

# convert the object into a dict
kubernetes_vlan_info_dict = kubernetes_vlan_info_instance.to_dict()
# create an instance of KubernetesVlanInfo from a dict
kubernetes_vlan_info_from_dict = KubernetesVlanInfo.from_dict(kubernetes_vlan_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


