# CassandraSourceRegistrationParamsAllOfJmxCredentials

JMX Credentials for this cluster. These should be the same for all the nodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | JMX password. | 
**username** | **str** | JMX username. | 

## Example

```python
from cohesity_sdk.models.cassandra_source_registration_params_all_of_jmx_credentials import CassandraSourceRegistrationParamsAllOfJmxCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraSourceRegistrationParamsAllOfJmxCredentials from a JSON string
cassandra_source_registration_params_all_of_jmx_credentials_instance = CassandraSourceRegistrationParamsAllOfJmxCredentials.from_json(json)
# print the JSON string representation of the object
print(CassandraSourceRegistrationParamsAllOfJmxCredentials.to_json())

# convert the object into a dict
cassandra_source_registration_params_all_of_jmx_credentials_dict = cassandra_source_registration_params_all_of_jmx_credentials_instance.to_dict()
# create an instance of CassandraSourceRegistrationParamsAllOfJmxCredentials from a dict
cassandra_source_registration_params_all_of_jmx_credentials_from_dict = CassandraSourceRegistrationParamsAllOfJmxCredentials.from_dict(cassandra_source_registration_params_all_of_jmx_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


