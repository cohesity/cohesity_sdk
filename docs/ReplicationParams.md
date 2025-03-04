# ReplicationParams

Specifies the replication config for a Remote Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_endpoints_reachable** | **bool** | Specifies if all endpoints on Remote Cluster are reachable. | [optional] [default to False]
**bandwidth_limit** | [**BandwidthThrottling**](BandwidthThrottling.md) |  | [optional] 
**compression_enabled** | **bool** | Specifies whether to compress the outbound data when transferring the replication data over the network to the Remote Cluster. | [optional] [default to True]
**encryption_key** | **str** | Specifies the encryption key used for encrypting the replication data from a local Cluster to a Remote Cluster. If a key is not specified, replication traffic encryption is disabled. When Snapshots are replicated from a local Cluster to a Remote Cluster, the encryption key specified on the local Cluster must be the same as the key specified on the Remote Cluster. | [optional] 
**storage_domain_pairs** | [**List[StorageDomainPair]**](StorageDomainPair.md) | Specifies a list of Storage Domain pairs. | [optional] 

## Example

```python
from cohesity_sdk.models.replication_params import ReplicationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationParams from a JSON string
replication_params_instance = ReplicationParams.from_json(json)
# print the JSON string representation of the object
print(ReplicationParams.to_json())

# convert the object into a dict
replication_params_dict = replication_params_instance.to_dict()
# create an instance of ReplicationParams from a dict
replication_params_from_dict = ReplicationParams.from_dict(replication_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


