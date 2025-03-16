# UpgradeCheckRunTestsResult

Specifies the result for upgrade checks run tests request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run_instance_id** | **int** | Specifies test run instance allocated for upgrade checks | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_check_run_tests_result import UpgradeCheckRunTestsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeCheckRunTestsResult from a JSON string
upgrade_check_run_tests_result_instance = UpgradeCheckRunTestsResult.from_json(json)
# print the JSON string representation of the object
print(UpgradeCheckRunTestsResult.to_json())

# convert the object into a dict
upgrade_check_run_tests_result_dict = upgrade_check_run_tests_result_instance.to_dict()
# create an instance of UpgradeCheckRunTestsResult from a dict
upgrade_check_run_tests_result_from_dict = UpgradeCheckRunTestsResult.from_dict(upgrade_check_run_tests_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


