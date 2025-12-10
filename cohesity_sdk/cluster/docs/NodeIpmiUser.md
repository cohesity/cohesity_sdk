# NodeIpmiUser

Specifies the ipmi user info for each node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipmi_username** | **str** | Specifies the ipmi user name of the node. | [optional] 
**node_ip** | **str** | Specifies the ip address of the node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_ipmi_user import NodeIpmiUser

# TODO update the JSON string below
json = "{}"
# create an instance of NodeIpmiUser from a JSON string
node_ipmi_user_instance = NodeIpmiUser.from_json(json)
# print the JSON string representation of the object
print(NodeIpmiUser.to_json())

# convert the object into a dict
node_ipmi_user_dict = node_ipmi_user_instance.to_dict()
# create an instance of NodeIpmiUser from a dict
node_ipmi_user_from_dict = NodeIpmiUser.from_dict(node_ipmi_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


