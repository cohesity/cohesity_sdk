# ExchangeProtectionGroupParams

Specifies the parameters which are specific to Exchange related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ExchangeProtectionGroupObjectParams]**](ExchangeProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 
**backups_copy_only** | **bool, none_type** | Specifies whether the backups should be copy-only. | [optional] 
**exclude_database_ids** | **[int, none_type]** | Specifies the list of IDs of the databases to not be protected by this Protection Group. This can be used to ignore specific databases under Exchange Server/DAG which has been included for protection. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


