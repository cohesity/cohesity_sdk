# Office365ObjectProtectionUpdateRequestParams

Specifies the update parameters specific to Microsoft 365 User Mailbox object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups_object_protection_params** | [**Office365GroupsObjectProtectionParams**](Office365GroupsObjectProtectionParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the Microsoft 365 Object Protection type. | 
**sharepoint_site_object_protection_params** | [**Office365SharepointSiteObjectProtectionParams**](Office365SharepointSiteObjectProtectionParams.md) |  | [optional] 
**teams_object_protection_params** | [**Office365TeamsObjectProtectionParams**](Office365TeamsObjectProtectionParams.md) |  | [optional] 
**user_mailbox_object_protection_params** | [**Office365UserMailboxObjectProtectionParams**](Office365UserMailboxObjectProtectionParams.md) |  | [optional] 
**user_one_drive_object_protection_params** | [**Office365UserOneDriveObjectProtectionParams**](Office365UserOneDriveObjectProtectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.office365_object_protection_update_request_params import Office365ObjectProtectionUpdateRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ObjectProtectionUpdateRequestParams from a JSON string
office365_object_protection_update_request_params_instance = Office365ObjectProtectionUpdateRequestParams.from_json(json)
# print the JSON string representation of the object
print(Office365ObjectProtectionUpdateRequestParams.to_json())

# convert the object into a dict
office365_object_protection_update_request_params_dict = office365_object_protection_update_request_params_instance.to_dict()
# create an instance of Office365ObjectProtectionUpdateRequestParams from a dict
office365_object_protection_update_request_params_from_dict = Office365ObjectProtectionUpdateRequestParams.from_dict(office365_object_protection_update_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


