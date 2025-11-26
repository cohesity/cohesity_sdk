# TargetMailboxParam

Specifies the target Mailbox to recover to.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_folder_path** | **str, none_type** | Specifies the path to the target folder. | 
**id** | **int, none_type** | Specifies the id of the target mailbox. Atleast one of id or primarySMTPAddress need to be defined. In case both id and primarySMTPAddress are defined then id takes precedence. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] [readonly] 
**parent_source_id** | **int, none_type** | Specifies the id of the domain for alternate domain recovery. | [optional] 
**primary_smtp_address** | **str, none_type** | Specifies the primary SMTP address of the target mailbox. Atleast one of id or primarySMTPAddress needs to be defined. In case both id and primarySMTPAddress are defined then id takes precedence. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


