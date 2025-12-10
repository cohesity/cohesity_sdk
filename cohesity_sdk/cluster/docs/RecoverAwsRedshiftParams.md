# RecoverAwsRedshiftParams

Specifies the parameters to recover Redshift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRedshift**](AwsTargetParamsForRecoverRedshift.md) |  | 
**snapshots** | [**List[RecoverAwsRedshiftSnapshotParams]**](RecoverAwsRedshiftSnapshotParams.md) | Specifies the details of the aws redshift objects to be recovered. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_redshift_params import RecoverAwsRedshiftParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRedshiftParams from a JSON string
recover_aws_redshift_params_instance = RecoverAwsRedshiftParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRedshiftParams.to_json())

# convert the object into a dict
recover_aws_redshift_params_dict = recover_aws_redshift_params_instance.to_dict()
# create an instance of RecoverAwsRedshiftParams from a dict
recover_aws_redshift_params_from_dict = RecoverAwsRedshiftParams.from_dict(recover_aws_redshift_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


