# CommonNoSqlRecoveryOptions

Specifies the common properties required by all Nosl adapters at the time of recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a recovery job. | [optional] 
**bandwidth_mbps** | **int** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**overwrite** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**warnings** | **List[str]** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.common_no_sql_recovery_options import CommonNoSqlRecoveryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CommonNoSqlRecoveryOptions from a JSON string
common_no_sql_recovery_options_instance = CommonNoSqlRecoveryOptions.from_json(json)
# print the JSON string representation of the object
print(CommonNoSqlRecoveryOptions.to_json())

# convert the object into a dict
common_no_sql_recovery_options_dict = common_no_sql_recovery_options_instance.to_dict()
# create an instance of CommonNoSqlRecoveryOptions from a dict
common_no_sql_recovery_options_from_dict = CommonNoSqlRecoveryOptions.from_dict(common_no_sql_recovery_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


