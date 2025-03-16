# CassandraSearchParams

Specifies the parameters which are specific for searching Cassandra objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_object_types** | **List[str]** | Specifies one or more Cassandra object types to be searched. | 
**search_string** | **str** | Specifies the search string to search the Cassandra Objects | 

## Example

```python
from cohesity_sdk.helios.models.cassandra_search_params import CassandraSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraSearchParams from a JSON string
cassandra_search_params_instance = CassandraSearchParams.from_json(json)
# print the JSON string representation of the object
print(CassandraSearchParams.to_json())

# convert the object into a dict
cassandra_search_params_dict = cassandra_search_params_instance.to_dict()
# create an instance of CassandraSearchParams from a dict
cassandra_search_params_from_dict = CassandraSearchParams.from_dict(cassandra_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


