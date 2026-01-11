# UpdateIpmiUser

Specifies the params for updating ipmi user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str, none_type** | Specifies the node id of the node for which ipmi user info needs to be added/updated. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
**node_ip** | **str, none_type** | Specifies the IP Address of the node for which ipmi user needs to be added/updated. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 
**password** | **str, none_type** | Specifies the password to be updated for the ipmi user.  | [optional] 
**username** | **str, none_type** | Specifies the ipmi username to be added/updated for given node.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


