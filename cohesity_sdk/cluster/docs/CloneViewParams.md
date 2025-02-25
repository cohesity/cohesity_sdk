# CloneViewParams

Specifies the parameters to clone a View.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the cloned View. | 
**data_lock_expiry_usecs** | **int, none_type** | DataLock (Write Once Read Many) lock expiry epoch time in microseconds. If a view is marked as a DataLock view, only a Data Security Officer (a user having Data Security Privilege) can delete the view until the lock expiry time. | [optional] 
**description** | **str, none_type** | Specifies the description of the cloned View. | [optional] 
**is_read_only** | **bool, none_type** | Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true. | [optional] 
**netgroup_whitelist** | [**NisNetgroups**](NisNetgroups.md) |  | [optional] 
**protocol_access** | [**[ViewProtocol], none_type**](ViewProtocol.md) | Specifies the supported Protocols for the View. | [optional] 
**qos** | [**QoS**](QoS.md) |  | [optional] 
**storage_policy_override** | [**StoragePolicyOverride**](StoragePolicyOverride.md) |  | [optional] 
**subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


