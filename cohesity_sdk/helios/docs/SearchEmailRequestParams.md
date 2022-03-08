# SearchEmailRequestParams

Specifies the request parameters to search for emails and email folders.

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
**o365_params** | [**O365SearchEmailsRequestParams**](O365SearchEmailsRequestParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


