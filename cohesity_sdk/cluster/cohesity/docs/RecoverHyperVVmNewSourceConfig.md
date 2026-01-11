# RecoverHyperVVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str, none_type** | Specifies the type of HyperV source to which the VMs are being restored. | 
**scvmm_server_params** | [**RecoverHyperVVmSCVMMSourceConfig**](RecoverHyperVVmSCVMMSourceConfig.md) |  | [optional] 
**standalone_cluster_params** | [**RecoverHyperVVmStandaloneClusterSourceConfig**](RecoverHyperVVmStandaloneClusterSourceConfig.md) |  | [optional] 
**standalone_host_params** | [**RecoverHyperVVmStandaloneHostSourceConfig**](RecoverHyperVVmStandaloneHostSourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


