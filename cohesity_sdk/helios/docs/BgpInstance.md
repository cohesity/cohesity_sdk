# BgpInstance

BGP instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_as** | **int** | Local AS. | [optional] 
**peers** | [**List[BgpPeer]**](BgpPeer.md) | List of bgp peer groups. | [optional] 
**timers** | [**BgpTimers**](BgpTimers.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.bgp_instance import BgpInstance

# TODO update the JSON string below
json = "{}"
# create an instance of BgpInstance from a JSON string
bgp_instance_instance = BgpInstance.from_json(json)
# print the JSON string representation of the object
print(BgpInstance.to_json())

# convert the object into a dict
bgp_instance_dict = bgp_instance_instance.to_dict()
# create an instance of BgpInstance from a dict
bgp_instance_from_dict = BgpInstance.from_dict(bgp_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


