# OracleDatabaseHost

Specifies details about an Oracle database host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_count** | **int** | Specifies the number of channels to be created for this host. Default value for the number of channels will be calculated as the minimum of number of nodes in Cohesity cluster and 2 * number of CPU on the host. | [optional] 
**host_id** | **str** | Specifies the id of the database host from which backup is allowed. | [optional] 
**port** | **int** | Specifies the port where the Database is listening. | [optional] 
**sbt_host_params** | [**OracleSbtHostParams**](OracleSbtHostParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.oracle_database_host import OracleDatabaseHost

# TODO update the JSON string below
json = "{}"
# create an instance of OracleDatabaseHost from a JSON string
oracle_database_host_instance = OracleDatabaseHost.from_json(json)
# print the JSON string representation of the object
print(OracleDatabaseHost.to_json())

# convert the object into a dict
oracle_database_host_dict = oracle_database_host_instance.to_dict()
# create an instance of OracleDatabaseHost from a dict
oracle_database_host_from_dict = OracleDatabaseHost.from_dict(oracle_database_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


