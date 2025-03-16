# CassandraProtectionRunParams

Specifies the parameters for Cassandra Adapter protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_primary_for_log** | **bool** | Specifies the parameters to set this cluster as primary and trigger a new protection run for Log backup job. Default value is false. | [optional] [default to False]

## Example

```python
from cohesity_sdk.helios.models.cassandra_protection_run_params import CassandraProtectionRunParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraProtectionRunParams from a JSON string
cassandra_protection_run_params_instance = CassandraProtectionRunParams.from_json(json)
# print the JSON string representation of the object
print(CassandraProtectionRunParams.to_json())

# convert the object into a dict
cassandra_protection_run_params_dict = cassandra_protection_run_params_instance.to_dict()
# create an instance of CassandraProtectionRunParams from a dict
cassandra_protection_run_params_from_dict = CassandraProtectionRunParams.from_dict(cassandra_protection_run_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


