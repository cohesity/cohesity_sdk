# CouchbaseSearchParams

Specifies the parameters which are specific for searching Couchbase objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**couchbase_object_types** | **List[str]** | Specifies Couchbase object types be searched. For Couchbase it can only be set to &#39;CouchbaseBuckets&#39;. | 
**search_string** | **str** | Specifies the search string to search the Couchbase Objects | 

## Example

```python
from cohesity_sdk.cluster.models.couchbase_search_params import CouchbaseSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of CouchbaseSearchParams from a JSON string
couchbase_search_params_instance = CouchbaseSearchParams.from_json(json)
# print the JSON string representation of the object
print(CouchbaseSearchParams.to_json())

# convert the object into a dict
couchbase_search_params_dict = couchbase_search_params_instance.to_dict()
# create an instance of CouchbaseSearchParams from a dict
couchbase_search_params_from_dict = CouchbaseSearchParams.from_dict(couchbase_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


