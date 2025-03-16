# Email

Specifies an email or an email folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_tags** | [**List[SnapshotTagInfo]**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**List[TagInfo]**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**bcc_recipient_addresses** | **List[str]** | \&quot;Specifies the email addresses of all the BCC receipients of this email.\&quot; | [optional] 
**cc_recipient_addresses** | **List[str]** | \&quot;Specifies the email addresses of all the CC receipients of this email.\&quot; | [optional] 
**created_time_secs** | **int** | \&quot;Specifies the Unix timestamp epoch in seconds at which this item is created.\&quot; | [optional] 
**directory_path** | **str** | Specifies the directory path to this mailbox item. | [optional] 
**email_addresses** | **List[str]** | Specifies the email addresses of a contact. | [optional] 
**email_subject** | **str** | Specifies the subject of this email. | [optional] 
**first_name** | **str** | Specifies the contact&#39;s first name. | [optional] 
**folder_name** | **str** | Specify the name of the email folder. | [optional] 
**has_attachment** | **bool** | Specifies whether email has an attachment. | [optional] 
**id** | **str** | Specifies the id of the email object. | [optional] 
**last_modification_name** | **str** | \&quot;Specifies the name of the person who modified this item.\&quot; | [optional] 
**last_modification_time_secs** | **int** | \&quot;Specifies the Unix timestamp epoch in seconds at which this item was modified.\&quot; | [optional] 
**last_name** | **str** | Specifies the contact&#39;s last name. | [optional] 
**optional_attendees_addresses** | **List[str]** | \&quot;Specifies the email addresses of all the optional attendees of this calendar item.\&quot; | [optional] 
**organizer_address** | **str** | \&quot;Specifies the calendar item organizer&#39;s email address.\&quot; | [optional] 
**parent_folder_id** | **int** | Specifies the id of parent folder the mailbox item. | [optional] 
**path** | **str** | Specifies the path to this mailbox item. | [optional] 
**protection_group_id** | **str** | \&quot;Specifies the Protection Group id protecting the mailbox.\&quot; | [optional] 
**protection_group_name** | **str** | \&quot;Specifies the Protection Group name protecting the mailbox item.\&quot; | [optional] 
**received_time_secs** | **int** | \&quot;Specifies the Unix timestamp epoch in seconds at which this email is received.\&quot; | [optional] 
**recipient_addresses** | **List[str]** | \&quot;Specifies the email addresses of all receipients of this email.\&quot; | [optional] 
**required_attendees_addresses** | **List[str]** | \&quot;Specifies the email addresses of all required attendees of this calendar item.\&quot; | [optional] 
**sender_address** | **str** | Specifies the sender&#39;s email address. | [optional] 
**sent_time_secs** | **int** | \&quot;Specifies the Unix timestamp epoch in seconds at which this email is sent.\&quot; | [optional] 
**storage_domain_id** | **int** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**task_completion_date_time_secs** | **int** | \&quot;Specifies the Unix timestamp epoch in seconds at which this task item was completed.\&quot; | [optional] 
**task_due_date_time_secs** | **int** | \&quot;Specifies the Unix timestamp epoch in seconds at which this task item is due.\&quot; | [optional] 
**task_status** | **str** | Specifies the task item status type. | [optional] 
**tenant_id** | **str** | \&quot;Specify the tenant id to which this email belongs to.\&quot; | [optional] 
**type** | **str** | Specifies the Mailbox item type. | [optional] 
**user_object_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.email import Email

# TODO update the JSON string below
json = "{}"
# create an instance of Email from a JSON string
email_instance = Email.from_json(json)
# print the JSON string representation of the object
print(Email.to_json())

# convert the object into a dict
email_dict = email_instance.to_dict()
# create an instance of Email from a dict
email_from_dict = Email.from_dict(email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


