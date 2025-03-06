# CassandraSourceRegistrationParamsAllOfCassandraCredentials

Cassandra Credentials for this cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Cassandra password. | 
**username** | **str** | Cassandra username. | 

## Example

```python
from cohesity_sdk.cluster.models.cassandra_source_registration_params_all_of_cassandra_credentials import CassandraSourceRegistrationParamsAllOfCassandraCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraSourceRegistrationParamsAllOfCassandraCredentials from a JSON string
cassandra_source_registration_params_all_of_cassandra_credentials_instance = CassandraSourceRegistrationParamsAllOfCassandraCredentials.from_json(json)
# print the JSON string representation of the object
print(CassandraSourceRegistrationParamsAllOfCassandraCredentials.to_json())

# convert the object into a dict
cassandra_source_registration_params_all_of_cassandra_credentials_dict = cassandra_source_registration_params_all_of_cassandra_credentials_instance.to_dict()
# create an instance of CassandraSourceRegistrationParamsAllOfCassandraCredentials from a dict
cassandra_source_registration_params_all_of_cassandra_credentials_from_dict = CassandraSourceRegistrationParamsAllOfCassandraCredentials.from_dict(cassandra_source_registration_params_all_of_cassandra_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


