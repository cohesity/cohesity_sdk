# RpoPolicySettings

Specifies all the additional settings that are applicable only to an RPO policy. This can include storage domain, settings of different environments, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerting_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**backup_qos_principal** | **str, none_type** | Specifies whether the data will be written to HDD or SSD. | [optional] 
**env_backup_params** | [**EnvironmentTypeJobParams**](EnvironmentTypeJobParams.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain to which data will be written | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


