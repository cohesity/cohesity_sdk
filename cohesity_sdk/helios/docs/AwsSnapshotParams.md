# AwsSnapshotParams

Specifies parameters of AWS type snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the protection type of AWS snapshots. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_snapshot_params import AwsSnapshotParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSnapshotParams from a JSON string
aws_snapshot_params_instance = AwsSnapshotParams.from_json(json)
# print the JSON string representation of the object
print(AwsSnapshotParams.to_json())

# convert the object into a dict
aws_snapshot_params_dict = aws_snapshot_params_instance.to_dict()
# create an instance of AwsSnapshotParams from a dict
aws_snapshot_params_from_dict = AwsSnapshotParams.from_dict(aws_snapshot_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


