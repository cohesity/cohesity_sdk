# ProtectedObjectInfoAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**[Tenant], none_type**](Tenant.md) | Specifies the list of tenants that have permissions for this accessing given protected object. | [optional] 
**object_backup_configuration** | [**ProtectedObjectBackupConfig**](ProtectedObjectBackupConfig.md) |  | [optional] 
**protection_group_configurations** | [**[ProtectedObjectGroupBackupConfig], none_type**](ProtectedObjectGroupBackupConfig.md) | Specifies the protection info associated with every object. There can be multiple instances of protection info since the same object can be protected in multiple protection groups. | [optional] 
**last_run** | [**ObjectProtectionRunSummary**](ObjectProtectionRunSummary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


