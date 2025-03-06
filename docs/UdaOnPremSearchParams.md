# UdaOnPremSearchParams

Parameters required to search Universal Data Adapter objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_string** | **str** | Specifies the search string to search the Universal Data Adapter Objects | 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.uda_on_prem_search_params import UdaOnPremSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaOnPremSearchParams from a JSON string
uda_on_prem_search_params_instance = UdaOnPremSearchParams.from_json(json)
# print the JSON string representation of the object
print(UdaOnPremSearchParams.to_json())

# convert the object into a dict
uda_on_prem_search_params_dict = uda_on_prem_search_params_instance.to_dict()
# create an instance of UdaOnPremSearchParams from a dict
uda_on_prem_search_params_from_dict = UdaOnPremSearchParams.from_dict(uda_on_prem_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


