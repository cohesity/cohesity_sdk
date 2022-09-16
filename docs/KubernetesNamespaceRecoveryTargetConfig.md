# KubernetesNamespaceRecoveryTargetConfig

Specifies the recovery target configuration of the Namespace recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool, none_type** | Specifies whether or not to recover the Namespaces to a different source than they were backed up from. | 
**new_source_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the new source configuration if a Kubernetes Namespace is being restored to a different source than the one from which it was protected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


