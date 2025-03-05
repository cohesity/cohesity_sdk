# OracleConnectionParams

Specifies the parameters to connect to a Oracle node/cluster using given IP or hostname FQDN.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Specifies the unique identifier to locate the Oracle node or cluster. The host identifier can be IP address or FQDN. | 

## Example

```python
from cohesity_sdk.models.oracle_connection_params import OracleConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleConnectionParams from a JSON string
oracle_connection_params_instance = OracleConnectionParams.from_json(json)
# print the JSON string representation of the object
print(OracleConnectionParams.to_json())

# convert the object into a dict
oracle_connection_params_dict = oracle_connection_params_instance.to_dict()
# create an instance of OracleConnectionParams from a dict
oracle_connection_params_from_dict = OracleConnectionParams.from_dict(oracle_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


