# CommonArchivalAwsExternalTargetParams

Specifies the common parameters which are specific to AWS related External Targets of archival purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies bucket name of the External Target. | 
**region** | **str** | Specifies region of the External Target. | 
**bucket_owner_account_id** | **str** | Specifies the account Id of the S3 bucket owner. | [optional] 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**source_side_deduplication** | **bool** | Specifies the Source Side Deduplication setting for the AWS external target | [optional] 
**storage_class** | **str** | Specifies the AWS External Target storage class. | 

## Example

```python
from cohesity_sdk.models.common_archival_aws_external_target_params import CommonArchivalAwsExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonArchivalAwsExternalTargetParams from a JSON string
common_archival_aws_external_target_params_instance = CommonArchivalAwsExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonArchivalAwsExternalTargetParams.to_json())

# convert the object into a dict
common_archival_aws_external_target_params_dict = common_archival_aws_external_target_params_instance.to_dict()
# create an instance of CommonArchivalAwsExternalTargetParams from a dict
common_archival_aws_external_target_params_from_dict = CommonArchivalAwsExternalTargetParams.from_dict(common_archival_aws_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


