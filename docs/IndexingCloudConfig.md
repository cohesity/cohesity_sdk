# IndexingCloudConfig

Config required for indexing in DMaaS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str, none_type** | Name of the cloud region. | 
**tenant_id** | **str, none_type** | Tenant ID to which this config belongs. | 
**azure_es_config** | [**AzureESConfigForIndexing**](AzureESConfigForIndexing.md) |  | [optional] 
**azure_storage_config** | [**AzureStorageConfigForIndexing**](AzureStorageConfigForIndexing.md) |  | [optional] 
**es_config** | [**ESConfigForIndexing**](ESConfigForIndexing.md) |  | [optional] 
**is_migrated_tenant** | **bool, none_type** | Whether this tenant is being migrated to this cluster or freshly onboarded. | [optional] 
**s3_config** | [**S3ConfigForIndexing**](S3ConfigForIndexing.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


