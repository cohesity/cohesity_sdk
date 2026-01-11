# RecoverKubernetesFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**[CommonRecoverFileAndFolderInfo], none_type**](CommonRecoverFileAndFolderInfo.md) | Specifies the information about the files and folders to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kKubernetes"
**kubernetes_target_params** | [**KubernetesTargetParamsForRecoverFileAndFolder**](KubernetesTargetParamsForRecoverFileAndFolder.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


