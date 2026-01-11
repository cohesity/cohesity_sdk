# RecoverKubernetesParams

Specifies the recovery options specific to Kubernetes environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**[KubernetesRecoveryObjectParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of objects which need to be recovered. | [optional] 
**recover_file_and_folder_params** | [**RecoverKubernetesFileAndFolderParams**](RecoverKubernetesFileAndFolderParams.md) |  | [optional] 
**recover_namespace_params** | [**RecoverKubernetesNamespaceParams**](RecoverKubernetesNamespaceParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


