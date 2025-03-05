# RegistrationInfo

Specifies the source registration informations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_status** | **str** | Specifies the status of the authentication during the registration of a Protection Source. &#39;Pending&#39; indicates the authentication is in progress. &#39;Scheduled&#39; indicates the authentication is scheduled. &#39;Finished&#39; indicates the authentication is completed. &#39;RefreshInProgress&#39; indicates the refresh is in progress. | [optional] [readonly] 
**last_refreshed_time_msecs** | **int** | Specifies the time when the source was last refreshed in milliseconds. | [optional] [readonly] 
**registration_time_msecs** | **int** | Specifies the time when the source was registered in milliseconds | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.registration_info import RegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInfo from a JSON string
registration_info_instance = RegistrationInfo.from_json(json)
# print the JSON string representation of the object
print(RegistrationInfo.to_json())

# convert the object into a dict
registration_info_dict = registration_info_instance.to_dict()
# create an instance of RegistrationInfo from a dict
registration_info_from_dict = RegistrationInfo.from_dict(registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


