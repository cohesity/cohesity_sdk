# RecoverAwsRDSOracleParams

Specifies the parameters to recover AWS RDS Oracle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRDSOracle**](AwsTargetParamsForRecoverRDSOracle.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_oracle_params import RecoverAwsRDSOracleParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRDSOracleParams from a JSON string
recover_aws_rds_oracle_params_instance = RecoverAwsRDSOracleParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRDSOracleParams.to_json())

# convert the object into a dict
recover_aws_rds_oracle_params_dict = recover_aws_rds_oracle_params_instance.to_dict()
# create an instance of RecoverAwsRDSOracleParams from a dict
recover_aws_rds_oracle_params_from_dict = RecoverAwsRDSOracleParams.from_dict(recover_aws_rds_oracle_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


