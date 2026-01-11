# StorageDomainConfig

Specifies a Storage Domain config. This contains the storage domain ids and names on the Primary Cluster and the Vault Cluster. The storage domain on the Primary Cluster is referred as Primary Domain, and the storage domain on the Vault Cluster is referred as Vault Domain. It also contains the vaulting window between the two domains.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_domain_id** | **int, none_type** | Specifies the Storage Domain id on the Primary Cluster. | 
**vault_domain_id** | **int, none_type** | Specifies the Storage Domain id on the Vault Cluster. | 
**primary_domain_name** | **str, none_type** | Specifies the Storage Domain name on the Primary Cluster. | [optional] 
**vault_domain_name** | **str, none_type** | Specifies the Storage Domain name on the Primary Cluster. | [optional] 
**vaulting_window_config** | [**VaultingWindowConfig**](VaultingWindowConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


