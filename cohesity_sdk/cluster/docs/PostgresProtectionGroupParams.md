# PostgresProtectionGroupParams

Specifies parameters related to the Postgres Protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convert_incremental_to_full_on_error** | **bool** | Specifies the flag to convert incremental backup to full backup on failure. | [optional] 
**max_view_counts_per_host** | **int** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional] [default to 1]
**num_concurrent_io_streams** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**objects** | [**List[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**postgres_user_name** | **str** | Postgres service user needed for accessing the Postgres source. | [optional] 
**source_id** | **int** | Specifies the source Id of the objects to be protected. | 

## Example

```python
from cohesity_sdk.cluster.models.postgres_protection_group_params import PostgresProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresProtectionGroupParams from a JSON string
postgres_protection_group_params_instance = PostgresProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(PostgresProtectionGroupParams.to_json())

# convert the object into a dict
postgres_protection_group_params_dict = postgres_protection_group_params_instance.to_dict()
# create an instance of PostgresProtectionGroupParams from a dict
postgres_protection_group_params_from_dict = PostgresProtectionGroupParams.from_dict(postgres_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


