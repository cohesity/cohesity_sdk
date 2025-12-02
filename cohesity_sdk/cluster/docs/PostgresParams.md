# PostgresParams

Specifies the recovery options specific to Postgres environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_postgres_params** | [**RecoverPostgresParams**](RecoverPostgresParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.postgres_params import PostgresParams

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresParams from a JSON string
postgres_params_instance = PostgresParams.from_json(json)
# print the JSON string representation of the object
print(PostgresParams.to_json())

# convert the object into a dict
postgres_params_dict = postgres_params_instance.to_dict()
# create an instance of PostgresParams from a dict
postgres_params_from_dict = PostgresParams.from_dict(postgres_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


