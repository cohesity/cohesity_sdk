# IpmiUsers

Specifies the list of IPMI users for the given node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int, none_type** | Specifies the channel through which the IPMI interface communicates on the network. | [optional] 
**max_user_id** | **int, none_type** | Specifies the highest occupied ID up to which no free user IDs are available. If a new user is created, it is assigned a user ID of maxUserId + 1. | [optional] 
**user_list** | [**[IpmiUserInfo], none_type**](IpmiUserInfo.md) | Specifies the list of ipmi users with their permissions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


