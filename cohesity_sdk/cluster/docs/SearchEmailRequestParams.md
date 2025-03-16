# SearchEmailRequestParams

Specifies the request parameters to search for emails and email folders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attendees_addresses** | **List[str]** | Filters the calendar items which have specified email addresses as attendees. | [optional] 
**bcc_recipient_addresses** | **List[str]** | Filters the emails which are sent to specified email addresses in BCC. | [optional] 
**cc_recipient_addresses** | **List[str]** | Filters the emails which are sent to specified email addresses in CC. | [optional] 
**created_end_time_secs** | **int** | Specifies the end time in Unix timestamp epoch in seconds where the created time of the email/item is less than specified value. | [optional] 
**created_start_time_secs** | **int** | Specifies the start time in Unix timestamp epoch in seconds where the created time of the email/item is more than specified value. | [optional] 
**due_date_end_time_secs** | **int** | Specifies the end time in Unix timestamp epoch in seconds where the last modification time of the email/item is less than specified value. | [optional] 
**due_date_start_time_secs** | **int** | Specifies the start time in Unix timestamp epoch in seconds where the last modification time of the email/item is more than specified value. | [optional] 
**email_address** | **str** | Filters the contact items which have specified text in email address. | [optional] 
**email_subject** | **str** | Filters the emails which have the specified text in its subject. | [optional] 
**first_name** | **str** | Filters the contacts with specified text in first name. | [optional] 
**folder_names** | **List[str]** | Filters the emails which are categorized to specified folders. | [optional] 
**has_attachment** | **bool** | Filters the emails which have attachment. | [optional] 
**last_modified_end_time_secs** | **int** | Specifies the end time in Unix timestamp epoch in seconds where the last modification time of the email/item is less than specified value. | [optional] 
**last_modified_start_time_secs** | **int** | Specifies the start time in Unix timestamp epoch in seconds where the last modification time of the email/item is more than specified value. | [optional] 
**last_name** | **str** | Filters the contacts with specified text in last name. | [optional] 
**middle_name** | **str** | Filters the contacts with specified text in middle name. | [optional] 
**organizer_address** | **str** | Filters the calendar items which are organized by specified User&#39;s email address. | [optional] 
**received_end_time_secs** | **int** | Specifies the end time in Unix timestamp epoch in seconds where the received time of the email is less than specified value. | [optional] 
**received_start_time_secs** | **int** | Specifies the start time in Unix timestamp epoch in seconds where the received time of the email is more than specified value. | [optional] 
**recipient_addresses** | **List[str]** | Filters the emails which are sent to specified email addresses. | [optional] 
**sender_address** | **str** | Filters the emails which are received from specified User&#39;s email address. | [optional] 
**source_environment** | **str** | Specifies the source environment. | [optional] 
**task_status_types** | **List[str]** | Specifies a list of task item status types. Task items having status within the given types will be returned. | [optional] 
**types** | **List[str]** | Specifies a list of mailbox item types. Only items within the given types will be returned. | [optional] 
**o365_params** | [**O365SearchEmailsRequestParams**](O365SearchEmailsRequestParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.search_email_request_params import SearchEmailRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEmailRequestParams from a JSON string
search_email_request_params_instance = SearchEmailRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchEmailRequestParams.to_json())

# convert the object into a dict
search_email_request_params_dict = search_email_request_params_instance.to_dict()
# create an instance of SearchEmailRequestParams from a dict
search_email_request_params_from_dict = SearchEmailRequestParams.from_dict(search_email_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


