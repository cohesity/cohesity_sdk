# IcapUriConnectionStatus

Specifies the ICAP Uri connection status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | Specifies the connection status. | [optional] 
**icap_uri** | **str** | Specifies the ICAP Uri. | [optional] 

## Example

```python
from cohesity_sdk.models.icap_uri_connection_status import IcapUriConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IcapUriConnectionStatus from a JSON string
icap_uri_connection_status_instance = IcapUriConnectionStatus.from_json(json)
# print the JSON string representation of the object
print(IcapUriConnectionStatus.to_json())

# convert the object into a dict
icap_uri_connection_status_dict = icap_uri_connection_status_instance.to_dict()
# create an instance of IcapUriConnectionStatus from a dict
icap_uri_connection_status_from_dict = IcapUriConnectionStatus.from_dict(icap_uri_connection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


