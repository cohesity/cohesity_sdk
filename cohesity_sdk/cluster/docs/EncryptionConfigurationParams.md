# EncryptionConfigurationParams

Specifies the parameters the user wants to use when configuring encryption for the new Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_fips_mode** | **bool** | Specifies whether or not to enable FIPS mode | [optional] 
**enable_hardware_encryption** | **bool** | Specifies whether or not to enable hardware encryption | [optional] 
**enable_software_encryption** | **bool** | Specifies whether or not to enable software encryption | [optional] 
**rotation_period** | **int** | Specifies the rotation period for encryption keys in days | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.encryption_configuration_params import EncryptionConfigurationParams

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionConfigurationParams from a JSON string
encryption_configuration_params_instance = EncryptionConfigurationParams.from_json(json)
# print the JSON string representation of the object
print(EncryptionConfigurationParams.to_json())

# convert the object into a dict
encryption_configuration_params_dict = encryption_configuration_params_instance.to_dict()
# create an instance of EncryptionConfigurationParams from a dict
encryption_configuration_params_from_dict = EncryptionConfigurationParams.from_dict(encryption_configuration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


