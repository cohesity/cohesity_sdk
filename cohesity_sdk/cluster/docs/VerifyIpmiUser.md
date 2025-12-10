# VerifyIpmiUser

Specifies the params for verifying ipmi user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Specifies the node id of the node for which ipmi user info needs to be verified. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
**node_ip** | **str** | Specifies the IP Address of the node for which ipmi user needs to be verified. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 
**password** | **str** | Specifies the password of the ipmi user provided that needs to be verified.  | [optional] 
**username** | **str** | Specifies the ipmi username to be verified for given node.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.verify_ipmi_user import VerifyIpmiUser

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyIpmiUser from a JSON string
verify_ipmi_user_instance = VerifyIpmiUser.from_json(json)
# print the JSON string representation of the object
print(VerifyIpmiUser.to_json())

# convert the object into a dict
verify_ipmi_user_dict = verify_ipmi_user_instance.to_dict()
# create an instance of VerifyIpmiUser from a dict
verify_ipmi_user_from_dict = VerifyIpmiUser.from_dict(verify_ipmi_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


