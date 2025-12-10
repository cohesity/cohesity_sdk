# RecoverGCPBigQueryObjectParams

Specifies details of recovery object to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_dataset_name** | **str** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 
**original_dataset_name** | **str** | Specifies the original name of the object to be restored, as it exists in the source. | 
**overwrite** | **bool** | Specifies whether to overwrite an existing object with the same name at the destination. If true, any existing object will be replaced; if false or unset, the restore may fail if a conflict occurs. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_big_query_object_params import RecoverGCPBigQueryObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPBigQueryObjectParams from a JSON string
recover_gcp_big_query_object_params_instance = RecoverGCPBigQueryObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPBigQueryObjectParams.to_json())

# convert the object into a dict
recover_gcp_big_query_object_params_dict = recover_gcp_big_query_object_params_instance.to_dict()
# create an instance of RecoverGCPBigQueryObjectParams from a dict
recover_gcp_big_query_object_params_from_dict = RecoverGCPBigQueryObjectParams.from_dict(recover_gcp_big_query_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


