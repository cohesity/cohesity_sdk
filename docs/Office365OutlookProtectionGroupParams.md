# Office365OutlookProtectionGroupParams

Specifies the parameters which are specific to Office 365 Outlook related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_folders** | **List[str]** | Array of prefixes used to exclude folders which are by default included. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all folders which are included by default will be included. These prefixes have no effect on folders that are excluded by default. The only folders excluded by default are documented with includeFolders. | [optional] 
**include_folders** | **List[str]** | Array of prefixes used to include folders which are by default excluded. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all folders which are excluded by default will be excluded. These prefixes have no effect on folders that are included by default. All folders are included by default except for the Recoverable Items folder. | [optional] 

## Example

```python
from cohesity_sdk.models.office365_outlook_protection_group_params import Office365OutlookProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365OutlookProtectionGroupParams from a JSON string
office365_outlook_protection_group_params_instance = Office365OutlookProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(Office365OutlookProtectionGroupParams.to_json())

# convert the object into a dict
office365_outlook_protection_group_params_dict = office365_outlook_protection_group_params_instance.to_dict()
# create an instance of Office365OutlookProtectionGroupParams from a dict
office365_outlook_protection_group_params_from_dict = Office365OutlookProtectionGroupParams.from_dict(office365_outlook_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


