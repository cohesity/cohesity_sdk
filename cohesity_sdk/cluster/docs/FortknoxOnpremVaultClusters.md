# FortknoxOnpremVaultClusters

Specifies a list of Fortknox Onprem Vault Clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fortknox_onprem_vault_clusters** | [**List[FortknoxOnpremVaultCluster]**](FortknoxOnpremVaultCluster.md) | Specifies the list of Fortknox Onprem Vault Clusters. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fortknox_onprem_vault_clusters import FortknoxOnpremVaultClusters

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxOnpremVaultClusters from a JSON string
fortknox_onprem_vault_clusters_instance = FortknoxOnpremVaultClusters.from_json(json)
# print the JSON string representation of the object
print(FortknoxOnpremVaultClusters.to_json())

# convert the object into a dict
fortknox_onprem_vault_clusters_dict = fortknox_onprem_vault_clusters_instance.to_dict()
# create an instance of FortknoxOnpremVaultClusters from a dict
fortknox_onprem_vault_clusters_from_dict = FortknoxOnpremVaultClusters.from_dict(fortknox_onprem_vault_clusters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


