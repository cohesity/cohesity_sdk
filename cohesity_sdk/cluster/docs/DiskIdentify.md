# DiskIdentify

Specifies the parameters needed to identify disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | Specifies the disk id of the disk. This parameter is incompatible with &#39;nodeId&#39; and &#39;serialNumber&#39;. | [optional] 
**identify** | **bool** | Turn on/off led light if it is set to true/false | 
**node_id** | **int** | Specifies the node id of node that disk belongs to. This parameter is incompatible with &#39;diskId&#39;. Must be used together with &#39;serialNumber&#39;. | [optional] 
**serial_number** | **str** | Specifies serial number of disk. This parameter is incompatible with &#39;diskId&#39;. Must be used together with &#39;nodeId&#39;. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.disk_identify import DiskIdentify

# TODO update the JSON string below
json = "{}"
# create an instance of DiskIdentify from a JSON string
disk_identify_instance = DiskIdentify.from_json(json)
# print the JSON string representation of the object
print(DiskIdentify.to_json())

# convert the object into a dict
disk_identify_dict = disk_identify_instance.to_dict()
# create an instance of DiskIdentify from a dict
disk_identify_from_dict = DiskIdentify.from_dict(disk_identify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


