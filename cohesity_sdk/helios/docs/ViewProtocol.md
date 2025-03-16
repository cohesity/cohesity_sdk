# ViewProtocol

Specifies the protocol options for view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Mode of protocol access.   &#39;ReadOnly&#39;   &#39;ReadWrite&#39; | [optional] 
**type** | **str** | Type of protocol. Specifies the supported Protocols for the View.   &#39;NFS&#39; enables protocol access to NFS v3.   &#39;NFS4&#39; enables protocol access to NFS v4.1.   &#39;SMB&#39; enables protocol access to SMB.   &#39;S3&#39; enables protocol access to S3.   &#39;Swift&#39; enables protocol access to Swift. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_protocol import ViewProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of ViewProtocol from a JSON string
view_protocol_instance = ViewProtocol.from_json(json)
# print the JSON string representation of the object
print(ViewProtocol.to_json())

# convert the object into a dict
view_protocol_dict = view_protocol_instance.to_dict()
# create an instance of ViewProtocol from a dict
view_protocol_from_dict = ViewProtocol.from_dict(view_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


