# CassandraConnectionParams

Specifies the parameters to connect to a Cassandra seed node and fetch information from its cassandra config file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_directory** | **str** | Directory path containing Cassandra configuration YAML file. | 
**dse_configuration_directory** | **str** | Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra. | [optional] 
**is_dse_authenticator** | **bool** | Set to true if this cluster has DSE Authenticator. | 
**is_dse_tiered_storage** | **bool** | Set to true if this cluster has DSE tiered storage. | 
**seed_node** | **str** | Any one seed node of the Cassandra cluster. | 
**ssh_password_credentials** | [**SshPasswordCredentials**](SshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**SshPrivateKeyCredentials**](SshPrivateKeyCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cassandra_connection_params import CassandraConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraConnectionParams from a JSON string
cassandra_connection_params_instance = CassandraConnectionParams.from_json(json)
# print the JSON string representation of the object
print(CassandraConnectionParams.to_json())

# convert the object into a dict
cassandra_connection_params_dict = cassandra_connection_params_instance.to_dict()
# create an instance of CassandraConnectionParams from a dict
cassandra_connection_params_from_dict = CassandraConnectionParams.from_dict(cassandra_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


