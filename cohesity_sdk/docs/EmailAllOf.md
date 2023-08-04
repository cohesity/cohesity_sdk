# EmailAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the id of the email object. | [optional] 
**user_object_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**folder_name** | **str, none_type** | Specify the name of the email folder. | [optional] 
**parent_folder_id** | **int, none_type** | Specifies the id of parent folder the mailbox item. | [optional] 
**path** | **str, none_type** | Specifies the path to this mailbox item. | [optional] 
**directory_path** | **str, none_type** | Specifies the directory path to this mailbox item. | [optional] 
**type** | **str, none_type** | Specifies the Mailbox item type. | [optional] 
**email_subject** | **str, none_type** | Specifies the subject of this email. | [optional] 
**has_attachment** | **bool, none_type** | Specifies whether email has an attachment. | [optional] 
**sender_address** | **str, none_type** | Specifies the sender&#39;s email address. | [optional] 
**recipient_addresses** | **[str], none_type** | \&quot;Specifies the email addresses of all receipients of this email.\&quot; | [optional] 
**cc_recipient_addresses** | **[str], none_type** | \&quot;Specifies the email addresses of all the CC receipients of this email.\&quot; | [optional] 
**bcc_recipient_addresses** | **[str], none_type** | \&quot;Specifies the email addresses of all the BCC receipients of this email.\&quot; | [optional] 
**sent_time_secs** | **int, none_type** | \&quot;Specifies the Unix timestamp epoch in seconds at which this email is sent.\&quot; | [optional] 
**received_time_secs** | **int, none_type** | \&quot;Specifies the Unix timestamp epoch in seconds at which this email is received.\&quot; | [optional] 
**created_time_secs** | **int, none_type** | \&quot;Specifies the Unix timestamp epoch in seconds at which this item is created.\&quot; | [optional] 
**organizer_address** | **str, none_type** | \&quot;Specifies the calendar item organizer&#39;s email address.\&quot; | [optional] 
**required_attendees_addresses** | **[str], none_type** | \&quot;Specifies the email addresses of all required attendees of this calendar item.\&quot; | [optional] 
**optional_attendees_addresses** | **[str], none_type** | \&quot;Specifies the email addresses of all the optional attendees of this calendar item.\&quot; | [optional] 
**first_name** | **str, none_type** | Specifies the contact&#39;s first name. | [optional] 
**last_name** | **str, none_type** | Specifies the contact&#39;s last name. | [optional] 
**email_addresses** | **[str], none_type** | Specifies the email addresses of a contact. | [optional] 
**last_modification_time_secs** | **int, none_type** | \&quot;Specifies the Unix timestamp epoch in seconds at which this item was modified.\&quot; | [optional] 
**last_modification_name** | **str, none_type** | \&quot;Specifies the name of the person who modified this item.\&quot; | [optional] 
**task_due_date_time_secs** | **int, none_type** | \&quot;Specifies the Unix timestamp epoch in seconds at which this task item is due.\&quot; | [optional] 
**task_completion_date_time_secs** | **int, none_type** | \&quot;Specifies the Unix timestamp epoch in seconds at which this task item was completed.\&quot; | [optional] 
**task_status** | **str, none_type** | Specifies the task item status type. | [optional] 
**protection_group_id** | **str, none_type** | \&quot;Specifies the Protection Group id protecting the mailbox.\&quot; | [optional] 
**protection_group_name** | **str, none_type** | \&quot;Specifies the Protection Group name protecting the mailbox item.\&quot; | [optional] 
**storage_domain_id** | **int, none_type** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**tenant_id** | **str, none_type** | \&quot;Specify the tenant id to which this email belongs to.\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


