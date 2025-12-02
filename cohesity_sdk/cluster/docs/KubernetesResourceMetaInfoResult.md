# KubernetesResourceMetaInfoResult

specifies included/excluded resources of a namespace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backed_up_pvcs** | [**List[KubernetesPvcInfo]**](KubernetesPvcInfo.md) | Specifies the list of PVCs that were backed up | [optional] 
**backed_up_resource_count** | **int** | Specifies the count of resources that were backed up | [optional] 
**backed_up_resources** | [**List[ResourceInfo]**](ResourceInfo.md) | Specifies the resources that backed up resources | [optional] 
**excluded_resources** | **List[str]** | Specifies the resources to excluded during backup | [optional] 
**included_resources** | **List[str]** | Specifies the resources to included during backup | [optional] 
**includes_cluster_scoped_resources** | **bool** | Specifies if the backed up object (namespace) contains any cluster scoped resources too. | [optional] 
**quiesce_rule_status** | [**List[KubernetesHookRuleStatus]**](KubernetesHookRuleStatus.md) | Execution status of each quiesce/unquiesce rule within the backup run. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_resource_meta_info_result import KubernetesResourceMetaInfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesResourceMetaInfoResult from a JSON string
kubernetes_resource_meta_info_result_instance = KubernetesResourceMetaInfoResult.from_json(json)
# print the JSON string representation of the object
print(KubernetesResourceMetaInfoResult.to_json())

# convert the object into a dict
kubernetes_resource_meta_info_result_dict = kubernetes_resource_meta_info_result_instance.to_dict()
# create an instance of KubernetesResourceMetaInfoResult from a dict
kubernetes_resource_meta_info_result_from_dict = KubernetesResourceMetaInfoResult.from_dict(kubernetes_resource_meta_info_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


