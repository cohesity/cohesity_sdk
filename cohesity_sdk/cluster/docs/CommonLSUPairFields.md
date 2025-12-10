# CommonLSUPairFields

Common fields representing an LSU pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_lsuid** | **int** | Specifies Id of the local LSU. | 
**remote_cluster_id** | **int** | Specifies Id of the remote cluster where the remote LSU exists. The remote cluster must already be paired before pairing LSU. | 
**remote_lsuid** | **int** | Indicates whether the remote LSU acts as the source in data transfer operations. The remote LSU must be designated as either a source, a target, or both. | 

## Example

```python
from cohesity_sdk.cluster.models.common_lsu_pair_fields import CommonLSUPairFields

# TODO update the JSON string below
json = "{}"
# create an instance of CommonLSUPairFields from a JSON string
common_lsu_pair_fields_instance = CommonLSUPairFields.from_json(json)
# print the JSON string representation of the object
print(CommonLSUPairFields.to_json())

# convert the object into a dict
common_lsu_pair_fields_dict = common_lsu_pair_fields_instance.to_dict()
# create an instance of CommonLSUPairFields from a dict
common_lsu_pair_fields_from_dict = CommonLSUPairFields.from_dict(common_lsu_pair_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


