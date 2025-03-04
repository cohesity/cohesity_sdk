# O365SearchEmailsRequestParams

Specifies email search request params specific to O365 environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_ids** | **List[int]** | Specifies the domain Ids in which mailboxes are registered. | [optional] 
**mailbox_ids** | **List[int]** | Specifies the mailbox Ids which contains the emails/folders. | [optional] 

## Example

```python
from cohesity_sdk.models.o365_search_emails_request_params import O365SearchEmailsRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of O365SearchEmailsRequestParams from a JSON string
o365_search_emails_request_params_instance = O365SearchEmailsRequestParams.from_json(json)
# print the JSON string representation of the object
print(O365SearchEmailsRequestParams.to_json())

# convert the object into a dict
o365_search_emails_request_params_dict = o365_search_emails_request_params_instance.to_dict()
# create an instance of O365SearchEmailsRequestParams from a dict
o365_search_emails_request_params_from_dict = O365SearchEmailsRequestParams.from_dict(o365_search_emails_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


