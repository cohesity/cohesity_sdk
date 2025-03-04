# RigelConnectionInfo

Specifies the Rigel connection info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Specifies if the connection is active. | [optional] 
**last_connected_timestamp_msecs** | **int** | Specifies last timestamp for which connection status was known. | [optional] 
**message** | **str** | Specifies possible error message when rigel is not able to connect. | [optional] 

## Example

```python
from cohesity_sdk.models.rigel_connection_info import RigelConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RigelConnectionInfo from a JSON string
rigel_connection_info_instance = RigelConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(RigelConnectionInfo.to_json())

# convert the object into a dict
rigel_connection_info_dict = rigel_connection_info_instance.to_dict()
# create an instance of RigelConnectionInfo from a dict
rigel_connection_info_from_dict = RigelConnectionInfo.from_dict(rigel_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


