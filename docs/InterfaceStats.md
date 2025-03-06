# InterfaceStats

Interface stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rx_bytes** | **int** | Total bytes received over the interface. | [optional] 
**rx_dropped** | **int** | Number of packets received but not processed. | [optional] 
**rx_errors** | **int** | Total number of bad packets received. | [optional] 
**rx_pkts** | **int** | Total number of packets received over the interface. | [optional] 
**tx_bytes** | **int** | Total bytes transmitted over the interface. | [optional] 
**tx_dropped** | **int** | Number of packets dropped on their way to transmission. | [optional] 
**tx_errors** | **int** | Total number of transmit problems. | [optional] 
**tx_pkts** | **int** | Total number of packets transmitted over the interface. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.interface_stats import InterfaceStats

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStats from a JSON string
interface_stats_instance = InterfaceStats.from_json(json)
# print the JSON string representation of the object
print(InterfaceStats.to_json())

# convert the object into a dict
interface_stats_dict = interface_stats_instance.to_dict()
# create an instance of InterfaceStats from a dict
interface_stats_from_dict = InterfaceStats.from_dict(interface_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


