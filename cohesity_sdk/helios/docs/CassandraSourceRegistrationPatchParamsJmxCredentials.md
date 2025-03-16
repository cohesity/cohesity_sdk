# CassandraSourceRegistrationPatchParamsJmxCredentials

JMX Credentials for this cluster. These should be the same for all the nodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | JMX password. | 
**username** | **str** | JMX username. | 

## Example

```python
from cohesity_sdk.helios.models.cassandra_source_registration_patch_params_jmx_credentials import CassandraSourceRegistrationPatchParamsJmxCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraSourceRegistrationPatchParamsJmxCredentials from a JSON string
cassandra_source_registration_patch_params_jmx_credentials_instance = CassandraSourceRegistrationPatchParamsJmxCredentials.from_json(json)
# print the JSON string representation of the object
print(CassandraSourceRegistrationPatchParamsJmxCredentials.to_json())

# convert the object into a dict
cassandra_source_registration_patch_params_jmx_credentials_dict = cassandra_source_registration_patch_params_jmx_credentials_instance.to_dict()
# create an instance of CassandraSourceRegistrationPatchParamsJmxCredentials from a dict
cassandra_source_registration_patch_params_jmx_credentials_from_dict = CassandraSourceRegistrationPatchParamsJmxCredentials.from_dict(cassandra_source_registration_patch_params_jmx_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


