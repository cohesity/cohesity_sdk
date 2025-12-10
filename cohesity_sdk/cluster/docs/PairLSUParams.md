# PairLSUParams

Defines the parameters required to pair a local LSU with a remote LSU in another cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_lsuid** | **int** | Specifies Id of the local LSU. | 
**remote_cluster_id** | **int** | Specifies Id of the remote cluster where the remote LSU exists. The remote cluster must already be paired before pairing LSU. | 
**remote_lsuid** | **int** | Indicates whether the remote LSU acts as the source in data transfer operations. The remote LSU must be designated as either a source, a target, or both. | 
**remote_cluster_fqdn** | **str** | Specifies FQDN of the remote cluster. | 
**remote_lsu_role** | [**RemoteLSURole**](RemoteLSURole.md) |  | [optional] [default to RemoteLSURole.SOURCE]

## Example

```python
from cohesity_sdk.cluster.models.pair_lsu_params import PairLSUParams

# TODO update the JSON string below
json = "{}"
# create an instance of PairLSUParams from a JSON string
pair_lsu_params_instance = PairLSUParams.from_json(json)
# print the JSON string representation of the object
print(PairLSUParams.to_json())

# convert the object into a dict
pair_lsu_params_dict = pair_lsu_params_instance.to_dict()
# create an instance of PairLSUParams from a dict
pair_lsu_params_from_dict = PairLSUParams.from_dict(pair_lsu_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


