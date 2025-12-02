# PostgresProperties

Specifies the properties for a Postgres Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**pg_bin** | **str** | Specifies the directory containing the PostgreSQL binaries. | [optional] 
**pg_host** | **str** | Specifies the host for the Postgres source. | [optional] 
**pg_port** | **int** | Specifies the port for the Postgres source. | 

## Example

```python
from cohesity_sdk.cluster.models.postgres_properties import PostgresProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresProperties from a JSON string
postgres_properties_instance = PostgresProperties.from_json(json)
# print the JSON string representation of the object
print(PostgresProperties.to_json())

# convert the object into a dict
postgres_properties_dict = postgres_properties_instance.to_dict()
# create an instance of PostgresProperties from a dict
postgres_properties_from_dict = PostgresProperties.from_dict(postgres_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


