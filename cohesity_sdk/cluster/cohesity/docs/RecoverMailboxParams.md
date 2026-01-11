# RecoverMailboxParams

Specifies the parameters to recover an Office 365 Mailbox.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectMailboxParam], none_type**](ObjectMailboxParam.md) | Specifies a list of Mailbox params associated with the objects to recover. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other Mailboxes if one of Mailbox failed to recover. Default value is false. | [optional] 
**ews_exchange_target** | [**EwsExchangeTargetParam**](EwsExchangeTargetParam.md) |  | [optional] 
**pst_params** | [**PstParam**](PstParam.md) |  | [optional] 
**skip_recover_archive_mailbox** | **bool, none_type** | Specifies whether to skip the recovery of the archive mailbox and/or items present in the archive mailbox. Default value is true | [optional] 
**skip_recover_archive_recoverable_items** | **bool, none_type** | Specifies whether to skip the recovery of the Archive Recoverable Items present in the selected snapshot. Default value is true | [optional] 
**skip_recover_primary_mailbox** | **bool, none_type** | Specifies whether to skip the recovery of items under Top of Information Store, aka the message folder root. Default value is false. | [optional] 
**skip_recover_recoverable_items** | **bool, none_type** | Specifies whether to skip the recovery of the Recoverable Items present in the selected snapshot. Default value is true | [optional] 
**target_mailbox** | [**TargetMailboxParam**](TargetMailboxParam.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


