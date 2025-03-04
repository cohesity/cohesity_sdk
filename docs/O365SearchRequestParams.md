# O365SearchRequestParams

Specifies O365 specific params search request params to search for indexed items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_ids** | **List[int]** | Specifies the domain Ids in which indexed items are searched. | [optional] 
**group_ids** | **List[int]** | Specifies the Group ids across which the indexed items needs to be searched. | [optional] 
**site_ids** | **List[int]** | Specifies the Sharepoint site ids across which the indexed items needs to be searched. | [optional] 
**teams_ids** | **List[int]** | Specifies the Teams ids across which the indexed items needs to be searched. | [optional] 
**user_ids** | **List[int]** | Specifies the user ids across which the indexed items needs to be searched. | [optional] 

## Example

```python
from cohesity_sdk.models.o365_search_request_params import O365SearchRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of O365SearchRequestParams from a JSON string
o365_search_request_params_instance = O365SearchRequestParams.from_json(json)
# print the JSON string representation of the object
print(O365SearchRequestParams.to_json())

# convert the object into a dict
o365_search_request_params_dict = o365_search_request_params_instance.to_dict()
# create an instance of O365SearchRequestParams from a dict
o365_search_request_params_from_dict = O365SearchRequestParams.from_dict(o365_search_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


