# HiveSourceRegistrationParams

Specifies parameters to register Hive source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authentication type. | [optional] [readonly] 
**metastore_address** | **str** | The MetastoreAddress for this Hive. | [optional] [readonly] 
**metastore_port** | **int** | The MetastorePort for this Hive. | [optional] [readonly] 
**configuration_directory** | **str** | The directory containing the hive-site.xml. | 
**hdfs_source_registration_id** | **int** | Protection Source registration id of the HDFS on which this Hive is running. | 
**host** | **str** | IP or hostname of any host from which the Hive configuration file hive-site.xml can be read. | 
**kerberos_principal** | **str** | The kerberos principal to be used to connect to this Hive source. | [optional] 
**ssh_password_credentials** | [**HiveSourceRegistrationParamsAllOfSshPasswordCredentials**](HiveSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.hive_source_registration_params import HiveSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of HiveSourceRegistrationParams from a JSON string
hive_source_registration_params_instance = HiveSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(HiveSourceRegistrationParams.to_json())

# convert the object into a dict
hive_source_registration_params_dict = hive_source_registration_params_instance.to_dict()
# create an instance of HiveSourceRegistrationParams from a dict
hive_source_registration_params_from_dict = HiveSourceRegistrationParams.from_dict(hive_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


