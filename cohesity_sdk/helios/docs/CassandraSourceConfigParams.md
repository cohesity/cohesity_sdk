# CassandraSourceConfigParams

Specifies the parameters fetched by reading cassandra configuration on the seed node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_partitioner** | **str** | Cassandra partitioner required in compaction. | [optional] 
**cassandra_port_info** | [**CassandraPortInfo**](CassandraPortInfo.md) |  | [optional] 
**cassandra_security_info** | [**CassandraSecurityInfo**](CassandraSecurityInfo.md) |  | [optional] 
**cassandra_version** | **str** | Cassandra Version. | [optional] 
**commit_log_backup_location** | **str** | Commit Logs backup location on cassandra nodes | [optional] 
**data_center_names** | **List[str]** | Data centers for this cluster. | [optional] 
**dse_version** | **str** | DSE Version | [optional] 
**endpoint_snitch** | **str** | Endpoint snitch used for this cluster. | [optional] 
**is_jmx_auth_enable** | **bool** | Is JMX Authentication enabled in this cluster ? | [optional] 
**kerberos_sasl_protocol** | **str** | Populated if cassandraAuthType is Kerberos. | [optional] 
**seeds** | **List[str]** | Seed nodes of this cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cassandra_source_config_params import CassandraSourceConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraSourceConfigParams from a JSON string
cassandra_source_config_params_instance = CassandraSourceConfigParams.from_json(json)
# print the JSON string representation of the object
print(CassandraSourceConfigParams.to_json())

# convert the object into a dict
cassandra_source_config_params_dict = cassandra_source_config_params_instance.to_dict()
# create an instance of CassandraSourceConfigParams from a dict
cassandra_source_config_params_from_dict = CassandraSourceConfigParams.from_dict(cassandra_source_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


