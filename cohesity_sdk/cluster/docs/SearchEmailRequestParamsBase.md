# SearchEmailRequestParamsBase

Specifies the request parameters to search for mailbox items and folders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **[str], none_type** | Specifies a list of mailbox item types. Only items within the given types will be returned. | [optional] 
**has_attachment** | **bool, none_type** | Filters the emails which have attachment. | [optional] 
**sender_address** | **str, none_type** | Filters the emails which are received from specified User&#39;s email address. | [optional] 
**recipient_addresses** | **[str], none_type** | Filters the emails which are sent to specified email addresses. | [optional] 
**cc_recipient_addresses** | **[str], none_type** | Filters the emails which are sent to specified email addresses in CC. | [optional] 
**bcc_recipient_addresses** | **[str], none_type** | Filters the emails which are sent to specified email addresses in BCC. | [optional] 
**received_start_time_secs** | **int, none_type** | Specifies the start time in Unix timestamp epoch in seconds where the received time of the email is more than specified value. | [optional] 
**received_end_time_secs** | **int, none_type** | Specifies the end time in Unix timestamp epoch in seconds where the received time of the email is less than specified value. | [optional] 
**email_subject** | **str, none_type** | Filters the emails which have the specified text in its subject. | [optional] 
**folder_names** | **[str], none_type** | Filters the emails which are categorized to specified folders. | [optional] 
**source_environment** | **str, none_type** | Specifies the source environment. | [optional]  if omitted the server will use the default value of "kO365"
**created_start_time_secs** | **int, none_type** | Specifies the start time in Unix timestamp epoch in seconds where the created time of the email/item is more than specified value. | [optional] 
**created_end_time_secs** | **int, none_type** | Specifies the end time in Unix timestamp epoch in seconds where the created time of the email/item is less than specified value. | [optional] 
**last_modified_start_time_secs** | **int, none_type** | Specifies the start time in Unix timestamp epoch in seconds where the last modification time of the email/item is more than specified value. | [optional] 
**last_modified_end_time_secs** | **int, none_type** | Specifies the end time in Unix timestamp epoch in seconds where the last modification time of the email/item is less than specified value. | [optional] 
**organizer_address** | **str, none_type** | Filters the calendar items which are organized by specified User&#39;s email address. | [optional] 
**attendees_addresses** | **[str], none_type** | Filters the calendar items which have specified email addresses as attendees. | [optional] 
**first_name** | **str, none_type** | Filters the contacts with specified text in first name. | [optional] 
**middle_name** | **str, none_type** | Filters the contacts with specified text in middle name. | [optional] 
**last_name** | **str, none_type** | Filters the contacts with specified text in last name. | [optional] 
**email_address** | **str, none_type** | Filters the contact items which have specified text in email address. | [optional] 
**due_date_start_time_secs** | **int, none_type** | Specifies the start time in Unix timestamp epoch in seconds where the last modification time of the email/item is more than specified value. | [optional] 
**due_date_end_time_secs** | **int, none_type** | Specifies the end time in Unix timestamp epoch in seconds where the last modification time of the email/item is less than specified value. | [optional] 
**task_status_types** | **[str], none_type** | Specifies a list of task item status types. Task items having status within the given types will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


