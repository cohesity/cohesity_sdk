# GetDataAccessSessionsResponseParams

Specifies list of data access sessions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_cookie** | **str** | pecifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 
**sessions** | [**List[DataAccessSession]**](DataAccessSession.md) | Specifies list of data access sessions. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_data_access_sessions_response_params import GetDataAccessSessionsResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataAccessSessionsResponseParams from a JSON string
get_data_access_sessions_response_params_instance = GetDataAccessSessionsResponseParams.from_json(json)
# print the JSON string representation of the object
print(GetDataAccessSessionsResponseParams.to_json())

# convert the object into a dict
get_data_access_sessions_response_params_dict = get_data_access_sessions_response_params_instance.to_dict()
# create an instance of GetDataAccessSessionsResponseParams from a dict
get_data_access_sessions_response_params_from_dict = GetDataAccessSessionsResponseParams.from_dict(get_data_access_sessions_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


