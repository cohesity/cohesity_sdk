# HbaseOnPremSearchParams

Parameters required to search Hbase on a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hbase_object_types** | **List[str]** | Specifies one or more Hbase object types be searched. | 
**search_string** | **str** | Specifies the search string to search the Hbase Objects | 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.hbase_on_prem_search_params import HbaseOnPremSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of HbaseOnPremSearchParams from a JSON string
hbase_on_prem_search_params_instance = HbaseOnPremSearchParams.from_json(json)
# print the JSON string representation of the object
print(HbaseOnPremSearchParams.to_json())

# convert the object into a dict
hbase_on_prem_search_params_dict = hbase_on_prem_search_params_instance.to_dict()
# create an instance of HbaseOnPremSearchParams from a dict
hbase_on_prem_search_params_from_dict = HbaseOnPremSearchParams.from_dict(hbase_on_prem_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


