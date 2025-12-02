# UpdateIpmiUser

Specifies the params for updating ipmi user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Specifies the node id of the node for which ipmi user info needs to be added/updated. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
**node_ip** | **str** | Specifies the IP Address of the node for which ipmi user needs to be added/updated. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 
**password** | **str** | Specifies the password to be updated for the ipmi user.  | [optional] 
**username** | **str** | Specifies the ipmi username to be added/updated for given node.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_ipmi_user import UpdateIpmiUser

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIpmiUser from a JSON string
update_ipmi_user_instance = UpdateIpmiUser.from_json(json)
# print the JSON string representation of the object
print(UpdateIpmiUser.to_json())

# convert the object into a dict
update_ipmi_user_dict = update_ipmi_user_instance.to_dict()
# create an instance of UpdateIpmiUser from a dict
update_ipmi_user_from_dict = UpdateIpmiUser.from_dict(update_ipmi_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


