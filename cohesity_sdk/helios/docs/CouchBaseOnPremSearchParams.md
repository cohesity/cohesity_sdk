# CouchBaseOnPremSearchParams

Parameters required to search CouchBase on a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**couchbase_object_types** | **List[str]** | Specifies Couchbase object types be searched. For Couchbase it can only be set to &#39;CouchbaseBuckets&#39;. | 
**search_string** | **str** | Specifies the search string to search the Couchbase Objects | 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.couch_base_on_prem_search_params import CouchBaseOnPremSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of CouchBaseOnPremSearchParams from a JSON string
couch_base_on_prem_search_params_instance = CouchBaseOnPremSearchParams.from_json(json)
# print the JSON string representation of the object
print(CouchBaseOnPremSearchParams.to_json())

# convert the object into a dict
couch_base_on_prem_search_params_dict = couch_base_on_prem_search_params_instance.to_dict()
# create an instance of CouchBaseOnPremSearchParams from a dict
couch_base_on_prem_search_params_from_dict = CouchBaseOnPremSearchParams.from_dict(couch_base_on_prem_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


