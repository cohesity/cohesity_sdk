# Office365TeamsProtectionGroupParams

Specifies the parameters which are specific to Office 365 Teams related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_types** | **List[str]** | Specifies the types of exclusions to apply for Teams backup. For now, only &#39;MeetingRecordings&#39; is supported, which excludes Microsoft Teams meeting recordings stored in default locations from backup. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.office365_teams_protection_group_params import Office365TeamsProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365TeamsProtectionGroupParams from a JSON string
office365_teams_protection_group_params_instance = Office365TeamsProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(Office365TeamsProtectionGroupParams.to_json())

# convert the object into a dict
office365_teams_protection_group_params_dict = office365_teams_protection_group_params_instance.to_dict()
# create an instance of Office365TeamsProtectionGroupParams from a dict
office365_teams_protection_group_params_from_dict = Office365TeamsProtectionGroupParams.from_dict(office365_teams_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


