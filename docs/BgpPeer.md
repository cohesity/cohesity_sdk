# BgpPeer

BGP peer information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_or_tag** | **str** | IP Address. | [optional] 
**description** | **str** | Peer&#39;s description. | [optional] 
**remote_as** | **int** | Remote AS. | [optional] 
**timers** | [**BgpTimers**](BgpTimers.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.bgp_peer import BgpPeer

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeer from a JSON string
bgp_peer_instance = BgpPeer.from_json(json)
# print the JSON string representation of the object
print(BgpPeer.to_json())

# convert the object into a dict
bgp_peer_dict = bgp_peer_instance.to_dict()
# create an instance of BgpPeer from a dict
bgp_peer_from_dict = BgpPeer.from_dict(bgp_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


