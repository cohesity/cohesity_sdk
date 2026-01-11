# QuiesceRule

Specifies the Kubernetes Quiesce rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_snapshot_hooks** | [**[KubernetesHook], none_type**](KubernetesHook.md) | Specifies the hooks to be applied after taking snapshot. | 
**pre_snapshot_hooks** | [**[KubernetesHook], none_type**](KubernetesHook.md) | Specifies the hooks to be applied before taking snapshot. | 
**pod_selector_labels** | [**[KubernetesLabel], none_type**](KubernetesLabel.md) | Specifies the labels to select a pod. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


