# EncryptionSettings

Specifis the encryption setting of the External Target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_additional_security** | **bool** | Enable Additional security by managing key manually | [optional] 
**encryption_key_file_downloaded** | **bool** | Specifies if the encryption key file has been downloaded using the Cohesity Dashboard (Cohesity UI). If true, the encryption key has been downloaded using the Cohesity Dashboard. An encryption key can only be downloaded once using the Cohesity Dashboard. After setting it to true once, subsequent updates to this field will be ignored. | [optional] 
**encryption_level** | **str** | Specifies the type of encryption for the Setting. | 
**key_file_download_time_usecs** | **int** | Specifies the time (in microseconds) when the encryption key file was downloaded from the Cohesity Dashboard (Cohesity UI). An encryption key can only be downloaded once using Cohesity Dashboard. Can be set only once when the key is downloaded. | [optional] [readonly] 
**key_file_download_user** | **str** | Specifies the user who downloaded the encryption key from the Cohesity Dashboard (Cohesity UI). This field is only populated if encryption is enabled for the Vault and customerManagingEncryptionKeys is true. Can be set only once when the key is downloaded. | [optional] [readonly] 
**kms_server_id** | **int** | Specifies the Key Management Service Server ID for the Encryption Setting. | [optional] 

## Example

```python
from cohesity_sdk.models.encryption_settings import EncryptionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionSettings from a JSON string
encryption_settings_instance = EncryptionSettings.from_json(json)
# print the JSON string representation of the object
print(EncryptionSettings.to_json())

# convert the object into a dict
encryption_settings_dict = encryption_settings_instance.to_dict()
# create an instance of EncryptionSettings from a dict
encryption_settings_from_dict = EncryptionSettings.from_dict(encryption_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


