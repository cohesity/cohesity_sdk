# Office365ObjectProtectionParams

Specifies the parameters which are specific to Microsoft 365 Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups_object_protection_params** | [**Office365ObjectProtectionCommonParams**](Office365ObjectProtectionCommonParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the Microsoft 365 Object Protection type. | 
**sharepoint_site_object_protection_params** | [**Office365SharepointSiteObjectProtectionParams**](Office365SharepointSiteObjectProtectionParams.md) |  | [optional] 
**teams_object_protection_params** | [**Office365ObjectProtectionCommonParams**](Office365ObjectProtectionCommonParams.md) |  | [optional] 
**user_mailbox_object_protection_params** | [**Office365UserMailboxObjectProtectionParams**](Office365UserMailboxObjectProtectionParams.md) |  | [optional] 
**user_one_drive_object_protection_params** | [**Office365UserOneDriveObjectProtectionParams**](Office365UserOneDriveObjectProtectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.office365_object_protection_params import Office365ObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ObjectProtectionParams from a JSON string
office365_object_protection_params_instance = Office365ObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(Office365ObjectProtectionParams.to_json())

# convert the object into a dict
office365_object_protection_params_dict = office365_object_protection_params_instance.to_dict()
# create an instance of Office365ObjectProtectionParams from a dict
office365_object_protection_params_from_dict = Office365ObjectProtectionParams.from_dict(office365_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


