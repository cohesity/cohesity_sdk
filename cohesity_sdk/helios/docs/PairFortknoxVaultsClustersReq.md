# PairFortknoxVaultsClustersReq

Request params for pairing claimed clusters with vaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ids** | **List[int]** | The cluster ids. | [optional] 
**global_vault_ids** | **List[str]** | IDs that identify Fortknox vaults. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.pair_fortknox_vaults_clusters_req import PairFortknoxVaultsClustersReq

# TODO update the JSON string below
json = "{}"
# create an instance of PairFortknoxVaultsClustersReq from a JSON string
pair_fortknox_vaults_clusters_req_instance = PairFortknoxVaultsClustersReq.from_json(json)
# print the JSON string representation of the object
print(PairFortknoxVaultsClustersReq.to_json())

# convert the object into a dict
pair_fortknox_vaults_clusters_req_dict = pair_fortknox_vaults_clusters_req_instance.to_dict()
# create an instance of PairFortknoxVaultsClustersReq from a dict
pair_fortknox_vaults_clusters_req_from_dict = PairFortknoxVaultsClustersReq.from_dict(pair_fortknox_vaults_clusters_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


