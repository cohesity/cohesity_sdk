# ProtectedObjectInfoAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_run** | [**ObjectProtectionRunSummary**](ObjectProtectionRunSummary.md) |  | [optional] 
**object_backup_configuration** | [**ProtectedObjectBackupConfig**](ProtectedObjectBackupConfig.md) |  | [optional] 
**permissions** | [**[Tenant], none_type**](TenantInfo.md) | Specifies the list of tenants that have permissions for this accessing given protected object. | [optional] 
**protection_group_configurations** | [**[ProtectedObjectGroupBackupConfig], none_type**](ProtectedObjectGroupBackupConfig.md) | Specifies the protection info associated with every object. There can be multiple instances of protection info since the same object can be protected in multiple protection groups. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


