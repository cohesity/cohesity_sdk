# SmbMountCredentials

Specifies the credentials to mount a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 

## Example

```python
from cohesity_sdk.helios.models.smb_mount_credentials import SmbMountCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SmbMountCredentials from a JSON string
smb_mount_credentials_instance = SmbMountCredentials.from_json(json)
# print the JSON string representation of the object
print(SmbMountCredentials.to_json())

# convert the object into a dict
smb_mount_credentials_dict = smb_mount_credentials_instance.to_dict()
# create an instance of SmbMountCredentials from a dict
smb_mount_credentials_from_dict = SmbMountCredentials.from_dict(smb_mount_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


