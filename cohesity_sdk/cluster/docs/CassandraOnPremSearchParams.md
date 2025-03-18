# CassandraOnPremSearchParams

Parameters required to search Cassandra on a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_object_types** | **List[str]** | Specifies one or more Cassandra object types to be searched. | 
**search_string** | **str** | Specifies the search string to search the Cassandra Objects | 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cassandra_on_prem_search_params import CassandraOnPremSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraOnPremSearchParams from a JSON string
cassandra_on_prem_search_params_instance = CassandraOnPremSearchParams.from_json(json)
# print the JSON string representation of the object
print(CassandraOnPremSearchParams.to_json())

# convert the object into a dict
cassandra_on_prem_search_params_dict = cassandra_on_prem_search_params_instance.to_dict()
# create an instance of CassandraOnPremSearchParams from a dict
cassandra_on_prem_search_params_from_dict = CassandraOnPremSearchParams.from_dict(cassandra_on_prem_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


