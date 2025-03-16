# CloneViewParams

Specifies the parameters to clone a View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_lock_expiry_usecs** | **int** | DataLock (Write Once Read Many) lock expiry epoch time in microseconds. If a view is marked as a DataLock view, only a Data Security Officer (a user having Data Security Privilege) can delete the view until the lock expiry time. | [optional] 
**description** | **str** | Specifies the description of the cloned View. | [optional] 
**is_read_only** | **bool** | Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true. | [optional] 
**name** | **str** | Specifies the name of the cloned View. | 
**netgroup_whitelist** | [**NisNetgroups**](NisNetgroups.md) | Array of Netgroups. Specifies a list of netgroups with domains that have permissions to access the View. (Overrides or extends the Netgroup specified at the global Cohesity Cluster level.) | [optional] 
**protocol_access** | [**List[ViewProtocol]**](ViewProtocol.md) | Specifies the supported Protocols for the View. | [optional] 
**qos** | [**QoS**](QoS.md) | Specifies the Quality of Service (QoS) Policy for the View. | [optional] 
**storage_policy_override** | [**StoragePolicyOverride**](StoragePolicyOverride.md) | Specifies if inline deduplication and compression settings inherited from the Storage Domain (View Box) should be disabled for this View. | [optional] 
**subnet_whitelist** | [**List[Subnet]**](Subnet.md) | Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.) | [optional] 

## Example

```python
from cohesity_sdk.helios.models.clone_view_params import CloneViewParams

# TODO update the JSON string below
json = "{}"
# create an instance of CloneViewParams from a JSON string
clone_view_params_instance = CloneViewParams.from_json(json)
# print the JSON string representation of the object
print(CloneViewParams.to_json())

# convert the object into a dict
clone_view_params_dict = clone_view_params_instance.to_dict()
# create an instance of CloneViewParams from a dict
clone_view_params_from_dict = CloneViewParams.from_dict(clone_view_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


