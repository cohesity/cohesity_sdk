# DeleteIpmiUser

Specifies the params for deleting ipmi user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Specifies the node id of the node for which ipmi user info needs to be deleted. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
**node_ip** | **str** | Specifies the IP Address of the node for which ipmi user needs to be deleted. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 
**username** | **str** | Specifies the ipmi username to be deleted for given node.  | [optional] 

## Example

```python
from cohesity_sdk.models.delete_ipmi_user import DeleteIpmiUser

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIpmiUser from a JSON string
delete_ipmi_user_instance = DeleteIpmiUser.from_json(json)
# print the JSON string representation of the object
print(DeleteIpmiUser.to_json())

# convert the object into a dict
delete_ipmi_user_dict = delete_ipmi_user_instance.to_dict()
# create an instance of DeleteIpmiUser from a dict
delete_ipmi_user_from_dict = DeleteIpmiUser.from_dict(delete_ipmi_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


