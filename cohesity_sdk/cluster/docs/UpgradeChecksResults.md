# UpgradeChecksResults

Specifies upgrade checks results from cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message if test results could not be fetched. | 
**request_type** | **str** | Type of the check(preupgrade/postupgrade). | 
**result_status** | **str** | Final result (running/pass/fail) of run. | 
**test_run_instance_id** | **str** | Specifies test run instance of upgrade checks. | 
**finish_time_secs** | **int, none_type** | Specifies unix epoch finish time of checks(in seconds). | [optional] 
**node_results** | [**[UpgradeCheckNodeResult]**](UpgradeCheckNodeResult.md) | The healthcheck result for node. | [optional] 
**start_time_secs** | **int, none_type** | Specifies unix epoch start time of checks(in seconds). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


