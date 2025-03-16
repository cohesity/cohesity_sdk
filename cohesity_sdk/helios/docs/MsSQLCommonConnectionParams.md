# MsSQLCommonConnectionParams

Specifies the common parameters to connect to a SQL node/cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_identifier** | **str** | Specifies the unique identifier to locate the SQL node or cluster. The host identifier can be IP address or FQDN. | 

## Example

```python
from cohesity_sdk.helios.models.ms_sql_common_connection_params import MsSQLCommonConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of MsSQLCommonConnectionParams from a JSON string
ms_sql_common_connection_params_instance = MsSQLCommonConnectionParams.from_json(json)
# print the JSON string representation of the object
print(MsSQLCommonConnectionParams.to_json())

# convert the object into a dict
ms_sql_common_connection_params_dict = ms_sql_common_connection_params_instance.to_dict()
# create an instance of MsSQLCommonConnectionParams from a dict
ms_sql_common_connection_params_from_dict = MsSQLCommonConnectionParams.from_dict(ms_sql_common_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


