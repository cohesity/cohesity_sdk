# HiveOnPremSearchParams

Parameters required to search Hive on a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hive_object_types** | **List[str]** | Specifies one or more Hive object types be searched. | 
**search_string** | **str** | Specifies the search string to search the Hive Objects | 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.models.hive_on_prem_search_params import HiveOnPremSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of HiveOnPremSearchParams from a JSON string
hive_on_prem_search_params_instance = HiveOnPremSearchParams.from_json(json)
# print the JSON string representation of the object
print(HiveOnPremSearchParams.to_json())

# convert the object into a dict
hive_on_prem_search_params_dict = hive_on_prem_search_params_instance.to_dict()
# create an instance of HiveOnPremSearchParams from a dict
hive_on_prem_search_params_from_dict = HiveOnPremSearchParams.from_dict(hive_on_prem_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


