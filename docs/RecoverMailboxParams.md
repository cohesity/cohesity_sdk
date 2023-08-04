# RecoverMailboxParams

Specifies the parameters to recover an Office 365 Mailbox.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectMailboxParam], none_type**](ObjectMailboxParam.md) | Specifies a list of Mailbox params associated with the objects to recover. | 
**target_mailbox** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the target Mailbox to recover to. If not specified, the objects will be recovered to original location. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other Mailboxes if one of Mailbox failed to recover. Default value is false. | [optional] 
**pst_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the PST conversion specific parameters. This should always be specified when need to convert selected items to PST. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


