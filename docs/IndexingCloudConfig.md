# IndexingCloudConfig

Config required for indexing in DMaaS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str, none_type** | Tenant ID to which this config belongs. | 
**region** | **str, none_type** | Name of the cloud region. | 
**es_config** | [**ESConfigForIndexing**](ESConfigForIndexing.md) |  | [optional] 
**azure_es_config** | [**AzureESConfigForIndexing**](AzureESConfigForIndexing.md) |  | [optional] 
**s3_config** | [**S3ConfigForIndexing**](S3ConfigForIndexing.md) |  | [optional] 
**azure_storage_config** | [**AzureStorageConfigForIndexing**](AzureStorageConfigForIndexing.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


