# PrecheckOptions

Specifies a list of precheck options for fortknox onprem vault configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cluster_storage_domains_encrypted** | **bool** | Specifies if encryption is enabled at cluster or all storage domains have encryption enabled. | [optional] 
**is_firewall_enabled** | **bool** | Specifies if firewall is enabled except for replication interface group with primary cluster IPs. | [optional] 
**is_local_user_mfa_enabled** | **bool** | Specifies if local user mfa is enabled. | [optional] 
**is_no_outgoing_replications_or_archivals** | **bool** | Specifies if the cluster does not have any policy with outgoing replication or archival. | [optional] 
**is_no_remote_clusters** | **bool** | Specifies if the cluster does not have any remote clusters configured. | [optional] 
**is_node_to_node_encryption_enabled** | **bool** | Specifies if node to node secure communication is enabled. | [optional] 
**is_support_channel_disabled** | **bool** | Specifies if support channel/reverse tunnel is disabled. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.precheck_options import PrecheckOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PrecheckOptions from a JSON string
precheck_options_instance = PrecheckOptions.from_json(json)
# print the JSON string representation of the object
print(PrecheckOptions.to_json())

# convert the object into a dict
precheck_options_dict = precheck_options_instance.to_dict()
# create an instance of PrecheckOptions from a dict
precheck_options_from_dict = PrecheckOptions.from_dict(precheck_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


