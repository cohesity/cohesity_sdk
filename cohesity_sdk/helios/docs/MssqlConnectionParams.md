# MssqlConnectionParams

Specifies the parameters to connect to a SQL node/cluster using given IP or hostname FQDN.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_identifier** | **str** | Specifies the unique identifier to locate the SQL node or cluster. The host identifier can be IP address or FQDN. | 

## Example

```python
from cohesity_sdk.helios.models.mssql_connection_params import MssqlConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlConnectionParams from a JSON string
mssql_connection_params_instance = MssqlConnectionParams.from_json(json)
# print the JSON string representation of the object
print(MssqlConnectionParams.to_json())

# convert the object into a dict
mssql_connection_params_dict = mssql_connection_params_instance.to_dict()
# create an instance of MssqlConnectionParams from a dict
mssql_connection_params_from_dict = MssqlConnectionParams.from_dict(mssql_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


