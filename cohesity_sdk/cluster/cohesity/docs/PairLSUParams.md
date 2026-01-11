# PairLSUParams

Defines the parameters required to pair a local LSU with a remote LSU in another cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_lsuid** | **int** | Specifies Id of the local LSU. | 
**remote_cluster_id** | **int** | Specifies Id of the remote cluster where the remote LSU exists. The remote cluster must already be paired before pairing LSU. | 
**remote_lsuid** | **int** | Indicates whether the remote LSU acts as the source in data transfer operations. The remote LSU must be designated as either a source, a target, or both. | 
**remote_cluster_fqdn** | **str** | Specifies FQDN of the remote cluster. | 
**remote_lsu_role** | [**RemoteLSURole**](RemoteLSURole.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


