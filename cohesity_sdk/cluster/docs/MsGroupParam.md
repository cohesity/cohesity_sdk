# MsGroupParam

Specifies parameters to recover MS group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_object** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | 
**mailbox_restore_params** | [**MailboxParam**](MailboxParam.md) |  | [optional] 
**mailbox_restore_type** | **str, none_type** | Specifies whether mailbox restore is full or granular. | [optional] 
**recover_entire_group** | **bool, none_type** | Specifies if the entire Group (mailbox + site) is to be restored. | [optional] 
**site_restore_params** | [**[OneDriveParam], none_type**](OneDriveParam.md) | Specifies the parameters to recover a MSGroup site document. | [optional] 
**site_restore_type** | **str, none_type** | Specifies whether site restore is full or granular. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


