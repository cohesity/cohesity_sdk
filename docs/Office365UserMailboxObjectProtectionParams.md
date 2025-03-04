# Office365UserMailboxObjectProtectionParams

Specifies the params to create a User Mailbox Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[Office365ObjectProtectionObjectParams]**](Office365ObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**exclude_folders** | **List[str]** | Array of prefixes used to exclude folders which are by default included. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all folders which are included by default will be included. These prefixes have no effect on folders that are excluded by default. The only folders excluded by default are documented with includeFolders. | [optional] 
**include_folders** | **List[str]** | Array of prefixes used to include folders which are by default excluded. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all folders which are excluded by default will be excluded. These prefixes have no effect on folders that are included by default. All folders are included by default except for the Recoverable Items folder. | [optional] 

## Example

```python
from cohesity_sdk.models.office365_user_mailbox_object_protection_params import Office365UserMailboxObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365UserMailboxObjectProtectionParams from a JSON string
office365_user_mailbox_object_protection_params_instance = Office365UserMailboxObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(Office365UserMailboxObjectProtectionParams.to_json())

# convert the object into a dict
office365_user_mailbox_object_protection_params_dict = office365_user_mailbox_object_protection_params_instance.to_dict()
# create an instance of Office365UserMailboxObjectProtectionParams from a dict
office365_user_mailbox_object_protection_params_from_dict = Office365UserMailboxObjectProtectionParams.from_dict(office365_user_mailbox_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


