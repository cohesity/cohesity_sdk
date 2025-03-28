# RecoverCouchbaseParams

Specifies the parameters to recover Couchbase objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a recovery job. | [optional] 
**bandwidth_mbps** | **int** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**overwrite** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**warnings** | **List[str]** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 
**append_documents** | **bool** | If set to true, docuements from the bucket being recovered will be appended into the bucket at the destination. | [optional] 
**ddl_only_recovery** | **bool** | Set to true to recover only the bucket configurations. No documents will be recovered. | [optional] 
**filter_documents_params** | [**FilterDocumentsParams**](FilterDocumentsParams.md) |  | 
**overwrite_users** | **bool** | If set to true existing users will be replaced with users from the bucket being recovered. | [optional] 
**snapshots** | [**List[RecoverCouchbaseSnapshotParams]**](RecoverCouchbaseSnapshotParams.md) | Specifies the local snapshot ids of the Objects to be recovered. | 
**suffix** | **str** | A suffix that is to be applied to all recovered objects. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_couchbase_params import RecoverCouchbaseParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverCouchbaseParams from a JSON string
recover_couchbase_params_instance = RecoverCouchbaseParams.from_json(json)
# print the JSON string representation of the object
print(RecoverCouchbaseParams.to_json())

# convert the object into a dict
recover_couchbase_params_dict = recover_couchbase_params_instance.to_dict()
# create an instance of RecoverCouchbaseParams from a dict
recover_couchbase_params_from_dict = RecoverCouchbaseParams.from_dict(recover_couchbase_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


