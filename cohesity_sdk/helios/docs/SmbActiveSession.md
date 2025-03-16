# SmbActiveSession

Specifies an active session and its file opens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_opens** | [**List[SmbActiveOpen]**](SmbActiveOpen.md) | Specifies an active open of an SMB file, its access and sharing information. | [optional] 
**client_ip** | **str** | Specifies the IP address from which the file is open. | [optional] 
**domain** | **str** | Specifies the domain of the user. | [optional] 
**session_id** | **int** | Specifies the id of the session. | [optional] 
**user_name** | **str** | Specifies the username who keeps the file open. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.smb_active_session import SmbActiveSession

# TODO update the JSON string below
json = "{}"
# create an instance of SmbActiveSession from a JSON string
smb_active_session_instance = SmbActiveSession.from_json(json)
# print the JSON string representation of the object
print(SmbActiveSession.to_json())

# convert the object into a dict
smb_active_session_dict = smb_active_session_instance.to_dict()
# create an instance of SmbActiveSession from a dict
smb_active_session_from_dict = SmbActiveSession.from_dict(smb_active_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


