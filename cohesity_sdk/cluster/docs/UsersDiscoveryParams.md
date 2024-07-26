# UsersDiscoveryParams

Specifies discovery params for User(mailbox/onedrive) entities. It should only be populated when the 'DiscoveryParams.discoverableObjectTypeList' includes 'kUsers' otherwise this will be ignored.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_chats_backup** | **bool, none_type** | Specifies whether users&#39; chats should be backed up or not. If this is false or not specified users&#39; chats backup will not be done. | [optional] 
**discover_users_with_mailbox** | **bool, none_type** | Specifies if office 365 users with valid mailboxes should be discovered or not. | [optional] 
**discover_users_with_onedrive** | **bool, none_type** | Specifies if office 365 users with valid Onedrives should be discovered or not. | [optional] 
**fetch_mailbox_info** | **bool, none_type** | Specifies whether users&#39; mailbox info including the provisioning status, mailbox type &amp; in-place archival support will be fetched and processed. | [optional] 
**fetch_one_drive_info** | **bool, none_type** | Specifies whether users&#39; onedrive info including the provisioning status &amp; storage quota will be fetched and processed. | [optional] 
**skip_users_without_my_site** | **bool, none_type** | Specifies whether to skip processing user who have uninitialized OneDrive or are without MySite. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


