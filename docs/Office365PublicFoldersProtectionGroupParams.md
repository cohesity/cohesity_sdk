# Office365PublicFoldersProtectionGroupParams

Specifies the parameters which are specific to Office 365 PublicFolders related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_folders** | **List[str]** | Array of Excluded Public folders. Specifies filters to match PublicFolder folders which should be excluded when backing up Office 365 source. Two kinds of filters are supported. a) prefix which always starts with &#39;/&#39;. b) posix which always starts with empty quotes(&#39;&#39;). Regular expressions are not supported. If not specified, all the PublicFolders will be protected. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.office365_public_folders_protection_group_params import Office365PublicFoldersProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365PublicFoldersProtectionGroupParams from a JSON string
office365_public_folders_protection_group_params_instance = Office365PublicFoldersProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(Office365PublicFoldersProtectionGroupParams.to_json())

# convert the object into a dict
office365_public_folders_protection_group_params_dict = office365_public_folders_protection_group_params_instance.to_dict()
# create an instance of Office365PublicFoldersProtectionGroupParams from a dict
office365_public_folders_protection_group_params_from_dict = Office365PublicFoldersProtectionGroupParams.from_dict(office365_public_folders_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


