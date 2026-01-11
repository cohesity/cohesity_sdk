# MongodbOpsManagerParams

Specifies the recovery options specific to MongoDB environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | defaults to "RecoverMongodbClusters"
**new_source_config** | [**MongodbNewOpsManagerConfig**](MongodbNewOpsManagerConfig.md) |  | [optional] 
**staging_directory** | **str, none_type** | Specifies the staging directory path for PIT recovery. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


