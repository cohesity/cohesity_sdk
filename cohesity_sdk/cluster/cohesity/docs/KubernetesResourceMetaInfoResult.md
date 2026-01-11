# KubernetesResourceMetaInfoResult

specifies included/excluded resources of a namespace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backed_up_pvcs** | [**[KubernetesPvcInfo], none_type**](KubernetesPvcInfo.md) | Specifies the list of PVCs that were backed up | [optional] 
**backed_up_resource_count** | **int, none_type** | Specifies the count of resources that were backed up | [optional] 
**backed_up_resources** | [**[ResourceInfo], none_type**](ResourceInfo.md) | Specifies the resources that backed up resources | [optional] 
**excluded_resources** | **[str], none_type** | Specifies the resources to excluded during backup | [optional] 
**included_resources** | **[str], none_type** | Specifies the resources to included during backup | [optional] 
**includes_cluster_scoped_resources** | **bool, none_type** | Specifies if the backed up object (namespace) contains any cluster scoped resources too. | [optional] 
**quiesce_rule_status** | [**[KubernetesHookRuleStatus], none_type**](KubernetesHookRuleStatus.md) | Execution status of each quiesce/unquiesce rule within the backup run. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


