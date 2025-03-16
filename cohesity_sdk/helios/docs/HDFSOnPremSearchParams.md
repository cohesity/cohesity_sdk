# HDFSOnPremSearchParams

Parameters required to search HDFS on a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hdfs_types** | **List[str]** | Specifies types as Folders or Files or both to be searched. | 
**search_string** | **str** | Specifies the search string to search the HDFS Folders and Files. | 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.hdfson_prem_search_params import HDFSOnPremSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of HDFSOnPremSearchParams from a JSON string
hdfson_prem_search_params_instance = HDFSOnPremSearchParams.from_json(json)
# print the JSON string representation of the object
print(HDFSOnPremSearchParams.to_json())

# convert the object into a dict
hdfson_prem_search_params_dict = hdfson_prem_search_params_instance.to_dict()
# create an instance of HDFSOnPremSearchParams from a dict
hdfson_prem_search_params_from_dict = HDFSOnPremSearchParams.from_dict(hdfson_prem_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


