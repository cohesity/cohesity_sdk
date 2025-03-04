# IcapUriConnectionStatusList

Specifies a list of ICAP Uri connection status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icap_uri_connection_status_list** | [**List[IcapUriConnectionStatus]**](IcapUriConnectionStatus.md) | Specifies the list of ICAP Uri connection status. | [optional] 

## Example

```python
from cohesity_sdk.models.icap_uri_connection_status_list import IcapUriConnectionStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of IcapUriConnectionStatusList from a JSON string
icap_uri_connection_status_list_instance = IcapUriConnectionStatusList.from_json(json)
# print the JSON string representation of the object
print(IcapUriConnectionStatusList.to_json())

# convert the object into a dict
icap_uri_connection_status_list_dict = icap_uri_connection_status_list_instance.to_dict()
# create an instance of IcapUriConnectionStatusList from a dict
icap_uri_connection_status_list_from_dict = IcapUriConnectionStatusList.from_dict(icap_uri_connection_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


